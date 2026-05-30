---
title: Gramps 6.0 Wiki Manual - Gramplets/tr
categories:
- Stub
- Tr:Documentation
managed: false
source: wiki-scrape
wiki_revid: 126613
wiki_fetched_at: '2026-05-30T20:56:47Z'
lang: tr
---

{{#vardefine:chapter\|12}} {{#vardefine:figure\|0}} This page details the functionality of the Gramplets that come with Gramps.

# Gramplet nedir?

<span id="definition"> ![[_media/DashboardCategory-DashboardView-default-gramplets-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dashboard Category (Default View)]]

A [Gramplet](wiki:Gramps_Glossary#gramplet) is an expansion to the core Gramps program that **hopefully** works seamlessly as a built-in feature. Gramplets provide a supplemental perspective of the Tree data which either: changes dynamically during the navigation of the Gramps Tree, or; provides interactivity to your genealogical data.

Gramplets are the plug-ins (also called [widgets](http://wikipedia.org/wiki/Widget_engine), plugins, addons, auxiliary components) that become embedded as part of Gramps and can be found in the **Dashboard Category** ... or the **Sidebars** and **Bottombars** in other Navigator Categories. They provide all kinds of functionality that can be useful for the researcher.</span>

## Aren't all Plugins also Gramplets?

What is the difference between Gramplets, reports, quick views, and tools?

All of these are **plugin** types. But Gramplets are subtype of plugins with more emphasis on the user interface. Gramplets add a **capability** or a **different perspective** to the View. They can be used to improve the workflow of a View.

The other plugins tend to interrupt the normal workflow to do another task. They also tend to be used more intermittently. A plugin might generate a static (even when hot-linked) snapshot of the data, be a way of doing mass change, or provide an alternative import/export/output system.

Some common [Plugin types](wiki:Gramps_6.0_Wiki_Manual_-_Plugin_Manager#Plugin_types) are:

- Reports - provide a static output format of your data, typically for presentation
- [Quick Views](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Quick_Views) - provides a typically short, interactive listing derived from your data
- Tools - provide a method of processing your data
- Gramplets - provide a dynamic view and interface to your data.

A deeper understanding of the different types of plugins can be gained by sorting the [Addon List](wiki:6.0_Addons#Addon_List) by **Type** and exploring the contrasting **Descriptions**.

Some of the more static types of plugins can be extended to work dynamically as a Gramplet.

Several plugins have evolved into multiple types. Some plugins are shells which layer extra capabilities around other plugins. The **Quick View** Gramplet is not a [type of Quick View plugin](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Quick_Views). Instead, it is a dockable shell that shows a **Quick View** plugin and pushes the plugin to refresh as the context changes.

## Starting with Gramplets

When you first start the [Dashboard Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Dashboard_Category) you will see two default Gramplets; the **** Gramplet and the ****.

Since Gramps 4.2 extended some Dashboard features to other Navigator Categories, we have **common** and **specific** Gramplets.

- Common Gramplets are applicable to any View ... and the data viewpoint is with respect to the Context of the Active Person and/or the Home Person. They can be docked on any Navigator Category View without making the View unambiguous.
- Specific Gramplets need the context of particular Views to give context to their perspective of the data. The list of Add Gramplets menu will differ according active Category view and Gramplets installed.

This list is leftover from an earlier revision of the wiki. It is unclear where the items fit in this discussion.

- Back references Gramplets - provide immediate visibility to data that tends be viewed occasionally and is buried in the interface... like the tab on object Editor.
- Filter Gramplet is like the previous filter sidebar
- Common models for Notes, Gallery, Sources, Citations, Events
- Children Gramplet on Person views (also charts category and relationships category), families view

## General Usage and Configuration

![[_media/WelcomeToGramps-Gramplet-docked-in-dashboard-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dashboard Welcome Gramplet]] The container controls for Gramplets are arranged a little differently in the Dashboard category View as opposed to the Sidebar and Bottombar. Being aware of how these Gramplet containers differ (and are similar) will let you focus on getting the high speed performance instead of wondering why it spun out of control.

Originally added in version 3, Gramplets in Dashboard category View are arranged in a configurable number of columns. The Sidebar and Bottombar [split panes](wiki:Split_Views) were selected from among later innovations proposed in [GEPS 19](wiki:GEPS_019:_Improved_Sidebar_and_Split_Views). They were built on the Filter Sidebar of the 3.3 version. The Filter was converted to a Gramplet'' and pre-docked in the Sidebar.

![[_media/Welcome-to-Gramps-Gramplet-detached-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detached Sidebar Welcome Gramplet]]The split panes provide limited screenspace for docking Gramplets in the other Navigator categories. But, unlike the many columns of the Dashboard View, each new split pane is a single column, filled with a single Gramplet. (The pane still supports holding multiple Gramplets, it just uses Tabs to display them one at a time.)

The split pane approach reduces the need for flipping between Category Views... and that lightens the demands on the database.

![[_media/DashboardCategory-gramplet-detached-and-docked-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detached Gramplet in the Dashboard View]] However, Gramplets can be undocked (detached, torn off) to float free from any of the three containers. When detached, an additional button in the lower left will open the Gramplet's page on this website. Clicking the  button in the upper right corner will re-docks a detached Gramplet. Clicking the similar  button of a docked Gramplet will remove it from the pane.

### The Dashboard Category View

In the [Dashboard](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Dashboard_Category), you can drag the  button (top left) of each Gramplet to reposition it in the Dashboard View area. You can click the  button to detach (or *‘undock’*) the Gramplet from Dashboard View and place it in its own window. The window will stay open regardless of page (relationships, charts, etc). Closing the detached view will put it back onto the Dashboard view. If you quit Gramps with a open Gramplet, when you start gramps again, it will open automatically.

When one or more Gramplets are undocked from the Dashboard View, they remain visible as you change to a different View (such as the People or Charts View). In this way, you can use these Gramplets to supplement a particular View with additional details and functionality provided by the Gramplet.

You can add new Gramplets by right-clicking on an open space on Dashboard view. Click the  button above the Gramplet to remove it from the Dashboard.

#### ⚙ Configurable Options

![[_media/Menubar-View-overview-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} View menu]] You can also change the number of columns by changing a *Gramplets Layout* tab setting in *Configure Dashboard* window. To open the window, click the ![[_media/Gramps-config.png]] button, choose from the View menu, or press the *Configure active view* [keyboard keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings). ![[_media/Whats-next-gramplet-configure-dashboard-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet Configuration tabs]] Each Gramplet docked in the Dashboard will also have a Configuration tab added. (But the same Gramplet may not have any Configuration options or tab when docked in the Sidebar or Bottombar.) The Dashboard provides extra options for each Gramplet to allow it be renamed, set to a fixed vertical size, or be maximized vertically in its column. The Configuration tab for Gramplets in docked in the Dashboard reflect at least these minimum options.

Double-clicking the title of a Gramplet docked in the Dashboard Category allows you to change the display title.

### The split-screen Sidebar & Bottombar

![[_media/Bottombar-sidebar-drop-down-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet split-screens showing Gramplet Bar Menu with the unlabeled Down Arrowhead  pull-down menu button]] Each of these split screens is a container of stacked Gramplet tabs. Like Windows with a tabbed section, each can show only a single tab at a time. But tabs can be added, re-ordered, undocked or disabled in a similar fashion to the Dashboard. However, instead of a Contextual Menu, each split-pane has a *Down Arrowhead* pull-down menu button to show the same pop-up list of options.

To add a Gramplet to the stacked tabs, select it from the submenu.

<span id="undock gramplet">To undock a tab, grab the tab title and drag out of the split-pane. To re-dock, click the Close button or the 'X' button.</span>

To remove the Gramplet from the stack tabs, select it from the submenu. (Alternatively, the Close button will be accessible if the 'Show close button in gramplet tabs' checkbox in the [Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) tab of Preferences is selected.)

Curiously, the same Gramplets might be tabs in the different split-screen section of a View but be configured to show information differently. It is important to be aware that each Gramplet (whether stacked as a Tab or floating undocked) bogs down performance of Gramps. Use fewer Gramplets to make Gramps more responsive.

The lists of Gramplets that can be added to the stack of tabs in a split pane are filtered by those appropriate to that category.

#### ⚙ Configurable Options

![[_media/Menubar-View-overview-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} View menu]]

In addition, there are a number of Third party Gramplets that you can easily install and use. These include:

- Headline News Gramplet - current, breaking news from Gramps
- Data Entry Gramplet - edit active person's name, birth date and place, death date and place, and add people
- Python Gramplet - a Python shell
- FAQ Gramplet - frequently asked questions
- Note Gramplet - see and edit active person's primary Person Note

and many others. See [Third-party Addons](wiki:Third-party_Addons) for more details.

# Summary of built-in Gramplets

Summary of all default built-in Gramplets and the view categories in which each gramplet can be used.

Independently for each Category view mode container, the Gramplets can be added or removed using the following controls:

- In the Dashboard Category, via the right-click context menu.
- In all other Categories, via the drop-down Gramplet selection menus (*Down Arrowhead* button) on either the Bottombar or Sidebar.

*There are no Menu options to add a Gramplet. This is because it would be ambiguous whether the Gramplet was to be added to that view mode's sidebar or bottombar.* {{-}}

## Yerleşik Gramplet Listesi

Click a Category header (twice) to sort the list and show that category's menu of available built-in Gramplet choices. (The actual menu will also include installed [3rd-party addon](wiki:6.0_Addons#Addon_List) Gramplets.)

| Gramplet | ![[_media/22x22-gramps-gramplet.png]] Dashboard | ![[_media/22x22-gramps-person.png]] People | ![[_media/22x22-gramps-relation.png]] Relationships | ![[_media/22x22-gramps-family.png]] Families | ![[_media/22x22-gramps-pedigree.png]] Charts | ![[_media/22x22-gramps-event.png]] Events | ![[_media/22x22-gramps-place.png]] Places | ![[_media/22x22-gramps-geo.png]] Geography | ![[_media/22x22-gramps-source.png]] Sources | ![[_media/22x22-gramps-citation.png]] Citations | ![[_media/22x22-gramps-repository.png]] Repositories | ![[_media/22x22-gramps-media.png]] Media | ![[_media/22x22-gramps-notes.png]] Notes |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| id="0" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="1" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="2" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="3" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="4" \| |  | ✔ | ✔ | ✔ | ✔ | ✔ |  | ✔ | ✔ | ✔ |  | ✔ |  |
| id="5" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="6" \| |  | ✔ | ✔ | ✔ | ✔ |  |  | ✔ |  |  |  |  |  |
| id="7" \| |  | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |  | ✔ |  |
| id="8" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="9" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="10" \| |  | ✔ | ✔ |  | ✔ |  | ✔ | ✔ |  |  | ✔ |  |  |
| id="18a" \| |  |  |  |  |  |  | ✔ |  |  |  |  |  |  |
| id="18b" \| |  |  |  |  |  |  | ✔ |  |  |  |  |  |  |
| id="11" \| |  | ✔ | ✔ | ✔ | ✔ |  |  | ✔ |  |  |  |  |  |
| id="11a" \| |  | ✔ | ✔ | ✔ | ✔ |  |  | ✔ |  |  |  |  |  |
| id="12" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="13" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="14" \| |  |  | ✔ |  | ✔ |  |  |  |  |  |  |  |  |
| id="15" \| |  | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |  |
| id="16" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="17" \| |  |  |  |  |  |  |  |  |  |  |  | ✔ |  |
| id="21" \| |  |  |  |  |  |  |  |  |  |  |  | ✔ |  |
| id="19" \| |  | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |  |
| id="20" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="22" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="23" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="24" \| |  | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="25" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="26" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="27" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="28" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="29" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="30" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="31" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="32" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="35" \| | ⚠ | ⚠ | ⚠ |  | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ |
| id="33" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="34" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="xx" \| |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |

For more detailed information on using the installed Gramplets, see [Gramplets](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Gramplets). {{-}}

# Gramplets

This following sections describe each Gramplet and its basic functionality. {{-}}

## 2-Way Fan Chart

![[_media/2-WayFanChart-detached-gramplet-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} 2-Way Fan Gramplet]]

**See also:** {{-}}

## Tarihteki Yaşı

![[_media/AgeOnDate-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Age On Date Gramplet - detached example]]

The Gramplet allows you to enter a [Calendar date](https://en.wikipedia.org/wiki/Calendar_date) in the entry field. If you select the the Gramplet will compute the ages for everyone in your Family Tree living on that Date and will show the results in a separate Quick View report dialog. The date must be entered in a calendar format that Gramps accepts eg: YYYY-MM-DD .

- No configuration options are available for this gramplet.

{{-}} ![[_media/AgeOnDate-Gramplet-QuickView-example-result-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Age On Date Gramplet - Quick View - result example]]

From the resulting Quick View report dialog you can sort by the Person, Age or Status columns. Right clicking the row opens a context menu that allows you to *Copy all* rows to the clipboard; or to *See the person details* in the Person Editor, or *Make the person active*.

{{-}}

- You can also drag a date to from [Calendar Gramplet](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Calendar) to the Gramplets entry field to enter that date.
- See also the [Third-party Addon](wiki:Third-party_Addons) [Date Calculator Gramplet](wiki:Addon:DateCalculator) which allows you to do date math.

{{-}}

## Age Stats

![[_media/AgeStats-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Age Stats Gramplet - detached example]]

The Gramplet shows statistics in the form of three text graphs grouped in 5 years age span breakdowns (use the vertical scroll bar to see the other two graphs):

- **Lifespan Age Distribution** - for all people having valid birth and death dates.
- **Father - *Child Age Diff Distribution*** - shows the age difference between child and father where both individuals have valid birth dates.
- **Mother - *Child Age Diff Distribution*** - shows the age difference between child and mother where both individuals have valid birth dates.

Rolling over a chart row will display a hint with the count of offspring matching the row's range.

Double-clicking a row in any of the statistics graphs opens a Quick Report of the offspring categorized by that row. You can sort the Quick Report by the Name, Birth Date and Name Type columns.

Right-clicking the Quick View report row displays a context menu for copying the list, opening the Person Editor or activating the person.

#### ⚙ Configurable Options

![[_media/AgeStats-Gramplet-configuration-tab-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Age Stats Gramplet - from Charts Configuration tab defaults]] Adjustable graph scaling limits

- Maximum Age 1-150; (*110 default*)
- Maximum Age of mother at birth: 1-150; (*40 default*)
- Maximum Age of father at birth: 1-150; (*60 default*)
- Chart Width: 1-150; (*60 default*)

In the Dashboard View, the Gramplet may be detached by clicking the button.

### See also

- An upgrade has been developed for the 6.0 version of Gramps.See the [screen capture](wiki::File:AgeStats-Gramplet-detached-51.png#Summary)

{{-}}

## Ancestors

![[_media/Ancestors-Gramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ancestors Gramplet - detached example]]

Gramplet showing active person's ancestors. {{-}}

## Nitelikler

![[_media/Attributes-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Attributes Gramplet]]

Nitelikler Grafiği, mevcut ve etkin kişi için tüm nitelikleri gösterir. Niteliğin adına çift tıklayın ve bu niteliğe sahip tüm kişileri ve onun değerlerini gösteren bir Hızlı Görünüm çalıştıracaksınız. Sütun adına tıklayarak Hızlı Görünümü nitelik değerine göre sıralayabilirsiniz. {{-}} ![[_media/Atttribute-Gramplet-QuickView-example-result-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Attributes Gramplet - Quick View example result]]

Hızlı Görünüm'de, etkin kişiyi değiştirmek için girişi vurgulayın (daha sonra Nitelikler Gramplet'ini değiştirir) ve Kişi Düzenle iletişim penceresini getirmek için Hızlı Görünüm girişine çift tıklayın. {{-}}

### Kişi Nitelikleri

See [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) {{-}}

### Aile Nitelikleri

See [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) {{-}}

### Etkinlik Nitelikleri

See [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) {{-}}

### Kaynak Nitelikleri

See [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) {{-}}

### Alıntı Nitelikleri

See [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) {{-}}

### Ortam Nitelikleri

See [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) {{-}}

## Takvim

![[_media/CalendarGramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Calendar Gramplet - detached example]]

The **Calendar Gramplet** shows a monthly calendar.

Surrounding the label at the top left corner, the and buttons can be used to change the month.

Surrounding the label at the top right corner, the and buttons can be used to change the year.

Double-click a **day** to run the Quick View. The Quick View window shows up to 3 table sections, the events (if any exist) of: the exact date, other events on the same month/day in history, and events in that year.

You can also drag a day from the Calendar to the date fields (such as for the [Event Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#New_Event_dialog) or the [Age on Date Gramplet](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Age_on_Date)) to enter that date. Similarly, a calendar day may also be dragged to the [Clipboard](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Using_the_Clipboard) where it will be stored in a plain text format.

{{-}}

## Çocuklar

![[_media/ChildrenGramplet-PeopleCategoryView-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Children Gramplet - detached example]]

Gramplet showing the active persons children.

[How do I change the order of children?](wiki:Gramps_6.0_Wiki_Manual_-_FAQ#How_do_I_change_the_order_of_children.3F) Use:

- The Family Editor [Children](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Children) tab to change the order of children in the family.
- The third party addon [Birth Order Tool](wiki:Addon:BirthOrderTool) which allows bulk updates of the children order.

{{-}}

### Person Children

See [Children](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Children)

Also shows the childs spouse if present. {{-}}

### Family Children

See [Children](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Children) {{-}}

## Alıntılar

![[_media/Citation-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Citation Gramplet - detached example]]

Gramplet showing the active persons citations. {{-}}

### Person Citations

See [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) {{-}}

### Family Citations

See [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) {{-}}

### Event Citations

See [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) {{-}}

### Place Citations

See [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) {{-}}

### Media Citations

See [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) {{-}}

## Descendant Fan Chart

![[_media/DescendantFan-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Descendant Fan (chart) Gramplet - detached example]]

Gramplet showing active person's direct descendants as a fan chart.

**See also:** {{-}}

## Descendants

![[_media/Descendants-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Descendants Gramplet - detached example]]

The Descendants Gramplet shows the direct descendants of the active person.

The order of the spouses and children is that given in the Gramps editor. To change the order of spouses, click on *Order* on the Relationship view. To change the order of children, [drag and drop](http://en.wikipedia.org/wiki/Drag-and-drop) them in the correct order in the Family edit window.

This Gramplet is based on the [Descendant Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Descendant_Report), available from the Textual Reports.

The Descendants Gramplet will update when you change the active person, or change family trees. It does not update automatically for edits or additions because this report is time-consuming to run.

Minimizing a Gramplet will prevent it from updating.

Moving the mouse over a person will show a tooltip summary which includes the death date. {{-}}

## Ayrıntılar

![[_media/Details-Gramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Details Gramplet - detached example]]

Etkin kişinin ayrıntılarını gösteren Gramplet.

Seçilen kişinin düzenlenemeyen kısa bir özetini sağlar, örneğin:

- Kişinin *Adı*:
- *Ayrıca şöyle bilinir:*
- *Diğer adı:*
- *Baba:*
- *Anne:*
- *Doğum:*
- *Ölüm:*
- *Defin:*

<!-- -->

- *Görüntü*: Varsa, ana görüntü ayrıntıların sağında gösterilecektir, aksi takdirde bir çarpı görüntünün eksik olduğunu gösterecektir, görüntüyü harici bir görüntüleyicide açmak için görüntüye çift tıklayabilirsiniz. Birincil etkin görüntüyü değiştirmek için bkz: [Kişi Düzenleyicilerini Düzenle - Galeri sekmesi](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1/tr#Galeri)

Tek tek metin alanlarını vurgulayabilir ve kopyalayabilirsiniz. {{-}}

### Kişi Ayrıntıları

[Ayrıntılara](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Ayrıntılar) bakınız {{-}}

### Yer Ayrıntıları

[Ayrıntılara](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Ayrıntılar) bakınız {{-}}

### Depo Ayrıntıları

[Ayrıntılara](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Ayrıntılar) bakınız {{-}}

## Encloses

![[_media/Encloses-Gramplet-detached-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Encloses Gramplet - detached example]]

Gramplet showing the locations of a place it encloses over time. {{-}}

- See also [Enclosed By](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Enclosed_By) tab

### Encloses Place Locations

See [Enclosed By](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Enclosed_By) {{-}}

## Enclosed By

![[_media/EnclosedBy-Gramplet-detached-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Enclosed By Gramplet - detached example]]

Gramplet showing the locations enclosed by a place over time. {{-}}

- See also [Enclosed By](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Enclosed_By) tab

### Enclosed By Place Locations

See [Encloses](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Encloses) {{-}}

## Etkinlikler

![[_media/Events-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Events Gramplet - detached example]]

Etkin kişi için etkinlikleri gösteren Gramplet.

Düzenlemek istediğiniz etkinliğin satırına çift tıklayın. {{-}}

### Kişi Etkinlikleri

[Etkinliklere](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Etkinlikler) bakınız {{-}}

### Aile Etkinlikleri

[Etkinliklere](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Etkinlikler) bakınız {{-}}

## Etkinlik Koordinatları

![[_media/EventsCoordinates-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Events Coordinates Gramplet - detached example]]

Etkin kişi için etkinlik koordinatlarını gösteren Gramplet.

Etkinliği düzenlemek için bir satırı çift tıklayın. {{-}}

## Fan Chart

![[_media/FanChart-detached-gramplet-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fan Chart Gramplet]]

The Fan Chart Gramplet shows the direct ancestors of the active person in a circular format. It is similar to the Pedigree View, but shown around the center/active person, and further generations spiralling out.

Click on a parent in the chart and they will expand or contract above their child. Right-click on a person and you can:

- select that person to be the active person
- edit the person which allows through Person Editor add children to person's families
- select from among the person's relatives to be the active person
- add partners (families) to person
- copy name, birth and death of person into clipboard

Clicking in an open area (non-person) and dragging the mouse will allow you to rotate the chart about the center. You may also left-click and drag in the center to reposition the fan chart.

A black edge on the outer radius of the chart indicates more parents for that person. A black circle in the center indicates that the center person has children.

The Fan Chart Gramplet will update when you change the active person, or change family trees.

Minimizing a Gramplet will prevent it from updating.

**See also:** {{-}}

## FAQ

![[_media/FAQ-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} FAQ Gramplet - detached example]]

The (Frequently Asked Questions) shows a list of common questions, and links to their answers from the Gramps Wiki (requires an internet connection).

This gramplet shows a manually curated list of **Frequently Asked Questions** hyperlinked to answers in articles of the Gramps wiki. The list is collated from new user postings to the [Gramps User maillist](wiki:Contact#Mailing_lists) that must be answered repeatedly.

The idea is to make the answers to the most common question easier to find, the primary objective is to let new users start using Gramps more quickly.

### See Also

- Bug Report : Dashboard FAQ links are obsolete (resolved)
- Bug Report : how to add/update FAQs

{{-}}

## Süzgeç

Kategoriye özel bir süzgeç sağlayan Gramplet.

See also [Which filters in which Category?](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Which_filters_in_which_Category.3F) {{-}}

### Kişi Süzgeci

![[_media/FilterGramplet-Person-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Person - Filter Gramplet - detached - default]]

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) {{-}}

### Aile Süzgeci

![[_media/FilterGramplet-Family-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Family - Filter Gramplet - detached - default]]

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) {{-}}

### Etkinlik Süzgeci

![[_media/FilterGramplet-Event-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Event - Filter Gramplet - detached - default]]

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) {{-}}

### Yer Süzgeci

![[_media/FilterGramplet-Place-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Place - Filter Gramplet - detached - default]]

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) {{-}}

### Kaynak Süzgeci

![[_media/FilterGramplet-Source-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Source - Filter Gramplet - detached - default]]

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) {{-}}

### Alıntı Süzgeci

![[_media/FilterGramplet-Citation-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Citation - Filter Gramplet - detached - default]]

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) {{-}}

### Depo Süzgeci

![[_media/FilterGramplet-Repository-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Repository - Filter Gramplet - detached - default]]

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) {{-}}

### Ortam Süzgeci

![[_media/FilterGramplet-Media-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Media - Filter Gramplet - detached - default]]

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) {{-}}

### Not Süzgeci

![[_media/FilterGramplet-Notes-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Notes - Filter Gramplet - detached - default]]

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) {{-}}

## Galeri

![[_media/Gallery-Gramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gallery Gramplet - detached example]]

Ortam nesnelerini gösteren Gramplet. İlk görüntü, raporlarda ve Kişi Düzenle iletişim kutusunda kullanılan birincil etkin ortam nesnesidir.

See also [Gallery](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Gallery) tab for where you can change which image is the primary active media object for reports etc... {{-}}

### Kişi Galerisi

[Galeriye](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Galeri) bakınız {{-}}

### Aile Galerisi

[Galeriye](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Galeri) bakınız {{-}}

### Etkinlik Galerisi

[Galeriye](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Galeri) bakınız {{-}}

### Yer Galerisi

[Galeriye](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Galeri) bakınız {{-}}

### Kaynak Galerisi

[Galeriye](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Galeri) bakınız {{-}}

### Alıntı Galerisi

[Galeriye](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Galeri) bakınız {{-}}

## Given Name Cloud

![[_media/GivenNameCloud-Gramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Given Name Cloud Gramplet - detached example]]

Like the [Surname Cloud Gramplet](#Surname_Cloud), the Given Name Cloud Gramplet shows the top most popular given names in your family tree. The size of the name indicates how popular it is. Mouse over the name to see the exact count, and the percent of people in the family tree that have that name.

The Gramplet splits up given names into words (broken up by spaces). For example "Sarah Elizabeth" would appear under both "Sarah" and "Elizabeth".

Double-click on the given name to bring up a Quick View of all of the matching people. {{-}}

## Image Metadata

![[_media/ImageMetadata-Gramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Image Metadata Gramplet - example]]

The Image Metadata Gramplet offers an interface to look at [Image Exif Metadata](https://en.wikipedia.org/wiki/Exchangeable_image_file_format) from your images (\*.jpg, \*.png. \*.tiff, \*.exv, \*.nef, \*.psd, \*.pgf). {{-}} See also the third party:

- [Addon:Edit Image Exif Metadata](wiki:Addon:Edit_Image_Exif_Metadata)

### Prerequisites

Once you have installed gexiv2, see above for directions to download and install this addon...

Pyexiv2 can be used from the command line interface (cli) as well, and from within a python script:

1.  import the pyexiv2 library
      
    from pyexiv2 import ImageMetadata, ExifTag
2.  specify your image
      
    image = ImageMetadata("/home/user/image.jpg")
3.  read the image
      
    image.read()

Exif, IPTC, XMP metadata reference tags can be found [here](http://www.exiv2.org/metadata.html).

Example:

  
image\["Exif.Image.Artist"\] \# Artist

Smith and Johnson's Photography Studio

<!-- -->

  
image\["Exif.Image.DateTime"\] \# DateTime

1826 Apr 12 14:00:00

<!-- -->

  
image\["Exif.Image.DateTime"\] = datetime.datetime.now() \# Add DateTime

<!-- -->

  
image.write() \# write the Metadata

### Usage scenario

The preferred way to use this addon is:

1.  install pyexiv2
2.  Install this addon
3.  Restart Gramps
4.  Click Views from the Menu bar, and select Media Views
5.  Open the Side Bar
6.  Slide the available empty right view to about half the screen.
7.  Right click text to the Side Bar tab, and select Add a Gramplet
8.  Select Image Metadata Gramplet
9.  Select an image from the left hand MediaView

{{-}}

## Media Preview

![[_media/MediaPreview-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Media Preview Gramplet - detached example]]

Gramplet shows a preview of a single media object. {{-}} See [Media Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Media_Category)

## Notlar

![[_media/Notes-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Notes Gramplet - detached example]]

Etkin kişilerin notlarını gösteren Gramplet.

Ayrıca bakınız:

- [Not Gramplet](wiki:Addon:NoteGramplet) - Üçüncü taraf Eklentisi

{{-}}

### Kişi Notları

[Notlara](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Notlar) bakınız {{-}}

### Aile Notları

[Notlara](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Notlar) bakınız {{-}}

### Etkinlik Notları

[Notlara](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Notlar) bakınız {{-}}

### Yer Notları

[Notlara](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Notlar) bakınız {{-}}

### Kaynak Notları

[Notlara](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Notlar) bakınız {{-}}

### Alıntı Notları

[Notlara](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Notlar) bakınız {{-}}

### Depo Notları

[Notlara](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Notlar) bakınız {{-}}

### Ortam Notları

[Notlara](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Notlar) bakınız {{-}}

## Pedigree

![[_media/Pedigree-Gramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pedigree Gramplet - detached example]]

The Pedigree Gramplet shows a compressed view of the active person's direct ancestors. It defaults to going back 100 generations. The names can be clicked to change the active person, right-click to edit the person. At the bottom of the Gramplet the number of people per generation is listed. Birth and death dates are shown next to each person's name. Double-click the Generation number to see the matching individuals.

Using the content of the Pedigree in another program requires a bit of effort Open a contextual pop-up menu by right-clicking anywhere in the gramplet except a hotlink. Or, you can begin a drag selection from the same inert areas. Copy the highlighted text the OS clipboard from that same context menu. (The keybinding for 'Copy' will not work.) When you paste the text into another text editing program, you may need change the font to a non-proportional font to preserve the indentation. Some online services collapse leading spaces when you post a chunk of text. Preserving the indentation for such services may require replacing doubled spaces with doubled placeholder characters... like periods/full stops.

#### ⚙ Configurable Options

- Maximum generations: 1 to 100 limit; (*100*)
- Show Dates checkbox; (*deselected*)
- Line Type menu: <abbr title="Unicode Transformation Format graphical symbols">UTF</abbr>, <abbr title="American Standard Code for Information Interchange text symbols">ASCII</abbr>; (*UTF*)

## Quick View

![[_media/QuickView-Gramplet-Configuration-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Quick View Gramplet - detached example]]

The Quick View Gramplet allows you to run a Quick View, it updates as you move from person to person. (When this Gramplet was introduced, it only supported running Quick Views from the People category. Other categories are now supported.)

You can run any of the [Quick Views](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Quick_Views) for a person. {{-}} ![[_media/QuickView-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Quick View Gramplet - Configuration tab shown]]

You can change the options by clicking the Option button (top, left hand button of the Gramplet) which will detach the Gramplet and bring it up an a window. Select on the top row, and a list of options will appear. Press to apply the changes to the Quick View. You may then close the window to reattach the Gramplet.

{{-}} See the following developer information if you are interested in creating your own:

- [Making your own Quick view](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Making_your_own_Quick_view).

{{-}}

## Records

![[_media/Records-Gramplet-detached-50.png|Fig {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Records Gramplet - detached example]]

The Records Gramplet shows a number of interesting facts about the records (mostly age related) from your database. The list shows the top three for each element.

- Person Records:
  - Youngest living person
  - Oldest living person
  - Person died at youngest age
  - Person died at oldest age
  - Person married at youngest age
  - Person married at oldest age
  - Person divorced at youngest age
  - Person divorced at oldest age
  - Youngest father
  - Youngest mother
  - Oldest father
  - Oldest mother
- Family Records
  - Couple with most children
  - Living couple married most recently
  - Living couple married most long ago
  - Shortest past marriage
  - Longest past marriage

{{-}} The list is not only interesting on its own, it is also a good sanity check of the data. For some items you have to fill in some additional information.

This following example shows that there was a marriage event (thus calculation of the offset) but none of the persons had a death event. Even if the date is not known, just enter a death event for one of the partners and the list will be corrected.

**Living couple married most long ago**

1.  van Dosselaere, Egidius and Rechters, Petronella (382 years, 1 month)
2.  de Richter, Petrus and Asscericx, Catharina (379 years, 9 months)

{{-}}

An identical [Records Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Records_Report) is also available.

## Referanslar

![[_media/References-Gramplet-detached-50.png|Fig {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Referanslar Gramplet&#39;i - ayrılmış örnek]] Etkin kişilerin Referanslarını gösteren Gramplet.

{{-}}

### Kişi Referansları

- Kişi Referansları : Bir kişi için geri bağlantı referanslarını gösteren Gramplet

[Referanslara](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Referanslar) bakın {{-}}

### Aile Referansları

- Aile Referansları : Bir aile için geri bağlantı referanslarını gösteren Gramplet

[Referanslara](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Referanslar) bakın {{-}}

### Etkinlik Referansları

- Etkinlik Referansları : Bir olay için geri bağlantı referanslarını gösteren Gramplet

[Referanslara](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Referanslar) bakın {{-}}

### Yer Referansları

- Yer Referansları : Bir yer için geri bağlantı referanslarını gösteren Gramplet

[Referanslara](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Referanslar) bakın {{-}}

### Kaynak Referansları

- Kaynak Referansları : Bir kaynak için geri bağlantı referanslarını gösteren Gramplet

[Referanslara](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Referanslar) bakın {{-}}

### Alıntı Referansları

- Alıntı Referansları : Bir alıntı için geri bağlantı referanslarını gösteren Gramplet

[Referanslara](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Referanslar) bakın {{-}}

### Depo Referansları

- Depo Referansları : Bir depo için geri bağlantı referanslarını gösteren Gramplet

[Referanslara](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Referanslar) bakın {{-}}

### Ortam Referansları

- Ortam Referansları : Bir medya nesnesi için geri bağlantı referanslarını gösteren Gramplet

[Referanslara](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Referanslar) bakın {{-}}

### Not Referansları

- Not Referansları : Bir not için geri bağlantı referanslarını gösteren Gramplet

[Referanslara](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Referanslar) bakın {{-}}

## Relatives

![[_media/Relatives-Gramplet-detached-example-60.png|Fig {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Relatives Gramplet - detached example]]

This Gramplet shows all direct relatives of the active person. It's intended use is as a navigation help, an alternative way to move through your family tree in Gramps . If you detach the Gramplet, and place it next to Gramps, it will allow you to use it to easily change the content of the current "Person view".

If you are working in the charts category Pedigree view, the active person is the left-most person. By clicking a name in the relatives Gramplet, you can easily change the active person, and all person view in the other window will update. As the relatives Gramplet shows all spouses, all children and all parents, this offers an alternative way of navigating your data.

The names in this Gramplet also allow you to call up the person editor directly, by right-clicking on any of the names.

The Relatives Gramplet can be added to the following categories:

- People Category
- Relationships Category
- Charts Category
- Geography Category (selected views only)

{{-}}

## Residence

![[_media/ResidenceGramplet-Person-detached-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Person - Residence Gramplet - detached - example]]

Gramplet showing residence events for the active person {{-}}

### Person Residence

See [Residence](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Residence) {{-}}

## Session Log

![[_media/SessionLog-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Session Log Gramplet - detached example]]

The session log keeps track of activity in this session. It lists selected and edited objects.

Click a name once to make this person the active person. Double-click on a name or family brings up the page for that object. In addition, if you want to edit a person, but don't want to change the active person, you can right-click on the person's name.

This Gramplet is handy because you can very quickly change the active person, or edit the object, from the session list. {{-}}

## SoundEx

![[_media/SoundEx-Gramplet-detached-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} SoundEx Gramplet - detached example]]

This Gramplet generates SoundEx codes for the names of people in the database.

From the window you can either choose a from the pop-up menu shown by selecting the down arrowhead, (triangle) or you can type a name into the text field.

The name you type in can be any name... even a name not present in your Family Tree.

The result is shown automatically eg: The SoundEx code for *Simpson* is *S512*

A button is available which brings you to this page. With the button (or using the keyboard shortcut ) you dismiss the window. {{-}}

#### Soundex what is this?

Soundex is the most widely known of all [phonetic algorithms](http://en.wikipedia.org/wiki/Phonetic_algorithm) which allow indexing of words by their sound, as pronounced in English.

The Soundex equivalent is a coded surname (last name) index based on the way a surname sounds rather than the way it is spelled. Surnames that sound the same, but are spelled differently, like SMITH and SMYTH, have the same code and are filed together. The Soundex coding system was developed so that surnames may be found even when recorded under variant spellings.

First applied to the 1880 US Census, Soundex is a "sound index", not a strictly alphabetical one. The key feature is that it codes surnames (last names) based on the way a name sounds rather than on how it is spelled. The Soundex phonetic coding system pre-dates computers and was to help researchers find a surname quickly even though it may have received different spellings.

Those doing census lookups must use the same method to encode and tabulate surnames as the census workers did when they generated the database.

To search for a particular surname, you must first work out its encoding equivalent.

- **Basic Soundex Coding Rule:**

Every Soundex code consists of a letter and three numbers, such as W-252. The letter is always the first letter of the surname. The numbers are assigned to the remaining letters of the surname according to the Soundex guide shown below. Zeroes are added at the end if necessary to produce a four-character code. Additional letters are disregarded. Examples: Washington is coded W-252 (W, 2 for the S, 5 for the N, 2 for the G, remaining letters disregarded). Lee is coded L-000 (L, 000 added).

| Number | Represents the Letters |
|--------|------------------------|
| 1      | B, F, P, V             |
| 2      | C, G, J, K, Q, S, X, Z |
| 3      | D, T                   |
| 4      | L                      |
| 5      | M, N                   |
| 6      | R                      |

Disregard the letters A, E, I, O, U, H, W, and Y.

- **Additional Soundex Coding Rules:**
  - Names With Double Letters: If the surname has any double letters, they should be treated as one letter. For example:
    - Gutierrez is coded G-362 (G, 3 for the T, 6 for the first R, second R ignored, 2 for the Z).
  - Names with Letters Side-by-Side that have the Same Soundex Code Number: If the surname has different letters side-by-side that have the same number in the Soundex coding guide, they should be treated as one letter. Examples:
    - Pfister is coded as P-236 (P, F ignored, 2 for the S, 3 for the T, 6 for the R).
    - Jackson is coded as J-250 (J, 2 for the C, K ignored, S ignored, 5 for the N, 0 added).
    - Tymczak is coded as T-522 (T, 5 for the M, 2 for the C, Z ignored, 2 for the K). Since the vowel "A" separates the Z and K, the K is coded.
  - Names with Prefixes: If a surname has a prefix, such as Van, Con, De, Di, La, or Le, code both with and without the prefix because the surname might be listed under either code. Note, however, that Mc and Mac are not considered prefixes.For example, VanDeusen might be coded two ways:V-532 (V, 5 for N, 3 for D, 2 for S) or D-250 (D, 2 for the S, 5 for the N, 0 added).
  - Consonant Separators: If a vowel (A, E, I, O, U) separates two consonants that have the same Soundex code, the consonant to the right of the vowel is coded. <Example:Tymczak> is coded as T-522 (T, 5 for the M, 2 for the C, Z ignored (see "Side-by-Side" rule above), 2 for the K). Since the vowel "A" separates the Z and K, the K is coded. If "H" or "W" separate two consonants that have the same Soundex code, the consonant to the right of the vowel is not coded. Example: Ashcraft is coded A-261 (A, 2 for the S, C ignored, 6 for the R, 1 for the F). It is not coded A-226.

Please visit the [NARA Soundex Indexing page](http://www.archives.gov/research/census/soundex.html) to learn more about Soundex Indexing System. {{-}}

## Statistics

![[_media/Statistics-Gramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Statistics Gramplet - detached example]]

The Statistics Gramplet runs a Statistics report. Double-click the phrases to bring up the matching items.

Following information is provided to you in this Gramplet:

- **Individuals**
  - Number of individuals
  - Males
  - Females
  - Individuals with unknown gender
  - Incomplete names
  - Individuals with missing birth dates
  - Disconnected individuals
- **Family information**
  - Number of families
  - Unique surnames
- **Media objects**
  - Individuals with media objects
  - Total numbers of media object references
  - Number of unique media objects
  - Total size of media objects
  - Missing Media Objects

As with all Gramplets if you click on the left hand side button you detach the window and if you add persons to your family tree, you will see the amount of individuals change dynamically.

The information given in this Gramplet is the same as in the [Database Summary Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Database_Summary_Report) {{-}}

## Surname Cloud

![[_media/SurnameCloud-Gramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Surname Cloud Gramplet - detached example]]

The Surname Cloud Gramplet shows the top 100 (by default) used surnames. The name font size is proportional to the amount of people with the same name.

Double-click a surname to run the . This will open the window where you can find all people with a matching or alternate name. Person, birth date and name type are given.

If you mouse over the name you see the percentage of occurrence and total counts. {{-}} ![[_media/SurnameCloud-Gramplet-Configuration-tab-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Surname Cloud Gramplet - Configuration tab shown]]

You can change the number of names displayed by configuring the view for this gramplet. {{-}}

## To Do

![[_media/ToDo-Gramplet-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} To Do Gramplet - detached example]]

The **To Do Gramplet** displays a free form text area showing the contents of Note objects of the "To Do" type.

You can use this area to put some notes, remarks, things you should to get your research going. There are several other To Do programs (e.g. Tomboy e.a.) but these Gramplets are useful as the information stays within the Gramps database.

To Do Gramplets allow you to create notes and attach them to Gramps objects. For example, you can add a Person To Do Gramplet to the sidebar of the Person View. Notes added using this Gramplet will be attached to the currently active person. There is a To Do Gramplet for each Gramps primary object type. {{-}} See also the experimental [Third-party Addon](wiki:Third-party_Addons):

- [ToDo Notes Gramplet](wiki:Addon:ToDoNotesGramplet) available for the Dashboard that lists all To Do notes in the database, together with the object to which they are attached.

{{-}}

### Person To Do

See [To Do](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#To_Do) {{-}}

### Family To Do

See [To Do](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#To_Do) {{-}}

### Event To Do

See [To Do](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#To_Do) {{-}}

### Place To Do

See [To Do](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#To_Do) {{-}}

### Source To Do

See [To Do](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#To_Do) {{-}}

### Citation To Do

See [To Do](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#To_Do) {{-}}

### Repository To Do

See [To Do](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#To_Do) {{-}}

### Media To Do

See [To Do](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#To_Do) {{-}}

## Top Surnames

![[_media/TopSurnames-Gramplet-detached-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Top Surnames Gramplet - detached example]]

The Top Surnames Gramplet shows the top 10 (by default) used surnames.

The top ten is presented as follows:

- Surname
- percentage
- occurrences

The list gives you also the Total unique surnames in the database as well as the total number of people in your database.

Double-click a surname to run the . This opens the window, which gives the people with the surname you double-clicked.

A table is presented which shows all people with a matching name or alternate name. Person's name, ID, birth date and name type is given. {{-}}

Advanced:

- Change the number of names displayed by editing this section in `~/.gramps/gramps50/gramplets.ini`

{{-}}

## Uncollected Objects

![[_media/UncollectedObjects-Gramplet-detached-example-60.png|Fig {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Uncollected Objects Gramplet - detached example]]

The Gramplet is intended to list the low-level Python objects that are left around in memory and cannot be (easily) automatically deleted when they are no longer in use. Developers use it to try to identify the source of memory 'leaks', which cause Gramps to continually use more and more memory, the longer it is used.

Because the tool is trying to display objects that might still be getting deleted, it sometimes has some trouble. {{-}}

## Welcome

![[_media/Welcome-to-Gramps-Gramplet-detached-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Welcome Gramplet - detached example]]

The **Welcome to Gramps!** Gramplet gives an introductory message to new users, and some basic instructions.

The welcome message describes what Gramps is, that the program is Open Source Software and how you start a [Family Tree](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees). {{-}}

## What's Next

![[_media/WhatsNext-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} What's Next? Gramplet - detached example]]

The What's Next Gramplet displays a list of the "most urgent" information gaps in your family tree. It is based on the following assumptions:

- You want to know first and last name, birth date and place, and death date and place of each person
- You want to know father, mother, marriage date and place, and - if divorced - divorce date and place of each family with married parents
- You want to know at least the mother of each family with unmarried parents
- The closer the relationship to the main person, the more "urgent" the information gap is.
- The closer the common ancestor is from the main person, the more "urgent" the information is (e.g. nephews are considered more "urgent" than uncles, even though both have a distance of 3 generations, because for nephews the common ancestor is father/mother, while for uncles, the common ancestor is grandfather/grandmother)
- Marriage data and personal data of the spouse is slightly less "urgent" than personal data of the directly related person
- Half siblings are less "urgent" than siblings

You may copy the text from inside of this Gramplet by selecting it and pasting into an empty document. {{-}} ![[_media/WhatsNext-Gramplet-Configuration-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} What&#39;s Next? Gramplet - Configuration tab shown]]

The Gramplet can ignore previously verified events by making use of some custom Tags. The tags are selected in the Gramplets configuration. For example you can tag the following to be ignored:

- that a person is complete
- that a family is complete
- that a person or family should be ignored for shortening lists

{{-}}

[Category:Tr:Documentation](wiki:Category:Tr:Documentation)
