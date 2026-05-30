---
title: Gramps 6.0 Wiki Manual - Plugin Manager
categories:
- Documentation
- Plugins
managed: false
source: wiki-scrape
wiki_revid: 121045
wiki_fetched_at: '2026-05-30T11:37:08Z'
---

{{#vardefine:chapter\|11}} {{#vardefine:figure\|0}} The dialog allows you to control how Gramps manages plugins and Third-party Addons. Gramps consists of a core plus many plugins. When Gramps starts, the core is loaded and only a limited number of plugins are loaded. This decreases the startup time and memory requirements of Gramps. Subsequently, many plugins are automatically loaded by Gramps as they are needed, so that many users will not need to be aware of the existence of plugins, or their delayed loading.

The dialog is available from the menu . Many of the features of the Plugin Manager are intended for developers, and the dialogues described below are those seen by developers. The features for normal users are noted below where they are different.

## Registration and loading

[Plugins](wiki:Gramps_6.0_Wiki_Manual_-_Plugin_Manager#Plugin_types) are either held locally on the computer and are known about by Gramps, when they are said to be **Registered**, or they are held on a remote computer and Gramps only knows their name, type and description, when they are said to be **Addons**.

When Gramps starts, information is automatically read about the local plugins, so that they become registered. The Addon Manager can be used to download remote Addons so that they too become registered.

Registered (i.e. local) plugins are **loaded** by Gramps in the following situations:

1.  they are automatically loaded at startup. Some plugin types are loaded at startup (e.g., non hidden views), some plugins can have a flag that forces load on startup,
2.  they are automatically loaded by virtue of the user clicking on a view or requesting a report,
3.  they are loaded by the user explicitly requesting load in the plugin manager,
4.  remote plugins are loaded at the same time as they are registered by using [Install Addons](wiki:6.0_Addons#Installing_Addons_in_Gramps) with the menu .

## Plugin Manager dialog

The dialog allows you to control how Gramps manages plugins and Third-party Addons there are two tabs for the dilaog:

- and

- 

### Registered Plugins

![[_media/PluginManager-RegisteredPlugins-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Registered Plugins" tab (developer mode)]]

Here you see a list of all plugins that Gramps has found. These are the plugins which are part of Gramps, as well as the plugins/addons found in the `gramps60/plugins` directory within the [Gramps User Directory](wiki:Gramps_6.0_Wiki_Manual_-_User_Directory). The type of plugin is shown in the first column.

You can show or hide a plugin by selecting a row and pressing the button. This is only useful for the User Plugins.

By selecting a row and double clicking or pressing the button you will be shown the dialog.

Use the button to exit. The button .... does?

In [developer mode](wiki:Gramps_6.0_Wiki_Manual_-_Plugin_Manager#User_mode_or_Developer_mode) two additional buttons are shown they are:

- \- Which will load the selected rows source code file in your associated text editor.

- \- Forces a reload the selected plugin/addon.

{{-}}

### Loaded Plugins

![[_media/PluginManager-LoadedPlugins-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Loaded Plugins" tab (developer mode)]]

Here you see a list of all plugins that have been attempted to be loaded. Normally, all views (such as the Relationship View) will be loaded, and all gramplets/reports/tools you have used will be loaded automatically.

If there was an error during the loading of a plugin, then the **Status** column will be shown in this tab. Double clicking a row showing a failure opens the dialog showing the error in detail. You can use this to contact the plugin author or the Gramps bug list.

Later if you decide that you do not like an Addon, you can mark it "hidden" and it will no longer show.

You can show or hide a plugin by selecting a row and pressing the button. This is only useful for the User Plugins.

By selecting a row and pressing the button you will be shown the dialog.

Use the button to exit.

In [developer mode](wiki:Gramps_6.0_Wiki_Manual_-_Plugin_Manager#User_mode_or_Developer_mode) two additional buttons are shown they are:

- \- Which will load the selected rows source code file in your associated text editor.

- \- Forces a reload the selected plugin/addon.

{{-}}

## Actions

### Hide/Unhide

The dialog can be used to hide or unhide plugins. Some menus will not display hidden addons, so that the addon cannot be selected. For example, if a Gramplet is hidden, then it will not appear in the context menu which appear when right clicking the background of the Gramplets main tab. However, hiding some addons (such as Relationships or Gramps Views) has no effect and may not even be allowed.

### Detailed Info dialog

![[_media/Detailed-Info-dialog-plugin-example-with-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Detailed Info" dialog - example with context menu]]

The dialog will display information about the selected plugin/Addon. A context menu is available to copy and paste information as required. You can use this to contact the plugin author or report an issue to the Gramps [bug tracker](wiki:Using_the_bug_tracker)

- *Plugin name:*
- *Description:*
- *Version:*
- *Authors:*
- *Email:*
- *Filename:*
- *Location:*

{{-}}

## Plugin types

There are two main categories of plugins in Gramps: **[User Plugins](wiki:Gramps_6.0_Wiki_Manual_-_Plugin_Manager#User_Plugins)** and **[System plugins](wiki:Gramps_6.0_Wiki_Manual_-_Plugin_Manager#User_Plugins)**. **User Plugins** are those that you use and control to provide different functionality for you. The **System Plugins** are used by Gramps.

There are many plugins that come with Gramps. However, anyone can also write a plugin and share it. These third-party plugins are called "addons". We highly encourage users and developers to share their creations with other Gramps users.

See also:

- [Addon_list_legend#Type](wiki:Addon_list_legend#Type)
- [Addons development](wiki:Addons_development)
  - [Addons_development#What_can_addons_extend.3F](wiki:Addons_development#What_can_addons_extend.3F)

### User Plugins

The following types of **User Plugins** are present in Gramps:

1.    
    Backends for which Gramps can write reports (pdf, odf, ascii text, ...)

2.    
    export formats you can export your data too via menu

3.    
    small programs you can embed in the Dashboard View, or detach and use as a normal window

4.    
    the views visible in the main window of Gramps

5.    
    import formats from which Gramps can import data via menu

6.    
    targets that can be used on the place view to go to an internet map service (*Go* toolbar button)

7.    
    know as *Quick Views* they are small reports that are available in the context menu on the listviews, or via the Quick View gramplet

8.    
    Textual or graphical reports Gramps can produce

9.    
    Tools you can start via the menu

### System Plugins

The following types of **System Plugins** are present in Gramps:

1.    
    Backends that allow Gramps to support [alternate database types](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Family_Tree).

2.    
    libraries that are present giving extra functionality.

3.    
    relationship calculators for different languages

4.    
    rules for custom filters

5.    
    Citation formatter

6.    
    thumbnail generation for previews of media

## User mode or Developer mode

Gramps detects whether it is being run in User mode or Developer mode by the 'optimise' [Python option](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line#Python_options) flag:

- `python -O gramps.py`

See [Debugging Gramps](wiki:Debugging_Gramps). {{-}}

[Category:Documentation](wiki:Category:Documentation) [Category:Plugins](wiki:Category:Plugins)
