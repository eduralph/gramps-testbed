---
title: Gramps 6.0 Wiki Manual - Categories/tr
categories:
- Stub
- Tr:Documentation
managed: false
source: wiki-scrape
wiki_revid: 125444
wiki_fetched_at: '2026-05-30T20:53:56Z'
lang: tr
---

{{#vardefine:chapter\|4}} {{#vardefine:figure\|0}}

[Soy bilgisi](https://en.wikipedia.org/wiki/Genealogy#Types_of_information) çok geniştir ve son derece ayrıntılı olabilir. Bunu sergilemek, Gramps'ın bilgileri her biri kendi Görüşlerine sahip bir dizi Kategoriye bölerek ve düzenleyerek üstlendiği bir zorluk teşkil eder. Her Görünüm, belirli bir kategoriye göre seçilen toplam bilginin bir bölümünü görüntüler. Farklı Kategorileri keşfettikçe bu daha net hale gelecektir.

## Gezginin Kategorileri

The different Categories of the [Navigator](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Navigator): The navigator is located at the left of the window and allows selection of the different categories.

![[_media/Navigator-mode-selection-dropdownlist-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Navigator mode selection drop down list]]

-   
  Displays different general purpose Gramplets, small widgets that can help in your genealogical research.

<!-- -->

-   
  List of people in the family tree.

<!-- -->

-   
  Displays the relationships between the Active Person and other people in a textual way. This includes the parents, siblings, spouses, and children of that person.

<!-- -->

-   
  List of families in the family tree.

<!-- -->

-   
  Displays graphical trees for the selected person.

<!-- -->

-   
  List of events in the family tree.

<!-- -->

-   
  List of places in the family tree.

<!-- -->

-   
  Displays place data of your family tree on a map.

<!-- -->

-   
  List of sources in the family tree.

<!-- -->

-   
  List of citations in the family tree.

<!-- -->

-   
  List of repositories in the family tree.

<!-- -->

-   
  List of media objects in the family tree.

<!-- -->

-   
  List of notes in the family tree.

![[_media/wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Drop-Down_navigator_mode|[_media/Navigator-mode-selection-drop-down-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} [Drop-Down navigator mode]] showing People Category view modes]]

The categories can contain several ways of presenting the data. Each specific way is called a View mode. For example:

- **People** *view category*

  - **Grouped People** *default hierarchical list mode*
  - **People** *alternate flat list mode*

For each category you have a variety of ways to switch between View modes:

1.  by selecting the relevant icon from the toolbar
2.  from the menu
3.  from the Navigator bar when the Drop-down or Expander features are selected (See [Switching Navigator modes](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Switching_Navigator_modes))
4.  Via the number-based [keybindings](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#List_Views) (aka keyboard shortcuts) to *Change the view mode to correspond to number key ///../ in this view category*

The following sections provide a brief description of each category and the view modes within.

## Gösterge Bölümleri

![[_media/DashboardCategory-DashboardView-default-gramplets-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dashboard Category view]] This contains the **Dashboard**, which shows a number of widgets, called [Gramplets](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#What_is_a_Gramplet), that can help you in your research. Two Gramplets are shown by default on start-up (the [Top Surname](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Top_Surnames) and [Welcome to Gramps!](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Welcome) Gramplets) in two column configuration. When you have an open Family Tree you can by using the context menu (right-clicking) on an empty area of the Dashboard View, to see a popup menu to "" that shows a list of the possible Gramplets you may add and use.

- Gramplet - list age span statistics in a number of graphs

- Gramplet - list the people alive and their ages on a particular date

- Gramplet - see people's events on a particular date, or in a month in the past

- \- Frequently asked questions about Gramps.

- Gramplet - most popular given names

- \- run a Quick View on the current person

- \- see world's records of your data

- Gramplet - keep track of what you have done, and what records you have visited

- generates [SoundEx codes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Soundex) for the names of people in the database.

- Gramplet - see stats on the database

- Gramplet - most popular surnames as a "text cloud"

- Gramplet - a notepad to keep tabs on your research

- Gramplet - top 10 most popular surnames

- Gramplet - a Gramps welcome message

- Gramplet - what needs to be done next

In addition, there are a number of Third party Gramplets that you can easily install and use. These include:

- \- current, breaking news from Gramps

- \- edit active person's name, birth date and place, death date and place, and add people

- \- a Python shell

- \- see and edit active person's primary Person Note

and many others. See [Third-party Addons](wiki:Third-party_Addons) for more details.

For more detailed information on using the installed Gramplets, see [Gramplets](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets).

{{-}}

### Gramplet Layout

![[_media/ConfigureTheActiveView-icon-on-toolbar-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  button]]

You can change the for the Dashboard on the Gramplet Layout tab or change the options for the other displayed Gramplets on the related tabs, click the ![[_media/Gramps-config.png]] button. {{-}}

## People Category

In the the or (default) views display a list of all people in the family tree without their connections. From this view, you may add, edit, remove, or merge people. Each view (List or Grouped) display several columns of information about each person.

By default, the view displays the `Name`, `ID`, `Gender`, `Birth Date` and `Death Date` columns for each Person. Additional columns for `Birth Place`, `Death Place`, `Spouse`, `Number of Parents` (in the [topmost or Primary family](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Reorder_Relationships_dialog)), `Number of Marriages`, `Number of Children`, `Number of To Do Notes`, `Private`, `Tags` and `Last Changed` may be displayed. The People view also defaults to showing the [Sidebar](#People_Category_Sidebar) tabs and [Bottombar](#People_Category_Bottombar_tabs)

The dialog can be used to show, hide and change the order of the displayed columns. This editor can be accessed by selecting from the menu or by clicking the ![[_media/Gramps-config.png]] button on the toolbar.

See also

- [Using the People Category](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Using_the_People_Category)
- [Editing information about people](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Editing_information_about_people)

{{-}}

### Ağaç Görünümü - Gruplandırılmış Kişiler

![[_media/PeopleTreeView-GroupedPeople-example-with-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} People Category - Ağaç Görünümü - Gruplandırılmış Kişiler]]

İnsanlar soyadlarına göre gruplandırılmıştır. Her aile adının solunda tipik olarak ya bir ok ya da başka türde bir gösterge bulunur (örn: +). Bir kez tıklamak, o adı paylaşan kişilerin tüm listesini ortaya çıkaracaktır. Göstergeye tekrar tıklamak listeyi "daraltacak" ve sadece aile adını gösterecektir.

Listeden bir kişi seçip sağ tıklayarak gösterilen bağlam/açılır menüyü kullanarak ek seçenekler mevcuttur:

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- - 

  - 

  - 

  - 

  - 

  - 

  - 

  - 

{{-}}

### People List View

### Tree View - People List View

![[_media/PersonView-PeopleListView-example-with-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} People Category - People List View]]

List of all the people in the database, sorted by first column which by default is the column.

Additional options are available by selecting a person from the list and using the context/pop-up menu shown by right-clicking:

- 

- 

- 

- 

- 

- 

- 

- 

- - 

  - 

  - 

  - 

  - 

  - 

  - 

  - 

{{-}}

### Kişiler Kategorisi Alt Çubuk sekmeleri

Her iki Ağaç Görünümü (Gruplanmış Kişiler/Kişi Listesi Görünümü) aşağıdaki [Alt Çubuk](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) sekmelerine sahiptir. Yapılandırma görünümlerden bağımsızdır. {{-}}

#### Ayrıntılar

[Ayrıntılar](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Ayrıntılar) Gramplet'e bakın {{-}}

#### Galeri

[Galeri](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Galeri) Gramplet'e bakın {{-}}

#### Etkinlikler

[Etkinlikler](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Etkinlikler) Gramplet'e bakın {{-}}

#### Çocuklar

[Çocuklar](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Çocuklar) Gramplet'e bakın {{-}}

#### Alıntılar

[Alıntılar](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Alıntılar) Gramplet'e bakın {{-}}

#### Notlar

[Notlar](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Notlar) Gramplet'e bakın {{-}}

#### Nitelikler

[Nitelikler](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Nitelikler) Gramplet'e bakın {{-}}

#### Referanslar

[Referanslar](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Referanslar) Gramplet'e bakın {{-}}

### Kişiler Kategorisi Kenar Çubuğu sekmeleri

Her iki Ağaç Görünümü de (Gruplanmış Kişiler/Kişi Listesi Görünümü) varsayılan olarak aşağıdaki [Kenar Çubuğu](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/tr#Alt_çubuk_ve_Kenar_çubuğu) sekmesine sahiptir. Yapılandırma görünümler arasında bağımsızdır. {{-}}

#### Süzgeç

[Süzgeç](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Süzgeç) Gramplet'ine bakınız {{-}}

## Relationships Category

![[_media/Relationships-category-view-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Relationships Category view]]

The Relationships Category shows the default which displays all the relationships of the Active Person (the selected person). Specifically, it shows the parents, siblings, spouses, and children of that person.

The Relationships Category is designed to allow for quick navigation. You can quickly change the Active Person simply by clicking the name of any person listed on the page. Each name is actually a [hypertext link](http://en.wikipedia.org/wiki/Hyperlink), similar to a web page.

The name of the Active Person is in **bold** style. Other names are shown either with or without ***bold and italic*** emphasis depending on whether certain relationships exist for the named person. For a person listed as a parent or spouse of the Active Person, the name is emphasized if that person has a parent family. For a person listed as a sibling or child of the Active Person, the name is emphasized if that person has children.

Dates are normally in regular style, and in *italic* style if the displayed event is a fallback event, i.e., a substitute event for another missing event. That may be christening event for birth event, burial event for death event, etc. {{-}}

### Relationships Category view

For the Relationships Category views via the menu or toolbar you may select:

- or the icon - opens the

- or the icon - to create a new family with the Active Person listed as a child.

- or the icon - which opens the [Select Family selector](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Select_Family_selector) allowing you to choose from a list of existing families, and then add the person as a child to that family.

- or the icon -

- or the icon - to open the [Reorder Relationships dialog](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Reorder_Relationships_dialog)

The following sections are available: {{-}}

#### Active Person

- At the top of the screen, name, , , and information, as well as the calculated age of the Active Person is displayed. You may highlight and copy the and text fields.

<!-- -->

- On the right hand side a photo of the person if available, will be shown. This photo shows the first image available in the tab of this person (if any exist). You can click on the photo to open it in the default picture viewer.

<!-- -->

- Next to the person's name is a symbol indicating gender, and an button. Clicking the button will allow you to edit all of the person's individual information in the dialog.

<!-- -->

- See also: [Setting the Active Person](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Setting_the_Active_Person)

#### Parents

The Parents section, displays the families in which the person is a child. Since it is possible for a person to have multiple sets of parents, it is possible to have several Parents sections.

You may edit an existing parents by selecting the button next to the parents. If you select the button next to a set of parents, then the Active Person will be removed as a child from the parents. This button does not delete the parents' relationship.

See the section to configure what details to show or hide etc...

##### Select Family selector

![[_media/SelectFamily-SelectorDialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Select Family - selector dialog example]]

The selector dialog allows you to link to an already existing Family.

The following columns are shown: ID(default sort for list), Father, Mother, Last Change.

You may use the button to filter the list based on one of the options from the drop down list:

- **ID contains** (default)
- *ID does not contain*
- *Father contains*
- *Father does not contain*
- *Mother contains*
- *Mother does not contain*
- *Last Change contains*
- *Last Change does not contain*

{{-}}

##### Siblings

The Sibling section show the active persons brothers and sisters.

{{-}}

#### Family

Similar to the Parents section is the Family section, which displays families where the Active Person is a parent. Because it is possible for a Person to have been a partner in multiple families, Gramps allows multiple Family sections to describe that. Each family section displays the spouse and any children. Children who were biological offspring of both partners in one Family might be a stepchild or adopted child for one partner of a subsequently formed family.

You may add a family by selecting the button in the toolbar. This will create a new family with the Active Person listed as a father or mother.

Selecting the button next to the spouse will allow you to edit the displayed family. Clicking the button will remove the person from the displayed family.

{{-}}

{{-}}

###### Reorder Relationships dialog

Select the ![[_media/Stock_reorder.png]] button to display the dialog that will allow you to reorder the families. The topmost family is considered the **Primary family** and is the family used for charts, graphs and summaries.

![[_media/ReorderRelationships-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Reorder Relationships - dialog - example]]

When more than one set of parents or more than one set of spouses exists for the Active Person.

Select one of the following:

- the menu
- or the toolbar icon button
- or the icon near the label
- or the icon near the label

to display the dialog that will allow you to reorder:

- the parents order in the top section using the up/down arrow buttons.
- or families order in the bottom section using the up/down arrow buttons.

{{-}}

##### Children

The Active persons children. {{-}}

#### Configuration

![[_media/ConfigureRelationshipsView-Content-tab-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Configure Relationships Category - Content (tab)]]

You can control how much information is displayed.

Use the menu or click the ![[_media/Gramps-config.png]] button in the [Toolbar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Toolbar).

The following options are available:

- On the tab
  -  (checkbox checked by default) show or hide the birth and death information (All except the Active person)

  -  (checkbox checked by default) show or hide siblings.

{{-}} ![[_media/ConfigureRelationshipsView-Layout-tab-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Configure Relationships Category - Layout (tab)]]

- On the tab
  -  (checkbox checked by default)

  -  (checkbox checked by default) - show or hide the button shown next to each person.

  -  (checkbox unchecked by default)

{{-}}

### Relationships Category Bottombar tabs

The by default displays no Gramplets in the [Bottombar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tab. You may add them as required. {{-}}

### Relationships Category Sidebar tabs

The by default displays no Gramplets in the [Sidebar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tab. You may add them as required. {{-}}

## Families Category

![[_media/Families-category-list-view-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Families Category - (List) View]]

In the the displays a list of all families in the database(see Fig. {{#var:chapter}}.{{#var:figure}}). From this view, you may , , , from the list, or . The default display lists the `ID, Father, Mother, Relationship and Marriage Date`. If you configure the active view you can, hide existing columns, show additional columns like `Private, Tags, Last Changed`, or rearrange the column order.

Additional options are available by selecting a family from the list and using the context/pop-up menu shown by right-clicking:

- 

- 

- 

- 

- 

- 

- 

- 

- - 

  - 

See also

- [Using the Families Category](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Using_the_Families_Category)
- [Editing information about relationships](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Editing_information_about_relationships)

{{-}}

### Families Category Bottombar tabs

The shows the following [Bottombar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs as default. {{-}}

#### Gallery

See [Gallery](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Gallery) Gramplet {{-}}

#### Events

See [Events](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Events) Gramplet {{-}}

#### Children

See [Children](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Children) Gramplet {{-}}

#### Citations

See [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) Gramplet {{-}}

#### Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) Gramplet {{-}}

#### Attributes

See [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) Gramplet {{-}}

#### References

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) Gramplet {{-}}

### Families Category Sidebar tabs

The shows the following [Sidebar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs as default. {{-}}

#### Filter

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) Gramplet {{-}}

## Charts Category

The Charts Category shows several graphical representations of the ancestry or descendants of the active person.

By default Gramps shows the View. With the View and chart View and chart view being selectable from the toolbar or menu via

### Pedigree View

![[_media/ChartsCategory-Pedigree-view1-horizontal-right-standard-5gen-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pedigree view 1 (Default) Tree direction:horizontal to right]]

The View shows up to nine generations in the form of a chart, depending on the size of the window you may need to use the scroll bars to see parts of the chart.

Each person is indicated by a box labeled with his or her name, birth information (indicated by an asterisk \* sign), death information (indicated by a plus + sign), a black stripe across the top left corner of the box is shown if the person is deceased (or determined by Gramps to be no longer alive) and optionally the primary image will be displayed if available.

Two lines branch from each person box. The top line leads to the person's father and the bottom line leads to the mother. Solid lines represent the biological birth type relationship, while dashed lines represent non-birth relationships such as adoption, step-parenthood, guardianship, etc.

The left arrow button beside the Active Person is a only selectable if the Active Person has children, clicking this button expands to show a list of the Active Person's children. Selecting one of the children makes that child the Active Person for the chart.

The appearance of the children's names in the menu differentiates the dead ends of the tree from the continuing branches.

Children who have children themselves appear in the menu in the boldface and italic type, while children without children (dead ends) appear in a regular font. If the Active Person has only one child, no menu will be displayed (since there is only one choice) and the child will become the Active Person when the arrow button is clicked.

The right-hand side of the window shows two right arrow buttons. When the top button is clicked, the Father of the Active Person becomes the Active Person. When the bottom button is clicked, the Mother of the Active Person becomes the Active Person.

{{-}} ![[_media/ChartsCategory-PedigreeView-PersonContextMenu-showing-Children-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Person context menu showing Children]]

Right-clicking on any person's box in the Pedigree View will bring up the Person "context menu".

Among other useful items, the context menu has sub-menus listing , , , and of that person.

"Greyed-out" sub-menus indicate the absence of the data in the appropriate category. Similar to the children menu above, Childrens' and Parents' menus distinguish continuing lines from dead ends.

{{-}}

#### Configure the active view

![[_media/ChartsCategory-PedigreeView-ConfigureCharts-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Charts Category - Pedigree View - Configure the active view - dialog - showing Defaults on Layout tab]]Use the menu or click the ![[_media/Gramps-config.png]] button in the [Toolbar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Toolbar).

The tab has the following option available:

-  (checked by default)

-  (checked by default)

-  (checked by default)

-  (unchecked by default)

- - **Standard**(default)
  - Compact
  - Expanded

- - Vertical (↑)
  - Vertical (↓)
  - **Horizontal (→)**(default)
  - Horizontal (←)

- slider range 2 to 9 generations. Set to `5`(by default)

![[_media/ChartsCategory-pedigreeview2-horizontal-left-standard-5gen-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pedigree view 2 - Tree direction:horizontal to left]] ![[_media/ChartsCategory-pedigreeview2-vertical-up-standard-5gen-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pedigree view 3 - Tree direction:vertical and up]] ![[_media/ChartsCategory-pedigreeview2-vertical-down-standard-5gen-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pedigree view 4 - Tree direction:vertical and down]]

{{-}}

### Fan Chart View

![[_media/ChartsCategory-fanchartview-fullcircle-9gen-default-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fan Chart View - full circle]]

The view shows the active persons ancestry as a pie chart. Clicking on a name in the chart will double the section of the pie allocated to that person. A second click brings the chart back to the original form. Right click brings up a context menu like in the pedigree view, allowing to navigate to other people.

This view enables to see large ancestries in a more compact manner, and to see very quickly which parts of an ancestry need further research.

You can rotate the view by click and drag outside the fan chart. You can move the view by click and drag inside the inner (white) region.

1.  The view can be a circle, a halfcircle or a quadrant of a circle. The latter are always attached to the bottom or side of the view
2.  Children of the center person are shown within the ring at the center
3.  Drag and drop people to the center to change the active person
4.  Color options
    1.  Colors of the boxes based on the age of the people
    2.  Colors of the boxes depending on the time period the person lived in
    3.  White, classic, gender based, and user defined colors
5.  Filtering: use the person filter in the sidebar to quickly obtain insight in the people shown. For example: which people have birth events, who has the attribute *blue eyes*, ... . Filtered results have bold font, the ones that don’t satisfy the filter are shown transparent
6.  Show up to 11 generations in the view.
7.  Print the view from the toolbar. The view as you see it (after rotating, expanding, changing color) can via the print button be printed or saved as svg (to edit further in Inkscape and view in eg Firefox), pdf or ps.
8.  The font used can be selected and automatically adjust to fit within the boxes. On a darker background, the font is white, and vice versa.

{{-}}

#### Configure the active view

![[_media/ChartsCategory-FanChartView-ConfigureCharts-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Charts Category - Fan Chart View - Configure the active view - dialog - showing Defaults Defaults on Layout tab]]Use the menu or click the ![[_media/Gramps-config.png]] button in the [Toolbar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Toolbar).

- *9* (default)

- *Sans* (default)

- - Gender colours
  - **Generation based gradient** (default)
  - Age (0-100) based gradient
  - Single main (filter) colour
  - Time period based gradient
  - White
  - Colour scheme classic report
  - Colour scheme classic view

- *\#ef2929* (default)

- *\#3d37e9* (default)

- - **Full Circle** (default)
  - Half Circle
  - Quadrant

- 

- 

- 

- 

#### See also

{{-}}

### Descendant Fan View

![[_media/ChartsCategory-DescendantFanChart-fullcircle-9gen-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Descendant Fan Chart View - full circle]]

View showing the active person's direct descendants as a fan chart.

- [Descendant Fan View](https://gramps-project.org/blog/2012/09/descendant-fanchart/)

{{-}}

#### Configure the active view

![[_media/ChartsCategory-DescendantFanChartView-ConfigureCharts-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Charts Category - Descendant Fan Chart View - Configure the active view - dialog - showing Defaults on Layout tab]]Use the menu or click the ![[_media/Gramps-config.png]] button in the [Toolbar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Toolbar).

- *9* (default)

- *Sans* (default)

- - Gender colours
  - **Generation based gradient** (default)
  - Age (0-100) based gradient
  - Single main (filter) colour
  - Time period based gradient
  - White
  - Colour scheme classic report
  - Colour scheme classic view

- *\#ef2929* (default)

- *\#3d37e9* (default)

- - **Full Circle** (default)
  - Half Circle
  - Quadrant

- - Homogeneous children distribution
  - **Size proportional to number of descendants** (default)

- 

- 

- 

#### See also

{{-}}

### 2-Way Fan View

![[_media/ChartsCategory-2-WayFan-fullcircle-ances4gen-descen4gen-example-defaults-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} 2-Way Fan Chart View - 4 Generations of Ancestors (Top) / 4 Generations of Descendants (bottom)]]

Chart consisting of both ascendants and descendants.

{{-}}

#### Configure the active view

![[_media/ChartsCategory-2-WayFanChartView-ConfigureCharts-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Charts Category - 2-Way Fan Chart View - Configure the active view - dialog - showing Defaults on Layout tab]]Use the menu or click the ![[_media/Gramps-config.png]] button in the [Toolbar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Toolbar).

- *4* (default)

- *4* (default)

- *Sans* (default)

- - Gender colours
  - **Generation based gradient** (default)
  - Age (0-100) based gradient
  - Single main (filter) colour
  - Time period based gradient
  - White
  - Colour scheme classic report
  - Colour scheme classic view

- 

- *\#ef2929* (default)

- *\#3d37e9* (default)

- *\#888a85* (default)

- - Homogeneous children distribution
  - **Size proportional to number of descendants** (default)

- 

- 

- 

#### See also

- [Feature: Gep-030 FanChart2Way](https://github.com/gramps-project/gramps/pull/222)

{{-}}

### Charts Category Bottombar tabs

The by default displays no Gramplets in the [Bottombar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tab. You may add them as required. {{-}}

### Charts Category Sidebar tabs

The shows the following [Sidebar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### Filter

Only the and have a Filter shown by default.

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) Gramplet {{-}}

## Events Category

The shows the that lists the all the events recorded in the Family Tree. Events can be shared between multiple people and multiple families.

See also:

- [Editing information about events](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Editing_information_about_events)

{{-}}

### Events View

![[_media/EventsCategory-EventsListView-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Events Category - Events (List) View - example]]

From the list the following columns are available for display: , , , , , and .

The default view displays the , , , and of the event. The dialog can be used to add, remove and rearrange the displayed columns. This can be accessed from the button on the toolbar.

The list of Events can be sorted in the usual manner, by clicking on the column heading. Clicking once sorts in ascending order, clicking again sorts in descending order.

Additional options are available by selecting an event from the list and using the context/pop-up menu shown by right-clicking:

- 

- 

- 

- 

- 

- 

- - 

  - 

#### ⚙ Configuration Options

As with most list style Views, you can control the layout (which columns will be displayed and their order of display) by clicking the ![[_media/Gramps-config.png]] button, choosing from the View menu, or pressing the *Configure active view* [keyboard keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings).

The displayable columns include:

- 

- 

- 

- 

- 

- 

- 

- 

- 

Drag and drop columns to change their order in the Event list. The view will not be changed unless the button is clicked. Clicking without first clicking will abandon the changes.

{{-}}

### Events Category Bottombar tabs

The shows the following [Bottombar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### Gallery

See [Gallery](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Gallery) Gramplet {{-}}

#### Citations

See [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) Gramplet {{-}}

#### Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) Gramplet {{-}}

#### Attributes

See [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) Gramplet {{-}}

#### References

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) Gramplet {{-}}

### Events Category Sidebar tabs

The shows the following [Sidebar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### Filter

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) Gramplet {{-}}

## Places Category

The holds two views that show [places](wiki:Gramps_Glossary#place): either as grouped (hierarchically in a tree) or ungrouped (in a simple flat list). Each view lists the geographical places in which the events of the database took place. These could be places of birth, death, and marriages of people, as well as their home, employment, education addresses, or any other conceivable reference to the geographical location.

![[_media/PlacesCategory-Toolbar-partial-overview-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Configure Relationships Category - Content (tab)]] The Places View lists the places' , , , , , , , , , and . All of these columns can be used for sorting by clicking on a column heading.

#### ⚙ Configuration Options

![[_media/Menubar-View-overview-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} View menu for the People category View]] You can control the layout (which columns will be displayed and their order of display) by clicking the ![[_media/Gramps-config.png]] button, choosing from the View menu, or pressing the *Configure active view* [keyboard keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings). {{-}} ![[_media/ConfigurePersonView-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Configure Person Category View]]The dialog may be used to add, remove and rearrange the displayed columns. Changes will only be enacted when the button is clicked.

Once the View columns are shown, clicking once on the column header sorts in ascending order, clicking again sorts in descending order.

These Configuration options and the current [filters](wiki:Gramps_6.0_Wiki_Manual_-_Filters) also constrain the data exported via the {{-}}

### Places List View

![[_media/PlacesCategory-PlaceView-list-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Places Category - Place (List) View - example]]

The Place List View shows all the places in one long list.

Additional options are available by selecting a place from the list and using the context/pop-up menu shown by right-clicking:

- 

- 

- 

- 

- 

- 

- 

- 

{{-}}

### Places Tree View

![[_media/PlacesCategory-PlaceTreeView-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Places Tree View - example]]

The Place Tree View groups the places in a hierarchy: country, county, ... etc

You can expand the listing using the arrows.

All the nodes of the tree view mode can be simultaneously collapsed or expanded from the context/pop-up menu shown by selecting a place and right-clicking:

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

{{-}}

### Map Service

![[_media/PlacesCategory-AttemptToSeeSelectedLocation-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Places Category - "Attempt to see selected locations with a Map Service (OpenstreetMap, Google Maps, ..." button - example]]

If a place has been highlighted, you may display the place in a web browser by selecting the button.

Your default web browser should open, attempting to use either the recorded coordinates (longitude and latitude) or the place name to display the location using the Maps provider web site. Different map services might have different requirements for the location description.

{{-}} ![[_media/PlacesCategory-MapServices-list-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Places Category - &quot;Select a Map Service&quot; button - showing list of options]]

From the drop down list you can choose the map service you want to use from the following three options:

- **OpenStreetMap**(default) - Uses longitude and latitude coordinates if present, otherwise uses city and country, or uses description of the place.
- *EniroMaps* - Valid for places within Sweden and Denmark, only if longitude and latitude are available, otherwise uses city and country, or uses description of the place.
- *GoogleMaps* - Uses longitude and latitude coordinates if present, otherwise uses city and country, or uses description of the place.

{{-}} See also:

- [Map Services - Google Earth](wiki:Addon:MapService-GoogleEarth) - addon allows you to use Google Earth.

### Places Category Bottombar tabs

The shows the following [Bottombar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### Details

See [Details](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Details) Gramplet {{-}}

#### Location

See [Locations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Locations) Gramplet {{-}}

#### Gallery

See [Gallery](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Gallery) Gramplet {{-}}

#### Events

See [Events](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Events) Gramplet {{-}}

#### Citations

See [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) Gramplet {{-}}

#### Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) Gramplet {{-}}

#### References

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) Gramplet {{-}}

### Places Category Sidebar tabs

The shows the following [Sidebar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### Filter

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) Gramplet {{-}}

## Geography Category

![[_media/GeographyCategory-GeoPlaces-view-AllKnownPlaces-openstreemap-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "All known Places" GeoPlaces View - Geography Category - example using Openstreetmap - sidebar and bottombar hidden]]

The shows place event data visually on a map. It contains many Geographic Views, which allows you to see the people and their events placed on a map via an internet map provider (OpenStreetMap, Google maps ...).

The following Geographic Views are available:

- Show all places in your family tree
- Show all places connected to the active person
- Show all places connected to the active family
- Show all places connected to all events
- Show all places connected to a filtered selection of events
- Show if two people have been able to meet
- Show if two families have been able to meet
- Show all displacements or moves for one person and their descendants

These views are accessible via the buttons on the toolbar. To filter on places or events, activate the filter sidebar via the menu

To have these Geographic views work correctly, you need:

- To have events related to places.
- These places must have coordinates : latitude and longitude.
- If one place has no coordinates, it will never appear on the map.
- If you have an active internet connection, for all moves on the map, all zoom ... all tile maps are saved.
  - When you are without an internet connection, all tile maps are cached from the previous session and can be used.
  - So, the map can be used without an internet connection and all already visited places can be shown again.
  - The only thing to do is for each place or area you want to use without an internet connection is to select them, zoom into these places. You'll be able to use them again without connection.

#### The different views

##### All known places

![[_media/GeographyCategory-GeoPlaces-view-AllKnownPlaces-openstreemap-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "All known Places" GeoPlaces View - Geography Category - example using Openstreetmap - sidebar and bottombar hidden]]

This view show all places with coordinates in the database.

From Gramps 4.2.2, for performances reason, by default, the view show only the place related to the places history or the filtered places. If you really want to see all places, you need to select the popup menu from the context menu [right button](wiki:Gramps_6.0_Wiki_Manual_-_Categories#button_3_.28_right_button_.29) and select "show all places". {{-}} ![[_media/GeographyCategory-AllKnownPlaces-Configure-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}  tab for the &quot;All known Places&quot; GeoPlaces View - Configure the active view]]

Configure the active view  
tab

The configuration menu tab for has the following options:

The view is the only Geography view that allows you to change the color used for the place type markers.

The colors are green for the following map renders:

- Openstreetmap
- Maps for free
- Opencyclemap and Public transport.

All other marker renders are red.

Click on the button on the toolbar.

Then click on the tab.

For each type of place, you can select and choose a color. The default color is green "#008b00"

See also:

- [Can we change the marker color?](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Can_we_change_the_marker.27s_color_.3F)

{{-}}

##### All known places for one Family

![[_media/GeographyCategory-AllKnownPlacesForOneFamily-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "All known places for one Family" GeoFamily View - Geography Category - example using Openstreetmap - sidebar and bottombar hidden]]

This view show all places visited by all family members during their lives.

This view is not connected to filters. It only depend on the active family and the history. {{-}}

Configure the active view  
tab

The configuration menu tab for this view has no additional options. {{-}}

##### Buluşabildiler mi?

![[_media/GeographyCategory-HaveTheyBeenAbleToMeet-default-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Have they been able to meet ?&quot; GeoClose View - Geography Category - example using Openstreetmap - sidebar and bottombar hidden]] Bu görüş, iki kişinin hayatları boyunca karşılaşıp karşılaşmadıklarını göstermek için kullanılır.

  
Bir karşılaştırma kişisi seçmelisiniz:

1.  Menü açılır penceresinden: Karşılaştırma kişisini seçin
2.  Araç çubuğundan

Karşılaştırma kişisi etkin olduğunda, onun yaşam yolunu göreceksiniz. Koordinatları bilinen her yer için boylamına bağlı olarak bir daire veya oval göreceksiniz. Daire yarıçapı, yapılandırma görünümünde ayarlanabilir. Bu değer, derecenin onda biri olarak tanımlanır. {{-}}

![[_media/GeographyCategory-HaveTheyBeenAbleToMeet-Configure-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "The selection parameters" tab for the "Have they been able to meet ?" GeoClose View - Configure the active view]]

Etkin görünümü yapılandırın  
sekmesi

Ek seçenekler için yapılandırma menüsü sekmesine bakın. {{-}}

##### All places related to Events

![[_media/GeographyCategory-AllPlacesRelatedToEvents-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "All places related to Events" GeoEvents View - Geography Category - example using Openstreetmap - sidebar and bottombar hidden]]

This view is used to show all places related to events. It can take some time to show when we have many events.

from Gramps 4.2.2, for performances reason, by default, the view show only the place related to the events history or the filtered events. If you really want to see all events, you need to select the popup menu from the context menu [right button](wiki:Gramps_6.0_Wiki_Manual_-_Categories#button_3_.28_right_button_.29) and select "show all events". {{-}}

Configure the active view  
tab

The configuration menu tab for this view has no additional options. {{-}}

##### Bir Kişi için bilinen tüm yerler

![[_media/GeographyCategory-AllKnownPlacesForOnePerson-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "All known places for one Person" GeoPerson View - Geography Category - example using Openstreetmap - sidebar and bottombar hidden]]

Bu görüntü, bir kişinin hayatı boyunca ziyaret ettiği tüm yerleri gösterir.

Bu görünüm süzgeçlere bağlı değil. Sadece etkin kişiye ve tarihe bağlıdır.

Canlandırma işlevini kullanmak istiyorsanız, farenin [sağ düğmesine](wiki:Gramps_6.0_Wiki_Manual_-_Categories/tr#düğme_3_(sağ_düğme)) tıklayın. Bir açılır menü gelecektir. Açılır menüden, o anki kişinin yaşam yolunu görmek için 'canlandır'ı seçebilirsiniz:

Etkin kişinin birkaç ilgili olayı varsa, bu işaretçiler arasında sanal bir hareket görebilirsiniz. Hareket, yıl veya mesafe ile ilgilidir ve kişi haritası tercihlerinde değiştirilebilir. İşaretçilere olan uzaklık derecenin onda biri değerinden büyükse, yıllar yerine mesafeye bağlı hareketler gösteririz. Bu durumda, bu iki işaret arasındaki adım sayısı değiştirilebilir. Adımlar arasında animasyon hızını değiştirebilirsiniz. Hareketler, ilk etkinlik yılından son etkinlik yılına kadar devam eder. {{-}}

![[_media/GeographyCategory-AllKnownPlacesForOnePerson-Configure-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "The animation parameters" tab for the "All known places for one Person" GeoPerson View - Configure the active view]]

Configure the active view  
tab

See the configuration menu tab for the following options you can change:

- A slider to set the (default: *100*)
- A slider to set the (default: *20*)
- A slider to set the (default: *5*)

{{-}}

###### Grafiksel bilgileri olan bir kişi için bilinen tüm yerler (KML dosyaları)

![[_media/gramps-person-kml.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} 3 KML dosyası olan bir kişi]]

KML dosyaları çeşitli kayıtlar için Galeri sekmesinde Ortam nesneleri olarak eklenirse, bu Coğrafya görünümü her KML dosyası için bir yol veya bir yüzey gösterecektir.

Aşağıdaki örnekte, bu Kişi tarafından referans verilen farklı Galeri sekmelerinden oluşturulan 3 katmanlı KML dosyalarını görüyorsunuz:

- a farm limits outline KML in the Birth Event.
- a path KML used to go to school in the Education Event.
- a parish (or municipality) limits outline KLM in the Place Gallery tab for the Baptism Event.

In the case of the Farm limits outline, the KLM was added to the Gallery tab of the Birth Event (rather than being applied to that of the re-useable ['Farm' type Place](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Place_Editor_dialog)) because acreage was bought and sold over the years. This outline represented the Farm size at the date of birth.

See [Adding places from KML files](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Adding_places_from_KML_files)

{{-}}

##### Every residence or move for a person and any descendants

![[_media/GeographyCategory-EveryResidenceOrMoveForAPersonAndAnyDescendants-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Every residence or move for a person and any descendants" GeoMoves View - Geography Category - example using Openstreetmap - sidebar and bottombar hidden]]

This view is used to show all descendant's life ways.

They are displayed by generation. You can change the delay between the generation display in the view configuration.

This view is not connected to filters. It only depend on the active person and the history. {{-}} ![[_media/GeographyCategory-EveryResidenceOrMoveForAPersonAndAnyDescendants-Configure-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;The parameters for moves&quot; tab for the &quot;Every residence or move for a person and any descendants&quot; GeoMoves View - Configure the active view]]

Configure the active view  
tab

See the configuration menu tab for the following options you can change:

- A slider to set to show. (default: *20*)
- A slider to set the (default: *500*)

{{-}}

##### Have these two families been able to meet ?

![[_media/GeographyCategory-HaveTheseTwoFamiliesBeenAbleToMeet-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Have these two families been able to meet ?" GeoFamClose View - Geography Category - example using Openstreetmap - sidebar and bottombar hidden]]

This view is used to show if two families were able to meet during their life.

You must select one reference family :

- From the menu popup : Choose the reference family
- From the toolbar

When the reference family is active, you'll see all its member's life way. For each known place with coordinates, you'll see a circle or an oval depending on the longitude.

The circle radius can be tuned in the configuration view. This value is defined in tenth of degree. {{-}} ![[_media/GeographyCategory-HaveTheseTwoFamiliesBeenAbleToMeet-Configure-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;The selection parameters&quot; tab for the &quot;Have these two families been able to meet ?&quot; GeoFamClose View - Configure the active view]]

Configure the active view  
tab

See the configuration menu tab for additional options. {{-}}

### Usage

#### The configuration

Via the toolbar button (or via the menu )

##### All views

![[_media/ConfigureGeography-the-map-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Configure Geography - "The map" tab]]

tab contains options common to all Geography views:

- (default is *`$HOME/.gramps/maps`*). If required you can change the directory where map tile files are stored on your computer. .

  - button

- A slider for (default: *12*). The zoom level for when we center the map or when we select one marker. Every time the Geographic View redraws the map, this zoomlevel will be used.

- A slider for (default: *5000*). Reducing this number for faster map drawing but with less life ways.

-  - checkbox selected by default.

{{-}}

##### Specific views

See the description of the view.

#### How to zoom and move around the map ?

##### Zoom in and Zoom out the map

To zoom, you can use :

- The +/- buttons on the top left of the map
- The scroll mouse.
- The "+" or "-" key on the keypad (default).

You can replace the numeric keypad by the alpha numeric keyboard in the configuration view.

##### Move around the map

To move around the map, you can :

- Click on the map, then drag it.
- Use the arrows.

#### The mouse actions on the map

The right button below is for one right handed person. This will be the left button for one left handed person.

##### button 1 ( left button )

You have two usages for the button 1 :

1.  The marker selection.
2.  Valid the region selection

##### button 2 ( middle button )

The only usage for this button is to select an area on the map.

1.  when pressed : start the region selection
2.  when released, end the region selection.

You must use the button 1 to validate the selected region when finished.

##### düğme 3 (sağ düğme)

Bu düğme için yalnızca bir kullanım.

- [Bağlam menüsü](https://tr.wikipedia.org/wiki/Ba%C4%9Flam_men%C3%BCs%C3%BC) açılır penceresini göster.

##### The mouse over a marker

When the mouse is placed over one marker, we display the place name in the status bar.

#### The menu popup

From this context menu, you have the following functions available for views :

- hide or show the crosshair
- lock or unlock the zoom
- change the default map (provider)
- add a place and link a place at the mouse position
- add a place from kml file
- center the map at the mouse position.
- center the map depending on a place from sub menu.
- remove all tiles already uploaded for the current provider
- "show all places" or "show all events" for the "all known places" view or "all places related to events" view.

#### Click on a marker

We have two cases :

1.  events : For each event, we can edit this event or center the map on this place.
2.  places : For each place, we can edit this place or center the map on this place.

When centering the map, the zoom used is defined in the geography preferences.

We may have several markers in the click area depending on the zoom. In this case, We show for each marker all related events and/or places. We obtain a mix between the two cases described above.

#### Adding or Linking to a place

For this, click on the [right button](wiki:Gramps_6.0_Wiki_Manual_-_Categories#button_3_.28_right_button_.29) of the mouse, you'll get a popup menu. In this menu, you can select or

When you add a place or try to link a place to the position of the mouse, you'll get a place selection in a region. You'll see on the map a circle in which you may choose markers place names. You can adjust the circle size with the cursor. Depending on the diameter of this circle, a list is created. If the place has already some filled fields, you'll see these values in a green color row. If you agree, you double click on this row. if you don't agree, you can choose another row.

Another way to set latitude and longitude :

- Download the [Place completion tool](wiki:Place_completion_tool) via the [Addons manager](wiki:6.0_Addons#Installing_Addons_in_Gramps). If you download the data of your country, this tool can add latitude-longitude to all your places.

#### Adding places from KML files

For this, click on the [right button](wiki:Gramps_6.0_Wiki_Manual_-_Categories#button_3_.28_right_button_.29) of the mouse, you'll get a context popup menu.

In this menu, you can select

You will get the file chooser dialog. Select the file you want to add.

If you have several places in the same KML file, you will get one place editor for each place. Be careful.

#### How to change the map provider ?

Several map providers are available in Gramps.

Click on the [right button](wiki:Gramps_6.0_Wiki_Manual_-_Categories#button_3_.28_right_button_.29) of the mouse, you'll get a popup menu.

In the bottom of this menu, you can select a new provider.

The following providers are available :

- **OpenStreetMap** (default) : The advantage of [OpenStreetMap](http://www.openstreetmap.org/) is that it is a free project, so you can update the maps yourself with missing information via their website.
- Maps For Free
- OpenCycleMap
- Public Transport
- Google street
- Google sat
- Google hybrid
- Virtualearth street
- Virtualearth sat
- Virtualearth hybrid

#### Can we change the marker's color ?

Only the view supports changing the place type markers colors all the other views are hard coded in Gramps. {{-}}

#### How to get/remove the crosshair ?

It can be useful to have the crosshair visible to see the center of the map. This functionality is available with the [right button](wiki:Gramps_6.0_Wiki_Manual_-_Categories#button_3_.28_right_button_.29) of the mouse. you'll get a popup menu. Select Add or Remove cross hair. This is useful to add or link places to the correct latitude-longitude coordinates

#### How to lock/unlock the map ?

When we change the map ( person to family, ... ), the zoom is recalculated. It can be useful in some case to keep the same zoom and position when we change the map provider. For this, click on the [right button](wiki:Gramps_6.0_Wiki_Manual_-_Categories#button_3_.28_right_button_.29) of the mouse, you'll get a popup menu. In this menu, you can select lock or unlock zoom and position.

### Prerequisites to see the geography view

For Gramps 5.x, you need to install [osmgpsmap](http://nzjrs.github.io/osm-gps-map/) version 1.0 and above and the associated gir package.

For example on ubuntu, you must have: `gir1.2-osmgpsmap-1.0` and `libosmgpsmap-1.0-0`

### Possible problems

- No view : do you have `osmgpsmap` installed ? (*`gramps -v`* from the command line may help you)
- No tiles : do you have an internet connection active ?
- No tiles for one provider : if other providers are OK, file a bug
- Missing tiles : you have no internet connection and it's the first time you try to show the current place.
- Missing tiles : this can be the same as no tiles for one provider if they modify the access rules (i.e user-agent)
- Other : [Report a bug](wiki:Using_the_bug_tracker)

### Geography Category Bottombar tabs

The by default displays no Gramplets in the [Bottombar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tab. You may add them as required.

{{-}}

### Geography Category Sidebar tabs

The shows the following [Sidebar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs.

{{-}}

#### Filter

The filter type may change depending on the view selected.

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) Gramplet {{-}}

## Sources Category

The offers two view modes ( View and View (default)) that list the sources of certain information stored in the family tree. The record selection, column configuration and Gramplet selections are independent for each view mode.

Sources can include various documents: birth, death, and marriage certificates; books; films; journals; private diaries - nearly anything that can be described as genealogical evidence. Gramps gives you the option to provide citations of sources for each (Event, Person, Place, Media, Note, et cetera) object you create.

By default, the Sources View mode lists the , , and of the source, as well as any information that may be associated with it. The list of Sources can be re-sorted by clicking on a different column heading. Clicking the header the first time sorts the rows in ascending order based on that column. Clicking again reverses to descending order.

The tab of the Configure Sources dialog can be used to add, remove and rearrange the displayed columns. Click the ![[_media/gramps-config.png]] toolbar button or select Configure… from the menu to open the dialog.

You can select the toolbar button to create a new source or button to edit the sources selected in the list. Either action will invoke the dialog.

- See [Editing information about sources](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Editing_information_about_sources)

{{-}}

### Citation Tree View

![[_media/SourcesCategory-CitationTree-View-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sources Category - Citation Tree - View]]

The View mode list will also show all the sources. In addition, it allows the user to see the [Citations](#Citations_Category) associated with each source by clicking on the [disclosure triangle](https://en.wikipedia.org/wiki/Disclosure_widget) node expand or collapse disclosure triangular widget.

All the nodes of the tree view mode can be simultaneously collapsed or expanded from the context/pop-up menu shown by right-clicking:

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

{{-}}

### Sources List View

![[_media/SourcesCategory-Sources-ListView-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sources Category - (List) View]]

The default, mode only shows the Sources as a list and displays the , , and of the source, as well as any information that may be associated with it. The list of Sources can be re-sorted by clicking on a different column heading. Clicking the header the first time sorts the rows in ascending order based on that column. Clicking again reverses to descending order.

Additional options are available by selecting a source from the list and using the context/pop-up menu shown by right-clicking:

- 

- 

- 

- 

- 

- 

- 

{{-}}

### Sources Category Bottombar tabs

The shows the following [Bottombar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### Gallery

See [Gallery](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Gallery) Gramplet {{-}}

#### Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) Gramplet {{-}}

#### References

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) Gramplet {{-}}

### Sources Category Sidebar tabs

The shows the following [Sidebar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### Filter

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) Gramplet {{-}}

## Alıntılar Bölümü

, soy ağacında saklanan belirli bilgiler için alıntıları gösteren Alıntı listesi Görünümünü açar.

Alıntılar, bir kaynağın hangi bölümlerinin veri tabanındaki bilgilerle ilgili olduğunu belirtir. Örneğin, Kaynak bir kitap olabilir ve alıntı kitaptaki belirli bir sayfa olabilir. Gramps, kaydettiğiniz her olay (doğumlar, ölümler, evlilikler vb.) için size bir alıntı yapma seçeneği sunar.

{{-}}

### Alıntılar Liste Görünümü

![[_media/CitationsCategory-CitationView-List-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Alıntılar Bölümü - Alıntılar (Liste) Görünümü - örnek]]

Alıntılar Liste Görünümü, alıntının , ve inin yanı sıra kanıtlara olan i gösterir.

Alıntılar listesi, bir sütun başlığına tıklanarak sıralanabilir.

Bir kez tıklama artan düzende, tekrar tıklama azalan düzende sıralar. iletişim kutusu, görüntülenen sütunları eklemek, kaldırmak ve yeniden düzenlemek için kullanılabilir.

Listeden bir alıntı seçip sağ tıklayarak gösterilen bağlam/açılır menüyü kullanarak ek seçenekler mevcuttur:

- 

- 

- 

- 

- 

- 

- 

{{-}}

### Citations Category Bottombar tabs

The shows the following [Bottombar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### Gallery

See [Gallery](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Gallery) Gramplet {{-}}

#### Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) Gramplet {{-}}

#### References

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) Gramplet {{-}}

### Citations Category Sidebar tabs

The shows the following [Sidebar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### Filter

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) Gramplet {{-}}

## Repositories Category

The shows the Repository List View. A repository can be thought of as a collection of sources. Each source in the family tree may be a reference to a repository (such as a library) in which it belongs.

{{-}}

### Repository List View

![[_media/RepositoriesCategory-Repositories-ListView-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Repositories (list) view - example]]

This view shows a list of all recorded repositories.

Additional options are available by selecting a repository from the list and using the context/pop-up menu shown by right-clicking:

- 

- 

- 

- 

- 

- 

- 

{{-}}

### Repository Category Bottombar tabs

The shows the following [Bottombar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### Details

See [Details](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Details) Gramplet {{-}}

#### Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) Gramplet {{-}}

#### References

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) Gramplet {{-}}

### Repository Category Sidebar tabs

The shows the following [Sidebar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### Filter

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) Gramplet {{-}}

## Media Category

The shows the Media List View, which list the Media Objects stored in the family tree.

Media Objects are technically any files that relate somehow to the stored genealogical data.

Most frequently, these are images, audio files, animation files, etc. {{-}}

### Media List View

![[_media/MediaCategory-Media-ListView-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Media Category - Media (List) View - example]]

The Media List View shows the following columns for the list , , , and of the Media Object.

The dialog may be used to rearrange the displayed columns, which obey usual sorting rules.

Selecting a media item from the list and using the context menu (right-clicking) offers the following options

- 

- 

- \- show the media item using an external program.

- \- which opens to the folder containing the media item.

- 

- 

- 

- 

- - 

{{-}}

### Media Category Bottombar tabs

The shows the following [Bottombar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### Preview

In the "Preview" tab you can double click on the media/photo to open it in the default picture viewer.

See [Media Preview](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Media_Preview) Gramplet {{-}}

#### Citations

See [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) Gramplet {{-}}

#### Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) Gramplet {{-}}

#### Attributes

See [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) Gramplet {{-}}

#### Image Metadata

See [Image Metadata](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Image_Metadata) Gramplet {{-}}

#### References

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) Gramplet {{-}}

### Media Category Sidebar tabs

The shows the following [Sidebar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### Filter

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) Gramplet {{-}}

## Notes Category

The View shows a List mode, which inventories the text notes (either pure text or pre-formatted) that can be referenced by the other objects.

See also:

- Using the [Note Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Editing_information_about_notes) to make new annotations or editing information about existing notes

{{-}}

### Notes List View

![[_media/NotesCategory-Notes-ListView-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Notes Category - Notes (List) view]]

The Notes List View shows a list of text notes.

The functionality of the notes View is similar to the other views. The view lists all stored in the Family Tree.

Using the menu you open the and you can change the displayed columns. The possibilities are , , , , and .

The can be ([amongst others](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#note_type)): *Event Note*, *Address Note*, *Source text*, *Place Note*. (In version 6.0, the built-in list includes: *Citation*, *General*, *HTML code*, *Link*, *Report*, *Research*, *Source text*, *To Do*, *Transcript*, *Unknown*)

Selecting a Note item from the list and using the context menu (right-clicking) offers the following options

- 

- 

- 

- 

- 

- 

- - 

  - 

Double-clicking on a Note item in the list will bring up the [Note editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#New_Note_editor_dialog) window where you can edit the Note. You can change fonts, font color and background color. A spellchecker is available for *English* and your local language. {{-}}

### Notes Category Bottombar tabs

The shows the following [Bottombar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### References

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) Gramplet {{-}}

### Notes Category Sidebar tabs

The shows the following [Sidebar](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) tabs. {{-}}

#### Süzgeç

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) Gramplet

{{-}}

[Category:Tr:Documentation](wiki:Category:Tr:Documentation)
