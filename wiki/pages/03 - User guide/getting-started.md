---
title: Gramps 6.0 Wiki Manual - Getting started
categories:
- Documentation
managed: false
source: wiki-scrape
wiki_revid: 120359
wiki_fetched_at: '2026-05-30T11:29:46Z'
---

{{#vardefine:chapter\|2}} {{#vardefine:figure\|0}} In this section, we'll begin with the basics. First, we'll describe the basic concepts in Gramps. Then, we'll show you how to start Gramps and how to get help when you need it. \_\_FORCETOC\_\_

## Overview of Gramps

Gramps is a free, open source program that has been designed to be a flexible and powerful genealogy tool. It is a framework for collecting genealogical data, noting how each piece of data interrelates and presenting those relationships.

One can generally use Gramps any way one wishes. There is no single, correct method of working with or recording your data. However, if you wish to collaborate with other researchers or programs, it helps to conform to some common guidelines. Even if you are familiar with common genealogy research practices, you still need to understand how Gramps works. Then you can jump into how to use the Gramps program in a way that complements a particular genealogical research style.

Gramps separates all genealogical information into 9 primary categories of items:

- [People](wiki:Gramps_Glossary#person)

- [Families](wiki:Gramps_Glossary#family)

- [Events](wiki:Gramps_Glossary#event)

- [Places](wiki:Gramps_Glossary#place)

- [Sources](wiki:Gramps_Glossary#source)

- [Citations](wiki:Gramps_Glossary#citation)

- [Repositories](wiki:Gramps_Glossary#repository)

- [Media](wiki:Gramps_Glossary#media)

- [Notes](wiki:Gramps_Glossary#note)

Each of these is composed of stand-alone items. That means that you can enter into your family tree one item at a time, and in any order that you want. You can connect the items to one another or leave them disconnected (or even chaotically disorganized) but searchable. Or you can start with a Tree design in mind and fill it outwards, connecting new items as you go.

For example, you might want to enter each Person item first, and then connect them together by creating Family items later. Or, you can start with a Family, anchor the family by adding a new Person as a child or parent, then add relatives, events & source materials in the prepared slots of the Family framework. Or, you might start with Source items, and only create a Person item when your research includes a mention of someone. Or, you can mix these styles of entering data by adding some Note and Source items, then Family items, then later return to Notes and Sources. In short, you do your genealogical research however you wish.

If you have additional questions, Gramps has a community of users and developers. There is a [FAQ](wiki:Gramps_6.0_Wiki_Manual_-_FAQ) (frequently asked question list); a [mailing list](wiki:Contact#Mailing_lists); [a bug, feature request, and issue tracker](wiki:Using_the_bug_tracker); and you can interact using on-line [chat rooms](wiki:Contact#Chat_Room) or [community forums](wiki:Contact#Forum).

### Connections

These 9 primary items are connected in a number of ways. Some of these connections are maintained implicitly. For example, adding a Person item to a Family item as a parent, or child, automatically creates a special connection, called a **Reference**. You can see the Families a Person is connected to in the References tab on the main Person window. There are many other ways that these connections are also visualized in Gramps, including the Relationship View.

To keep from repeating information, Gramps allows you to reuse, or share, items. These are also special connections, called **links**. For example, a Person item can be linked to any number of Note items. If a note mentions two separate people, then it might make sense to share that single note with both of the person items.

Some links have information themselves. For example, you can link a person to another couple's marriage event, say, because the person was a witness at their wedding. However, the husband and wife are linked to the marriage event in a **primary** role, whereas a witness fills a different role, e.g. as a **witness**. This type of information is kept on the link itself, in the role property.

### Privacy

Gramps supports two different methods to protect the privacy of sensitive data in your family tree. These methods are used when sharing your data with others, either through the creation of a report, exporting of data, or through the creation of a website.

The first method protects information on people who Gramps believes are alive. If you have not specifically indicated that a person is dead (by adding a Death Event to a Person item), then Gramps has a sophisticated, automatic function for determining if someone is alive. Living people have their sensitive data redacted when using this method. For example, a person named "Smith, John" could appear as "Smith, \[Living\]".

The second privacy method is an explicit ["private" flag](wiki:Gramps_Glossary#private_tag) shown as a ![[_media/22x22-gramps-lock.png]]locked padlock when private, which you can set on each item. For example, you might have sensitive, personal information in a note. If you mark such a note as private, then that note will not be shown in textual and narrative reports or exports. Also be aware that some links themselves can be marked private. This is useful when you want to mark the connection from, say, a person to an event as private, but still have the person and the event available in the report, export, or website.

![[_media/Include-data-marked-private-checkbox-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Privacy overrides for Reports]]In order to activate these two methods of privacy, you will need to indicate their use when creating some reports or exporting your data. {{-}}

### GEDCOM

Gramps derives its core structure of items from a standard called GEDCOM. However, Gramps extends this standard where it has been deemed necessary. If you plan on using your family data with another system which uses GEDCOM, then you probably will want to try to restrict your use of features that are Gramps-only extensions. On the other hand, if you are not limited by other genealogical software, then you can enter your data in whatever ways make sense to you.

You can read more details about this issue in the section on [Gramps and GEDCOM](wiki:Gramps_and_GEDCOM).

## Start Gramps

The best way to learn Gramps is by working with your data. Let's get started!

The way you start Gramps depends on the operating system you are using.

As well as starting Gramps using the normal graphical user interface (GUI) as described below, it is also possible to start Gramps using a command line interface (CLI). CLI use can produce reports that are not available via the GUI, it can be used to create reports, do conversions etc. without opening a window, and can provide [extra information](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference#Seeing_all_the_error_messages) in the event of problems. For more information, see [the Command Line appendix](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line).

### Linux

Only the Linux platform is officially supported as Gramps developers use and test the source code on that platform, fixing any problems that arise due to upgrades.

Assuming you have used the standard Package Manager (either through a CLI or a GUI) for your Linux distribution, you will start Gramps in the normal way for your distribution. For example in Ubuntu 18.04, an icon is placed in the launcher, or the program can be started from Dash. For other distributions, an entry may be created in the Application menu (normally in the **Office** section).

Starting Gramps through the CLI on Linux is covered [here](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line#Linux).

### MS Windows

MS(Microsoft) Windows is a [community supported](wiki:Download#MS_Windows) platform. If you install the [Windows AIO](wiki:All_In_One_Gramps_Software_Bundle_for_Windows) GrampsAIO64 executable, then this will place an icon on the desktop as well as a menu item in the 'Start' menu, and you click on that to start Gramps.

Starting Gramps through the command line (CLI) on MS Windows is covered [here](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line#MS_Windows).

There are other ways to install Gramps for MS Windows, but these are much more complicated and are not covered here.

### macOS

Apple macOS (originally Mac OS X shortened as OS X) is a [community supported](wiki:Download) platform. If you download the macOS disk image (.dmg), then you simply drag the application to your application folder (or anywhere else you want to store it) and start Gramps by double clicking on the application in the normal way.

Starting Gramps through the CLI on macOS is covered [here](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line#macOS).

There are other ways to install Gramps for macOS, but these are much more complicated and are not covered here.

## Choosing a Family Tree

![[_media/Dashboard-category-view-first-open-no-family-tree-loaded-60.png|Fig {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dashboard Category View - First open of Gramps with no family tree loaded(Gramps 6.0.0; MS-Windows 10)]]

If Gramps is started without a family tree selected, the initial screen will have little functionality. Most operations will not be available. To load a family tree (also referred to as *database*), select in the menu to open the family tree manager, or click the icon in the toolbar. Gramps keeps track of your recently opened Family Trees, and these can be selected by clicking on the arrow next to the button and choosing from the drop down menu.

For more detailed information on the Family Tree manager and the Family Trees menu, see the chapter dedicated to this: [Manage Family Trees](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees).

{{-}}

## Tell me how to start right now!

We advise everyone to read the manual to learn all about using Gramps. Genealogy takes time, so learning the tools is time well used.

However, if you really want the bare minimum to start, then read this:

- [Gramps 6.0 Wiki Manual - Entering and editing data: brief](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_brief)
- [How-To start with Genealogy using Gramps](wiki:Start_with_Genealogy).

## Obtaining Help

Gramps has a menu that you can consult at any time.

- See the menu section.

{{-}}

[Category:Documentation](wiki:Category:Documentation)
