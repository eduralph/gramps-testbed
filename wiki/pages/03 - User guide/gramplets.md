---
title: Gramps 6.0 Wiki Manual - Gramplets
categories:
- Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 126847
wiki_fetched_at: '2026-05-30T11:29:59Z'
---

{{#vardefine:chapter\|12}} {{#vardefine:figure\|0}} Here we detail the functionality of the [Gramplets](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#What_is_a_Gramplet.3F) that come with Gramps.

## What is a Gramplet?

<span id="definition"> ![[_media/DashboardCategory-DashboardView-default-gramplets-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dashboard Category view (default gramplets)]]

A [Gramplet](wiki:Gramps_Glossary#gramplet) is an expansion to the Gramps program that *ideally* works seamlessly as if it was a core feature. They actually become embedded as part of Gramps. But while the core features of a view are needed almost constantly, the bundled Gramplets extend the view in ways that are only needed occasionally. Gramplets provide a supplemental perspective of the Tree data which either: changes dynamically during the navigation of the Gramps Tree, or; provides interactivity to your genealogical data.

Gramplets are the division of plug-ins (also called [widgets](http://wikipedia.org/wiki/Widget_engine), plugins, addons, auxiliary components) that can be found in the **[Dashboard Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Dashboard_Category)** ... or the **[Sidebars](#The_split-screen_Sidebar_.26_Bottombar)** and **[Bottombars](#The_split-screen_Sidebar_.26_Bottombar)** in other Navigator [View Categories](wiki:Gramps_Glossary#view). They provide all kinds of functionality that can be useful for the researcher.

A [selection of builtin plugins](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Gramplet_List) are bundled and pre-installed with Gramps. The Gramps project hosts a [selection of addon plugins](wiki:6.0_Addons#Addon_List) that might only be of interest to certain audiences.

There are also third-parties, such as The Taapeli Project in Finland, who hosts their own selection of [Isotammi group addon plugins](wiki:Addon:Isotammi_addons) developed to tune Gramps for their needs. Members of the Gramps community also share special purpose addons privately or via GitHub repositories. And, of course, users are [invited to develop their own addons](wiki:Addons_development#Develop_your_addon).</span>

### Aren't all Plugins also Gramplets?

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

### Starting with Gramplets

When you first start the [Dashboard Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Dashboard_Category) you will see two default Gramplets; the **** Gramplet and the ****.

The Dashboard and Gramplet Split Bars of the Navigator Categories may have **common** and **specific** Gramplets.

- Common Gramplets are applicable to any View ... and the data viewpoint is with respect to the Context of the Active Person and/or the Home Person. They can be docked on any Navigator Category View without making that View seem ambiguous.
- Specific Gramplets need the context of particular Views to give context to their perspective of the data. The list in the Dashboard's Add a Gramplet submenu and the Gramplet Bar Menu will differ according active Category view and Gramplets installed.

This list is leftover from an earlier revision of the wiki. It is unclear where the items fit in this discussion.

- Back references Gramplets - provide immediate visibility to data that tends be viewed occasionally and is buried in the interface... like the tab on object Editor.
- Filter Gramplet is like the previous filter sidebar
- Common models for Notes, Gallery, Sources, Citations, Events
- Children Gramplet on Person views (also charts category and relationships category), families view

### General Usage and Configuration

![[_media/WelcomeToGramps-Gramplet-docked-in-dashboard-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Example Gramplet Docked on Dashboard showing controls at top]] The container controls for Gramplets are arranged a little differently in the Dashboard category View as opposed to the Sidebar and Bottombar. Being aware of how these Gramplet containers differ (and are similar) will let you focus on getting the high speed performance instead of wondering why it spun out of control.

Originally added in version 3, Gramplets in Dashboard category View are arranged in a configurable number of columns. The Sidebar and Bottombar [split panes](wiki:Split_Views) were selected from among later innovations proposed in [GEPS 19](wiki:GEPS_019:_Improved_Sidebar_and_Split_Views). They were built on the Filter Sidebar of the 3.3 version. The Filter was converted to a Gramplet'' and pre-docked in the Sidebar.

![[_media/Welcome-to-Gramps-Gramplet-detached-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detached Sidebar Welcome Gramplet]]The split panes provide limited screenspace for docking Gramplets in the other Navigator categories. But, unlike the many columns of the Dashboard View, each new split pane is a single column, filled with a single Gramplet. (The pane still supports holding multiple Gramplets, it just uses Tabs to display them one at a time.)

The split pane approach reduces the need for flipping between Category Views... and that lightens the demands on the database.

![[_media/DashboardCategory-gramplet-detached-and-docked-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detached Gramplet in the Dashboard View (with docked Gramplet underneath]] However, Gramplets can be undocked (detached, torn off) to float free from any of the three containers. When detached, an additional button in the lower left will open the Gramplet's page on this website and button on the lower right. Clicking the  button in the upper right corner will re-docks a detached Gramplet. Clicking the similar  button of a docked Gramplet will remove it from the pane.

#### The Dashboard Category View

In the [Dashboard](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Dashboard_Category), you can drag the  button (top left) of each Gramplet to reposition it in the Dashboard View area. You can click the  button to detach (or *‘undock’*) the Gramplet from Dashboard View and place it in its own window. The window will stay open regardless of page (relationships, charts, etc). Closing the detached view will put it back onto the Dashboard view. If you quit Gramps with a open Gramplet, when you start gramps again, it will open automatically.

When one or more Gramplets are undocked from the Dashboard View, they remain visible as you change to a different View (such as the People or Charts View). In this way, you can use these Gramplets to supplement a particular View with additional details and functionality provided by the Gramplet.

You can add new Gramplets by right-clicking on an open space on Dashboard view. Click the  button above the Gramplet to remove it from the Dashboard.

##### ⚙ Configurable Options

![[_media/Menubar-View-overview-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} View menu]] You can also change the number of columns by changing a *Gramplets Layout* tab setting in *Configure Dashboard* window. To open the window, click the ![[_media/Gramps-config.png]] button, choose from the View menu, or press the *Configure active view* [keyboard keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings). ![[_media/Whats-next-gramplet-configure-dashboard-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet Configuration tabs]] Each Gramplet docked in the Dashboard will also have a Configuration tab added. (But the same Gramplet may not have any Configuration options or tab when docked in the Sidebar or Bottombar.) The Dashboard provides extra options for each Gramplet to allow it be renamed, set to a fixed vertical size, or be maximized vertically in its column. The Configuration tab for Gramplets in docked in the Dashboard reflect at least these minimum options.

Double-clicking the title of a Gramplet docked in the Dashboard Category allows you to change the display title.

#### The split-screen Sidebar & Bottombar

![[_media/Bottombar-sidebar-drop-down-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramplet split-screens showing Gramplet Bar Menu with the unlabeled Down Arrowhead  pull-down menu button]] Each of these split screen panes is a container of stacked Gramplet tabs. Like Windows with a tabbed section, each can show only a single tab at a time. But tabs can be added, re-ordered, undocked or disabled in a similar fashion to the Dashboard. However, instead of a Contextual Menu, each split-pane has a *Down Arrowhead* pull-down menu button to show the same pop-up list of options.

To add a Gramplet to the stacked tabs, select it from the submenu.

<span id="undock gramplet">To undock a tab, grab the tab title and drag out of the split-pane onto the toolbar or menubar. To re-dock, click the Close button or the 'X' button.</span>

To remove the Gramplet from the stack tabs, select it from the submenu. (Alternatively, the Close button will be accessible if the 'Show close button in gramplet tabs' checkbox in the [Display](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) tab of Preferences is selected.)

Curiously, the same Gramplets might be tabs in the different split-screen section of a View but be configured to show information differently. It is important to be aware that each Gramplet (whether stacked as a Tab or floating undocked) bogs down performance of Gramps. Use fewer Gramplets to make Gramps more responsive.

The lists of Gramplets that can be added to the stack of tabs in a split pane are filtered by those appropriate to that category.

##### ⚙ Configurable Options

![[_media/Menubar-View-overview-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} View menu]]

In addition, there are a number of Third-party Gramplets that you can easily install and use. These include:

- Headline News Gramplet - current, breaking news from Gramps
- Data Entry Gramplet - edit active person's name, birth date and place, death date and place, and add people
- Python Gramplet - a Python shell
- FAQ Gramplet - frequently asked questions
- Note Gramplet - see and edit active person's primary Person Note

and many others. See [Third-party Addons](wiki:Third-party_Addons) for more details.

## Summary of Gramplets

Summary of all default builtin Gramplets and the view categories in which each gramplet can be used.

Independently for each Category view mode container, the Gramplets can be added or removed using the following controls:

- In the Dashboard Category, via the right-click context menu.
- In all other Categories, via the drop-down Gramplet selection menus (*Down Arrowhead* button) on either the Bottombar or Sidebar.

*There are no Menu options to add a Gramplet. This is because it would be ambiguous whether the Gramplet was to be added to that view mode's sidebar or bottombar.* {{-}}

### Gramplet List

Click a Category header (twice) to sort the list and show that category's menu of available builtin Gramplet choices. (The actual menu will also include installed [Third-party addon](wiki:6.0_Addons#Addon_List) Gramplets.)

| Gramplet | ![[_media/22x22-gramps-gramplet.png]] <small>Dashboard</small> | ![[_media/22x22-gramps-person.png]] <small>People</small> | ![[_media/22x22-gramps-relation.png]] <small>Relationships</small> | ![[_media/22x22-gramps-family.png]] <small>Families</small> | ![[_media/22x22-gramps-pedigree.png]] <small>Charts</small> | ![[_media/22x22-gramps-event.png]] <small>Events</small> | ![[_media/22x22-gramps-place.png]] <small>Places</small> | ![[_media/22x22-gramps-geo.png]] <small>Geography</small> | ![[_media/22x22-gramps-source.png]] <small>Sources</small> | ![[_media/22x22-gramps-citation.png]] <small>Citations</small> | ![[_media/22x22-gramps-repository.png]] <small>Repositories</small> | ![[_media/22x22-gramps-media.png]] <small>Media</small> | ![[_media/22x22-gramps-notes.png]] <small>Notes</small> |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| id="0" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="1" \| | <big>🗹</big> | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="2" \| | <big>🗹</big> | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="3" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="4" \| |  | <big>❖</big> | ✔ | <big>❖</big> | ✔ | <big>❖</big> |  | ✔ | <big>❖</big> | <big>❖</big> |  | <big>❖</big> |  |
| id="5" \| | <big>🗹</big> | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="6" \| |  | <big>❖</big> | ✔ | <big>❖</big> | ✔ |  |  | ✔ |  |  |  |  |  |
| id="7" \| |  | <big>❖</big> | ✔ | <big>❖</big> | ✔ | <big>❖</big> | <big>❖</big> | ✔ |  |  |  | <big>❖</big> |  |
| id="8" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="9" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="10" \| |  | <big>❖</big> | ✔ |  | ✔ |  | <big>❖</big> | ✔ |  |  | <big>❖</big> |  |  |
| id="18a" \| |  |  |  |  |  |  | ✔ |  |  |  |  |  |  |
| id="18b" \| |  |  |  |  |  |  | ✔ |  |  |  |  |  |  |
| id="11" \| |  | <big>❖</big> | ✔ | <big>❖</big> | ✔ |  |  | ✔ |  |  |  |  |  |
| id="11a" \| |  | <big>❖</big> | ✔ | <big>❖</big> | ✔ |  |  | ✔ |  |  |  |  |  |
| id="12" \| | <big>🗹</big> | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="13" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="14" \| |  | <big>♦</big> | <big>♦</big> | <big>♦</big> | <big>♦</big> | <big>♦</big> | <big>♦</big> | <big>♦</big> | <big>♦</big> | <big>♦</big> | <big>♦</big> | <big>♦</big> | <big>♦</big> |
| id="15" \| |  | <big>❖</big> | ✔ | <big>❖</big> | ✔ | <big>❖</big> | <big>❖</big> | ✔ | <big>❖</big> | <big>❖</big> |  |  |  |
| id="16" \| | <big>🗹</big> | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="17" \| |  |  |  |  |  |  |  |  |  |  |  | ✔ |  |
| id="21" \| |  |  |  |  |  |  |  |  |  |  |  | ✔ |  |
| id="19" \| |  | <big>❖</big> | ✔ | <big>❖</big> | ✔ | <big>❖</big> | <big>❖</big> | ✔ | <big>❖</big> | <big>❖</big> | <big>❖</big> | <big>❖</big> | <big>❖</big> |
| id="20" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="22" \| | <big>🗹 ⚙</big> | <big>♦ ⚙</big> | <big>♦ ⚙</big> | <big>♦ ⚙</big> | <big>♦ ⚙</big> | <big>♦ ⚙</big> | <big>♦ ⚙</big> | <big>♦ ⚙</big> | <big>♦ ⚙</big> | <big>♦ ⚙</big> | <big>♦ ⚙</big> | <big>♦ ⚙</big> | <big>♦ ⚙</big> |
| id="23" \| | <big>🗹</big> | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="24" \| |  | <big>❖</big> | ✔ | <big>❖</big> | ✔ | <big>❖</big> | <big>❖</big> | ✔ | <big>❖</big> | <big>❖</big> | <big>❖</big> | <big>❖</big> | <big>❖</big> |
| id="25" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="26" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="27" \| | <big>🗹</big> | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="28" \| | <big>🗹</big> | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="29" \| | <big>🗹</big> | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="30" \| | <big>🗹</big> | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="31" \| | <big>🗹</big> | <big>❖</big> | <big>❖</big> | <big>❖</big> | <big>❖</big> | <big>❖</big> | <big>❖</big> | <big>❖</big> | <big>❖</big> | <big>❖</big> | <big>❖</big> | <big>❖</big> |  |
| id="32" \| | <big>🗹</big> | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="33" \| | <big>🗹</big> | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="34" \| | <big>🗹</big> | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="37" \| | <big>🗹</big> ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ |
| id="38" \| | <big>🗹</big> ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ |
| id="xx" \| |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |

| Symbol         | Meaning                                    |
|----------------|--------------------------------------------|
| ⚠              | Dangerous. Available in debug mode only    |
| ✔              | listed in gramplet menu for view           |
| <big>🗹</big>   | different container behavior               |
| <big>♦ ⚙</big> | category specific configuration options    |
| <big>♦</big>   | category specific interface                |
| <big>❖</big>   | Content based on active record or category |

For more detailed information on using the installed Gramplets, see [Gramplets](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Gramplets). {{-}}

## Gramplets

This following sections describe each Gramplet and its basic functionality. {{-}}

### 2-Way Fan Chart

![[_media/2-WayFanChart-detached-gramplet-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} 2-Way Fan Gramplet]] Chart consisting of both ascendants and descendants. The **2-Way Fan View** view interactively displays the active person's ancestors and descendants in a pie chart format. The Descendant Fan provides a comprehensive and visually appealing way to explore and analyze an individual's descendants within your family tree.

See also: {{-}}

### Age on Date

![[_media/AgeOnDate-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Age On Date Gramplet - detached example]]

The Gramplet allows you to enter a [Calendar date](https://en.wikipedia.org/wiki/Calendar_date) in the entry field. If you select the the Gramplet will compute the ages for everyone in your Family Tree living on that Date and will show the results in a separate Quick View report dialog. The date must be entered in a calendar format that Gramps accepts eg: YYYY-MM-DD .

- No configuration options are available for this gramplet.

{{-}}

- You can also drag a date to from [Calendar Gramplet](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Calendar) to the Gramplets entry field to enter that date.
- See also the [Third-party Addon](wiki:Third-party_Addons) [Date Calculator Gramplet](wiki:Addon:DateCalculator) which allows you to do date math.

{{-}}

#### People and their ages (the/on) <date> Quick View report dialog

![[_media/AgeOnDate-Gramplet-QuickView-example-result-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Age On Date Gramplet - Quick View - result example]]

From the resulting Quick View report dialog you can sort by the Person, Age or Status columns. Right clicking the row opens a context menu that allows you to *Copy all* rows to the clipboard; or to *See the person details* in the Person Editor, or *Make the person active*. {{-}} See also:

- [Quick_Views](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Quick_Views)

### Age Stats

![[_media/AgeStats-Gramplet-detached-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Age Stats Gramplet - detached example]]

The Gramplet shows statistics in the form of three graphs grouped in 5 years age span breakdowns (use the vertical scroll bar to see the other two graphs or detach and maximize the Gramplet):

- **Lifespan Age Distribution** - for all people having valid birth and death dates.
- **Father - *Child Age Diff Distribution*** - shows the age difference between child and father where both individuals have valid birth dates.
- **Mother - *Child Age Diff Distribution*** - shows the age difference between child and mother where both individuals have valid birth dates.

Rolling the mouse cursor over a chart row will display a hint with the count of offspring matching the row's range.

Double-clicking a row in any of the statistics graphs opens a Quick View report of the offspring categorized by that row. You can sort the Quick View report by the Name, Birth Date and Name Type columns.

Right-clicking the Quick View report row displays a context menu for copying the list, opening the Person Editor or activating the person.

{{-}}

#### Age Stats - Quick View

##### ⚙ Configurable Options

![[_media/AgeStats-Gramplet-configuration-tab-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Age Stats&quot; Gramplet - from People category Configuration tab defaults]] Adjustable graph scaling limits

- (`110` default) - Maximum age ranging between 1-150.

- (`55` default) - Maximum age ranging between 1-150.

- (`70` default) - Maximum age ranging between 1-70.

Select the button to apply your changes.

In the Dashboard View, the Gramplet may be detached by clicking the button. {{-}}

### Ancestors

![[_media/Ancestors-Gramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ancestors Gramplet - detached example]]

Use the Gramplet to show ancestors of the active person. It is intended to be used as a navigation help, an alternative way to move through your family tree in Gramps . If you detach the Gramplet, and place it next to Gramps, it will allow you to use it to easily change the content of the current "Person view".

Hovering the mouse over a person shows a tooltip with details for them.

Using the context menu to:

- \- the selected person.

- \- the contents of the gramplet to the OS clipboard

{{-}} See also:

- Gramplet - relatives of the active person navigation aid.

### Attributes

![[_media/Attributes-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Attributes Gramplet]]

The Attributes Gramplet shows all of the attributes for the current, active person. Double click on the name of the attribute, and you will run a Quick View that shows all of the people that have that attribute, and the values for it. You can sort the Quick View by the attribute value by clicking on the column name. {{-}}

##### Attributes Quick View

![[_media/Atttribute-Gramplet-QuickView-example-result-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Attributes Gramplet - Quick View example result]]

In the Quick View, highlight the entry to change the active person (which will then change the Attributes Gramplet), and double-click the Quick View entry to bring up the Edit Person dialog window. {{-}}

#### Person Attributes

See [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) {{-}}

#### Family Attributes

See [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) {{-}}

#### Event Attributes

See [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) {{-}}

#### Source Attributes

See [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) {{-}}

#### Citation Attributes

See [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) {{-}}

#### Media Attributes

See [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) {{-}}

### Calendar

![[_media/CalendarGramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Calendar Gramplet" - detached example]]

The **Calendar Gramplet** shows a monthly calendar.

Surrounding the label at the top left corner, the and buttons can be used to change the month.

Surrounding the label at the top right corner, the and buttons can be used to change the year.

Double-click a **day** to run the Quick View. The Quick View window shows up to 3 table sections, the events (if any exist) of: the exact date, other events on the same month/day in history, and events in that year.

You can also drag a day from the Calendar to the date fields (such as for the [Event Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#New_Event_dialog) or the [Age on Date Gramplet](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Age_on_Date)) to enter that date. Similarly, a calendar day may also be dragged to the [Clipboard](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Using_the_Clipboard) where it will be stored in a plain text format.

{{-}}

### Children

![[_media/ChildrenGramplet-PeopleCategoryView-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Children Gramplet - detached example with tooltip]]

Gramplet showing the active persons children from **all marriages**. Children are displayed as ordered in the family record(s).

Double-click on a row to edit the selected child.

Select a column title to sort temporarily until you exit Gramps.

[How do I change the order of children?](wiki:Gramps_6.0_Wiki_Manual_-_FAQ#How_do_I_change_the_order_of_children.3F)

- Use the [Children](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Children) tab in the Family Editor to change the order of children in the active family.
- Use the third-party addon tool which allows bulk updates of the children order.

See also:

- This [Children](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Children) gramplet in the [People Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#People_Category) views displays all children from **all marriages** for the active person. Children are displayed as ordered in the family record(s).

{{-}}

#### Person Children

See [Children](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Children)

Also the `Spouse` column shows if present which other parent the active person had the child with. (and is not the spouse of the listed child!) {{-}}

#### Family Children

See [Children](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Children) {{-}}

### Citations

![[_media/Citation-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Citation Gramplet - detached example]]

Gramplet showing the active persons citations. {{-}}

#### Person Citations

See [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) {{-}}

#### Family Citations

See [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) {{-}}

#### Event Citations

See [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) {{-}}

#### Place Citations

See [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) {{-}}

#### Media Citations

See [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) {{-}}

### Descendant Fan Chart

![[_media/DescendantFan-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Descendant Fan (chart) Gramplet - detached example]]

Gramplet showing active person's direct descendants as a fan chart.

**See also:** {{-}}

### Descendants

![[_media/Descendants-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Descendants Gramplet - detached example]]

The Descendants Gramplet shows the direct descendants of the active person.

The order of the spouses and children is that given in the Gramps editor. To change the order of spouses, click on *Order* on the Relationship view. To change the order of children, [drag and drop](http://en.wikipedia.org/wiki/Drag-and-drop) them in the correct order in the Family edit window.

This Gramplet is based on the [Descendant Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Descendant_Report), available from the Textual Reports.

The Descendants Gramplet will update when you change the active person, or change family trees. It does not update automatically for edits or additions because this report is time-consuming to run.

Minimizing a Gramplet will prevent it from updating.

Moving the mouse over a person will show a tooltip summary which includes the death date. {{-}}

### Details

![[_media/Details-Gramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Details" Gramplet - detached example with context menu]]

Gramplet showing details and image of the active person.

Provides a brief non editable summary of the selected person for example:

- *Name*: of person
- *Also Known As:*
- *Other Name:*
- *Father:*
- *Mother:*
- *Birth:*
- *Death:*
- *Burial:*

<!-- -->

- *Image*: If available the primary image will be shown to the right of the details, otherwise a cross will indicate the image is missing, you may double click the image to open it in an external viewer. To change the primary active image see: [Edit Person Editors - Gallery tab](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Gallery)

You can use the context menu to right click and

You may highlight and copy the individual text fields.

- [Missing Media Objects 'broken link' icon of a box with a red 'x'](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Missing_Media_Objects_.27broken_link.27_icon_of_a_box_with_a_red_.27x.27)

{{-}}

#### Person Details

See [Details](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Details) {{-}}

#### Place Details

See [Details](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Details) {{-}}

#### Repository Details

See [Details](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Details) {{-}}

<span id="Place_Encloses">

### Encloses

</span> ![[_media/Encloses-Gramplet-detached-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Encloses Gramplet - detached example]]

Gramplet showing the hierarchical locations of a place it encloses over time.

{{-}}

- See also [Enclosed By](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Enclosed_By) tab

<span id="Place_Enclosed_By">

#### Encloses Place Locations

</span> See [Enclosed By](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Enclosed_By) {{-}}

### Enclosed By

![[_media/EnclosedBy-Gramplet-detached-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Enclosed By Gramplet - detached example]]

Gramplet showing the locations hierarchically enclosed by a place over time.

- See also [Enclosed By](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Enclosed_By) tab

{{-}}

#### Enclosed By Place Locations

See [Encloses](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Encloses) {{-}}

### Events

![[_media/Events-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Events Gramplet - detached example]] Primarily designed as an alternative to opening a Edit Object dialog layout tab .

Double click a row to edit the event.

See [Events](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Events)

#### Family Events

Gramplet added in the Person category will show the events for the active Family.

#### Person Events

Gramplet added in the Person category will show the events for the active person.

{{-}}

### Events Coordinates

Primarily designed to verify that the key data exists to plot the Events in the Geography view. Beyond the coordinates, a date and event type are needed for some of the animated views.

Right-click a row to open a context menu to edit the event or place. <span id="Geography coordinates for Family Events">

#### Family Events Audit

</span>![[_media/EventsCoordinates-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Events Coordinates Gramplet - detached example]]

Gramplet added in the Family category will show the Events for the active Family.  
<span id="Geography_coordinates_for_Person_Events">

#### Person Events Audit

</span> Gramplet added in the Person category will show the Events for the active person. {{-}}

### Fan Chart

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

### FAQ

![[_media/FAQ-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} FAQ Gramplet - detached example]]

The (Frequently Asked Questions) shows a list of common questions, and links to their answers from the Gramps Wiki (requires an internet connection).

This gramplet shows a manually curated list of **Frequently Asked Questions** hyperlinked to answers in articles of the Gramps wiki. The list is collated from new user postings to the [Gramps User Forum](wiki:Contact#Forum) that must be answered repeatedly.

The idea is to make the answers to the most common question easier to find, the primary objective is to let new users start using Gramps more quickly.

#### See Also

- Bug Report : how to add/update FAQs

{{-}}

### Filter

Gramplet providing a filter specific to the Category:

- 

- 

- \- *Interface is the same as the*

- 

- 

- \- *Interface is the same as the*

- 

- 

- 

- 

- 

###### General usage

Enter the term to be searched for and adjust any required options and then select the button to see the result(s) if any.

###### See Also

- [Which filters (rules) in which Category?](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Which_filters_in_which_Category.3F)
- Gramps Glossary term: [Regular Expressions](wiki:Gramps_Glossary#regex) for pattern matching in searches
- Third-party *Isotammi* [Filter+ gramplet addon](wiki:Addon:Isotammi_addons#Filter.2B)

{{-}} <span id="Person Filter"></span>

#### People Filter

![[_media/FilterGramplet-Person-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} People - &quot;Filter Gramplet&quot; - detached - default]] Equivalent to the [builtin Custom Filter rules](wiki:Gramps_6.0_Wiki_Manual_-_Filters#toc):

- : [People with a name matching &lt;text&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#People_with_the_.3Cname.3E)

- : [People with Id containing &lt;text&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#People_with_.3Cid.3E)

- : [Male](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Males) • [Female](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Females) • [People with unknown gender](wiki:Gramps_6.0_Wiki_Manual_-_Filters#People_with_unknown_gender)

- : [People with the &lt;birth data&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#People_with_the_.3Cbirth_data.3E)

  - Date selection editor

- : [People with the &lt;death data&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#People_with_the_.3Cdeath_data.3E)

  - Date selection editor

- : [People with the personal &lt;event&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#People_with_the_personal_.3Cevent.3E)

- : [People having notes containing &lt;text&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#People_having_notes_containing_.3Ctext.3E)

- : [People with the &lt;tag&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Families_with_the_.3Ctag.3E)

- : [People matching the &lt;filter&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#People_matching_the_.3Cfilter.3E)

  - Define filter editor

- :

- :

- :

- :

- button that automatically creates a custom filter based on the given criteria. This makes it easy to create simple custom filters.

##### People Filter example

Some simple regular expressions to filter out persons with surnames spelled slightly different.

With this regular expression in the sidebar filter entry:

`eri[ck](s|ss)on`

or

`eri[ck]ss?on`

or

`eri[ck]s+on`

You get all four versions as result:

`Ericson`  
`Ericsson`  
`Erikson `  
`Eriksson`

{{-}} <span id="Family Filter"></span>

#### Families Filter

![[_media/FilterGramplet-Family-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Families - &quot;Filter Gramplet&quot; - detached - default]] Equivalent to the [builtin Custom Filter rules](wiki:Gramps_6.0_Wiki_Manual_-_Filters#toc):

- ID : [Families with Id containing &lt;text&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Families_having_child_with_id_containing_.3Ctext.3E)
- Father :[Families with father matching the &lt;regex_name&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Families_with_father_with_the_.3Cname.3E)
- Mother : [Families with mother matching the &lt;regex_name&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Families_with_mother_with_the_.3Cname.3E)
- Child : [Families with child matching the &lt;regex_name&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Families_with_child_with_the_.3Cname.3E)
- Relationship : [Families with the relationship type](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Families_with_the_relationship_type)
- Family Event : [Families with the &lt;event&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Families_with_the_.3Cevent.3E)
- Family Note : [Families having notes containing &lt;text&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Families_having_notes_containing_.3Ctext.3E)
- Tag : [Families with the &lt;tag&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Families_with_the_.3Ctag.3E)
- Custom filter : [Families matching the &lt;filter&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Families_matching_the_.3Cfilter.3E)

{{-}}

#### Charts Filter

![[_media/FilterGramplet-Person-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Charts - Filter Gramplet - detached - default (Same as People Filter)]] The diagrams in Charts need the context of connecting records to define the connections between blocks. So rather than only displaying *only* the matching records in the Charts view modes, Filters for the Charts still displays all the records but dims the non-matching ones.

*Interface is the same as the* {{-}}

<span id="Event Filter"></span>

#### Events Filter

![[_media/FilterGramplet-Event-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Events - Filter Gramplet - detached - default]] Equivalent to the [builtin Custom Filter rules](wiki:Gramps_6.0_Wiki_Manual_-_Filters#toc):

- ID : [Events with Id containing &lt;text&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Events_with_Id_containing_.3Ctext.3E)
- Description : [Events matching parameters](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Events_matching_parameters)
- Type : <small>*Events matching parameters*</small>
- Participants : <small>*Events matching parameters*</small>
- Date : <small>*Events matching parameters*</small>
- Place : <small>*Events matching parameters*</small>
- Note : [Events having notes containing &lt;text&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Events_having_notes_containing_.3Ctext.3E)
- Tag : [Events with the &lt;tag&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Events_with_the_.3Ctag.3E)
- Custom filter : [Events matching the particular &lt;filter&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Events_matching_the_.3Cfilter.3E)

{{-}} <span id="Place Filter"></span>

#### Places Filter

![[_media/FilterGramplet-Place-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Places - Filter Gramplet - detached - default]] Equivalent to the [builtin Custom Filter rules](wiki:Gramps_6.0_Wiki_Manual_-_Filters#toc):

- ID : [Places with Id containing &lt;text&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Places_with_Id_containing_.3Ctext.3E)
- Name : [Places matching parameters](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Places_matching_parameters)
- Type : <small>*Places matching parameters*</small>
- Code : <small>*Places matching parameters*</small>
- Enclosed By : [Places enclosed by another place](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Places_enclosed_by_another_place)
- Within : [Places within an area](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Places_within_an_area)
- Note : [Places having notes containing &lt;text&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Places_having_notes_containing_.3Ctext.3E)
- Tag : [Places with the &lt;tag&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Places_with_the_.3Ctag.3E)
- Custom filter : [Places matching the &lt;filter&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Places_matching_the_.3Cfilter.3E)

{{-}}

#### Geography Filter

![[_media/FilterGramplet-Place-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Geography - Filter Gramplet - detached - default (Same as Places Filter)]] *Interface is the same as the*

{{-}} <span id="Source Filter"></span>

#### Sources Filter

![[_media/FilterGramplet-Source-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Sources - Filter Gramplet - detached - default]] Equivalent to the [builtin Custom Filter rules](wiki:Gramps_6.0_Wiki_Manual_-_Filters#toc):

- ID : [Sources with Id containing &lt;text&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Sources_with_Id_containing_.3Ctext.3E)
- Title : [Sources matching parameters](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Sources_matching_parameters)
- Author : <small>*Sources matching parameters*</small>
- Abbreviation : <small>*Sources matching parameters*</small>
- Publication : <small>*Sources matching parameters*</small>
- Note : [Sources having notes containing &lt;text&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Sources_having_notes_containing_.3Ctext.3E)
- Tag : [Sources matching the &lt;tag&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Sources_with_the_.3Ctag.3E)
- Custom filter : [Sources matching the &lt;filter&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Sources_matching_the_.3Cfilter.3E)

{{-}} <span id="Citation Filter"></span>

#### Citations Filter

![[_media/FilterGramplet-Citation-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Citations - Filter Gramplet - detached - default]] Equivalent to the [builtin Custom Filter rules](wiki:Gramps_6.0_Wiki_Manual_-_Filters#toc):

**Source:**

- ID : [Sources with Id containing &lt;text&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Citations_with_Id_containing_.3Ctext.3E)
- Title : [Sources matching parameters](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Sources_matching_parameters)
- Author : <small>*Sources matching parameters*</small>
- Abbreviation : <small>*Sources matching parameters*</small>
- Publication : <small>*Sources matching parameters*</small>
- Note : [Citations having source notes containing &lt;text&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Citations_having_source_notes_containing_.3Ctext.3E)

**Citation:**

- ID : [Citations with Id containing &lt;text&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Citations_with_Id_containing_.3Ctext.3E)
- Volume/Page : [Citations matching parameters](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Citations_matching_parameters)
- Date : <small>*Citations matching parameters*</small>
- Min. Conf. : <small>*Citations matching parameters*</small>
- Note : [Citations having notes containing &lt;text&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Citations_having_notes_containing_.3Ctext.3E)
- Tag : [Citations with the &lt;tag&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Citations_with_the_.3Ctag.3E)
- Custom filter : [Citations matching the &lt;filter&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Citations_matching_the_.3Cfilter.3E)

{{-}} <span id="Repository Filter"></span>

#### Repositories Filter

![[_media/FilterGramplet-Repository-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Repositories - &quot;Filter Gramplet&quot; - detached - default]] Equivalent to the [builtin Custom Filter rules](wiki:Gramps_6.0_Wiki_Manual_-_Filters#toc):

- ID : [Repositories with Id containing &lt;text&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Repositories_with_Id_containing_.3Ctext.3E)
- Name : [Repositories matching parameters](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Repositories_matching_parameters)
- Type : <small>*Repositories matching parameters*</small>
- Address : <small>*Repositories matching parameters*</small>
- URL : <small>*Repositories matching parameters*</small>
- Note : [Repositories having notes containing &lt;text&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Repositories_having_notes_containing_.3Ctext.3E)
- Tag : [Repositories with the &lt;tag&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Repositories_with_the_.3Ctag.3E)
- Custom filter : [Repositories matching &lt;filter&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Repositories_matching_the_.3Cfilter.3E)

{{-}}

#### Media Filter

![[_media/FilterGramplet-Media-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Media - Filter Gramplet - detached - default]] Equivalent to the [builtin Custom Filter rules](wiki:Gramps_6.0_Wiki_Manual_-_Filters#toc):

- ID : [Media objects with Id containing &lt;text&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Media_objects_with_Id_containing_.3Ctext.3E)
- Title : [Media objects matching parameters](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Media_objects_matching_parameters)
- Type : <small>*Media objects matching parameters*</small>
- Path : <small>*Media objects matching parameters*</small>
- Date : <small>*Media objects matching parameters*</small>
- Note : [Media objects having notes containing &lt;text&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Media_objects_having_notes_containing_.3Ctext.3E)
- Tag : [Media objects with the &lt;tag&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Media_objects_with_the_.3Ctag.3E)
- Custom filter : [Media objects matching the &lt;filter&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Media_objects_matching_the_.3Cfilter.3E)

{{-}}

#### Notes Filter

![[_media/FilterGramplet-Notes-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Notes - Filter Gramplet - detached - default]] Equivalent to the [builtin Custom Filter rules](wiki:Gramps_6.0_Wiki_Manual_-_Filters#toc):

- ID : [Notes with Id containing &lt;text&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Notes_with_Id_containing_.3Ctext.3E)
- Text : [Notes matching parameters](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Notes_matching_parameters)
- Type : <small>*Notes matching parameters*</small>
- Tag : [Notes with the &lt;tag&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Notes_with_the_.3Ctag.3E)
- Custom filter : [Notes matching the &lt;filter&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Notes_matching_the_.3Cfilter.3E)

{{-}}

### Gallery

![[_media/Gallery-Gramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gallery Gramplet - detached example]]

Gramplet showing media objects. The first image is the primary active media object that is used in reports and the .

You can use the context menu to right click and

Double-click on the picture to view it in the default image viewer application.

See also:

- To change the primary media object for reports etc... use the s [Gallery](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Gallery) tab.

{{-}}

#### Person Gallery

See [Gallery](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Gallery) {{-}}

#### Family Gallery

See [Gallery](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Gallery) {{-}}

#### Event Gallery

See [Gallery](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Gallery) {{-}}

#### Place Gallery

See [Gallery](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Gallery) {{-}}

#### Source Gallery

See [Gallery](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Gallery) {{-}}

#### Citation Gallery

See [Gallery](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Gallery) {{-}}

### Given Name Cloud

![[_media/GivenNameCloud-Gramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Given Name Cloud Gramplet - detached example]]

The Gramplet shows the top most popular given names in your family tree. The font size of the name indicates how popular it is. Mouse over the name to see the exact count, and the percent of people in the family tree that have that name.

The Gramplet splits up [preferred given names](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Preferred_Name_section) into words (broken up by spaces) unless a connector (such as a hyphen or non-breaking space) has been specified to bridge between the names to create a compound name. For example "Sarah Elizabeth" would appear under both "Sarah" and "Elizabeth".

Double-click on the given name to bring up a Quick View of all of the matching people. {{-}}

See also:

- [Surname Cloud Gramplet](#Surname_Cloud)

#### Given Name Cloud Quick View

### Image Metadata

![[_media/ImageMetadata-Gramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Image Metadata" Gramplet - example]]

The Gramplet offers an interface to look at [Image Exif Metadata](https://en.wikipedia.org/wiki/Exchangeable_image_file_format) from your images (\*.jpg, \*.png. \*.tiff, \*.exv, \*.nef, \*.psd, \*.pgf). {{-}} See also the third-party:

- [Addon:Edit Image Exif Metadata](wiki:Addon:Edit_Image_Exif_Metadata)

#### Prerequisites

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

#### Usage scenario

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

### Media Preview

![[_media/MediaPreview-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Media Preview Gramplet - detached example]]

Gramplet shows a preview of the single primary media object if it exists. {{-}} See [Media Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Media_Category)

### Notes

![[_media/Notes-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Notes Gramplet - detached example]]

Gramplet showing the active persons notes.

See also:

- [Notes Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Notes_Category)
- [Editing information about notes](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Editing_information_about_notes)
- [Note Gramplet](wiki:Addon:NoteGramplet) - Third party Addon

{{-}}

#### Person Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) {{-}}

#### Family Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) {{-}}

#### Event Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) {{-}}

#### Place Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) {{-}}

#### Source Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) {{-}}

#### Citation Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) {{-}}

#### Repository Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) {{-}}

#### Media Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) {{-}}

### Pedigree

![[_media/Pedigree-Gramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pedigree Gramplet - detached example]]

The Gramplet shows a compressed view of the active person's direct ancestors. It defaults to going back 100 generations. The names can be clicked to change the active person, right-click to edit the person. At the bottom of the Gramplet the number of people per generation is listed. Birth and death dates are shown next to each person's name. Double-click the Generation number to see the matching individuals in a Quick View report.

Using the content of the Pedigree in another program requires a bit of effort Open a contextual pop-up menu by right-clicking anywhere in the gramplet except a hotlink. Or, you can begin a drag selection from the same inert areas. Copy the highlighted text the OS clipboard from that same context menu. (The keybinding for 'Copy' will not work.) When you paste the text into another text editing program, you may need change the font to a non-proportional font to preserve the indentation. Some online services collapse leading spaces when you post a chunk of text. Preserving the indentation for such services may require replacing doubled spaces with doubled placeholder characters... like periods/full stops.

#### ⚙ Configurable Options

- 1 to 100 limit; (default: *100*) - Maximum generations to display.

-  (default: checkbox selected)

- - <abbr title="Unicode Transformation Format graphical symbols">**UTF**</abbr> (default)
  - <abbr title="American Standard Code for Information Interchange text symbols">*ASCII*</abbr>

### Python Evaluation

![[_media/PythonEvaluationGramplet-detached-example-60.png|Fig {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Python Evaluation Gramplet&quot; - detached example]] The Gramplet tool is intended to test Python scripts with Gramps data.

#### Example usage

Sample code for listing Gramps internal "[constants](https://github.com/gramps-project/gramps/blob/master/gramps/gen/const.py)":

    import os
    import sys
    from gramps.gen.const import *

    # Get all uppercase variables from the current namespace
    ENV = {
        name: value for name, value in locals().items()
        if name.isupper() and not name.startswith('_') and isinstance(value, str)
    }

    # Print each item in the dictionary, indicating if it's a hidden directory
    for key, value in ENV.items():
        try:
            if os.path.isdir(value):
                if sys.platform.startswith('win'):
                    import ctypes
                    attrs = ctypes.windll.kernel32.GetFileAttributesW(value)
                    hidden_status = "HIDDEN" if attrs != -1 and bool(attrs & 2) else "NOT HIDDEN"
                else:
                    hidden_status = "HIDDEN" if os.path.basename(value).startswith('.') else "NOT HIDDEN"
                print(f"({hidden_status})    {key}  :    {value}")
            else:
                print(f"{key}  :    {value}     (NOT A DIRECTORY)")
        except Exception as e:
            print(f"{key}  :    {value}     (ERROR :    {str(e)})")

#### See Also

- [Python Shell](wiki:Addon:Python_Shell_Gramplet) addon gramplet. Where possible, use the **Python Shell** instead of **Python Eval**. It has extra garbage collection functionality
- Debug submenu in the [Tools](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Tools) menu before version 4.0.2
- [Gramps-devel](wiki:Contact#Mailing_lists) maillist: [Converting tools to gramplets](https://sourceforge.net/p/gramps/mailman/gramps-devel/thread/524D973D.9000604%40hotmail.com/#msg31477962) - Oct 2013
- Discourse -- Sample scripts:
  - [sample script to Parse selected JSON to CSV](https://gramps.discourse.group/t/need-some-json-parsing-tools/6855/7)
  - [troubleshooting Gramps paths and environmental variables](https://gramps.discourse.group/t/troubleshooting-gramps-paths-and-environmental-variables/5692)
- [Command Line: Python options](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line#Python_options)
- [Uncollected Objects](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Uncollected_Objects) Gramplet

{{-}}

### Quick View

![[_media/QuickView-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Quick View Gramplet - detached example]]

The Gramplet allows the selected [Quick View report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Quick_Views) to be updated dynamically as active records are changed. Instead of a window with a static report, the gramplet updates as different active records are selected within the target Category. (When this Gramplet was introduced, it only offered choosing Quick View Reports from the People category. A Configuration pop-up menu to select View categories has since been added.)

You can run any of the builtin [Quick Views](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Quick_Views) or [addon](wiki:6.0_Addons#Addon_List) QuickView reports. {{-}} ![[_media/QuickView-Gramplet-Configuration-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Quick View Gramplet - Configuration tab shown]]

You can change the options by clicking the Option button (top, left hand button of the Gramplet) which will detach the Gramplet and bring it up an a window. Select on the top row, and a list of options will appear. Press to apply the changes to the Quick View. You may then close the window to reattach the Gramplet.

{{-}} See the following developer information if you are interested in creating your own:

- [Making your own Quick Views](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8#Making_your_own_Quick_Views).

{{-}}

### Records

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

### References

![[_media/References-Gramplet-detached-50.png|Fig {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} References Gramplet - detached example]] Gramplet showing the active persons References.

{{-}}

#### Person References

- Person References : Gramplet showing the backlink references for a person

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) {{-}}

#### Family References

- Family References : Gramplet showing the backlink references for a family

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) {{-}}

#### Event References

- Event References : Gramplet showing the backlink references for an event

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) {{-}}

#### Place References

- Place References : Gramplet showing the backlink references for a place

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) {{-}}

#### Source References

- Source References : Gramplet showing the backlink references for a source

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) {{-}}

#### Citation References

- Citation References : Gramplet showing the backlink references for a citation

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) {{-}}

#### Repository References

- Repository References : Gramplet showing the backlink references for a repository

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) {{-}}

#### Media References

- Media References : Gramplet showing the backlink references for a media object

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) {{-}}

#### Note References

- Note References : Gramplet showing the backlink references for a note

See [References](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#References) {{-}}

### Relatives

![[_media/Relatives-Gramplet-detached-example-60.png|Fig {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Relatives Gramplet - detached example]]

Use the Gramplet to show all direct relatives of the active person. It is intended to be used as a navigation help, an alternative way to move through your family tree in Gramps . If you detach the Gramplet, and place it next to Gramps, it will allow you to use it to easily change the content of the current "Person view".

If you are working in the charts category Pedigree view, the active person is the left-most person. By clicking a name in the relatives Gramplet, you can easily change the active person, and all person view in the other window will update. As the relatives Gramplet shows all spouses, all children and all parents, this offers an alternative way of navigating your data.

The names in this Gramplet also allow you to call up the person editor directly, by right-clicking on any of the names.

The Relatives Gramplet can be added to the following categories:

- People Category
- Relationships Category
- Charts Category
- Geography Category (selected views only)

{{-}} See also:

- Gramplet - ancestors of the active person navigation aid.

### Residence

![[_media/ResidenceGramplet-Person-detached-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Person - Residence Gramplet - detached - example]]

Gramplet showing residence events for the active person {{-}}

#### Person Residence

See [Residence](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Residence) {{-}}

### Session Log

![[_media/SessionLog-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Session Log Gramplet - detached example]]

The session log keeps track of activity in this session. It lists selected and edited objects.

Click a name once to make this person the active person. Double-click on a name or family brings up the page for that object. In addition, if you want to edit a person, but don't want to change the active person, you can right-click on the person's name.

This Gramplet is handy because you can very quickly change the active person, or edit the object, from the session list.

- [Using Undo History](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Using_Undo_History)\]

{{-}}

### SoundEx

![[_media/SoundEx-Gramplet-detached-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} SoundEx Gramplet - detached example showing context menu]]

The generates SoundEx codes for the names of people in the Family Tree.

From the window you can either choose a from the pop-up menu shown by selecting the down arrowhead, (triangle) or you can type a name into the text field.

The name you type in can be any name... even a name not present in your Family Tree.

The field shows the result automatically eg: The SoundEx code for *Simpson* is *S512*

You can right click on the field to copy the result.

A button is available which brings you to this page. With the button (or using the keyboard shortcut ) you dismiss the window. {{-}}

##### Soundex what is this?

Soundex is the most widely known of all [phonetic algorithms](https://wikipedia.org/wiki/Phonetic_algorithm) which allow indexing of words by their sound, as pronounced in English. Soundex support is included with searching via a [Soundex match of People with the &lt;name&gt;](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Soundex_match_of_People_with_the_.3Cname.3E) Custom Filter rule, a [Soundex Gramplet](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#SoundEx), and as a quality control for matching in the [Find Possible Duplicate People](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Find_Possible_Duplicate_People) tool.

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

### Statistics

![[_media/Statistics-Gramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Statistics Gramplet - detached example]]

The Gramplet runs a Statistics report. Double-click the phrases to bring up the matching items Quick View reports.

Following information is provided to you in this Gramplet:

- **Individuals**
  - Number of individuals
  - Males
  - Females
  - Individuals with other gender
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

The information given in this Gramplet is the same as in the [Database Summary Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Database_Summary_Report) and similar to the result from the dialog. {{-}}

#### Quick Views

### Surname Cloud

![[_media/SurnameCloud-Gramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Surname Cloud Gramplet - detached example]]

The Surname Cloud Gramplet shows the top 150 (by default) used surnames. The name font size is proportional to the amount of people with the same name.

Double-click a surname to run the . This will open the window where you can find all people with a matching or alternate name. Person, birth date and name type are given.

If you mouse over the name you see the percentage of occurrence and total counts.

At the bottom of the gramplet you are shown:

- Total unique surnames:
- Total surnames showing:
- Total people:

Using the context menu you can select the text and copy it elsewhere. {{-}} ![[_media/SurnameCloud-Gramplet-Configuration-tab-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Surname Cloud Gramplet - Configuration tab shown]]

You can change the number of surnames displayed as well minimum and maximum font sizes by configuring the view for this gramplet. {{-}}

#### Quick View

<span id="Person To Do"></span><span id="Family To Do"></span><span id="Event To Do"></span><span id="Place To Do"></span><span id="Source To Do"></span><span id="Citation To Do"></span><span id="Repository To Do"></span><span id="Media To Do"></span>

### To Do

![[_media/ToDo-Gramplet-detached-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} To Do Gramplet - detached example]] The **Gramplet** displays a free form text area showing the contents of Note objects of the "To Do" type. The Type of To Do note is filtered to the current category.

You can use this area to put some notes, remarks, things you should to get your research going. There are several other To Do programs (e.g. [Tomboy](https://github.com/tomboy-notes/tomboy-ng) e.a.) but these Gramplets are useful as the information stays within the Gramps database.

To Do Gramplets allow you to create notes and attach them to Gramps objects. For example, you can add a Person To Do Gramplet to the sidebar of the Person View. Notes added using this Gramplet will be attached to the currently active person. There is a To Do Gramplet for each Gramps primary object type. {{-}} See also the [Third-party Addon](wiki:Third-party_Addons):

- [ToDo Notes Gramplet](wiki:Addon:ToDoNotesGramplet) available for the Dashboard that lists all To Do notes in the database, together with the object to which they are attached.

{{-}}

### Top Surnames

![[_media/TopSurnames-Gramplet-detached-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Top Surnames Gramplet - detached example]]

The Gramplet shows a list of the top 10 (by default) used surnames and is installed by default on the Dashboard category view.

The top ten is presented as follows:

- Surname
- percentage
- occurrences

The list gives you also the Total unique surnames in the database as well as the total number of people in your database.

Double-click a surname to run the . This opens the window, which gives the people with the surname you double-clicked.

A table is presented which shows all people with a matching name or alternate name. Person's name, ID, birth date and name type is given. {{-}}

{{-}}

### Uncollected Objects

![[_media/UncollectedObjects-Gramplet-detached-example-60.png|Fig {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Uncollected Objects Gramplet" - detached example]]

The Gramplet is intended to list the low-level Python objects that are left around in memory and cannot be (easily) automatically deleted when they are no longer in use. Developers use it to try to identify the source of memory 'leaks', which cause Gramps to continually use more and more memory, the longer it is used.

Because the tool is trying to display objects that might still be getting deleted, it sometimes has some trouble.

To use select the button and if any results; they will be shown in the list that shows the following columns; `Number`, `Referrer`, `Uncollected object`

Also See:

- [Command Line: Python options](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line#Python_options)
- [Python Evaluation](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Python_Evaluation) Gramplet

{{-}}

### Welcome

![[_media/Welcome-to-Gramps-Gramplet-detached-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Welcome Gramplet - detached example]]

The **Welcome to Gramps!** Gramplet gives an introductory message to new users, and some basic instructions and is installed by default on the Dashboard category view.

The welcome message describes what Gramps is, that the program is Open Source Software and how you start a [Family Tree](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees). {{-}}

### What's Next

![[_media/WhatsNext-Gramplet-detached-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} What's Next? Gramplet - detached example]]

The **** Gramplet displays a list of the "most urgent" information gaps in your family tree. It is based on the following assumptions:

- The [Home Person](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Setting_the_Home_Person) defines the focus
- Searches for gaps. The search begins with the Home Person's descendants and works up the tree
- The record for each person is expected to contain: the given name, surname, birth (with date and place), and death (with date and place)
- You want to know parents, their marriage (with date and place), and - if divorced - divorce date and place of each family with married parents
- You want to know at least the mother of each family with unmarried parents
- The closer the relationship to the Home Person, the more "urgent" the information gap is.
- The closer the common ancestor is from the main person, the more "urgent" the information is (e.g. nephews are considered more "urgent" than uncles, even though both have a distance of 3 generations, because for nephews the common ancestor is father/mother, while for uncles, the common ancestor is grandfather/grandmother)
- Marriage data and personal data of the spouse is slightly less "urgent" than personal data of the directly related person
- Half-siblings are less "urgent" than siblings

You may copy the text from inside of this Gramplet by selecting it and pasting into an empty document. {{-}}

#### ⚙ Configurable Options

![[_media/WhatsNext-Gramplet-Configuration-tab-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} What's Next? Gramplet - Configuration tab shown]]

The Gramplet can ignore previously verified events by making use of some custom Tags. The tags are selected in the Gramplets configuration. For example you can tag the following to be ignored:

- that a person is complete
- that a family is complete
- that a person or family should be ignored for shortening lists

{{-}}

[Category:Documentation](wiki:Category:Documentation)
