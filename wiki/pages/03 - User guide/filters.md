---
title: Gramps 6.0 Wiki Manual - Filters
categories:
- Documentation
- Filters
- Stub
managed: false
source: wiki-scrape (html-fallback)
wiki_revid: 127213
wiki_fetched_at: '2026-05-30T16:24:51Z'
---

|  |  |  |
|:---|:--:|---:|
| [**Previous**](wiki:Gramps_6.0_Wiki_Manual_-_Settings) | [**Index**](wiki:Gramps_6.0_Wiki_Manual) | [**Next**](wiki:Gramps_6.0_Wiki_Manual_-_FAQ) |

<div class="LanguageLinks">

|  |  |  |
|----|----|----|
| ![[_media/Gramps-config-language.png]] | **[Languages](wiki:Portal:Translators):**  | <span class="mw-selflink selflink">English</span>     • <span lang="da"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/da" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/da">dansk</a></span>  • <span lang="de"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/de" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/de">Deutsch</a></span>  • <span lang="es"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/es" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/es">español</a></span>  • <span lang="fi"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/fi" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/fi">suomi</a></span>  • <span lang="fr"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/fr" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/fr">français</a></span>  • <span lang="he">[עברית](wiki:Gramps_6.0_Wiki_Manual_-_Filters/he)</span>      • <span lang="mk"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/mk" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/mk">македонски</a></span>   • <span lang="nl"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/nl" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/nl">Nederlands</a></span>      • <span lang="ru"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/ru" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/ru">русский</a></span>   • <span lang="sq"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/sq" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/sq">shqip</a></span>   • <span lang="sk">[slovenčina](wiki:Gramps_6.0_Wiki_Manual_-_Filters/sk)</span>   • <span lang="tr">[Türkçe](wiki:Gramps_6.0_Wiki_Manual_-_Filters/tr)</span> |

</div>

  

<div class="thumb tright">

<div class="thumbinner" style="width:398px;">

![[_media/DefineFilter-dialog-default-60.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:DefineFilter-dialog-default-60.png" class="internal" title="Enlarge"></a>

</div>

Fig. 16.1 **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">[Define filter](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Define_Filter_dialog)</span>** - dialog - default

</div>

</div>

</div>

Filters allow Gramps to limit operations to a smaller part of a family Tree. The filtered part of the Trees shares a certain characteristic in common. (e.g., females born in France between the years 1550 and 1575.) The filter specifies which characteristics are important and allows choosing values for which to look. (In the example, the Filter looks for People of a particular sex who have an Event in specific Place during a small timespan.)

Database queries can be a challenge to compose without errors in syntax. So Filters provide structured and pre-tested database queries that hide most of the syntax complexity while providing some safety nets to avoid routine mistakes. Common characteristics used for filtering are normally presented as "parameter" fields in a form. Then the form composes a properly written query around the parameter. Forms with multiple parameter fields will compound complex queries.

Lists of all the filtering query rules currently defined in Gramps. Each of these rules is available for use when creating custom filters.

The rules are listed by their [categories](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Which_filters_in_which_Category.3F).

- [<span class="tocnumber">1</span> <span class="toctext">Filter vs. Search</span>](#Filter_vs._Search)
  - [<span class="tocnumber">1.1</span> <span class="toctext">See also</span>](#See_also)
- [<span class="tocnumber">2</span> <span class="toctext">Regular Expressions</span>](#Regular_Expressions)
  - [<span class="tocnumber">2.1</span> <span class="toctext">Find all defined values or blanks</span>](#Find_all_defined_values_or_blanks)
  - [<span class="tocnumber">2.2</span> <span class="toctext">Groups and Sets</span>](#Groups_and_Sets)
  - [<span class="tocnumber">2.3</span> <span class="toctext">Examples</span>](#Examples)
    - [<span class="tocnumber">2.3.1</span> <span class="toctext">Common variations of a surname</span>](#Common_variations_of_a_surname)
    - [<span class="tocnumber">2.3.2</span> <span class="toctext">Testing regular expressions</span>](#Testing_regular_expressions)
  - [<span class="tocnumber">2.4</span> <span class="toctext">See Also</span>](#See_Also_2)
- [<span class="tocnumber">3</span> <span class="toctext">Custom Filters</span>](#Custom_Filters)
  - [<span class="tocnumber">3.1</span> <span class="toctext">\<category\> Filters editor dialog</span>](#.3Ccategory.3E_Filters_editor_dialog)
    - [<span class="tocnumber">3.1.1</span> <span class="toctext">Filter Test dialog</span>](#Filter_Test_dialog)
  - [<span class="tocnumber">3.2</span> <span class="toctext">Define Filter dialog</span>](#Define_Filter_dialog)
  - [<span class="tocnumber">3.3</span> <span class="toctext">Add Rule dialog</span>](#Add_Rule_dialog)
- [<span class="tocnumber">4</span> <span class="toctext">Which filter rules in which Category?</span>](#Which_filter_rules_in_which_Category.3F)
- [<span class="tocnumber">5</span> <span class="toctext">Ancestral filters</span>](#Ancestral_filters)
  - [<span class="tocnumber">5.1</span> <span class="toctext">Ancestor of \<filter\> match</span>](#Ancestor_of_.3Cfilter.3E_match)
  - [<span class="tocnumber">5.2</span> <span class="toctext">Ancestor of \<person\></span>](#Ancestor_of_.3Cperson.3E)
  - [<span class="tocnumber">5.3</span> <span class="toctext">Ancestor of \<person\> at least \<N\> generations away</span>](#Ancestor_of_.3Cperson.3E_at_least_.3CN.3E_generations_away)
  - [<span class="tocnumber">5.4</span> <span class="toctext">Ancestor of \<person\> not more than \<N\> generations away</span>](#Ancestor_of_.3Cperson.3E_not_more_than_.3CN.3E_generations_away)
  - [<span class="tocnumber">5.5</span> <span class="toctext">Ancestor of bookmarked people not more than \<N\> generations away</span>](#Ancestor_of_bookmarked_people_not_more_than_.3CN.3E_generations_away)
  - [<span class="tocnumber">5.6</span> <span class="toctext">Ancestor of the default person not more than \<N\> generations away</span>](#Ancestor_of_the_default_person_not_more_than_.3CN.3E_generations_away)
  - [<span class="tocnumber">5.7</span> <span class="toctext">Duplicate ancestors of \<person\></span>](#Duplicate_ancestors_of_.3Cperson.3E)
  - [<span class="tocnumber">5.8</span> <span class="toctext">People with a common ancestor with \<filter\> match</span>](#People_with_a_common_ancestor_with_.3Cfilter.3E_match)
  - [<span class="tocnumber">5.9</span> <span class="toctext">People with a common ancestor with \<person\></span>](#People_with_a_common_ancestor_with_.3Cperson.3E)
- [<span class="tocnumber">6</span> <span class="toctext">Child filters</span>](#Child_filters)
  - [<span class="tocnumber">6.1</span> <span class="toctext">Families having child with id containing \<text\></span>](#Families_having_child_with_id_containing_.3Ctext.3E)
  - [<span class="tocnumber">6.2</span> <span class="toctext">Families with child with the \<name\></span>](#Families_with_child_with_the_.3Cname.3E)
  - [<span class="tocnumber">6.3</span> <span class="toctext">Families with twins</span>](#Families_with_twins)
- [<span class="tocnumber">7</span> <span class="toctext">Citation/source filters</span>](#Citation.2Fsource_filters)
  - [<span class="tocnumber">7.1</span> <span class="toctext">People-, and Relationships Category</span>](#People-.2C_and_Relationships_Category)
    - [<span class="tocnumber">7.1.1</span> <span class="toctext">People with \<count\> source</span>](#People_with_.3Ccount.3E_source)
    - [<span class="tocnumber">7.1.2</span> <span class="toctext">People with the \<citation\></span>](#People_with_the_.3Ccitation.3E)
    - [<span class="tocnumber">7.1.3</span> <span class="toctext">People with the \<source\></span>](#People_with_the_.3Csource.3E)
    - [<span class="tocnumber">7.1.4</span> <span class="toctext">Person with at least one direct source \>= \<confidence level\></span>](#Person_with_at_least_one_direct_source_.3E.3D_.3Cconfidence_level.3E)
  - [<span class="tocnumber">7.2</span> <span class="toctext">Families Category</span>](#Families_Category)
    - [<span class="tocnumber">7.2.1</span> <span class="toctext">Families with \<count\> sources</span>](#Families_with_.3Ccount.3E_sources)
    - [<span class="tocnumber">7.2.2</span> <span class="toctext">Families with at least one direct source \>= \<confidence level\></span>](#Families_with_at_least_one_direct_source_.3E.3D_.3Cconfidence_level.3E)
    - [<span class="tocnumber">7.2.3</span> <span class="toctext">Families with the \<citation\></span>](#Families_with_the_.3Ccitation.3E)
    - [<span class="tocnumber">7.2.4</span> <span class="toctext">Families with the \<source\></span>](#Families_with_the_.3Csource.3E)
  - [<span class="tocnumber">7.3</span> <span class="toctext">Events Category</span>](#Events_Category)
    - [<span class="tocnumber">7.3.1</span> <span class="toctext">Events with \<count\> source</span>](#Events_with_.3Ccount.3E_source)
    - [<span class="tocnumber">7.3.2</span> <span class="toctext">Events with at least one direct source \>= \<confidence level\></span>](#Events_with_at_least_one_direct_source_.3E.3D_.3Cconfidence_level.3E)
    - [<span class="tocnumber">7.3.3</span> <span class="toctext">Events with source matching the \<source filter\></span>](#Events_with_source_matching_the_.3Csource_filter.3E)
    - [<span class="tocnumber">7.3.4</span> <span class="toctext">Events with the \<citation\></span>](#Events_with_the_.3Ccitation.3E)
  - [<span class="tocnumber">7.4</span> <span class="toctext">Places Category</span>](#Places_Category)
    - [<span class="tocnumber">7.4.1</span> <span class="toctext">Place with \<count\> sources</span>](#Place_with_.3Ccount.3E_sources)
    - [<span class="tocnumber">7.4.2</span> <span class="toctext">Place with a direct source \>= \<confidence level\></span>](#Place_with_a_direct_source_.3E.3D_.3Cconfidence_level.3E)
    - [<span class="tocnumber">7.4.3</span> <span class="toctext">Place with the \<citation\></span>](#Place_with_the_.3Ccitation.3E)
    - [<span class="tocnumber">7.4.4</span> <span class="toctext">Places with the \<source\></span>](#Places_with_the_.3Csource.3E)
  - [<span class="tocnumber">7.5</span> <span class="toctext">Media Category</span>](#Media_Category)
    - [<span class="tocnumber">7.5.1</span> <span class="toctext">Media with \<count\> sources</span>](#Media_with_.3Ccount.3E_sources)
    - [<span class="tocnumber">7.5.2</span> <span class="toctext">Media with a direct source \>= \<confidence level\></span>](#Media_with_a_direct_source_.3E.3D_.3Cconfidence_level.3E)
    - [<span class="tocnumber">7.5.3</span> <span class="toctext">Media with the \<citation\></span>](#Media_with_the_.3Ccitation.3E)
    - [<span class="tocnumber">7.5.4</span> <span class="toctext">Media with the \<source\></span>](#Media_with_the_.3Csource.3E)
- [<span class="tocnumber">8</span> <span class="toctext">Descendant filters</span>](#Descendant_filters)
  - [<span class="tocnumber">8.1</span> <span class="toctext">Descendant family member of \<filter\> match</span>](#Descendant_family_member_of_.3Cfilter.3E_match)
  - [<span class="tocnumber">8.2</span> <span class="toctext">Descendant family member of \<person\></span>](#Descendant_family_member_of_.3Cperson.3E)
  - [<span class="tocnumber">8.3</span> <span class="toctext">Descendant of \<filter\> match</span>](#Descendant_of_.3Cfilter.3E_match)
  - [<span class="tocnumber">8.4</span> <span class="toctext">Descendant of \<person\></span>](#Descendant_of_.3Cperson.3E)
  - [<span class="tocnumber">8.5</span> <span class="toctext">Descendant of \<person\> at least \<N\> generations away</span>](#Descendant_of_.3Cperson.3E_at_least_.3CN.3E_generations_away)
  - [<span class="tocnumber">8.6</span> <span class="toctext">Descendant of \<person\> not more than \<N\> generations away</span>](#Descendant_of_.3Cperson.3E_not_more_than_.3CN.3E_generations_away)
- [<span class="tocnumber">9</span> <span class="toctext">Event filters</span>](#Event_filters)
  - [<span class="tocnumber">9.1</span> <span class="toctext">Events matching parameters</span>](#Events_matching_parameters)
  - [<span class="tocnumber">9.2</span> <span class="toctext">These filter rules are view dependent</span>](#These_filter_rules_are_view_dependent)
  - [<span class="tocnumber">9.3</span> <span class="toctext">People-, and Relationships Category</span>](#People-.2C_and_Relationships_Category_2)
    - [<span class="tocnumber">9.3.1</span> <span class="toctext">Families with incomplete events</span>](#Families_with_incomplete_events)
    - [<span class="tocnumber">9.3.2</span> <span class="toctext">People with incomplete events</span>](#People_with_incomplete_events)
    - [<span class="tocnumber">9.3.3</span> <span class="toctext">People with the \<birth data\></span>](#People_with_the_.3Cbirth_data.3E)
    - [<span class="tocnumber">9.3.4</span> <span class="toctext">People with the \<death data\></span>](#People_with_the_.3Cdeath_data.3E)
    - [<span class="tocnumber">9.3.5</span> <span class="toctext">People with the family \<event\></span>](#People_with_the_family_.3Cevent.3E)
    - [<span class="tocnumber">9.3.6</span> <span class="toctext">People with the personal \<event\></span>](#People_with_the_personal_.3Cevent.3E)
    - [<span class="tocnumber">9.3.7</span> <span class="toctext">Persons with events matching the \<event filter\></span>](#Persons_with_events_matching_the_.3Cevent_filter.3E)
    - [<span class="tocnumber">9.3.8</span> <span class="toctext">Witnesses</span>](#Witnesses)
      - [<span class="tocnumber">9.3.8.1</span> <span class="toctext">See Also</span>](#See_Also_3)
  - [<span class="tocnumber">9.4</span> <span class="toctext">Families Category</span>](#Families_Category_2)
    - [<span class="tocnumber">9.4.1</span> <span class="toctext">Families with the \<event\></span>](#Families_with_the_.3Cevent.3E)
- [<span class="tocnumber">10</span> <span class="toctext">Family filters</span>](#Family_filters)
  - [<span class="tocnumber">10.1</span> <span class="toctext">Adopted people</span>](#Adopted_people)
  - [<span class="tocnumber">10.2</span> <span class="toctext">Children of \<filter\> match</span>](#Children_of_.3Cfilter.3E_match)
  - [<span class="tocnumber">10.3</span> <span class="toctext">Parents of \<filter\> match</span>](#Parents_of_.3Cfilter.3E_match)
  - [<span class="tocnumber">10.4</span> <span class="toctext">People missing parents</span>](#People_missing_parents)
  - [<span class="tocnumber">10.5</span> <span class="toctext">People with children</span>](#People_with_children)
  - [<span class="tocnumber">10.6</span> <span class="toctext">People with multiple marriage records</span>](#People_with_multiple_marriage_records)
  - [<span class="tocnumber">10.7</span> <span class="toctext">People with no marriage records</span>](#People_with_no_marriage_records)
  - [<span class="tocnumber">10.8</span> <span class="toctext">People with the \<relationships\></span>](#People_with_the_.3Crelationships.3E)
  - [<span class="tocnumber">10.9</span> <span class="toctext">Siblings of \<filter\> match</span>](#Siblings_of_.3Cfilter.3E_match)
  - [<span class="tocnumber">10.10</span> <span class="toctext">Spouses of \<filter\> match</span>](#Spouses_of_.3Cfilter.3E_match)
- [<span class="tocnumber">11</span> <span class="toctext">Father filters</span>](#Father_filters)
  - [<span class="tocnumber">11.1</span> <span class="toctext">Families having father with Id containing \<text\></span>](#Families_having_father_with_Id_containing_.3Ctext.3E)
  - [<span class="tocnumber">11.2</span> <span class="toctext">Families with father with the \<name\></span>](#Families_with_father_with_the_.3Cname.3E)
- [<span class="tocnumber">12</span> <span class="toctext">General filters</span>](#General_filters)
  - [<span class="tocnumber">12.1</span> <span class="toctext">People-, and Relationships Category</span>](#People-.2C_and_Relationships_Category_3)
    - [<span class="tocnumber">12.1.1</span> <span class="toctext">Bookmarked people</span>](#Bookmarked_people)
    - [<span class="tocnumber">12.1.2</span> <span class="toctext">Home person</span>](#Home_person)
    - [<span class="tocnumber">12.1.3</span> <span class="toctext">Disconnected People</span>](#Disconnected_People)
    - [<span class="tocnumber">12.1.4</span> <span class="toctext">Everyone</span>](#Everyone)
    - [<span class="tocnumber">12.1.5</span> <span class="toctext">Females</span>](#Females)
    - [<span class="tocnumber">12.1.6</span> <span class="toctext">Males</span>](#Males)
    - [<span class="tocnumber">12.1.7</span> <span class="toctext">People having \<count\> notes</span>](#People_having_.3Ccount.3E_notes)
    - [<span class="tocnumber">12.1.8</span> <span class="toctext">People having notes containing \<text\></span>](#People_having_notes_containing_.3Ctext.3E)
    - [<span class="tocnumber">12.1.9</span> <span class="toctext">People marked private</span>](#People_marked_private)
    - [<span class="tocnumber">12.1.10</span> <span class="toctext">People matching the \<filter\></span>](#People_matching_the_.3Cfilter.3E)
    - [<span class="tocnumber">12.1.11</span> <span class="toctext">People not marked private</span>](#People_not_marked_private)
    - [<span class="tocnumber">12.1.12</span> <span class="toctext">People probably alive</span>](#People_probably_alive)
    - [<span class="tocnumber">12.1.13</span> <span class="toctext">People with \<count\> LDS events</span>](#People_with_.3Ccount.3E_LDS_events)
    - [<span class="tocnumber">12.1.14</span> <span class="toctext">People with \<count\> addresses</span>](#People_with_.3Ccount.3E_addresses)
    - [<span class="tocnumber">12.1.15</span> <span class="toctext">People with \<count\> associations</span>](#People_with_.3Ccount.3E_associations)
    - [<span class="tocnumber">12.1.16</span> <span class="toctext">People with \<count\> media</span>](#People_with_.3Ccount.3E_media)
    - [<span class="tocnumber">12.1.17</span> <span class="toctext">People with id containing \<text\></span>](#People_with_id_containing_.3Ctext.3E)
    - [<span class="tocnumber">12.1.18</span> <span class="toctext">People with a name matching \<text\></span>](#People_with_a_name_matching_.3Ctext.3E)
    - [<span class="tocnumber">12.1.19</span> <span class="toctext">People with a nickname</span>](#People_with_a_nickname)
    - [<span class="tocnumber">12.1.20</span> <span class="toctext">People with an alternate name</span>](#People_with_an_alternate_name)
    - [<span class="tocnumber">12.1.21</span> <span class="toctext">People with incomplete names</span>](#People_with_incomplete_names)
    - [<span class="tocnumber">12.1.22</span> <span class="toctext">People with records containing \<substring\></span>](#People_with_records_containing_.3Csubstring.3E)
    - [<span class="tocnumber">12.1.23</span> <span class="toctext">People with the \<Name type\></span>](#People_with_the_.3CName_type.3E)
    - [<span class="tocnumber">12.1.24</span> <span class="toctext">People with the \<Surname origin type\></span>](#People_with_the_.3CSurname_origin_type.3E)
    - [<span class="tocnumber">12.1.25</span> <span class="toctext">People with the \<name\></span>](#People_with_the_.3Cname.3E)
      - [<span class="tocnumber">12.1.25.1</span> <span class="toctext">See also</span>](#See_also_4)
    - [<span class="tocnumber">12.1.26</span> <span class="toctext">People with \<tag\></span>](#People_with_.3Ctag.3E)
    - [<span class="tocnumber">12.1.27</span> <span class="toctext">People with the family \<attribute\></span>](#People_with_the_family_.3Cattribute.3E)
    - [<span class="tocnumber">12.1.28</span> <span class="toctext">People with the personal \<attribute\></span>](#People_with_the_personal_.3Cattribute.3E)
    - [<span class="tocnumber">12.1.29</span> <span class="toctext">People with unknown gender</span>](#People_with_unknown_gender)
    - [<span class="tocnumber">12.1.30</span> <span class="toctext">People without a known birth date</span>](#People_without_a_known_birth_date)
    - [<span class="tocnumber">12.1.31</span> <span class="toctext">People without a known death date</span>](#People_without_a_known_death_date)
    - [<span class="tocnumber">12.1.32</span> <span class="toctext">People with \<id\></span>](#People_with_.3Cid.3E)
    - [<span class="tocnumber">12.1.33</span> <span class="toctext">People changed after \<date time\></span>](#People_changed_after_.3Cdate_time.3E)
    - [<span class="tocnumber">12.1.34</span> <span class="toctext">Soundex match of People with the \<name\></span>](#Soundex_match_of_People_with_the_.3Cname.3E)
  - [<span class="tocnumber">12.2</span> <span class="toctext">Families Category</span>](#Families_Category_3)
    - [<span class="tocnumber">12.2.1</span> <span class="toctext">Ancestor families of \<family\></span>](#Ancestor_families_of_.3Cfamily.3E)
    - [<span class="tocnumber">12.2.2</span> <span class="toctext">Bookmarked families</span>](#Bookmarked_families)
    - [<span class="tocnumber">12.2.3</span> <span class="toctext">Descendant families of \<family\></span>](#Descendant_families_of_.3Cfamily.3E)
    - [<span class="tocnumber">12.2.4</span> <span class="toctext">Every family</span>](#Every_family)
    - [<span class="tocnumber">12.2.5</span> <span class="toctext">Families changed after \<date time\></span>](#Families_changed_after_.3Cdate_time.3E)
    - [<span class="tocnumber">12.2.6</span> <span class="toctext">Families having \<count\> notes</span>](#Families_having_.3Ccount.3E_notes)
    - [<span class="tocnumber">12.2.7</span> <span class="toctext">Families having notes containing \<text\></span>](#Families_having_notes_containing_.3Ctext.3E)
    - [<span class="tocnumber">12.2.8</span> <span class="toctext">Families marked private</span>](#Families_marked_private)
    - [<span class="tocnumber">12.2.9</span> <span class="toctext">Families matching the \<filter\></span>](#Families_matching_the_.3Cfilter.3E)
    - [<span class="tocnumber">12.2.10</span> <span class="toctext">Families with \<count\> LDS events</span>](#Families_with_.3Ccount.3E_LDS_events)
    - [<span class="tocnumber">12.2.11</span> <span class="toctext">Families with \<count\> media</span>](#Families_with_.3Ccount.3E_media)
    - [<span class="tocnumber">12.2.12</span> <span class="toctext">Families with id containing \<text\></span>](#Families_with_id_containing_.3Ctext.3E)
    - [<span class="tocnumber">12.2.13</span> <span class="toctext">Families with a reference count of \<count\></span>](#Families_with_a_reference_count_of_.3Ccount.3E)
    - [<span class="tocnumber">12.2.14</span> <span class="toctext">Families with the \<tag\></span>](#Families_with_the_.3Ctag.3E)
    - [<span class="tocnumber">12.2.15</span> <span class="toctext">Families with the family \<attribute\></span>](#Families_with_the_family_.3Cattribute.3E)
    - [<span class="tocnumber">12.2.16</span> <span class="toctext">Families with the relationship type</span>](#Families_with_the_relationship_type)
    - [<span class="tocnumber">12.2.17</span> <span class="toctext">Families with \<id\></span>](#Families_with_.3Cid.3E)
  - [<span class="tocnumber">12.3</span> <span class="toctext">Events Category</span>](#Events_Category_2)
    - [<span class="tocnumber">12.3.1</span> <span class="toctext">Event with \<id\></span>](#Event_with_.3Cid.3E)
    - [<span class="tocnumber">12.3.2</span> <span class="toctext">Events changed after \<date time\></span>](#Events_changed_after_.3Cdate_time.3E)
    - [<span class="tocnumber">12.3.3</span> <span class="toctext">Events having \<count\> notes</span>](#Events_having_.3Ccount.3E_notes)
    - [<span class="tocnumber">12.3.4</span> <span class="toctext">Events having notes containing \<text\></span>](#Events_having_notes_containing_.3Ctext.3E)
    - [<span class="tocnumber">12.3.5</span> <span class="toctext">Events marked private</span>](#Events_marked_private)
    - [<span class="tocnumber">12.3.6</span> <span class="toctext">Events matching the \<filter\></span>](#Events_matching_the_.3Cfilter.3E)
    - [<span class="tocnumber">12.3.7</span> <span class="toctext">Events occurring on a particular day of the week</span>](#Events_occurring_on_a_particular_day_of_the_week)
    - [<span class="tocnumber">12.3.8</span> <span class="toctext">Events of persons matching the \<person filter\></span>](#Events_of_persons_matching_the_.3Cperson_filter.3E)
    - [<span class="tocnumber">12.3.9</span> <span class="toctext">Events of places matching the \<place filter\></span>](#Events_of_places_matching_the_.3Cplace_filter.3E)
    - [<span class="tocnumber">12.3.10</span> <span class="toctext">Events with \<count\> media</span>](#Events_with_.3Ccount.3E_media)
    - [<span class="tocnumber">12.3.11</span> <span class="toctext">Events with \<data\></span>](#Events_with_.3Cdata.3E)
    - [<span class="tocnumber">12.3.12</span> <span class="toctext">Events with Id containing \<text\></span>](#Events_with_Id_containing_.3Ctext.3E)
    - [<span class="tocnumber">12.3.13</span> <span class="toctext">Events with a reference count of \<count\></span>](#Events_with_a_reference_count_of_.3Ccount.3E)
    - [<span class="tocnumber">12.3.14</span> <span class="toctext">Events with the \<tag\></span>](#Events_with_the_.3Ctag.3E)
    - [<span class="tocnumber">12.3.15</span> <span class="toctext">Events with the attribute \<attribute\></span>](#Events_with_the_attribute_.3Cattribute.3E)
    - [<span class="tocnumber">12.3.16</span> <span class="toctext">Events with the particular type</span>](#Events_with_the_particular_type)
    - [<span class="tocnumber">12.3.17</span> <span class="toctext">Every event</span>](#Every_event)
  - [<span class="tocnumber">12.4</span> <span class="toctext">Places Category</span>](#Places_Category_2)
    - [<span class="tocnumber">12.4.1</span> <span class="toctext">Every place</span>](#Every_place)
    - [<span class="tocnumber">12.4.2</span> <span class="toctext">Place with \<Id\></span>](#Place_with_.3CId.3E)
    - [<span class="tocnumber">12.4.3</span> <span class="toctext">Places changed after \<date time\></span>](#Places_changed_after_.3Cdate_time.3E)
    - [<span class="tocnumber">12.4.4</span> <span class="toctext">Places enclosed by another place</span>](#Places_enclosed_by_another_place)
    - [<span class="tocnumber">12.4.5</span> <span class="toctext">Places having \<count\> notes</span>](#Places_having_.3Ccount.3E_notes)
    - [<span class="tocnumber">12.4.6</span> <span class="toctext">Places having notes containing \<text\></span>](#Places_having_notes_containing_.3Ctext.3E)
    - [<span class="tocnumber">12.4.7</span> <span class="toctext">Places marked private</span>](#Places_marked_private)
    - [<span class="tocnumber">12.4.8</span> <span class="toctext">Places matching a title</span>](#Places_matching_a_title)
    - [<span class="tocnumber">12.4.9</span> <span class="toctext">Places matching parameters</span>](#Places_matching_parameters)
    - [<span class="tocnumber">12.4.10</span> <span class="toctext">Places matching the \<filter\></span>](#Places_matching_the_.3Cfilter.3E)
    - [<span class="tocnumber">12.4.11</span> <span class="toctext">Places of events matching the \<event filter\></span>](#Places_of_events_matching_the_.3Cevent_filter.3E)
    - [<span class="tocnumber">12.4.12</span> <span class="toctext">Places with \<count\> media</span>](#Places_with_.3Ccount.3E_media)
    - [<span class="tocnumber">12.4.13</span> <span class="toctext">Places with Id containing \<text\></span>](#Places_with_Id_containing_.3Ctext.3E)
    - [<span class="tocnumber">12.4.14</span> <span class="toctext">Places with a reference count of \<count\></span>](#Places_with_a_reference_count_of_.3Ccount.3E)
    - [<span class="tocnumber">12.4.15</span> <span class="toctext">Places with the \<tag\></span>](#Places_with_the_.3Ctag.3E)
  - [<span class="tocnumber">12.5</span> <span class="toctext">Sources Category</span>](#Sources_Category)
    - [<span class="tocnumber">12.5.1</span> <span class="toctext">Every source</span>](#Every_source)
    - [<span class="tocnumber">12.5.2</span> <span class="toctext">Source with \<Id\></span>](#Source_with_.3CId.3E)
    - [<span class="tocnumber">12.5.3</span> <span class="toctext">Sources changed after \<date time\></span>](#Sources_changed_after_.3Cdate_time.3E)
    - [<span class="tocnumber">12.5.4</span> <span class="toctext">Sources having \<count\> notes</span>](#Sources_having_.3Ccount.3E_notes)
    - [<span class="tocnumber">12.5.5</span> <span class="toctext">Sources having notes containing \<text\></span>](#Sources_having_notes_containing_.3Ctext.3E)
    - [<span class="tocnumber">12.5.6</span> <span class="toctext">Sources marked private</span>](#Sources_marked_private)
    - [<span class="tocnumber">12.5.7</span> <span class="toctext">Sources matching the \<filter\></span>](#Sources_matching_the_.3Cfilter.3E)
    - [<span class="tocnumber">12.5.8</span> <span class="toctext">Sources with \<count\> Repository references</span>](#Sources_with_.3Ccount.3E_Repository_references)
    - [<span class="tocnumber">12.5.9</span> <span class="toctext">Sources with \<count\> media</span>](#Sources_with_.3Ccount.3E_media)
    - [<span class="tocnumber">12.5.10</span> <span class="toctext">Sources with Id containing \<text\></span>](#Sources_with_Id_containing_.3Ctext.3E)
    - [<span class="tocnumber">12.5.11</span> <span class="toctext">Sources with a reference count of \<count\></span>](#Sources_with_a_reference_count_of_.3Ccount.3E)
    - [<span class="tocnumber">12.5.12</span> <span class="toctext">Sources with repository reference containing \<text\> in "Call Number"</span>](#Sources_with_repository_reference_containing_.3Ctext.3E_in_.22Call_Number.22)
    - [<span class="tocnumber">12.5.13</span> <span class="toctext">Sources with repository reference matching the \<repository filter\></span>](#Sources_with_repository_reference_matching_the_.3Crepository_filter.3E)
    - [<span class="tocnumber">12.5.14</span> <span class="toctext">Sources with the \<tag\></span>](#Sources_with_the_.3Ctag.3E)
    - [<span class="tocnumber">12.5.15</span> <span class="toctext">Sources with title containing \<text\></span>](#Sources_with_title_containing_.3Ctext.3E)
  - [<span class="tocnumber">12.6</span> <span class="toctext">Citations Category</span>](#Citations_Category)
    - [<span class="tocnumber">12.6.1</span> <span class="toctext">Citation with \<Id\></span>](#Citation_with_.3CId.3E)
    - [<span class="tocnumber">12.6.2</span> <span class="toctext">Citations changed after \<date time\></span>](#Citations_changed_after_.3Cdate_time.3E)
    - [<span class="tocnumber">12.6.3</span> <span class="toctext">Citations having \<count\> notes</span>](#Citations_having_.3Ccount.3E_notes)
    - [<span class="tocnumber">12.6.4</span> <span class="toctext">Citations having notes containing \<text\></span>](#Citations_having_notes_containing_.3Ctext.3E)
    - [<span class="tocnumber">12.6.5</span> <span class="toctext">Citations marked private</span>](#Citations_marked_private)
    - [<span class="tocnumber">12.6.6</span> <span class="toctext">Citations matching parameters</span>](#Citations_matching_parameters)
    - [<span class="tocnumber">12.6.7</span> <span class="toctext">Citations matching the \<filter\></span>](#Citations_matching_the_.3Cfilter.3E)
    - [<span class="tocnumber">12.6.8</span> <span class="toctext">Citations with \<count\> media</span>](#Citations_with_.3Ccount.3E_media)
    - [<span class="tocnumber">12.6.9</span> <span class="toctext">Citations with Id containing \<text\></span>](#Citations_with_Id_containing_.3Ctext.3E)
    - [<span class="tocnumber">12.6.10</span> <span class="toctext">Citations with Volume/Page containing \<text\></span>](#Citations_with_Volume.2FPage_containing_.3Ctext.3E)
    - [<span class="tocnumber">12.6.11</span> <span class="toctext">Citations with a reference count of \<count\></span>](#Citations_with_a_reference_count_of_.3Ccount.3E)
    - [<span class="tocnumber">12.6.12</span> <span class="toctext">Citations with a source with a repository reference matching the \<repository filter\></span>](#Citations_with_a_source_with_a_repository_reference_matching_the_.3Crepository_filter.3E)
    - [<span class="tocnumber">12.6.13</span> <span class="toctext">Citations with source matching the \<source filter\></span>](#Citations_with_source_matching_the_.3Csource_filter.3E)
    - [<span class="tocnumber">12.6.14</span> <span class="toctext">Citations with the \<tag\></span>](#Citations_with_the_.3Ctag.3E)
    - [<span class="tocnumber">12.6.15</span> <span class="toctext">Every citation</span>](#Every_citation)
  - [<span class="tocnumber">12.7</span> <span class="toctext">Repositories Category</span>](#Repositories_Category)
    - [<span class="tocnumber">12.7.1</span> <span class="toctext">Every repository</span>](#Every_repository)
    - [<span class="tocnumber">12.7.2</span> <span class="toctext">Repositories changed after \<date time\></span>](#Repositories_changed_after_.3Cdate_time.3E)
    - [<span class="tocnumber">12.7.3</span> <span class="toctext">Repositories having notes containing \<text\></span>](#Repositories_having_notes_containing_.3Ctext.3E)
    - [<span class="tocnumber">12.7.4</span> <span class="toctext">Repositories marked private</span>](#Repositories_marked_private)
    - [<span class="tocnumber">12.7.5</span> <span class="toctext">Repositories matching parameters</span>](#Repositories_matching_parameters)
    - [<span class="tocnumber">12.7.6</span> <span class="toctext">Repositories matching the \<filter\></span>](#Repositories_matching_the_.3Cfilter.3E)
    - [<span class="tocnumber">12.7.7</span> <span class="toctext">Repositories with Id containing \<text\></span>](#Repositories_with_Id_containing_.3Ctext.3E)
    - [<span class="tocnumber">12.7.8</span> <span class="toctext">Repositories with a reference count of \<count\></span>](#Repositories_with_a_reference_count_of_.3Ccount.3E)
    - [<span class="tocnumber">12.7.9</span> <span class="toctext">Repositories with name containing \<text\></span>](#Repositories_with_name_containing_.3Ctext.3E)
    - [<span class="tocnumber">12.7.10</span> <span class="toctext">Repositories with the \<tag\></span>](#Repositories_with_the_.3Ctag.3E)
    - [<span class="tocnumber">12.7.11</span> <span class="toctext">Repository with \<Id\></span>](#Repository_with_.3CId.3E)
  - [<span class="tocnumber">12.8</span> <span class="toctext">Media Category</span>](#Media_Category_2)
    - [<span class="tocnumber">12.8.1</span> <span class="toctext">Every media object</span>](#Every_media_object)
    - [<span class="tocnumber">12.8.2</span> <span class="toctext">Media object with \<Id\></span>](#Media_object_with_.3CId.3E)
    - [<span class="tocnumber">12.8.3</span> <span class="toctext">Media objects changed after \<date time\></span>](#Media_objects_changed_after_.3Cdate_time.3E)
    - [<span class="tocnumber">12.8.4</span> <span class="toctext">Media objects having notes containing \<text\></span>](#Media_objects_having_notes_containing_.3Ctext.3E)
    - [<span class="tocnumber">12.8.5</span> <span class="toctext">Media objects marked private</span>](#Media_objects_marked_private)
    - [<span class="tocnumber">12.8.6</span> <span class="toctext">Media objects matching parameters</span>](#Media_objects_matching_parameters)
    - [<span class="tocnumber">12.8.7</span> <span class="toctext">Media objects matching the \<filter\></span>](#Media_objects_matching_the_.3Cfilter.3E)
    - [<span class="tocnumber">12.8.8</span> <span class="toctext">Media objects with Id containing \<text\></span>](#Media_objects_with_Id_containing_.3Ctext.3E)
    - [<span class="tocnumber">12.8.9</span> <span class="toctext">Media objects with a reference count of \<count\></span>](#Media_objects_with_a_reference_count_of_.3Ccount.3E)
    - [<span class="tocnumber">12.8.10</span> <span class="toctext">Media objects with the \<tag\></span>](#Media_objects_with_the_.3Ctag.3E)
    - [<span class="tocnumber">12.8.11</span> <span class="toctext">Media objects with the attribute \<attribute\></span>](#Media_objects_with_the_attribute_.3Cattribute.3E)
  - [<span class="tocnumber">12.9</span> <span class="toctext">Notes Category</span>](#Notes_Category)
    - [<span class="tocnumber">12.9.1</span> <span class="toctext">Every note</span>](#Every_note)
    - [<span class="tocnumber">12.9.2</span> <span class="toctext">Note with \<Id\></span>](#Note_with_.3CId.3E)
    - [<span class="tocnumber">12.9.3</span> <span class="toctext">Notes changed after \<date time\></span>](#Notes_changed_after_.3Cdate_time.3E)
    - [<span class="tocnumber">12.9.4</span> <span class="toctext">Notes containing \<text\></span>](#Notes_containing_.3Ctext.3E)
    - [<span class="tocnumber">12.9.5</span> <span class="toctext">Notes marked private</span>](#Notes_marked_private)
    - [<span class="tocnumber">12.9.6</span> <span class="toctext">Notes matching parameters</span>](#Notes_matching_parameters)
    - [<span class="tocnumber">12.9.7</span> <span class="toctext">Notes matching the \<filter\></span>](#Notes_matching_the_.3Cfilter.3E)
    - [<span class="tocnumber">12.9.8</span> <span class="toctext">Notes with Id containing \<text\></span>](#Notes_with_Id_containing_.3Ctext.3E)
    - [<span class="tocnumber">12.9.9</span> <span class="toctext">Notes with a reference count of \<count\></span>](#Notes_with_a_reference_count_of_.3Ccount.3E)
    - [<span class="tocnumber">12.9.10</span> <span class="toctext">Notes with the \<tag\></span>](#Notes_with_the_.3Ctag.3E)
    - [<span class="tocnumber">12.9.11</span> <span class="toctext">Notes with the particular type</span>](#Notes_with_the_particular_type)
- [<span class="tocnumber">13</span> <span class="toctext">Mother filters</span>](#Mother_filters)
  - [<span class="tocnumber">13.1</span> <span class="toctext">Families having mother with Id containing \<text\></span>](#Families_having_mother_with_Id_containing_.3Ctext.3E)
  - [<span class="tocnumber">13.2</span> <span class="toctext">Families with mother with the \<name\></span>](#Families_with_mother_with_the_.3Cname.3E)
- [<span class="tocnumber">14</span> <span class="toctext">Position filters</span>](#Position_filters)
  - [<span class="tocnumber">14.1</span> <span class="toctext">Places in neighborhood of given position</span>](#Places_in_neighborhood_of_given_position)
  - [<span class="tocnumber">14.2</span> <span class="toctext">Places with no latitude or longitude given</span>](#Places_with_no_latitude_or_longitude_given)
  - [<span class="tocnumber">14.3</span> <span class="toctext">Places within an area</span>](#Places_within_an_area)
- [<span class="tocnumber">15</span> <span class="toctext">Source filters</span>](#Source_filters)
  - [<span class="tocnumber">15.1</span> <span class="toctext">Citation with Source \<Id\></span>](#Citation_with_Source_.3CId.3E)
  - [<span class="tocnumber">15.2</span> <span class="toctext">Citations having source notes containing \<text\></span>](#Citations_having_source_notes_containing_.3Ctext.3E)
  - [<span class="tocnumber">15.3</span> <span class="toctext">Citations with Source Id containing \<text\></span>](#Citations_with_Source_Id_containing_.3Ctext.3E)
  - [<span class="tocnumber">15.4</span> <span class="toctext">Sources matching parameters</span>](#Sources_matching_parameters)
- [<span class="tocnumber">16</span> <span class="toctext">Relationship filters</span>](#Relationship_filters)
  - [<span class="tocnumber">16.1</span> <span class="toctext">People related to \<Person\></span>](#People_related_to_.3CPerson.3E)
  - [<span class="tocnumber">16.2</span> <span class="toctext">Relationship path between \<person\> and people matching \<filter\></span>](#Relationship_path_between_.3Cperson.3E_and_people_matching_.3Cfilter.3E)
  - [<span class="tocnumber">16.3</span> <span class="toctext">Relationship path between \<persons\></span>](#Relationship_path_between_.3Cpersons.3E)
  - [<span class="tocnumber">16.4</span> <span class="toctext">Relationship path between bookmarked persons</span>](#Relationship_path_between_bookmarked_persons)
- [<span class="tocnumber">17</span> <span class="toctext">Tagging</span>](#Tagging)
  - [<span class="tocnumber">17.1</span> <span class="toctext">Tag menu</span>](#Tag_menu)
  - [<span class="tocnumber">17.2</span> <span class="toctext">Tag selected rows icon toolbar</span>](#Tag_selected_rows_icon_toolbar)
  - [<span class="tocnumber">17.3</span> <span class="toctext">New Tag dialog</span>](#New_Tag_dialog)
    - [<span class="tocnumber">17.3.1</span> <span class="toctext">Tagging a selection of objects</span>](#Tagging_a_selection_of_objects)
  - [<span class="tocnumber">17.4</span> <span class="toctext">Organize Tags Window</span>](#Organize_Tags_Window)
    - [<span class="tocnumber">17.4.1</span> <span class="toctext">Remove tag \<tag name\> dialog</span>](#Remove_tag_.3Ctag_name.3E_dialog)
  - [<span class="tocnumber">17.5</span> <span class="toctext">Tag selection dialog</span>](#Tag_selection_dialog)
  - [<span class="tocnumber">17.6</span> <span class="toctext">Usage of tags</span>](#Usage_of_tags)
    - [<span class="tocnumber">17.6.1</span> <span class="toctext">Filtering</span>](#Filtering)
    - [<span class="tocnumber">17.6.2</span> <span class="toctext">Tags Column</span>](#Tags_Column)
    - [<span class="tocnumber">17.6.3</span> <span class="toctext">Tag Usage Report</span>](#Tag_Usage_Report)
  - [<span class="tocnumber">17.7</span> <span class="toctext">See also</span>](#See_also_5)

## <span id="Filter_vs._Search" class="mw-headline">Filter vs. Search</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

There are two primary ways to find data in Gramps: Search and Filter.

- Search uses the [Search Bar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Search_bar) above a listing View (such as People, Families, etc).  
  The [Search Bar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Search_bar) only appears when the entire sidebar is closed. You can show or hide the Gramplet bars through changing the selection of the **View ➡ ☑Sidebar** or **View ➡ ☑Bottombar** menus.
- Custom Filters are selected from pop-up menus in the Filter Gramplet, export option and in some reports. They can be used in combination with Search, or stand-alone in the sidebar/bottombar Gramplets. Custom Filters are created or edited from the filter Gramplet or **Edit ➡ Filter Editor** menu.

(There is also a basic *seek-as-you-type* [Find box](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Finding_records) for navigating the active record focus within list view and object selector lists.)

  

<table style="width:80%;margin-top:+.7em;margin-bottom:+.7em;background-color: #ddffcc85;border:1px solid #ccc; padding: 5px" data-align="center">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 60px">![[_media/Gramps-notes.png]]</td>
<td><div style="font-size:110%">
<strong>Name filtering behavior has <a href="/wiki/index.php/Addon:Rule_expansions#Gramps_5.1.0_.28Aug._2019.29" title="Addon:Rule expansions">changed</a>. In prior versions of Gramps, the name portion of the Filter Gramplet would try to match on any single name field (given, surname, prefix, etc) of all names (primary and alternate) but only field per name — you couldn't match the given field and surname field in the same name. You could match surname, but simultaneously matching surname and given in the same query wasn't possible. For example, if you Filter on "John", you would get matches of people with firstname "John" but also those with surname "Johnson". More complex search required use of the regular expressions pattern matching options or custom filters.<br />
<br />
This constraint has been removed and simultaneous search of multiple terms is now the default behavior.</strong>
</div>
<hr /></td>
</tr>
</tbody>
</table>

Search and Filter work completely differently and it is useful to understand these differences:

- *Search* - the [Search Bar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Search_bar) looks through the database as it appears in the rows and columns on the screen. The Search functionality is probably the one you want to use most of the time, as it is fast and most straightforward. But speed and simplicity imposes some limitations (see below).

For example, if you have the Name Display in Preferences set to show "Surname, Given" then you can match names such as "Smith, J" and all of the correct rows will match. If you change the way that names are displayed (in Preferences) then you can match that format (for example, "John Smith").

<div class="thumb tright">

<div class="thumbinner" style="width:452px;">

![[_media/MainWindow-SearchBar-sidebar-hidden-example-60.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:MainWindow-SearchBar-sidebar-hidden-example-60.png" class="internal" title="Enlarge"></a>

</div>

Fig. 16.2 Gramps Main Window showing [Search Bar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Search_bar)

</div>

</div>

</div>

- *Filter* - Filters use a more elaborate system. It is not limited to what you see on the screen, but looks at the actual data in all name fields, rather than just what is showing in the View. Entering multiple words does phrase matching for most text fields. However, the Name filter line is far more powerful. Each word in the Name search is handled separately as though it was a sub-search on the records found with the previous search word. And it simultaneously searches ***all*** the Name fields.

e.g. a name search of "geo r." in the [example tree](wiki:Example.gramps) database finds 5 people: with a variety 'Jr.' & 'Sr.' as the suffix and 'George's as first & middle names. Or searching "garn ski ph" finds Phoebe Emily who has a birth surname of Zieliński and alternate married surname of Garner.

<div class="thumb tright">

<div class="thumbinner" style="width:372px;">

![[_media/Sidebar-PeopleTreeView-Filter-TagDropDownList-example-60.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:Sidebar-PeopleTreeView-Filter-TagDropDownList-example-60.png" class="internal" title="Enlarge"></a>

</div>

Fig. 16.3 Gramps Filter SideBar for People view - [Tag](wiki:Gramps_Glossary#tag) drop-down list example

</div>

</div>

</div>

Filters can be created and controlled from the menu **Edit ➡ Filter Editor**, or from a special sidebar/bottombar Gramplet. The Filter Gramplets allow for some quick filters that are similar to the [Search Bar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Search_bar), but all Filters follow the distinction outlined here.

Some additional points:

- The Filter will search alternative & multiple names too; the [Search Bar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Search_bar) only looks in the primary name... the one showing in the People view. That is why doing a Filter on "Smith" might list people that superficially don't appear to match. But if you drill down into that person's details with the [Name Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_3#Name_Editor), you might see that they have an alternate name containing "smith".
- The Filter allows "regular expressions". So you can find all of the names that start with "B" and end in "ship": "B.\*ship". You can't do that with the [Search Bar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Search_bar).
- The Search will only match what is visible. If a name or text is too big to see in listing below [Search Bar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Search_bar), then you won't find it. This is something to keep in mind when Searching through Notes. Best to use Filter for notes and other long text fields.
- All Filters default to use case-insensitive matching; "Ship" will match "ship", "SHIP", or "ShIp". As explained below under Regular Expressions, using Regular Expressions does not currently give a means of changing from the default.

### <span id="See_also" class="mw-headline">See also</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

- [Find a Record](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Find_a_Record) - (aka: "interactive type-ahead search" or "seek as you type")
- [Filter](wiki:Gramps_Glossary#filter) - a definition
- <span class="mw-selflink selflink">Filters introduction</span> in the Gramps Manual
- [Which filters in which Category?](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Which_filters_in_which_Category.3F)
- [Filter](wiki:Filter)
- [Example filters](wiki:Example_filters) - Multi-stage filters
- [Rules](wiki:Gramps_Glossary#rule) - a definition
- [Addon list - Rules](wiki:6.0_Addons#Addon_List)
- [Expanding the Filter rulebook](wiki:Addon:Rule_expansions) with Addons
- [Category: Filters](wiki:Category:Filters)
- [Custom Filter migration](wiki:Template:Backup_Omissions) - backing up a Gramps Tree does not include any filter customizations

  

## <span id="Regular_Expressions" class="mw-headline">Regular Expressions</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

<a href="https://wikipedia.org/wiki/Regular_expression" class="external text" rel="nofollow">Regular Expressions</a>(aka *regex*, *regexp*, or sometimes *rational expression*) are a condensed, precise and powerful way to describe text that matches a pattern.

Designing a effective search pattern can be formulaic. Like math formulas, a search pattern can be quickly composed which finds a subset of records but does so very crudely and slowly. Elegant and efficient RegEx phrases are collected by optimization experts in data manipulations. There are many resources (books, websites, professional training) for RegEx design and strategy.

Gramps uses RegEx as a matching option that may be enabled for Custom Filters and in the Filter Gramplets of each Category view.

RegEx pattern matching is an advanced feature and so its checkbox is not selected by default. For Custom Filters, each individual Rule has a

<div style="float:left; width:.9em; height:.9em; margin-right:0.5em; vertical-align:-.1em; border:1px solid #111; background:#666;">

</div>

<span style=""></span>**<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Use regular expressions</span>** option check box in its Edit Rule dialog. The Filter Gramplets also have

<div style="float:left; width:.9em; height:.9em; margin-right:0.5em; vertical-align:-.1em; border:1px solid #111; background:#666;">

</div>

<span style=""></span>**<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Use regular expressions</span>** option check boxes to allow regexp expression to be used directly for matching strings in their text boxes.

For example, if you were looking for a surname that started with a "B", and ended with "ship" then you could use regular expressions to describe that pattern. That would be **`^B.*ship`**:

- The **`^B`** indicates text that starts with B
- The **`.`** indicates any single character (letter, number, or anything)
- The **`*`** indicates zero or more of the previous (in this case, any single character)
- The **`ship`** matches the exact letters s, h, i, p in that order.

Regular expressions are quite powerful, and there are many options. We use the <a href="https://docs.python.org/3/library/re.html" class="external text" rel="nofollow">Python Regular Expression</a> system, and we will document that here. In addition, you can use any Python Regular Expression resource.

Gramps is currently implemented to make all string matching case-insensitive (which is the opposite of the usual default in Python). There is no easy way at present to override this behaviour for the relatively uncommon purpose of matching strings that have been entered into the database in a particular case format. Regular expressions in Gramps currently give identical results regardless of whether the target string is entered in upper case, title case, lower case or some mixture.

*whitespace* - The term "whitespace" is used below to mean one or more character that you don't see. For example, whitespace includes tabs, spaces, and newlines.

There are some characters that have special meaning with regular expressions. They are:

- **`. ^ $ * + ? { } [ ] \ | ( )`**  
  decimal point (full stop), caret, dollar sign, asterisk, plus sign, question mark, left and right curly braces, left and right square brackets, backslash, vertical bar (pipe), left and right parentheses

  
They can be used as described:

- '`.`' matches any character (letter, number, or other)
- '`^`' matches beginning of text
- '`$`' matches end of text
- '`*`' matches zero or more of the previous item
- '`+`' matches one or more of the previous item
- '`?`' matches zero or one of the previous item (makes it optional)
- '`{`' - defines a number of matches
- '`}`' - ends number of matches
- '`[`' - beginning of set
- '`]`' - end of set
- '`\`' - next character is special sequence
- '`|`' - or
- '`(`' - beginning of a group
- '`)`' - ending of a group

Some of the special sequences beginning with '`\`' represent predefined sets of characters that are often useful, such as the set of digits, the set of letters, or the set of anything that isn't whitespace. The following predefined special sequences are a subset of those available.

- `\d` Matches any decimal digit; this is equivalent to the class `[0-9]`.
- `\D` Matches any non-digit character; this is equivalent to the class `[^0-9]`.
- `\s` Matches any whitespace character; this is equivalent to the class `[ \t\n\r\f\v]`.
- `\S` Matches any non-whitespace character; this is equivalent to the class `[^ \t\n\r\f\v]`.
- `\w` Matches any alphanumeric character; this is equivalent to the class `[a-zA-Z0-9_]`.
- `\W` Matches any non-alphanumeric character; this is equivalent to the class `[^a-zA-Z0-9_]`.

The most complicated repeated qualifier is `{m,n}`, where `m` and `n` are decimal integers. This qualifier means there must be at least `m` repetitions, and at most `n`.

### <span id="Find_all_defined_values_or_blanks" class="mw-headline">Find all defined values or blanks</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

<span id="regex_all">To find all values, `(.|\s)*` will match: any character or any whitespace character; and zero or more repetitions of those.</span>

<span id="regex_null">To find empty (blank or null) strings, `^.{0}$` looks from the start of the match `^` for any character (except newline) `.` occurring precisely zero times `{0}` before the end of the match `$`</span>

### <span id="Groups_and_Sets" class="mw-headline">Groups and Sets</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Groups are marked by the '`('`, '`)`' metacharacters. '`(`' and '`)`' have much the same meaning as they do in mathematical expressions; they group together the expressions contained inside them, and you can repeat the contents of a group with a repeating qualifier, such as `*, +, ?, or {m,n}`. For example, `(ab)*` will match zero or more repetitions of `ab`.

Sets are marked by the '`[`' and '`]`' metacharacters.

You can think of groups as a list of alternatives separated by the '`|`' metacharacter, where each alternative consists of one, several or zero characters and sets as a list of alternatives where each alternative is a single character.

### <span id="Examples" class="mw-headline">Examples</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

- **`^B.*ship$`** - matches all text that starts with a '`B`', followed by anything, ending with '`ship`'.
  - matches: **`Blankenship`**, **`Blueship`**, **`Beeship`**
  - does not match: **`Blankenships`**
- **`^B.*ship`** - matches all text that starts with a '`B`', followed by anything, followed by '`ship`' (could be followed by more).
  - matches: **`Blankenship`**, **`Blankenships`**, **`Blueship`**, **`Blueshipman`**, **`Beeship`**, **`Beeshipness`**
  - does not match: **`Blankenschips`**

#### <span id="Common_variations_of_a_surname" class="mw-headline">Common variations of a surname</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Example 1  
Using the expression **`Eri(ch|ck|k|c)(ss|s)on`** the following are matched:

<!-- -->

    Erikson
    Eriksson
    Ericson
    Ericsson
    Erickson
    Ericksson
    Erichson
    Erichsson

**Explanation**: Because of the following

- **`Eri`** = Eri
- **`(ch|ck|k|c)`** = group matching **`ch`**, **`ck`**, **`k`** or **`c`**. It tries to make the longest match first
- **`(ss|s)`** = group matching **`ss`** or **`s`**. It tries to make the longest match first
- **`on`** = on

------------------------------------------------------------------------

Example 2  
Using the expression **`Ba(in|yn|m|n)bri(dge|cke|g(g|e|))`** the following are matched:

<!-- -->

    Bainbricke
    Bainbridge
    Bainbrig
    Bainbrigg
    Bambridge
    Banbrig
    Banbrige
    Baynbrige

**Explanation:** Because of the following

- **`Ba`** = Ba
- **`(in|yn|m|n)`** = group matching **in**, **yn**, **m** or **n**. It tries to make the longest match first.
- **`bri`** = bri
- **`(dge|cke|g(g|e|))`** = group matching **dge**, **cke** or (**g** with **g**, **g** with **e** or **g** with nothing)

------------------------------------------------------------------------

Example 3  
Using the expression **`n(es|oua|oai|o[iya]|a[iy])r(r|)(on|((e|)au(x|t|d|lt|)))`** the following are matched:

<!-- -->

    nairaud
    nairault
    naireaud
    nayrault
    nesrau                
    nesrault
    nesreau
    nesreaud
    noirau
    noiraud
    noirauld
    noirault
    noiraut
    noiraux
    noireau
    noireaud
    noireault
    noireaut
    noirraux
    noirreau
    noirreaud
    nouarault
    noyraud
    noyrault 

**Explanation:** Because of the following

- **`n`** = n
- **`(es|oua|oai|set1|set2)`** = group matching **es**, **oua**, **oai**, **set1** or **set2**
- **`set1`** is **`o[iya]`** = set matching **o** AND **i**, **y** or **a**. In other words **oi**, **oy** or **oa**
- **`set2`** is **`a[iy]`** = set matching **a** AND **i** or **y**. In other words **ai** or **ay**
- **`r`** = r
- **`(r|)`** = group matching **r** or nothing
- **`(on|(subgroup1)`** = group matching **on** or **subgroup1**.
- **subgroup1** is group matching (**subgroup2 au subgroup3**)
- **subgroup2** is **(e\|)** = group matching **e** or nothing
- **`au`** = au
- **subgroup3** is **(x\|t\|d\|lt)** = group matching **x**, **t**, **d** or **lt**

#### <span id="Testing_regular_expressions" class="mw-headline">Testing regular expressions</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Regular Expression testers can be found online through Google. <a href="https://regexr.com/" class="external free" rel="nofollow">https://regexr.com/</a> is simple and convenient

### <span id="See_Also_2" class="mw-headline">See Also</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Regular expressions have been in wide use across the computer industry since the 1950s. But they are "expert tools" designed for power and efficiency rather than intuitiveness. As a result, many resources have been developed on the web.

Some of these resources have excellent tutorials. Some have cheat sheets. Some have “sand boxes” where regular expressions can be explored in real-time.

A sampling of RegEx reference websites:

- <a href="http://rexegg.com/" class="external text" rel="nofollow">rexegg.com</a> (tutorials)
- <a href="https://www.regular-expressions.info/" class="external text" rel="nofollow">RegexBuddy</a>
- <a href="https://regex101.com/" class="external text" rel="nofollow">regex101.com</a> (sandbox with feedback)

## <span id="Custom_Filters" class="mw-headline">Custom Filters</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

<table style="width:80%;margin-top:+.7em;margin-bottom:+.7em;background-color: #c0f0ff85;border:1px solid #ccc; padding: 5px" data-align="center">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 60px">![[_media/Tango-Dialog-information.png]]</td>
<td><div style="font-size:110%">
<strong>Custom Filter migration</strong>
</div>
<hr />
<p>Keep your collection of custom filters through a minor updates of Gramps (e.g., from version 5.0.x to 6.0.x) by manually copying your <em>custom_filter.xml</em> from <a href="/wiki/index.php/Gramps_User_Directory" class="mw-redirect" title="Gramps User Directory">Gramps User Directory</a> to the corresponding directory in new <em>gramps_version_number</em>.<br />
<br />
Even minor upgrades (e.g., from a 5.0.x to a 6.0.x version) may include format changes since the recent innovation of addon rules are causing rapid evolution in Filters. So porting filters in this manner requires verification that the XML definitions haven't changed. Also, Addon rules may have to be installed in the new upgrade before copied custom filters will work safely.</p></td>
</tr>
</tbody>
</table>

  
You can carry out a considerable amount of selection of persons, events, places, etc., just using the Filter Sidebar in Person, Event, Place,etc. Views; but note, however, that the 'Use regular expressions' option **only works with particular fields** in each View.

If the Filter Sidebar is inadequate for your purpose, you will need to build custom filters.

<table style="width:80%;margin-top:+.7em;margin-bottom:+.7em;background-color: #c0f0ff85;border:1px solid #ccc; padding: 5px" data-align="center">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 60px">![[_media/Tango-Dialog-information.png]]</td>
<td><div style="font-size:110%">
<strong>Building a quick Custom Filter for an object</strong>
</div>
<hr />
<p>The clipboard has a Custom Filter generation shortcut. Copy any View object to the Clipboard (by drag'n'drop or by selecting and pressing the <kbd class="keyboard-key" style="border: 1px solid; border-color: #ddd #bbb #bbb #ddd; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; background-color: #f9f9f9; padding: 1px 3px; font-family: inherit; font-size: 0.85em; white-space: nowrap;">Ctrl</kbd>+<kbd class="keyboard-key" style="border: 1px solid; border-color: #ddd #bbb #bbb #ddd; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; background-color: #f9f9f9; padding: 1px 3px; font-family: inherit; font-size: 0.85em; white-space: nowrap;">C</kbd> <a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Keybindings" title="Gramps 6.0 Wiki Manual - Keybindings">keybinding</a>), then select the object on the Clipboard and right-click to reveal the <a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Navigation#Clipboard_context_menu" title="Gramps 6.0 Wiki Manual - Navigation">Clipboard's contextual pop-up menu</a>. The bottom menu item will offer to create a Filter for the selected object.</p></td>
</tr>
</tbody>
</table>

<span id="CategoryName_Filters_dialog"></span>

### <span id="<category>_Filters_editor_dialog"></span><span id=".3Ccategory.3E_Filters_editor_dialog" class="mw-headline">\<category\> Filters editor dialog</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

There is a **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">'\<category\>' Filter Editor</span>** option in the **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Edit</span>** menu for each category. (i.e., The '\<category\>' is a placeholder. We mean it stands for the Person, Event, Sources or other categories that is currently active.) This dialog shows a list all the Custom Filters specific to the current category and allows you to manage those Custom Filters. (Similar to the way the [Organize Tags dialog](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Organize_Tags_Window) allows managing Tags.) There is no option to simultaneously organize the custom filters in all categories.

<table style="width:80%;margin-top:+.7em;margin-bottom:+.7em;background-color: #ddffcc85;border:1px solid #ccc; padding: 5px" data-align="center">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 60px">![[_media/Gramps-notes.png]]</td>
<td><div style="font-size:110%">
<strong>Note:Changes on filters</strong>
</div>
<hr />
<p>The changes made to the filters only take effect after you use the <kbd style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Close</kbd> button from this window.</p></td>
</tr>
</tbody>
</table>

<div class="thumb tright">

<div class="thumbinner" style="width:400px;">

![[_media/PersonFilters-dialog-example-50.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:PersonFilters-dialog-example-50.png" class="internal" title="Enlarge"></a>

</div>

Fig. 16.4 Person Filters - dialog - example

</div>

</div>

</div>

To create new or show previously created custom filters use the **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">*\<category\>* Filters</span>** editor dialog list where the *\<category\>* name changes based on the category currently selected in the Navigator:

- ![[_media/16x16-gramps-person.png|People]] Person Filters
- ![[_media/16x16-gramps-family.png|Family]] Family Filters
- ![[_media/22x22-gramps-event.png|Events]] Event Filters
- ![[_media/16x16-gramps-place.png|Places]] Place Filters
- ![[_media/48x48-gramps-source34.png|Sources (v3.4.x)]] Source Filters
- ![[_media/48x48-gramps-citation.png|Citations]] Citation Filters
- ![[_media/16x16-gramps-repository.png|Repositories]] Repository Filters
- ![[_media/Gramps-media.png|Media]] Media Filters
- ![[_media/16x16-gramps-notes.png|Notes]] Note Filters

When in the **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">*CategoryName* Filters</span>** dialog you have the following options from the right hand side icons:

- <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;"> ![[_media/Stock_add.png|STOCK_ADD]]</span> **<span class="kbd" style="background:#f7f7d7; color:#000000; font-family:Sans-Serif; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;border-style: dotted;}">Add a new filter</span>**

shows the **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Define filter</span>** dialog and adds a new (as yet unnamed) custom filter framework.

- <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;"> ![[_media/Stock_edit.png|STOCK_EDIT]]</span> **<span class="kbd" style="background:#f7f7d7; color:#000000; font-family:Sans-Serif; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;border-style: dotted;}">Edit the selected filter</span>**

opens the **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Define filter</span>** dialog and loads your existing custom filter for editing.

- <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Clone</span> **<span class="kbd" style="background:#f7f7d7; color:#000000; font-family:Sans-Serif; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;border-style: dotted;}">Clone the selected filter</span>**

makes an exact copy of the selected filter

- <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Test</span> **<span class="kbd" style="background:#f7f7d7; color:#000000; font-family:Sans-Serif; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;border-style: dotted;}">Test the selected filter</span>**

brings up the **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Filter Test</span>** results dialog containing a list of matches following a successful test. If the filter test is invalid, an error may be shown instead.

- <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;"> ![[_media/Stock_remove.png|STOCK_REMOVE]]</span> **<span class="kbd" style="background:#f7f7d7; color:#000000; font-family:Sans-Serif; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;border-style: dotted;}">Delete the selected filter</span>**:

removes the selected filter from the Gramps collection of custom filters.

  

#### <span id="Filter_Test_dialog" class="mw-headline">Filter Test dialog</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

<div class="thumb tright">

<div class="thumbinner" style="width:452px;">

![[_media/FilterTest-results-for-TestTheSelectedFilter-button-example-50.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:FilterTest-results-for-TestTheSelectedFilter-button-example-50.png" class="internal" title="Enlarge"></a>

</div>

Fig. 16.5 Filter Test - results list example from Person Filters

</div>

</div>

</div>

The results list of a successful **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Filter Test</span>** dialog might be empty, a valid custom filter might not match any records.  

### <span id="Define_Filter_dialog" class="mw-headline">Define Filter dialog</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

<table style="width:80%;margin-top:+.7em;margin-bottom:+.7em;background-color: #c0f0ff85;border:1px solid #ccc; padding: 5px" data-align="center">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 60px">![[_media/Tango-Dialog-information.png]]</td>
<td><div style="font-size:110%">
<strong>Addon Rules for custom filters are available</strong>
</div>
<hr />
<p>Filter Rules can be expanded through the addons interface starting with the Aug.2019 version.<br />
<em>See: <strong><a href="/wiki/index.php/Example_filters" title="Example filters">Example filters</a></strong>, <strong><a href="#Which_filter_rules_in_which_Category.3F">built-in rules</a></strong> and <strong><a href="/wiki/index.php/Addon:Rule_expansions" title="Addon:Rule expansions">Addon Rules</a></strong></em></p></td>
</tr>
</tbody>
</table>

  

<div class="thumb tright">

<div class="thumbinner" style="width:398px;">

![[_media/DefineFilter-dialog-default-60.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:DefineFilter-dialog-default-60.png" class="internal" title="Enlarge"></a>

</div>

Fig. 16.6 Define filter - dialog - default

</div>

</div>

</div>

The **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Define filter</span>** dialog allow you to build custom filters that can be used to select people included in reports, exports, and other tools and utilities. This is in fact a very powerful tool in genealogical analysis.

To list all the filters (if any) previously defined by you, access the **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Define filter</span>** dialog from:

- The Sidebar/Bottombar Filters
- In most categories via the menu **Edit \> *CategoryName* Filter Editor** which will bring up the **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">*CategoryName* Filters</span>** dialog where you can select the <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">+ (Add another rule to filter)</span> button or <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Edit the selected filter</span> button.

In the **Definition** section type the **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Name:</span>** for your new filter and add a **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Comment:</span>** that would help you identify this filter in the future. Add as many rules to the **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Rule list</span>** as you would like to your filter using <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">+</span> button.

<span id="multiple_rule_options">If the filter has more than one rule, select one of the **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Options</span>** from the drop down list which allows you to choose whether </span>

- **All rules must apply**(default)
- At least one rule must apply
- Exactly one rule must apply

in order for the filter to generate a match. If your filter has only one rule, this selection has no effect.

- Select
  <div style="float:left; width:.9em; height:.9em; margin-right:0.5em; vertical-align:-.1em; border:1px solid #111; background:#EEE;">

  </div>

  <span style=""></span> **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Return values that do not match the filter rules</span>** to invert the filter rule. For example, inverting **"has a common ancestor with I1"** rule will match everyone who does not have a common ancestor with that person). (Check box unchecked by default)

  

### <span id="Add_Rule_dialog" class="mw-headline">Add Rule dialog</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

<table style="width:80%;margin-top:+.7em;margin-bottom:+.7em;background-color: #c0f0ff85;border:1px solid #ccc; padding: 5px" data-align="center">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 60px">![[_media/Tango-Dialog-information.png]]</td>
<td><div style="font-size:110%">
<strong>A filter you have already designed may be used as a rule parameter for another filter.</strong>
</div>
<hr />
<p>This gives you nearly infinite flexibility in custom-tailoring your selection criteria that can be later used in most of the exports, reports, and some of the tools (such as comparing individual events).<br />
<em>See: <strong><a href="/wiki/index.php/Example_filters" title="Example filters">Example filters</a></strong>, <strong><a href="#Which_filter_rules_in_which_Category.3F">builtin rules</a></strong> and <strong><a href="/wiki/index.php/Addon:Rule_expansions" title="Addon:Rule expansions">Addon Rules</a></strong></em></p></td>
</tr>
</tbody>
</table>

  

<div class="thumb tright">

<div class="thumbinner" style="width:452px;">

![[_media/AddRule-selector-dialog-PersonFilters-example-60.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:AddRule-selector-dialog-PersonFilters-example-60.png" class="internal" title="Enlarge"></a>

</div>

Fig. 16.7 "Add Rule" - selector dialog - available for Person filters - example

</div>

</div>

</div>

To define a new filter click the <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">+ (Add another rule to filter)</span> button from the **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Define filter</span>** dialog as this invokes the **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Add Rule</span>** dialog

The pane on the left-hand side displays available filter rules arranged by their categories in an expandable tree.

For detailed filter rule reference you can either, use the search box to find the rule, or:

- Click on the <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">▶</span> arrows to fold/unfold the appropriate category.
- Select the rule from the tree by clicking on its name. The right-hand side displays the name, the description, and the values for the currently selected rule.

<table style="width:80%;margin-top:+.7em;margin-bottom:+.7em;background-color: #c0f0ff85;border:1px solid #ccc; padding: 5px" data-align="center">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 60px">![[_media/Tango-Dialog-information.png]]</td>
<td><div style="font-size:110%">
<strong>Finding a rule</strong>
</div>
<hr />
<p>It can be hard to remember which filter grouping contains a rule. And, since the "<a href="/wiki/index.php/Addon:Rule_expansions" title="Addon:Rule expansions">addon rule</a>" is a recent innovation, there can be too many rules to peruse easily. So you can narrow down the rule list -- based on keywords from the rule titles.<br />
<br />
Type a keyword by using the search box (box with the magnifying glass) and only the groupings with matches will be expanded.</p></td>
</tr>
</tbody>
</table>

Once you are satisfied with your rule selection and its values, click <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">OK</span> to add this rule to the rule list of the currently edited filter. Clicking <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Cancel</span> will abort adding the rule to the filter.

See also [Which filters in which Category?](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Which_filters_in_which_Category.3F)  

<span id="Which_filters_in_which_Category.3F"> </span>

## <span id="Which_filter_rules_in_which_Category?"></span><span id="Which_filter_rules_in_which_Category.3F" class="mw-headline">Which filter rules in which Category?</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Depending on the used [Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories), you will get a different set of [filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) rules. Also see [Summary of Gramplets](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Summary_of_Gramplets).

- Dashboard Category  
  no filter rules available

<!-- -->

- People, Relationships and Charts Category  
  rules for [Ancestral filters](#Ancestral_filters), [Citation/source filters](#Citation.2Fsource_filters), [Descendant filters](#Descendant_filters), [Event filters](#Event_filters), [Family filters](#Family_filters), [General filters](#General_filters), and [Relationship Filters](#Relationship_filters).

<!-- -->

- Families Category  
  rules for [Child filters](#Child_filters), [Citation/source filters](#Citation.2Fsource_filters), [Event filters](#Event_filters), [Father filters](#Father_filters), [General filters](#General_filters), and [Mother filters](#Mother_filters)

<!-- -->

- Charts Category  
  rules for [Ancestral filters](#Ancestral_filters), [Citation/source filters](#Citation.2Fsource_filters), [Descendant filters](#Descendant_filters), [Event filters](#Event_filters), [Family filters](#Family_filters), [General filters](#General_filters), and [Relationship Filters](#Relationship_filters)

<!-- -->

- Events, and Media Category  
  rules for [Citation/source filters](#Citation.2Fsource_filters), and [General filters](#General_filters).

<!-- -->

- Places Category  
  rules for [Citation/source filters](#Citation.2Fsource_filters), [General filters](#General_filters), and [Position filters](#Position_filters).

<!-- -->

- Geography Category  
  rules for [Ancestral filters](#Ancestral_filters), [Citation/source filters](#Citation.2Fsource_filters), [Descendant filters](#Descendant_filters), [Event filters](#Event_filters), [Family filters](#Family_filters), [General filters](#General_filters), and [Relationship Filters](#Relationship_filters).

<!-- -->

- Sources, Repositories, and Notes Category  
  rules for only [General filters](#General_filters) available

<!-- -->

- Citations Category  
  rules for [General filters](#General_filters), and [Source filters](#Source_filters)

<!-- -->

- Repositories Category  
  rules for [General filters](#General_filters)

<!-- -->

- Media Category  
  rules for [Citation/source filters](#Citation.2Fsource_filters), and [General filters](#General_filters)

<!-- -->

- Notes Category  
  rules for [General filters](#General_filters)

## <span id="Ancestral_filters" class="mw-headline">Ancestral filters</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule category includes the following rules that match people based on their ancestral relations to other people:

### <span id="Ancestor_of_<filter>_match"></span><span id="Ancestor_of_.3Cfilter.3E_match" class="mw-headline">Ancestor of \<filter\> match</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule matches people who are ancestors of someone who is matched by the specified filter. The specified filter name should be selected from the menu.

### <span id="Ancestor_of_<person>"></span><span id="Ancestor_of_.3Cperson.3E" class="mw-headline">Ancestor of \<person\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule matches people who are ancestors of the specified person. The Inclusive option determines whether the specified person should be considered his/her own ancestor (useful for building reports). You can either enter the ID into a text entry field, or select a person from the list by clicking <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Select...</span> button. In the latter case, the ID will appear in the text field after the selection was made.

### <span id="Ancestor_of_<person>_at_least_<N>_generations_away"></span><span id="Ancestor_of_.3Cperson.3E_at_least_.3CN.3E_generations_away" class="mw-headline">Ancestor of \<person\> at least \<N\> generations away</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule matches people who are ancestors of the specified person and are at least N generations away from that person in their lineage. For example, using this rule with the value of 2 for the number of generations will match grandparents, great-grandparents, etc., but not the parents of the specified person.

### <span id="Ancestor_of_<person>_not_more_than_<N>_generations_away"></span><span id="Ancestor_of_.3Cperson.3E_not_more_than_.3CN.3E_generations_away" class="mw-headline">Ancestor of \<person\> not more than \<N\> generations away</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule matches people who are ancestors of the specified person and are no more than N generations away from that person in their lineage. For example, using this rule with the value of 2 for the number of generations will match parents and grandparents, but not great-grandparents, etc., of the specified person.

### <span id="Ancestor_of_bookmarked_people_not_more_than_<N>_generations_away"></span><span id="Ancestor_of_bookmarked_people_not_more_than_.3CN.3E_generations_away" class="mw-headline">Ancestor of bookmarked people not more than \<N\> generations away</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches however many generations Ancestors (defined by \<n\>) for each person on the bookmark list.

### <span id="Ancestor_of_the_default_person_not_more_than_<N>_generations_away"></span><span id="Ancestor_of_the_default_person_not_more_than_.3CN.3E_generations_away" class="mw-headline">Ancestor of the default person not more than \<N\> generations away</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

The ”default person” is the individual that has been defined as the ”Home Person”. (The ”default” is a legacy term in Gramps that caused minor confusion she nice the word is used in so many different parts of the wiki to describe different things.)

### <span id="Duplicate_ancestors_of_<person>"></span><span id="Duplicate_ancestors_of_.3Cperson.3E" class="mw-headline">Duplicate ancestors of \<person\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people that are ancestors twice or more of a specified person

### <span id="People_with_a_common_ancestor_with_<filter>_match"></span><span id="People_with_a_common_ancestor_with_.3Cfilter.3E_match" class="mw-headline">People with a common ancestor with \<filter\> match</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule matches people who have common ancestors with someone who is matched by the specified filter. The specified filter name should be selected from the menu.

### <span id="People_with_a_common_ancestor_with_<person>"></span><span id="People_with_a_common_ancestor_with_.3Cperson.3E" class="mw-headline">People with a common ancestor with \<person\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule matches people who have common ancestors with the specified person.

## <span id="Child_filters" class="mw-headline">Child filters</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule category finds families having children that match the rule:

### <span id="Families_having_child_with_id_containing_<text>"></span><span id="Families_having_child_with_id_containing_.3Ctext.3E" class="mw-headline">Families having child with id containing \<text\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches families where child has a specified Gramps ID

### <span id="Families_with_child_with_the_<name>"></span><span id="Families_with_child_with_the_.3Cname.3E" class="mw-headline">Families with child with the \<name\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches families where child has a specified (partial) name

### <span id="Families_with_twins" class="mw-headline">Families with twins</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches families with two (or more) children having a ['Birth' role for the Relationship to the Mother](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Child_Reference_Editor) and the same birthdate.

## <span id="Citation/source_filters"></span><span id="Citation.2Fsource_filters" class="mw-headline">Citation/source filters</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

These filter rules are view dependent

- [People-, and Relationships Category](#People-.2C_and_Relationships_Category)
- [Families Category](#Families_Category)
- [Events Category](#Events_Category)
- [Places Category](#Places_Category)
- [Media Category](#Media_Category)

### <span id="People-,_and_Relationships_Category"></span><span id="People-.2C_and_Relationships_Category" class="mw-headline">People-, and Relationships Category</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following citation and source rules:

#### <span id="People_with_<count>_source"></span><span id="People_with_.3Ccount.3E_source" class="mw-headline">People with \<count\> source</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people with a certain number of items in the source. Values: Number of instances -- Number must be greater than/lesser/equal to

#### <span id="People_with_the_<citation>"></span><span id="People_with_the_.3Ccitation.3E" class="mw-headline">People with the \<citation\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people with a citation of a particular value

#### <span id="People_with_the_<source>"></span><span id="People_with_the_.3Csource.3E" class="mw-headline">People with the \<source\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people who have a particular source. values: Source ID

#### <span id="Person_with_at_least_one_direct_source_>=_<confidence_level>"></span><span id="Person_with_at_least_one_direct_source_.3E.3D_.3Cconfidence_level.3E" class="mw-headline">Person with at least one direct source \>= \<confidence level\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches persons who have a Citation attached directly to the Person object. Citations to the Family, or secondary objects such as Events are ignored.

The minimum acceptable confidence threshold is selectable: Very Low, Low, Normal, High, Very High

### <span id="Families_Category" class="mw-headline">Families Category</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following citation and source rules:

#### <span id="Families_with_<count>_sources"></span><span id="Families_with_.3Ccount.3E_sources" class="mw-headline">Families with \<count\> sources</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches families with a certain number of items in the source. Values: Number of instances -- Number must be greater than/lesser/equal to

#### <span id="Families_with_at_least_one_direct_source_>=_<confidence_level>"></span><span id="Families_with_at_least_one_direct_source_.3E.3D_.3Cconfidence_level.3E" class="mw-headline">Families with at least one direct source \>= \<confidence level\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches families who have a Citation attached directly to the Family object. Citations to the Person, or secondary objects such as Events are ignored.

The minimum acceptable confidence threshold is selectable: Very Low, Low, Normal, High, Very High

#### <span id="Families_with_the_<citation>"></span><span id="Families_with_the_.3Ccitation.3E" class="mw-headline">Families with the \<citation\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches families with a citation of a particular value

#### <span id="Families_with_the_<source>"></span><span id="Families_with_the_.3Csource.3E" class="mw-headline">Families with the \<source\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches families who have a particular source. values: Source ID

### <span id="Events_Category" class="mw-headline">Events Category</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following citation and source rules:

#### <span id="Events_with_<count>_source"></span><span id="Events_with_.3Ccount.3E_source" class="mw-headline">Events with \<count\> source</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches events with a certain number of items in the source. Values: Number of instances -- Number must be greater than/lesser/equal to

#### <span id="Events_with_at_least_one_direct_source_>=_<confidence_level>"></span><span id="Events_with_at_least_one_direct_source_.3E.3D_.3Cconfidence_level.3E" class="mw-headline">Events with at least one direct source \>= \<confidence level\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches events which have a Citation attached directly to the Event object. Citations to the Family, or secondary objects such as Notes are ignored.

The minimum acceptable confidence threshold is selectable: Very Low, Low, Normal, High, Very High

#### <span id="Events_with_source_matching_the_<source_filter>"></span><span id="Events_with_source_matching_the_.3Csource_filter.3E" class="mw-headline">Events with source matching the \<source filter\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches events with any source (or citation under a Source) which matches a specified source fileter and is directly attached to the Event object. Sources attache to Event's media or attributes are ignored.

#### <span id="Events_with_the_<citation>"></span><span id="Events_with_the_.3Ccitation.3E" class="mw-headline">Events with the \<citation\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches events with a citation of a particular value

### <span id="Places_Category" class="mw-headline">Places Category</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following citation and source rules:

#### <span id="Place_with_<count>_sources"></span><span id="Place_with_.3Ccount.3E_sources" class="mw-headline">Place with \<count\> sources</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches places with a certain number of items in the source. Values: Number of instances -- Number must be greater than/lesser/equal to

#### <span id="Place_with_a_direct_source_>=_<confidence_level>"></span><span id="Place_with_a_direct_source_.3E.3D_.3Cconfidence_level.3E" class="mw-headline">Place with a direct source \>= \<confidence level\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches places which have a Citation attached directly to the Place object. Citations to secondary objects such as Notes are ignored.

The minimum acceptable confidence threshold is selectable: Very Low, Low, Normal, High, Very High

#### <span id="Place_with_the_<citation>"></span><span id="Place_with_the_.3Ccitation.3E" class="mw-headline">Place with the \<citation\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches places with a citation of a particular value

#### <span id="Places_with_the_<source>"></span><span id="Places_with_the_.3Csource.3E" class="mw-headline">Places with the \<source\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches places who have a particular source. values: Source ID

### <span id="Media_Category" class="mw-headline">Media Category</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following citation and source rules:

#### <span id="Media_with_<count>_sources"></span><span id="Media_with_.3Ccount.3E_sources" class="mw-headline">Media with \<count\> sources</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches media with a certain number of items in the source. Values: Number of instances -- Number must be greater than/lesser/equal to

#### <span id="Media_with_a_direct_source_>=_<confidence_level>"></span><span id="Media_with_a_direct_source_.3E.3D_.3Cconfidence_level.3E" class="mw-headline">Media with a direct source \>= \<confidence level\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches media which have a Citation attached directly to the Media object. Citations to the secondary objects such as Events are ignored.

The minimum acceptable confidence threshold is selectable: Very Low, Low, Normal, High, Very High

#### <span id="Media_with_the_<citation>"></span><span id="Media_with_the_.3Ccitation.3E" class="mw-headline">Media with the \<citation\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches media with a citation of a particular value

#### <span id="Media_with_the_<source>"></span><span id="Media_with_the_.3Csource.3E" class="mw-headline">Media with the \<source\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches media who have a particular source. values: Source ID

## <span id="Descendant_filters" class="mw-headline">Descendant filters</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This descendant filters category include the following rules that match people based on their descendant relations to other people:

### <span id="Descendant_family_member_of_<filter>_match"></span><span id="Descendant_family_member_of_.3Cfilter.3E_match" class="mw-headline">Descendant family member of \<filter\> match</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people that are descendants or the spouse of anybody matched by a filter

### <span id="Descendant_family_member_of_<person>"></span><span id="Descendant_family_member_of_.3Cperson.3E" class="mw-headline">Descendant family member of \<person\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule not only matches people who are descendants of the specified person, but also those descendants' spouses.

### <span id="Descendant_of_<filter>_match"></span><span id="Descendant_of_.3Cfilter.3E_match" class="mw-headline">Descendant of \<filter\> match</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule matches people who are descendants of someone who is matched by the specified filter. The specified filter name should be selected from the menu.

### <span id="Descendant_of_<person>"></span><span id="Descendant_of_.3Cperson.3E" class="mw-headline">Descendant of \<person\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule matches people who are descendants of the specified person. The Inclusive option determines whether the specified person should be considered his/her own descendant (useful for building reports). You can either enter the ID into a text entry field, or select a person from the list by clicking <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;"> Select...</span> button. In the latter case, the ID will appear in the text field after the selection was made.

### <span id="Descendant_of_<person>_at_least_<N>_generations_away"></span><span id="Descendant_of_.3Cperson.3E_at_least_.3CN.3E_generations_away" class="mw-headline">Descendant of \<person\> at least \<N\> generations away</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule matches people who are descendants of the specified person and are at least N generations away from that person in their lineage. For example, using this rule with the value of 2 for the number of generations will match grandchildren, great-grandchildren, etc., but not the children of the specified person.

### <span id="Descendant_of_<person>_not_more_than_<N>_generations_away"></span><span id="Descendant_of_.3Cperson.3E_not_more_than_.3CN.3E_generations_away" class="mw-headline">Descendant of \<person\> not more than \<N\> generations away</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule matches people who are descendants of the specified person and are no more than N generations away from that person in their lineage. For example, using this rule with the value of 2 for the number of generations will match children and grandchildren, but not great-grandchildren, etc., of the specified person.

## <span id="Event_filters" class="mw-headline">Event filters</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

### <span id="Events_matching_parameters" class="mw-headline">Events matching parameters</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

General filters rule that matches Events with particular parameters:

- **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Event type</span>**
- **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Date</span>**
- **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Place</span>**
- **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Description</span>**
- **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Main Participants</span>**

Also offers the option to **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Use regular expression</span>**.

### <span id="These_filter_rules_are_view_dependent" class="mw-headline">These filter rules are view dependent</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

- [People-, and Relationships Category](#People-.2C_and_Relationships_Category_2)
- [Families Category](#Families_Category_2)

### <span id="People-,_and_Relationships_Category_2"></span><span id="People-.2C_and_Relationships_Category_2" class="mw-headline">People-, and Relationships Category</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following rules that match people based on their recorded events:

#### <span id="Families_with_incomplete_events" class="mw-headline">Families with incomplete events</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule matches people missing date or place in any family event of any of their families.

#### <span id="People_with_incomplete_events" class="mw-headline">People with incomplete events</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule matches people missing date or place in any personal event.

#### <span id="People_with_the_<birth_data>"></span><span id="People_with_the_.3Cbirth_data.3E" class="mw-headline">People with the \<birth data\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule matches people whose birth event matches specified values for Date, Place, and Description. The rule returns a match even if the person's birth event matches the value partially. The matching rules are case-insensitive. For example, anyone born in Sweden will be matched by the rule using the value "sw" for the Place. The rule returns a match if, and only if, all non-empty values are (partially) matched by a person's birth. To use just one value, leave the other values empty.

#### <span id="People_with_the_<death_data>"></span><span id="People_with_the_.3Cdeath_data.3E" class="mw-headline">People with the \<death data\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule matches people whose death event matches specified values for Date, Place, and Description. The rule returns a match even if the person's death event matches the value partially. The matching rules are case-insensitive. For example, anyone who died in Sweden will be matched by the rule using the value "sw" for the Place. The rule returns a match if, and only if, all non-empty values are (partially) matched by a person's death. To use just one value, leave the other values empty.

#### <span id="People_with_the_family_<event>"></span><span id="People_with_the_family_.3Cevent.3E" class="mw-headline">People with the family \<event\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule matches people that have a family event matching specified values for the Event type, Date, Place, and Description. The rule returns a match even if the person's event matches the value partially. The matching rules are case-insensitive. For example, anyone who was married in Sweden will be matched by the rule using the Marriage event and the value "sw" for the Place. The family events should be selected from a pull-down menu. The rule returns a match if, and only if, all non-empty values are (partially) matched by the personal event. To use just one value, leave the other values empty.

#### <span id="People_with_the_personal_<event>"></span><span id="People_with_the_personal_.3Cevent.3E" class="mw-headline">People with the personal \<event\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule matches people that have a personal event matching specified values for the Event type, Date, Place, and Description. The rule returns a match even if the person's event matches the value partially. The matching rules are case-insensitive. For example, anyone who graduated in Sweden will be matched by the rule using the Graduation event and the value "sw" for the Place. The personal events should be selected from a pull-down menu. The rule returns a match if, and only if, all non-empty values are (partially) matched by the personal event. To use just one value, leave the other values empty.

#### <span id="Persons_with_events_matching_the_<event_filter>"></span><span id="Persons_with_events_matching_the_.3Cevent_filter.3E" class="mw-headline">Persons with events matching the \<event filter\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches persons who have events that match a certain event filter. Values: Event filter name.

#### <span id="Witnesses" class="mw-headline">Witnesses</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule matches people who are in a "Witness" [Event Role](wiki:Gramps_Glossary#event_role). If the (personal or family) event type is specified, only the events of this type will be searched.

##### <span id="See_Also_3" class="mw-headline">See Also</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

[FilterRules](wiki:Addon:Rule_expansions#FilterRules_:_Plugin_Manager_Rulebook_Collection) : Plugin Manager Rulebook Collection include rules to search for Persons or Families with Events having specific Roles:

- [People with events with a selected role](wiki:Addon:Rule_expansions#People_with_events_with_a_selected_role) : People filter rule
- [Families with Events with a selected role](wiki:Addon:Rule_expansions#Families_with_Events_with_a_selected_role) : Family filter rule

### <span id="Families_Category_2" class="mw-headline">Families Category</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following rules that match families based on their recorded events:

#### <span id="Families_with_the_<event>"></span><span id="Families_with_the_.3Cevent.3E" class="mw-headline">Families with the \<event\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule matches families that have a event matching specified values for the Event type, Date, Place, and Description. The rule returns a match even if the person's event matches the value partially. The matching rules are case-insensitive. For example, anyone who was married in Sweden will be matched by the rule using the Marriage event and the value "sw" for the Place. The family events should be selected from a pull-down menu. The rule returns a match if, and only if, all non-empty values are (partially) matched by the personal event. To use just one value, leave the other values empty.

## <span id="Family_filters" class="mw-headline">Family filters</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following rules that match people based on their family relationships:

### <span id="Adopted_people" class="mw-headline">Adopted people</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule matches adopted people.

### <span id="Children_of_<filter>_match"></span><span id="Children_of_.3Cfilter.3E_match" class="mw-headline">Children of \<filter\> match</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule matches people for whom either parent is matched by the specified filter. The specified filter name should be selected from the menu.

### <span id="Parents_of_<filter>_match"></span><span id="Parents_of_.3Cfilter.3E_match" class="mw-headline">Parents of \<filter\> match</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule matches people whose child is matched by the specified filter. The specified filter name should be selected from the menu.

### <span id="People_missing_parents" class="mw-headline">People missing parents</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people that are children in a family with less than two parents or are not children in any family.

### <span id="People_with_children" class="mw-headline">People with children</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule matches people with children.

### <span id="People_with_multiple_marriage_records" class="mw-headline">People with multiple marriage records</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule matches people with more than one spouse.

### <span id="People_with_no_marriage_records" class="mw-headline">People with no marriage records</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule matches people with no spouses.

### <span id="People_with_the_<relationships>"></span><span id="People_with_the_.3Crelationships.3E" class="mw-headline">People with the \<relationships\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule matches people with a particular relationship. The relationship must match the type selected from the menu. Optionally, the number of relationships and the number of children can be specified. The rule returns a match if, and only if, all non-empty values are (partially) matched by a person's relationship. To use just one value, leave the other values empty.

### <span id="Siblings_of_<filter>_match"></span><span id="Siblings_of_.3Cfilter.3E_match" class="mw-headline">Siblings of \<filter\> match</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule matches people whose sibling is matched by the specified filter. The specified filter name should be selected from the menu.

### <span id="Spouses_of_<filter>_match"></span><span id="Spouses_of_.3Cfilter.3E_match" class="mw-headline">Spouses of \<filter\> match</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule matches people married to someone who is matched by the specified filter. The specified filter name should be selected from the menu.

## <span id="Father_filters" class="mw-headline">Father filters</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule category finds families having fathers that match the rule:

### <span id="Families_having_father_with_Id_containing_<text>"></span><span id="Families_having_father_with_Id_containing_.3Ctext.3E" class="mw-headline">Families having father with Id containing \<text\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches families whose father has a specified Gramps ID

### <span id="Families_with_father_with_the_<name>"></span><span id="Families_with_father_with_the_.3Cname.3E" class="mw-headline">Families with father with the \<name\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches families whose father has a specified (partial) name

## <span id="General_filters" class="mw-headline">General filters</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

These filter rules are view dependent

- [People-, and Relationships Category](#People-.2C_and_Relationships_Category_3)
- [Families Category](#Families_Category_3)
- [Events Category](#Events_Category_2)
- [Places Category](#Places_Category_2)
- [Sources Category](#Sources_Category)
- [Citations Category](#Citations_Category)
- [Repositories Category](#Repositories_Category)
- [Media Category](#Media_Category_2)
- [Notes Category](#Notes_Category)

### <span id="People-,_and_Relationships_Category_3"></span><span id="People-.2C_and_Relationships_Category_3" class="mw-headline">People-, and Relationships Category</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following general rules:

#### <span id="Bookmarked_people" class="mw-headline">Bookmarked people</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches the people on the bookmark list.

<span id="Default_person"> </span>

#### <span id="Home_person" class="mw-headline">Home person</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches the [Home Person](wiki:Gramps_Glossary#home_person).

#### <span id="Disconnected_People" class="mw-headline">Disconnected People</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people that have no family relationships to any other person in the database.

#### <span id="Everyone" class="mw-headline">Everyone</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches everyone in the family tree database.

#### <span id="Females" class="mw-headline">Females</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches all females.

#### <span id="Males" class="mw-headline">Males</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches all males.

#### <span id="People_having_<count>_notes"></span><span id="People_having_.3Ccount.3E_notes" class="mw-headline">People having \<count\> notes</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people having a certain number of notes: Values: Number of instances -- Number must be greater than/lesser/equal to

#### <span id="People_having_notes_containing_<text>"></span><span id="People_having_notes_containing_.3Ctext.3E" class="mw-headline">People having notes containing \<text\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people whose notes contain text matching a regular expression

#### <span id="People_marked_private" class="mw-headline">People marked private</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people that are indicated as private.

#### <span id="People_matching_the_<filter>"></span><span id="People_matching_the_.3Cfilter.3E" class="mw-headline">People matching the \<filter\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people matched by the specified filter name. Values: Filter name. The specified filter name should be selected from the menu.

#### <span id="People_not_marked_private" class="mw-headline">People not marked private</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people that are not indicated as private

#### <span id="People_probably_alive" class="mw-headline">People probably alive</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people without indications of death by a specified date. If the specified "On Date" value is blank then compare to "today()". The probably alive considers the date approximations and lifespan lengths set in the Preferences.

For more detailed information about this calculation, read the "[Probably Alive](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive)" section.

- [Probably Alive Filter](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive#Probably_Alive_Filter)

#### <span id="People_with_<count>_LDS_events"></span><span id="People_with_.3Ccount.3E_LDS_events" class="mw-headline">People with \<count\> LDS events</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people with a certain number of LDS events. Values: Number of instances -- Number must be greater than/lesser/equal to

#### <span id="People_with_<count>_addresses"></span><span id="People_with_.3Ccount.3E_addresses" class="mw-headline">People with \<count\> addresses</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people with a certain number of personal addresses. Values: Number of instances -- Number must be greater than/lesser/equal to

#### <span id="People_with_<count>_associations"></span><span id="People_with_.3Ccount.3E_associations" class="mw-headline">People with \<count\> associations</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people with a certain number of associations. Values: Number of instances -- Number must be greater than/lesser/equal to

#### <span id="People_with_<count>_media"></span><span id="People_with_.3Ccount.3E_media" class="mw-headline">People with \<count\> media</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people with a certain number of items in the gallery. Values: Number of instances -- Number must be greater than/lesser/equal to

#### <span id="People_with_id_containing_<text>"></span><span id="People_with_id_containing_.3Ctext.3E" class="mw-headline">People with id containing \<text\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people whose Gramps ID matches the regular expression

#### <span id="People_with_a_name_matching_<text>"></span><span id="People_with_a_name_matching_.3Ctext.3E" class="mw-headline">People with a name matching \<text\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people's names containing a substring or matching a [regular expression](wiki:Gramps_Glossary#regex)

#### <span id="People_with_a_nickname" class="mw-headline">People with a nickname</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people with a nickname

#### <span id="People_with_an_alternate_name" class="mw-headline">People with an alternate name</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people with an alternate name

#### <span id="People_with_incomplete_names" class="mw-headline">People with incomplete names</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people with first-name or last-name missing.

#### <span id="People_with_records_containing_<substring>"></span><span id="People_with_records_containing_.3Csubstring.3E" class="mw-headline">People with records containing \<substring\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people whose records contain text matching a substring. Values: Substring -- Case Sensitive or not -- Regular-Expression matching or not

*The filter doesn't search in notes.*

#### <span id="People_with_the_<Name_type>"></span><span id="People_with_the_.3CName_type.3E" class="mw-headline">People with the \<Name type\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people with a type of name

#### <span id="People_with_the_<Surname_origin_type>"></span><span id="People_with_the_.3CSurname_origin_type.3E" class="mw-headline">People with the \<Surname origin type\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people with a surname origin

#### <span id="People_with_the_<name>"></span><span id="People_with_the_.3Cname.3E" class="mw-headline">People with the \<name\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people with a specified (partial) name.

Values:

- Given name
- Full Family name : searches Prefix, surname and connectors with multiple surnames
- Title
- Suffix
- Call Name
- Nick Name
- Prefix
- Single Surname : searches only the [Preferred name](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Preferred_name_section)
- Connector : search in connectors for [multiple surnames](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Multiple_Surnames)
- Patronymic
- Family Nick Name

Options:

- <div style="float:left; width:.9em; height:.9em; margin-right:0.5em; vertical-align:-.1em; border:1px solid #111; background:#EEE;">

  </div>

  <span style="">Use [regular expressions](wiki:Gramps_Glossary#regex)</span> - select this option and enter the regular expressions in any of the entry fields.
  - For example if you enter the regular expression `(.|\s)*\S(.|\s)*` in the **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Prefix</span>** field and select this option you can find non-blank prefixes.

- <div style="float:left; width:.9em; height:.9em; margin-right:0.5em; vertical-align:-.1em; border:1px solid #111; background:#EEE;">

  </div>

  <span style="">Case sensitive</span>

  

##### <span id="See_also_4" class="mw-headline">See also</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

- [People with a name matching \<text\>](wiki:Gramps_6.0_Wiki_Manual_-_Filters#People_with_a_name_matching_.3Ctext.3E)
- [People with a nickname](wiki:Gramps_6.0_Wiki_Manual_-_Filters#People_with_a_nickname)
- [People with an alternate name](wiki:Gramps_6.0_Wiki_Manual_-_Filters#People_with_an_alternate_name)
- [People with incomplete names](wiki:Gramps_6.0_Wiki_Manual_-_Filters#People_with_incomplete_names)
- [People with the \<Name type\>](wiki:Gramps_6.0_Wiki_Manual_-_Filters#People_with_the_.3CName_type.3E)
- [People with the \<Surname origin type\>](wiki:Gramps_6.0_Wiki_Manual_-_Filters#People_with_the_.3CSurname_origin_type.3E)
- [People with the \<name\>](wiki:Gramps_6.0_Wiki_Manual_-_Filters#People_with_the_.3Cname.3E)
- [Soundex match of People with the \<name\>](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Soundex_match_of_People_with_the_.3Cname.3E)
- [Families with child with the \<name\>](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Families_with_child_with_the_.3Cname.3E)
- [Families with father with the \<name\>](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Families_with_father_with_the_.3Cname.3E)
- [Families with mother with the \<name\>](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Families_with_mother_with_the_.3Cname.3E)
- [Search bar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Search_bar) (Names contains, Name does not contain)
- [People Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#People_Filter) gramplet (Name)
- Isotammi [People Filter+](wiki:Addon:Isotammi_addons#Filter.2B) addon gramplet (Name)
- Isotammi [SuperTool](wiki:Addon:Isotammi_addons#SuperTool) query tool (People category)

  

#### <span id="People_with_<tag>"></span><span id="People_with_.3Ctag.3E" class="mw-headline">People with \<tag\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people with a tag of a particular value. Values: Tag name.

#### <span id="People_with_the_family_<attribute>"></span><span id="People_with_the_family_.3Cattribute.3E" class="mw-headline">People with the family \<attribute\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people with the family attribute of a particular value. Use RegEx pattern matching to search for [all values](wiki:Gramps_6.0_Wiki_Manual_-_Filters#regex_all) or attributes that have been [left blank](wiki:Gramps_6.0_Wiki_Manual_-_Filters#regex_null). Values: Family Attribute: Identification Number -- Age ...

#### <span id="People_with_the_personal_<attribute>"></span><span id="People_with_the_personal_.3Cattribute.3E" class="mw-headline">People with the personal \<attribute\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people with the personal attribute of a particular value. Use RegEx pattern matching to search for [all values](wiki:Gramps_6.0_Wiki_Manual_-_Filters#regex_all) or attributes that have been [left blank](wiki:Gramps_6.0_Wiki_Manual_-_Filters#regex_null). Values: Personal Attribute: Identification Number -- Age ...

#### <span id="People_with_unknown_gender" class="mw-headline">People with unknown gender</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches all people with unknown gender.

#### <span id="People_without_a_known_birth_date" class="mw-headline">People without a known birth date</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This General filter in the People category will matches people without a known birth date.

This rule includes both Persons without any birth-type event and Persons with undated Birth-type events.

#### <span id="People_without_a_known_death_date" class="mw-headline">People without a known death date</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people without a known death date.

#### <span id="People_with_<id>"></span><span id="People_with_.3Cid.3E" class="mw-headline">People with \<id\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people with Gramps ID. The rule returns a match only if the ID is matched exactly. You can either enter the ID into a text entry field, or select an object from the list by clicking <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Select...</span> button. In the latter case, the ID will appear in the text field after the selection was made.

#### <span id="People_changed_after_<date_time>"></span><span id="People_changed_after_.3Cdate_time.3E" class="mw-headline">People changed after \<date time\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches person records changed during a particular time period. Used to identify records that were imported or modified during particular work-sessions.

Filtering based on specified date and timestamp being after a particular timestamp in the format `yyyy-mm-dd hh:mm:ss`. This filter rules will look for records modified within a date range, if a second date-time is given.

Values:

     Changed after: 
     but before: 

Values must be after January 1st, 1970 at UTC. Future dates until `3001-01-01 01:59:59` are valid.

The **People changed after \<date time\>** filter rules are available in the **General filters** section for custom rules in the People, Relationships, Charts, and Geography views.

Equivalent rules exist for records of the corresponding category type in People, Families, Events, Places, Sources, Citations, Repositories, Media, and Notes category views.

#### <span id="Soundex_match_of_People_with_the_<name>"></span><span id="Soundex_match_of_People_with_the_.3Cname.3E" class="mw-headline">Soundex match of People with the \<name\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Soundex Match of people with a specified name. First name, Surname, Call name, and Nickname are searched in primary and alternate names.

This rule compares names of People against a phonetic pattern. It uses the [Soundex](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Soundex_what_is_this.3F) phonetic algorithm for indexing names by sound, as pronounced in English.

Match criteria can be a Soundex code (which can be found with the Soundex Gramplet) consisting of of a letter followed by three numerical digits: the letter is the first letter of the name, and the digits encode the remaining consonants. But if the match criteria is not a valid Soundex code, the filter will simply generate Soundex code for the word entered.

All name fields (and the separate words within those fields) are searched individually against the Soundex code.

### <span id="Families_Category_3" class="mw-headline">Families Category</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following general rules:

#### <span id="Ancestor_families_of_<family>"></span><span id="Ancestor_families_of_.3Cfamily.3E" class="mw-headline">Ancestor families of \<family\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches families who are ancestor families of the partners in a specified Family. There is an option to include specified Family in the results. Included blended families and non-birth relationship families.

#### <span id="Bookmarked_families" class="mw-headline">Bookmarked families</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches the families on the bookmark list.

#### <span id="Descendant_families_of_<family>"></span><span id="Descendant_families_of_.3Cfamily.3E" class="mw-headline">Descendant families of \<family\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches the Family object descended from a specific Family. (No person objects are included.)

Also see:

- Descendant family member of \<filter\> match
- Descendant family member of \<person\>

#### <span id="Every_family" class="mw-headline">Every family</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches every family in the database.

#### <span id="Families_changed_after_<date_time>"></span><span id="Families_changed_after_.3Cdate_time.3E" class="mw-headline">Families changed after \<date time\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches families records changed after a specified date-time (yyy-mm-dd hh:mm:ss) or in the range, if a second date-time is given: Values: Changed after: -- but before:.

#### <span id="Families_having_<count>_notes"></span><span id="Families_having_.3Ccount.3E_notes" class="mw-headline">Families having \<count\> notes</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches families having a certain number of notes: Values: Number of instances -- Number must be greater than/lesser/equal to

#### <span id="Families_having_notes_containing_<text>"></span><span id="Families_having_notes_containing_.3Ctext.3E" class="mw-headline">Families having notes containing \<text\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches families whose notes contain text matching a regular expression

#### <span id="Families_marked_private" class="mw-headline">Families marked private</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches families that are indicated as private.

#### <span id="Families_matching_the_<filter>"></span><span id="Families_matching_the_.3Cfilter.3E" class="mw-headline">Families matching the \<filter\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches families matched by the specified filter name. Values: Filter name. The specified filter name should be selected from the menu.

#### <span id="Families_with_<count>_LDS_events"></span><span id="Families_with_.3Ccount.3E_LDS_events" class="mw-headline">Families with \<count\> LDS events</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches families with a certain number of LDS events. Values: Number of instances -- Number must be greater than/lesser/equal to

#### <span id="Families_with_<count>_media"></span><span id="Families_with_.3Ccount.3E_media" class="mw-headline">Families with \<count\> media</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches families with a certain number of items in the gallery. Values: Number of instances -- Number must be greater than/lesser/equal to

#### <span id="Families_with_id_containing_<text>"></span><span id="Families_with_id_containing_.3Ctext.3E" class="mw-headline">Families with id containing \<text\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches families whose Gramps ID matches the regular expression

#### <span id="Families_with_a_reference_count_of_<count>"></span><span id="Families_with_a_reference_count_of_.3Ccount.3E" class="mw-headline">Families with a reference count of \<count\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches families with a certain number of references. Values: Number of references -- Number must be greater than/lesser/equal to

#### <span id="Families_with_the_<tag>"></span><span id="Families_with_the_.3Ctag.3E" class="mw-headline">Families with the \<tag\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches families with a tag of a particular value. Values: Tag name.

#### <span id="Families_with_the_family_<attribute>"></span><span id="Families_with_the_family_.3Cattribute.3E" class="mw-headline">Families with the family \<attribute\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches families with the family attribute of a particular value. Values: Family Attribute: Identification Number -- Age ...

#### <span id="Families_with_the_relationship_type" class="mw-headline">Families with the relationship type</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches families with the relationship type of a particular value

#### <span id="Families_with_<id>"></span><span id="Families_with_.3Cid.3E" class="mw-headline">Families with \<id\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches families with Gramps ID. The rule returns a match only if the ID is matched exactly. You can either enter the ID into a text entry field, or select an object from the list by clicking <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Select...</span> button. In the latter case, the ID will appear in the text field after the selection was made.

### <span id="Events_Category_2" class="mw-headline">Events Category</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following general rules:

#### <span id="Event_with_<id>"></span><span id="Event_with_.3Cid.3E" class="mw-headline">Event with \<id\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches events with Gramps ID. The rule returns a match only if the ID is matched exactly. You can either enter the ID into a text entry field, or select an object from the list by clicking <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Select...</span> button. In the latter case, the ID will appear in the text field after the selection was made.

#### <span id="Events_changed_after_<date_time>"></span><span id="Events_changed_after_.3Cdate_time.3E" class="mw-headline">Events changed after \<date time\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches events records changed after a specified date-time (yyy-mm-dd hh:mm:ss) or in the range, if a second date-time is given: Values: Changed after: -- but before:.

#### <span id="Events_having_<count>_notes"></span><span id="Events_having_.3Ccount.3E_notes" class="mw-headline">Events having \<count\> notes</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches events having a certain number of notes: Values: Number of instances -- Number must be greater than/lesser/equal to

#### <span id="Events_having_notes_containing_<text>"></span><span id="Events_having_notes_containing_.3Ctext.3E" class="mw-headline">Events having notes containing \<text\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches events whose notes contain text matching a regular expression

#### <span id="Events_marked_private" class="mw-headline">Events marked private</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches events that are indicated as private.

#### <span id="Events_matching_the_<filter>"></span><span id="Events_matching_the_.3Cfilter.3E" class="mw-headline">Events matching the \<filter\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches events matched by the specified filter name. Values: Filter name. The specified filter name should be selected from the menu.

#### <span id="Events_occurring_on_a_particular_day_of_the_week" class="mw-headline">Events occurring on a particular day of the week</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches events occurring on a particular day of the week

#### <span id="Events_of_persons_matching_the_<person_filter>"></span><span id="Events_of_persons_matching_the_.3Cperson_filter.3E" class="mw-headline">Events of persons matching the \<person filter\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches events of person matched by the specified person filter name

#### <span id="Events_of_places_matching_the_<place_filter>"></span><span id="Events_of_places_matching_the_.3Cplace_filter.3E" class="mw-headline">Events of places matching the \<place filter\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches events that occurred at places that match the specified place filter name

#### <span id="Events_with_<count>_media"></span><span id="Events_with_.3Ccount.3E_media" class="mw-headline">Events with \<count\> media</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches events with a certain number of items in the gallery. Values: Number of instances -- Number must be greater than/lesser/equal to

#### <span id="Events_with_<data>"></span><span id="Events_with_.3Cdata.3E" class="mw-headline">Events with \<data\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches events with data of a particular value

#### <span id="Events_with_Id_containing_<text>"></span><span id="Events_with_Id_containing_.3Ctext.3E" class="mw-headline">Events with Id containing \<text\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches events whose Gramps ID matches the regular expression

#### <span id="Events_with_a_reference_count_of_<count>"></span><span id="Events_with_a_reference_count_of_.3Ccount.3E" class="mw-headline">Events with a reference count of \<count\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches events with a certain number of references. Values: Number of references -- Number must be greater than/lesser/equal to

#### <span id="Events_with_the_<tag>"></span><span id="Events_with_the_.3Ctag.3E" class="mw-headline">Events with the \<tag\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches events with a tag of a particular value. Values: Tag name.

#### <span id="Events_with_the_attribute_<attribute>"></span><span id="Events_with_the_attribute_.3Cattribute.3E" class="mw-headline">Events with the attribute \<attribute\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches events with the attribute of a particular value. Values: Family Attribute: Identification Number -- Age ...

#### <span id="Events_with_the_particular_type" class="mw-headline">Events with the particular type</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches events with the particular type

#### <span id="Every_event" class="mw-headline">Every event</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches every event in the database.

### <span id="Places_Category_2" class="mw-headline">Places Category</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following general rules:

#### <span id="Every_place" class="mw-headline">Every place</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches every place in the database.

#### <span id="Place_with_<Id>"></span><span id="Place_with_.3CId.3E" class="mw-headline">Place with \<Id\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches places with Gramps ID. The rule returns a match only if the ID is matched exactly. You can either enter the ID into a text entry field, or select an object from the list by clicking <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Select...</span> button. In the latter case, the ID will appear in the text field after the selection was made.

#### <span id="Places_changed_after_<date_time>"></span><span id="Places_changed_after_.3Cdate_time.3E" class="mw-headline">Places changed after \<date time\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches places records changed after a specified date-time (yyyy-mm-dd hh:mm:ss) or in the range, if a second date-time is given: Values: Changed after: -- but before:.

#### <span id="Places_enclosed_by_another_place" class="mw-headline">Places enclosed by another place</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches Places under the Hierarchical structure of a Specified place. Does not include the Enclosing Place and ignores dates.

#### <span id="Places_having_<count>_notes"></span><span id="Places_having_.3Ccount.3E_notes" class="mw-headline">Places having \<count\> notes</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches places having a certain number of notes: Values: Number of instances -- Number must be greater than/lesser/equal to

#### <span id="Places_having_notes_containing_<text>"></span><span id="Places_having_notes_containing_.3Ctext.3E" class="mw-headline">Places having notes containing \<text\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches places whose notes contain text matching a regular expression

#### <span id="Places_marked_private" class="mw-headline">Places marked private</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches places that are indicated as private.

#### <span id="Places_matching_a_title" class="mw-headline">Places matching a title</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches places with a particular title

#### <span id="Places_matching_parameters" class="mw-headline">Places matching parameters</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

General filters rule that matches Places with particular parameters:

- **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Name</span>**
- **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Place type</span>**
- **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Code</span>**

Also offers the option to **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Use regular expression</span>**.

#### <span id="Places_matching_the_<filter>"></span><span id="Places_matching_the_.3Cfilter.3E" class="mw-headline">Places matching the \<filter\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches places matched by the specified filter name. Values: Filter name. The specified filter name should be selected from the menu.

#### <span id="Places_of_events_matching_the_<event_filter>"></span><span id="Places_of_events_matching_the_.3Cevent_filter.3E" class="mw-headline">Places of events matching the \<event filter\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches places where events happened that match the specified event filter name

#### <span id="Places_with_<count>_media"></span><span id="Places_with_.3Ccount.3E_media" class="mw-headline">Places with \<count\> media</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches places with a certain number of items in the gallery. Values: Number of instances -- Number must be greater than/lesser/equal to

#### <span id="Places_with_Id_containing_<text>"></span><span id="Places_with_Id_containing_.3Ctext.3E" class="mw-headline">Places with Id containing \<text\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches places whose Gramps ID matches the regular expression

#### <span id="Places_with_a_reference_count_of_<count>"></span><span id="Places_with_a_reference_count_of_.3Ccount.3E" class="mw-headline">Places with a reference count of \<count\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches places with a certain number of references. Values: Number of references -- Number must be greater than/lesser/equal to

#### <span id="Places_with_the_<tag>"></span><span id="Places_with_the_.3Ctag.3E" class="mw-headline">Places with the \<tag\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches places with a tag of a particular value. Values: Tag name.

### <span id="Sources_Category" class="mw-headline">Sources Category</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following general rules:

#### <span id="Every_source" class="mw-headline">Every source</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches every source in the database.

#### <span id="Source_with_<Id>"></span><span id="Source_with_.3CId.3E" class="mw-headline">Source with \<Id\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches sources with Gramps ID. The rule returns a match only if the ID is matched exactly. You can either enter the ID into a text entry field, or select an object from the list by clicking <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Select...</span> button. In the latter case, the ID will appear in the text field after the selection was made.

#### <span id="Sources_changed_after_<date_time>"></span><span id="Sources_changed_after_.3Cdate_time.3E" class="mw-headline">Sources changed after \<date time\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches sources records changed after a specified date-time (yyy-mm-dd hh:mm:ss) or in the range, if a second date-time is given: Values: Changed after: -- but before:.

#### <span id="Sources_having_<count>_notes"></span><span id="Sources_having_.3Ccount.3E_notes" class="mw-headline">Sources having \<count\> notes</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches sources having a certain number of notes: Values: Number of instances -- Number must be greater than/lesser/equal to

#### <span id="Sources_having_notes_containing_<text>"></span><span id="Sources_having_notes_containing_.3Ctext.3E" class="mw-headline">Sources having notes containing \<text\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches sources whose notes contain text matching a regular expression

#### <span id="Sources_marked_private" class="mw-headline">Sources marked private</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches sources that are indicated as private.

#### <span id="Sources_matching_the_<filter>"></span><span id="Sources_matching_the_.3Cfilter.3E" class="mw-headline">Sources matching the \<filter\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches sources matched by the specified filter name. Values: Filter name. The specified filter name should be selected from the menu.

#### <span id="Sources_with_<count>_Repository_references"></span><span id="Sources_with_.3Ccount.3E_Repository_references" class="mw-headline">Sources with \<count\> Repository references</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches sources with a certain number of repository references

#### <span id="Sources_with_<count>_media"></span><span id="Sources_with_.3Ccount.3E_media" class="mw-headline">Sources with \<count\> media</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches sources with a certain number of items in the gallery. Values: Number of instances -- Number must be greater than/lesser/equal to

#### <span id="Sources_with_Id_containing_<text>"></span><span id="Sources_with_Id_containing_.3Ctext.3E" class="mw-headline">Sources with Id containing \<text\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches sources whose Gramps ID matches the regular expression

#### <span id="Sources_with_a_reference_count_of_<count>"></span><span id="Sources_with_a_reference_count_of_.3Ccount.3E" class="mw-headline">Sources with a reference count of \<count\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches sources with a certain number of references. Values: Number of references -- Number must be greater than/lesser/equal to

#### <span id="Sources_with_repository_reference_containing_<text>_in_"Call_Number""></span><span id="Sources_with_repository_reference_containing_.3Ctext.3E_in_.22Call_Number.22" class="mw-headline">Sources with repository reference containing \<text\> in "Call Number"</span>[edit](/wiki/index.php?title=Gramps_6.0_Wiki_Manual_-_Filters&action=edit&section=193 "Edit section: Sources with repository reference containing <text> in "Call Number"")<span class="mw-editsection-bracket">\]</span>

Matches sources with a repository reference containing a substring in 'Call Number'

#### <span id="Sources_with_repository_reference_matching_the_<repository_filter>"></span><span id="Sources_with_repository_reference_matching_the_.3Crepository_filter.3E" class="mw-headline">Sources with repository reference matching the \<repository filter\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches sources with a repository reference that match a certain repository filter

#### <span id="Sources_with_the_<tag>"></span><span id="Sources_with_the_.3Ctag.3E" class="mw-headline">Sources with the \<tag\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches sources with a tag of a particular value. Values: Tag name.

#### <span id="Sources_with_title_containing_<text>"></span><span id="Sources_with_title_containing_.3Ctext.3E" class="mw-headline">Sources with title containing \<text\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches sources whose title contains a certain substring

### <span id="Citations_Category" class="mw-headline">Citations Category</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following general rules:

#### <span id="Citation_with_<Id>"></span><span id="Citation_with_.3CId.3E" class="mw-headline">Citation with \<Id\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches citations with Gramps ID. The rule returns a match only if the ID is matched exactly. You can either enter the ID into a text entry field, or select an object from the list by clicking <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Select...</span> button. In the latter case, the ID will appear in the text field after the selection was made.

#### <span id="Citations_changed_after_<date_time>"></span><span id="Citations_changed_after_.3Cdate_time.3E" class="mw-headline">Citations changed after \<date time\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches citations records changed after a specified date-time (yyy-mm-dd hh:mm:ss) or in the range, if a second date-time is given: Values: Changed after: -- but before:.

#### <span id="Citations_having_<count>_notes"></span><span id="Citations_having_.3Ccount.3E_notes" class="mw-headline">Citations having \<count\> notes</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches citations having a certain number of notes: Values: Number of instances -- Number must be greater than/lesser/equal to

#### <span id="Citations_having_notes_containing_<text>"></span><span id="Citations_having_notes_containing_.3Ctext.3E" class="mw-headline">Citations having notes containing \<text\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches citations whose notes contain text matching a regular expression

#### <span id="Citations_marked_private" class="mw-headline">Citations marked private</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches citations that are indicated as private.

#### <span id="Citations_matching_parameters" class="mw-headline">Citations matching parameters</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

General filters rule that matches Citations with particular parameters:

- **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Volume/Page</span>**
- **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Date</span>**
- **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Confidence level</span>**

Also offers the option to **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Use regular expression</span>**.

#### <span id="Citations_matching_the_<filter>"></span><span id="Citations_matching_the_.3Cfilter.3E" class="mw-headline">Citations matching the \<filter\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches citations matched by the specified filter name. Values: Filter name. The specified filter name should be selected from the menu.

#### <span id="Citations_with_<count>_media"></span><span id="Citations_with_.3Ccount.3E_media" class="mw-headline">Citations with \<count\> media</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches citations with a certain number of items in the gallery. Values: Number of instances -- Number must be greater than/lesser/equal to

#### <span id="Citations_with_Id_containing_<text>"></span><span id="Citations_with_Id_containing_.3Ctext.3E" class="mw-headline">Citations with Id containing \<text\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches citations whose Gramps ID matches the regular expression

#### <span id="Citations_with_Volume/Page_containing_<text>"></span><span id="Citations_with_Volume.2FPage_containing_.3Ctext.3E" class="mw-headline">Citations with Volume/Page containing \<text\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches citations whose Volume/Page contains a certain substring

#### <span id="Citations_with_a_reference_count_of_<count>"></span><span id="Citations_with_a_reference_count_of_.3Ccount.3E" class="mw-headline">Citations with a reference count of \<count\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches citations with a certain number of references. Values: Number of references -- Number must be greater than/lesser/equal to

#### <span id="Citations_with_a_source_with_a_repository_reference_matching_the_<repository_filter>"></span><span id="Citations_with_a_source_with_a_repository_reference_matching_the_.3Crepository_filter.3E" class="mw-headline">Citations with a source with a repository reference matching the \<repository filter\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches citations with a source with a repository reference that match a certain repository filter

#### <span id="Citations_with_source_matching_the_<source_filter>"></span><span id="Citations_with_source_matching_the_.3Csource_filter.3E" class="mw-headline">Citations with source matching the \<source filter\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches citations with sources that match the specified source filter name

#### <span id="Citations_with_the_<tag>"></span><span id="Citations_with_the_.3Ctag.3E" class="mw-headline">Citations with the \<tag\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches citations with a tag of a particular value. Values: Tag name.

#### <span id="Every_citation" class="mw-headline">Every citation</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches every citation in the database.

### <span id="Repositories_Category" class="mw-headline">Repositories Category</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following general rules:

#### <span id="Every_repository" class="mw-headline">Every repository</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches every repository in the database.

#### <span id="Repositories_changed_after_<date_time>"></span><span id="Repositories_changed_after_.3Cdate_time.3E" class="mw-headline">Repositories changed after \<date time\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches repository records changed after a specified date-time (yyy-mm-dd hh:mm:ss) or in the range, if a second date-time is given: Values: Changed after: -- but before:.

#### <span id="Repositories_having_notes_containing_<text>"></span><span id="Repositories_having_notes_containing_.3Ctext.3E" class="mw-headline">Repositories having notes containing \<text\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches repositories whose notes contain text matching a regular expression

#### <span id="Repositories_marked_private" class="mw-headline">Repositories marked private</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches repositories that are indicated as private.

#### <span id="Repositories_matching_parameters" class="mw-headline">Repositories matching parameters</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

General filters rule that matches Repositories with particular parameters:

- **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Name</span>**
- **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Type</span>**
- **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Address</span>** : searches all text fields in all mailing addresses
- **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">URL</span>** : searches all text fields in all URLs (See Bug <a href="https://gramps-project.org/bugs/view.php?id=13225" class="external text" rel="nofollow">13225</a>)

Also offers the option to **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Use regular expression</span>**.

#### <span id="Repositories_matching_the_<filter>"></span><span id="Repositories_matching_the_.3Cfilter.3E" class="mw-headline">Repositories matching the \<filter\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches repositories matched by the specified filter name. Values: Filter name. The specified filter name should be selected from the menu.

#### <span id="Repositories_with_Id_containing_<text>"></span><span id="Repositories_with_Id_containing_.3Ctext.3E" class="mw-headline">Repositories with Id containing \<text\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches repositories whose Gramps ID matches the regular expression

#### <span id="Repositories_with_a_reference_count_of_<count>"></span><span id="Repositories_with_a_reference_count_of_.3Ccount.3E" class="mw-headline">Repositories with a reference count of \<count\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches repositories with a certain number of references. Values: Number of references -- Number must be greater than/lesser/equal to

#### <span id="Repositories_with_name_containing_<text>"></span><span id="Repositories_with_name_containing_.3Ctext.3E" class="mw-headline">Repositories with name containing \<text\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches repositories whose name contains substring

#### <span id="Repositories_with_the_<tag>"></span><span id="Repositories_with_the_.3Ctag.3E" class="mw-headline">Repositories with the \<tag\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches repositories with a tag of a particular value. Values: Tag name.

#### <span id="Repository_with_<Id>"></span><span id="Repository_with_.3CId.3E" class="mw-headline">Repository with \<Id\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches repositories with Gramps ID. The rule returns a match only if the ID is matched exactly. You can either enter the ID into a text entry field, or select an object from the list by clicking <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Select...</span> button. In the latter case, the ID will appear in the text field after the selection was made.

### <span id="Media_Category_2" class="mw-headline">Media Category</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following general rules:

#### <span id="Every_media_object" class="mw-headline">Every media object</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches every media object in the database.

#### <span id="Media_object_with_<Id>"></span><span id="Media_object_with_.3CId.3E" class="mw-headline">Media object with \<Id\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches media objects with Gramps ID. The rule returns a match only if the ID is matched exactly. You can either enter the ID into a text entry field, or select an object from the list by clicking <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Select...</span> button. In the latter case, the ID will appear in the text field after the selection was made.

#### <span id="Media_objects_changed_after_<date_time>"></span><span id="Media_objects_changed_after_.3Cdate_time.3E" class="mw-headline">Media objects changed after \<date time\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches media object records changed after a specified date-time (yyy-mm-dd hh:mm:ss) or in the range, if a second date-time is given: Values: Changed after: -- but before:.

#### <span id="Media_objects_having_notes_containing_<text>"></span><span id="Media_objects_having_notes_containing_.3Ctext.3E" class="mw-headline">Media objects having notes containing \<text\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches media objects whose notes contain text matching a regular expression

#### <span id="Media_objects_marked_private" class="mw-headline">Media objects marked private</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches media objects that are indicated as private.

#### <span id="Media_objects_matching_parameters" class="mw-headline">Media objects matching parameters</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

General filters rule that matches Media objects with particular parameters:

- **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Text</span>**
- **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Media type</span>**

Also offers the option to **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Use regular expression</span>**.

#### <span id="Media_objects_matching_the_<filter>"></span><span id="Media_objects_matching_the_.3Cfilter.3E" class="mw-headline">Media objects matching the \<filter\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches media objects matched by the specified filter name. Values: Filter name. The specified filter name should be selected from the menu.

#### <span id="Media_objects_with_Id_containing_<text>"></span><span id="Media_objects_with_Id_containing_.3Ctext.3E" class="mw-headline">Media objects with Id containing \<text\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches media objects whose Gramps ID matches the regular expression

#### <span id="Media_objects_with_a_reference_count_of_<count>"></span><span id="Media_objects_with_a_reference_count_of_.3Ccount.3E" class="mw-headline">Media objects with a reference count of \<count\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches media objects with a certain number of references. Values: Number of references -- Number must be greater than/lesser/equal to

#### <span id="Media_objects_with_the_<tag>"></span><span id="Media_objects_with_the_.3Ctag.3E" class="mw-headline">Media objects with the \<tag\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches media objects with a tag of a particular value. Values: Tag name.

#### <span id="Media_objects_with_the_attribute_<attribute>"></span><span id="Media_objects_with_the_attribute_.3Cattribute.3E" class="mw-headline">Media objects with the attribute \<attribute\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches media objects with the attribute of a particular value

### <span id="Notes_Category" class="mw-headline">Notes Category</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following general rules:

#### <span id="Every_note" class="mw-headline">Every note</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches every note in the database.

#### <span id="Note_with_<Id>"></span><span id="Note_with_.3CId.3E" class="mw-headline">Note with \<Id\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches notes with Gramps ID. The rule returns a match only if the ID is matched exactly. You can either enter the ID into a text entry field, or select an object from the list by clicking <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Select...</span> button. In the latter case, the ID will appear in the text field after the selection was made.

#### <span id="Notes_changed_after_<date_time>"></span><span id="Notes_changed_after_.3Cdate_time.3E" class="mw-headline">Notes changed after \<date time\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches notes records changed after a specified date-time (yyy-mm-dd hh:mm:ss) or in the range, if a second date-time is given: Values: Changed after: -- but before:.

#### <span id="Notes_containing_<text>"></span><span id="Notes_containing_.3Ctext.3E" class="mw-headline">Notes containing \<text\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches notes contain text matching a regular expression

#### <span id="Notes_marked_private" class="mw-headline">Notes marked private</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches notes that are indicated as private.

#### <span id="Notes_matching_parameters" class="mw-headline">Notes matching parameters</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches Notes with particular parameters

- **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Text</span>**
- **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Note type</span>**

Also offers the option to **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Use regular expression</span>**.

#### <span id="Notes_matching_the_<filter>"></span><span id="Notes_matching_the_.3Cfilter.3E" class="mw-headline">Notes matching the \<filter\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches notes matched by the specified filter name. Values: Filter name. The specified filter name should be selected from the menu.

#### <span id="Notes_with_Id_containing_<text>"></span><span id="Notes_with_Id_containing_.3Ctext.3E" class="mw-headline">Notes with Id containing \<text\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches notes whose Gramps ID matches the regular expression

#### <span id="Notes_with_a_reference_count_of_<count>"></span><span id="Notes_with_a_reference_count_of_.3Ccount.3E" class="mw-headline">Notes with a reference count of \<count\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches notes with a certain number of references. Values: Number of references -- Number must be greater than/lesser/equal to

#### <span id="Notes_with_the_<tag>"></span><span id="Notes_with_the_.3Ctag.3E" class="mw-headline">Notes with the \<tag\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches notes with a tag of a particular value. Values: Tag name.

#### <span id="Notes_with_the_particular_type" class="mw-headline">Notes with the particular type</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches notes with the particular type

## <span id="Mother_filters" class="mw-headline">Mother filters</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule category finds families having mothers that match the rule:

### <span id="Families_having_mother_with_Id_containing_<text>"></span><span id="Families_having_mother_with_Id_containing_.3Ctext.3E" class="mw-headline">Families having mother with Id containing \<text\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches families whose mother has a specified Gramps ID

### <span id="Families_with_mother_with_the_<name>"></span><span id="Families_with_mother_with_the_.3Cname.3E" class="mw-headline">Families with mother with the \<name\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches families whose mother has a specified (partial) name

## <span id="Position_filters" class="mw-headline">Position filters</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule category finds Places by their Global Positioning System coordinates proximity:

### <span id="Places_in_neighborhood_of_given_position" class="mw-headline">Places in neighborhood of given position</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches places with latitude or longitude position in a rectangle of given height and width (in degrees), and with middle point the given latitude and longitude.

### <span id="Places_with_no_latitude_or_longitude_given" class="mw-headline">Places with no latitude or longitude given</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches places with empty latitude or longitude

### <span id="Places_within_an_area" class="mw-headline">Places within an area</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches places within a given distance of a specified place.

After selecting a place (which must have a valid set of coordinates), match any place whose coordinates lie within a circle on the globe (an ellipse on a flatten map) centered on those coordinates of a specified radius.

The units of distance can be selected: kilometers (linear measure), degrees (angular measure), and miles (linear measure).

## <span id="Source_filters" class="mw-headline">Source filters</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule category finds Citations that match the rule:

### <span id="Citation_with_Source_<Id>"></span><span id="Citation_with_Source_.3CId.3E" class="mw-headline">Citation with Source \<Id\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches a citation with a source with a specified Gramps ID

### <span id="Citations_having_source_notes_containing_<text>"></span><span id="Citations_having_source_notes_containing_.3Ctext.3E" class="mw-headline">Citations having source notes containing \<text\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches citations whose source notes contain a substring or match a regular expression

### <span id="Citations_with_Source_Id_containing_<text>"></span><span id="Citations_with_Source_Id_containing_.3Ctext.3E" class="mw-headline">Citations with Source Id containing \<text\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches citations whose source has a Gramps ID that matches the regular expression

### <span id="Sources_matching_parameters" class="mw-headline">Sources matching parameters</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

General filters rule that matches Sources with a source of a particular value:

- **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Title</span>**
- **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Author</span>**
- **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Abbreviation</span>**
- **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Publication</span>**

Also offers the option to **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Use regular expression</span>**.

## <span id="Relationship_filters" class="mw-headline">Relationship filters</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This category includes the following rules that match people based on their mutual relationship:

### <span id="People_related_to_<Person>"></span><span id="People_related_to_.3CPerson.3E" class="mw-headline">People related to \<Person\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches people related to a specified person

### <span id="Relationship_path_between_<person>_and_people_matching_<filter>"></span><span id="Relationship_path_between_.3Cperson.3E_and_people_matching_.3Cfilter.3E" class="mw-headline">Relationship path between \<person\> and people matching \<filter\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Searches over the database starting from a specified person and returns everyone between that person and a set of target people specified with a filter. This produces a set of relationship paths (including by marriage) between the specified person and the target people. Each path is not necessarily the shortest path.

### <span id="Relationship_path_between_<persons>"></span><span id="Relationship_path_between_.3Cpersons.3E" class="mw-headline">Relationship path between \<persons\></span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

This rule matches all ancestors of both people back to their common ancestors (if exist). This produces the "relationship path" between these two people, through their common ancestors. You can either enter the ID of each person into the appropriate text entry fields, or select people from the list by clicking their <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Select...</span> buttons. In the latter case, the ID will appear in the text field after the selection was made.

### <span id="Relationship_path_between_bookmarked_persons" class="mw-headline">Relationship path between bookmarked persons</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Matches the ancestors of bookmarked individuals back to common ancestors, producing the relationship path(s) between bookmarked persons.

## <span id="Tagging" class="mw-headline">Tagging</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

<div class="floatleft">

![[_media/Gramps-tag.png]]

</div>

A [Tag](wiki:Gramps_Glossary#tag) is a custom titled and color-coded label that can be created with the **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">[Organize Tags](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Organize_Tags_Window)</span>** dialog and attached to selected ![[_media/48x48-gramps-citation.png|Citations]] [Citation](#citation), ![[_media/22x22-gramps-event.png|Events]] [Event](#event), ![[_media/16x16-gramps-family.png|Family]] [Family](#family), ![[_media/Gramps-media.png|Media]] [Media](#media), ![[_media/16x16-gramps-notes.png|Notes]] [Note](#note), ![[_media/16x16-gramps-person.png|People]] [Person](#person), ![[_media/16x16-gramps-place.png|Places]] [Place](#place), ![[_media/16x16-gramps-repository.png|Repositories]] [Repository](#repository) or ![[_media/48x48-gramps-source34.png|Sources (v3.4.x)]] [Source](#source) objects for the purpose of easy identification and filtering.

A custom titled keyword or phrase can be used to group the collection to produce a report. Multiple tags may be used to label and categorize objects into multiple groups when filtering by other attributes is not viable.

For example, when you have a big family tree, you might want to make subsets of the family tree, and these subsets might be overlapping. For example, the subsets of your fathers family and your mothers family, some subset of your family that emigrated to Australia. The idea would be to assign a different tag to each subset: *Paternal*, *Maternal*, *Australia* and *ToDo* to identify each group.

Technical: For those of you that use the *Gmail* or *Thunderbird* Email programs, the [Tag](wiki:Gramps_Glossary#tag) feature will seem quite familiar. Where instead of classifying emails into folders like in *Outlook* (Windows) or *Evolution* (Linux), emails are classified by assigning tags to them. So instead of having a disjoint N:1 classification (a email can be in one and only one folder, and a folder can contain many emails), in *Gmail* or *Thunderbird* there is a N:M classification (where a email can have several tags, and a tag can be applied to several emails)  

### <span id="Tag_menu" class="mw-headline">Tag menu</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

<div class="thumb tright">

<div class="thumbinner" style="width:452px;">

![[_media/Menu-Edit-Tag-Options-60.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:Menu-Edit-Tag-Options-60.png" class="internal" title="Enlarge"></a>

</div>

Fig. 16.8 Tag actions from Edit menu

</div>

</div>

</div>

From the **[Edit -\> Tag](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Edit)** menu you can select from the following options:

- **[New Tag...](wiki:Gramps_6.0_Wiki_Manual_-_Filters#New_Tag_dialog)** dialog
- **[Organize Tags...](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Organize_Tags_Window)** Window
- A list of previously created Tag's that you can select for the following actions:
  - **Add tag 'xxxx'**
  - **Remove tag 'xxxx'**

  

### <span id="Tag_selected_rows_icon_toolbar" class="mw-headline">Tag selected rows icon toolbar</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

<div class="thumb tright">

<div class="thumbinner" style="width:283px;">

![[_media/Toolbar-TagSelectedRows-Icon-DropDownMenu-overview-example-60.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:Toolbar-TagSelectedRows-Icon-DropDownMenu-overview-example-60.png" class="internal" title="Enlarge"></a>

</div>

Fig. 16.9 Available Tag actions from "Tag selected rows" Toolbar icon - drop down menu overview - example

</div>

</div>

</div>

Or click the Toolbar ![[_media/16x16-gramps-tag.png]]<span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Tag selected rows</span> button to access the same options as the **[Edit -\> Tag](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Tag_menu)** menu.  
See also:

- [Tag Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Tag_Report) that lists primary objects (person, family, notes) who match the selected Tag.

  

### <span id="New_Tag_dialog" class="mw-headline">New Tag dialog</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

<div class="thumb tright">

<div class="thumbinner" style="width:331px;">

![[_media/NewTag-dialog-default-60.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:NewTag-dialog-default-60.png" class="internal" title="Enlarge"></a>

</div>

Fig. 16.10 "New Tag" dialog - default

</div>

</div>

</div>

<div class="thumb tright">

<div class="thumbinner" style="width:452px;">

![[_media/NewTag-dialog-ShowingMultipleListSelection-example-50.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:NewTag-dialog-ShowingMultipleListSelection-example-50.png" class="internal" title="Enlarge"></a>

</div>

Fig. 16.11 Attaching a "New Tag" to multiple list entry selections - example with "New Tag" dialog

</div>

</div>

</div>

You are able to add a new Tag to either a single list entry or multiple list entries from any of the category list views, by making the selection and then using the **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">New Tag</span>** dialog to enter the name of the Tag and if desired selecting a Color for Tag using the **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Pick a Color</span>** selector. Note the order of the Tags in the Organize Tag list define the priority for coloring rows in the category list views.

Tags are available to use with all [primary objects](wiki:Gramps_Glossary#primary_object).  

##### <span id="Tagging_a_selection_of_objects" class="mw-headline">Tagging a selection of objects</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Due to the **static** nature of Tags, it might be useful to add a Tag to a selection of objects. For example one should be able to select a number of people in the [Person (list) View](wiki:Gramps_6.0_Wiki_Manual_-_Categories#People_Category), and add a new Tag or an existing one to them.  

### <span id="Organize_Tags_Window" class="mw-headline">Organize Tags Window</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

<div class="thumb tright">

<div class="thumbinner" style="width:418px;">

![[_media/MenuEditTag-OrganizeTags-dialog-example-60.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:MenuEditTag-OrganizeTags-dialog-example-60.png" class="internal" title="Enlarge"></a>

</div>

Fig. 16.12 Organize Tags - dialog - example

</div>

</div>

</div>

In the **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Organize Tags</span>** dialog Tags are shown in a list showing the `Name` and `Color` with the order of the Tags in the list defining the priority for coloring rows in the category views. You may also reorder the Tags by selecting one and using the <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Up</span> or <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Down</span> buttons, <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Add</span> will show the **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">New Tag</span>** dialog and the <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Remove</span> button will show the **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Remove tag \<tag name\></span>** dialog. The <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Help</span> button accesses this page. Once completed you can <span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Close</span> the dialog.

  
  

#### <span id="Remove_tag_<tag_name>_dialog"></span><span id="Remove_tag_.3Ctag_name.3E_dialog" class="mw-headline">Remove tag \<tag name\> dialog</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

<div class="thumb tright">

<div class="thumbinner" style="width:452px;">

![[_media/Remove-tag-dialog-example-60.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:Remove-tag-dialog-example-60.png" class="internal" title="Enlarge"></a>

</div>

Fig. 16.13 Remove tag \<tag name\> dialog - example

</div>

</div>

</div>

<table style="width:40%;margin-top:+.7em;margin-bottom:+.7em;background-color: #ffd43385;border:1px solid #cccccc85; padding: 5px" data-align="left">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>![[_media/Gramps-notes.png]]</td>
<td><p>This article's content is incomplete or a placeholder stub.<br />
Please update or expand this section.</p></td>
</tr>
</tbody>
</table>

  

### <span id="Tag_selection_dialog" class="mw-headline">Tag selection dialog</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

<div class="thumb tright">

<div class="thumbinner" style="width:307px;">

![[_media/TagSelection-dialog-example-60.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:TagSelection-dialog-example-60.png" class="internal" title="Enlarge"></a>

</div>

Fig. 16.14 "Tag selection" dialog - example

</div>

</div>

</div>

When you use ![[_media/16x16-gramps-tag.png]]<span class="kbd" style="border: 1px solid; color:#5e4638; background-color: #f9f9f9; border-bottom-width: 2px; -moz-border-radius: 3px; -webkit-border-radius: 3px; border-radius: 3px; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Edit the tag list</span> button from any of the Editor dialogs like **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">Person Edit</span>** the **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">[Tag selection](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Tag_selection_dialog)</span>** dialog list is shown that lets you remove or assign existing custom tags. The tags are shown in alphabetical order and not the order shown in the Organize Tags Window.  

### <span id="Usage_of_tags" class="mw-headline">Usage of tags</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

Here are a some ideas of operations that can be done with tags

#### <span id="Filtering" class="mw-headline">Filtering</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

<div class="thumb tright">

<div class="thumbinner" style="width:372px;">

![[_media/Sidebar-PeopleTreeView-Filter-TagDropDownList-example-60.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:Sidebar-PeopleTreeView-Filter-TagDropDownList-example-60.png" class="internal" title="Enlarge"></a>

</div>

Fig. 16.15 Gramps Filter SideBar - Tag list example

</div>

</div>

</div>

The most obvious use is that of filtering.

- Tags and filters both create subsets of the tree. However they have practical differences in usage.

Specifying your fathers family using filters is an easy thing; there are already filters based on some logic's that do it. On the other hand, specifying the people that emigrated to the USA is harder, while for the famous people in your family it is simply impossible as there is no logical rule. Tags are much more practical here.

However filters have the advantage of being **dynamical**. If you add an ancestor of your father to the family tree, it will be automatically added to the filter.

On the other hand, tags are **static**. When adding a famous person in the tree, you have to explicitly tag them as *FAMOUS*.

- The most immediate object that comes to mind are the individuals, and that is also the most useful. However, other objects could be tagged:
  - Places: For example "places to visit",
  - Source: For example "sources in german",
  - Notes: For example "notes in progress", or "notes in german",
  - Media: For example "Picture belonging to Uncle Alfred".

Tags are available to use with **all primary objects**.  

#### <span id="Tags_Column" class="mw-headline">Tags Column</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

<div class="thumb tright">

<div class="thumbinner" style="width:452px;">

![[_media/PeopleListView-ExampleTagColoredRows-50.png]]

<div class="thumbcaption">

<div class="magnify">

<a href="/wiki/index.php/File:PeopleListView-ExampleTagColoredRows-50.png" class="internal" title="Enlarge"></a>

</div>

Fig. 16.16 People (List) View - Showing "Tag" column and colored tag rows - example

</div>

</div>

</div>

Use the **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">[Columns Editor](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Columns_editor)</span>** to add the `Tags` column to the list views of objects to easily see your tags. The content of the `Tags` column is then displayed as a comma-separated list of the tags attached to the objects. Note the order of the Tags in the **<span class="kbd" style="background:#D3D3D3; letter-spacing:0.1em; padding-left:0.5em; padding-right:0.4em;">[Organize Tags](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Organize_Tags_Window)</span>** dialog list define the priority for coloring rows in the category list views.

#### <span id="Tag_Usage_Report" class="mw-headline">Tag Usage Report</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

The [Tag Usage Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Tag_Report) lists [primary objects](wiki:Gramps_Glossary#primary_object) (person, family, notes) having the selected Tag.

### <span id="See_also_5" class="mw-headline">See also</span>[edit](wiki:index.php)<span class="mw-editsection-bracket">\]</span>

- [Tags in Gramps](wiki:Tags_in_Gramps) - an introduction
- Automatic [Import timestamp Tags](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Import)
- filtered [Add/Remove Tag Tool](wiki:Addon:AddRemoveTagTool) (Third-party addon for Gramps)

  

|  |  |  |
|:---|:--:|---:|
| [**Previous**](wiki:Gramps_6.0_Wiki_Manual_-_Settings) | [**Index**](wiki:Gramps_6.0_Wiki_Manual) | [**Next**](wiki:Gramps_6.0_Wiki_Manual_-_FAQ) |

<div class="LanguageLinks">

|  |  |  |
|----|----|----|
| ![[_media/Gramps-config-language.png]] | **[Languages](wiki:Portal:Translators):**  | <span class="mw-selflink selflink">English</span>     • <span lang="da"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/da" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/da">dansk</a></span>  • <span lang="de"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/de" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/de">Deutsch</a></span>  • <span lang="es"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/es" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/es">español</a></span>  • <span lang="fi"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/fi" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/fi">suomi</a></span>  • <span lang="fr"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/fr" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/fr">français</a></span>  • <span lang="he">[עברית](wiki:Gramps_6.0_Wiki_Manual_-_Filters/he)</span>      • <span lang="mk"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/mk" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/mk">македонски</a></span>   • <span lang="nl"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/nl" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/nl">Nederlands</a></span>      • <span lang="ru"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/ru" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/ru">русский</a></span>   • <span lang="sq"><a href="/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Filters/sq" class="mw-redirect" title="Gramps 6.0 Wiki Manual - Filters/sq">shqip</a></span>   • <span lang="sk">[slovenčina](wiki:Gramps_6.0_Wiki_Manual_-_Filters/sk)</span>   • <span lang="tr">[Türkçe](wiki:Gramps_6.0_Wiki_Manual_-_Filters/tr)</span> |

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
