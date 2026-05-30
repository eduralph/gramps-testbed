---
title: Gramplets development
categories:
- Addons
- Developers/General
- Developers/Tutorials
- Gramplets
- Plugins
- Stub
managed: false
source: wiki-scrape
wiki_revid: 126836
wiki_fetched_at: '2026-05-30T18:11:35Z'
---

A **Gramplet** is a [type of Gramps plugin](wiki:Addon_list_legend#Type). Gramplets are mini-views designed to be composited with other Gramplets or Views to create a way to see your Family Tree that is just right for you. In fact, Gramplets can be made to do just about anything that you want.

![[_media/DashboardCategory-DashboardView-default-gramplets-60.png|Default Gramplets on Dashboard - With Example Family Tree Open]] ![[_media/Dashboard-category-view-first-open-no-family-tree-loaded-60.png|Default Gramplets on Dashboard - No Family Tree Loaded]]

# Gramplet Interface

Gramplet only operate after being added to a view. Add (or remove and restore) to the [sidebar or bottombar](wiki:Gramps_{{man_version}}_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar) of a view by clicking the (*Down Arrowhead* button) also known as the **Gramplet Bar Menu** at the far top right of the bars titles, and then using one of the options from the drop-down menu. In the Dashboard view, this menu is accessed by right-clicking in-between gramplets in the main view.

Gramplet can dramatically degrade the performance of Gramps. Some Gramplets consume huge amounts of memory, processor power and move a lot of data through storage. Don't keep a Gramplet active when it isn't being used!

When the view is not active or Gramplet tab is not the foremost in the splitbar, the Gramplet is inactive. A detached (undocked) Gramplet is always active.

The user interface for a Gramplet is left completely to the discretion of the developer. Detach/undock a Gramplet to reveal the "Help" button. Explore the Configure options after adding a Gramplet.

## Are Gramplets and 'plug-ins' the same thing?

There are many [types of plugins](wiki:Addon_list_legend#Type). The 6 most common are:

1.  **Reports**: output for printing or display
2.  **Tools**: a method for processing data
3.  **Quick View**: a list of details based on the current object
4.  **Importer**: reads a file into your current tree
5.  **Exporter**: writes a file from your current tree
6.  **Gramplets**: interactive views for moving, analysing, displaying, etc.

There are two plugin directories: a global/system one, and a private/personal one. You can easily create a plugin by simply putting a file in plugins folder of your [User Directory](wiki:Gramps_{{man_version}}_Wiki_Manual_-_User_Directory) (usually in *`.gramps/grampsxx/plugins/gramplet/`* ).

## Hello World

In teaching programming, a common "first program" is to write a program that says "Hello World".

Let us jump right in and take a look at such a gramplet named *HelloWorld.py*:

Create a python file named *HelloWorld.py* and add the following content:

    # File: HelloWorld.py
    def init(gui):
        gui.set_text("Hello world!")

And create another python file named *HelloWorld.gpr.py* with the following content:

    # File: HelloWorld.gpr.py
    register(GRAMPLET,
             id="Hello World Gramplet", 
             name=_("Hello World Gramplet"),
             description = _("a program that says 'Hello World'"),
             status = STABLE,
             version="0.0.1",
             fname="HelloWorld.py",
             height = 20,
             gramplet = 'init',
             gramplet_title=_("Sample Gramplet"),
             gramps_target_version="6.0",
             help_url="Sample Gramplet"
             )

You can read more about the gpr.py file in [Addons development](wiki:Addons_development#Create_a_Gramps_Plugin_Registration_file) and the [source code implementation](https://github.com/gramps-project/gramps/blob/master/gramps/gen/plug/_pluginreg.py).

If you place these files in **your personal [user plugins directory](wiki:Gramps_{{man_version}}_Wiki_Manual_-_User_Directory)** (usually in *.gramps/grampsxx/plugins/gramplet/* ), and then restart Gramps, you will be able to create this Gramplet. On the **Dashboard Category View**, right-click in an open area and select the "Hello World Gramplet". You should then see:

![[_media/HelloWorldGramplet-example-shown-embeded-on-DashboardCategory-60.png|Hello World Gramplet - example (shown embedded on Dashboard Category View / Context menu "Add a gramplet" also shown)]]

{{-}}

### Explanation

The main work of a Gramplet is performed in a function, or a class. In this very simple example, a function `init` is defined that takes a single argument, `gui`. The function simply sets the gui's text area to be "Hello World!", and that's it. It does this just once, and never changes.

Before a plugin can be used, it needs to be "registered". You call the register function with a number of named-arguments. There are a number of named-arguments that you can provide, including: name, height, content, title, expand, state, and data. We will explore those in detail, below.

## Hello World, with Class

Here is the same functionality again, but this time as a class:

    # File: HelloWorld2.py
    from gramps.gen.plug import Gramplet

    class HelloWorldGramplet(Gramplet):
        def init(self):
            self.set_text("Hello world!")

    # File: HelloWorld2.gpr.py
    register(GRAMPLET,
             id="Hello World2 Gramplet", 
             name=_("Hello World2 Gramplet"),
             description = _("a program that says 'Hello World'"),
             version="0.0.1",
             gramps_target_version="6.0",
             status = STABLE,
             fname="HelloWorld2.py",
             height = 20, 
             gramplet = 'HelloWorldGramplet',
             gramplet_title=_("Sample Gramplet"),
             help_url="6.0_Addons#Addon_List"
             )

This is the **recommended method** of creating a Gramplet. The following details describe the properties and methods of this class.

## Register Options

Gramps Plugin Registration attributes are defined in the [`gramps/gen/plug/_pluginreg.py`](https://github.com/gramps-project/gramps/blob/0f8d4ecd429431b4df64910962f8764af9ff1766/gramps/gen/plug/_pluginreg.py#L244) module.

- **`GRAMPLET`**: the first argument is the keyword GRAMPLET
- **`id`**: the identifying name of the gramplet, unique among all plugins
- **`name`**: the translated gramplet's name
- **`height`**: the minimum (or maximum) height of the gramplet in normal mode
- **`fname`**: the name of your gramplet file
- **`gramplet`**: the name of the function or class in fname that creates the gramplet
- **`gramplet_title`**: the default gramplet title; user changeable in *Configure View*
- **`status`**: STABLE or UNSTABLE for Gramps 5.1 version. EXPERIMENTAL, BETA
- **`audience`**: ALL, DEVELOPER, EXPERT
- **`version`**: a string with 2 dots (such as "1.23.14") representing the version number
- **`gramps_target_version`**: a string with 2 dots representing the version of Gramps for which this gramplet was written. Only gramplets matching the installed version will be available for installation.

At the bare minimum, you need to have the above 11 options when registering your Gramplets.

Optionally, you are encouraged to use the following, if known:

- **`detached_width`**: the size in pixels of the minimum and default detached height
- **`detached_height`**: the size in pixels of the minimum and default detached height
- **`expand`**: whether or not the Gramplet should expand to fill the column, if it can
- **`description`**: a description of the Gramplet
- **`authors`**: List (comma separated strings) of authors of the plugin, default=\[\]
- **`authors_email`**: List of emails of the authors (in the same order as the **`authors`** list) of the plugin, default=\[\]
- **`maintainers`**: List of maintainers of the plugin, default=\[\]
- **`maintainers_email`**: List of emails of the maintainers (in the same order as the **`maintainers`** list) of the plugin, default=\[\]
- **`navtypes`**: Restrict view to specific navigation tabs. Available options are "Dashboard", "Person", "Family", "Event", "Place", "Source", "Citation", "Repository", "Media", "Note"
- **`requires_mod`**: specifies python modules that the addon requires. If you want to allow Gramps to try to install a module using pip, then it should be pure python.
- **`requires_gi`**: specifies GObject introspection modules that are required. Gramps cannot install these
- **`requires_exe`**: specifies executables that must be present in the PATH. Again, the user must install these themselves
- **`help_url`**: the title of the wiki page that describes the plugin.  
  If the help_url starts with [`http://`](http://) (or the secure [`https://`](https://) ) then that fully qualified URL will be used as is. Otherwise, the paths will be interpreted as relative to `http://gramps-project.org/wiki/index.php?title=` base URL. The base URL will be prepended to the **help_url** and may get a language extension (such as `/nl` ) appended at the end, if the operating language is one of **nl** **fr** **sq** **mk** **de** **fi** **ru** **sk**. You should ***not*** use the `_(` `)` translate function around the **`help_url`** string, unless you specifically intend to create web pages named with the translated string.

## Core Methods

The class-based gramplet utilizes the following methods:

- **`init()`**: run once, on construction
- **`main()`**: run once per update
- **`update()`**: don't change this, it calls main
- **`active_changed()`**: run when active-changed is triggered
- **`db_changed()`**: run when db-changed is triggered
- **`set_tooltip(TEXT)`** - tooltip for gramplet

Don't call main directly; use the update method.

In the `db_changed` method, you should connect all of the signals that will trigger an update. That typically looks like:

        def db_changed(self):
            self.dbstate.db.connect('person-add', self.update)
            self.dbstate.db.connect('person-delete', self.update)
            self.dbstate.db.connect('person-update', self.update)
            self.dbstate.db.connect('family-add', self.update)
            self.dbstate.db.connect('family-delete', self.update)
            self.dbstate.db.connect('family-update', self.update)

The method `main()` can be written as a normal Python method, or it can be written to run nicely in parallel with other Gramps code. To make it run nicely in parallel, you should issue a **`yield True`** every once in a while. For example:

        def main(self):
            for i in range(5000):
                if i % 500 == 0:
                    yield True
            yield False

The **True** means that there is more to do; **False** means that there is nothing left to do.

### See also

- [**`DisplayState(Callback)`**](https://github.com/gramps-project/gramps/blob/d84282c496385ffc874d90a692f7d2628d314be7/gramps/gui/displaystate.py#L422) class for additional signals. (Including Custom Filters, Gramplet display and other updates.)

## Textual Output Methods

The most common kinds of Gramplets are text-based. There are a number of methods to assist with handling this text.

- **set_text(TEXT)** - clear and set text to TEXT
- **append_text(TEXT, scroll_to=POSITION)**
  - POSITION is 'begin' (top), 'end' (bottom) or 'start' (start of append)
- **clear_text()** - clears all text
- **set_use_markup(BOOLEAN-VALUE)**
- **render_text(TEXT)** - for use with A, B, I, U, and TT tags
  - A for creating links; use tag **HREF="url"** for URLs, and **WIKI="name"** for pages on the wiki
  - B for bold
  - I for italics
  - U for underlined
  - TT for a fixed-width, typewriter font
- **link(TEXT, LINK-TYPE, DATA)** -
  - TEXT can be any text
  - LINK-TYPE is:
    - 'Person' - and DATA is a person handle
    - 'PersonList' - and DATA is a list of handles
    - 'Family' - and DATA is a family handle
    - 'Surname' - and DATA is a person
    - 'Given' -
    - 'Filter' - and DATA is either:
      - 'all people' -
      - 'males' - all males
      - 'females' - all females
      - 'people with unknown gender' - people marked as unknown
      - 'people with incomplete names' - people who have a missing surname or given name
      - 'people with missing birth dates' - people who have missing birth dates
      - 'disconnected people' - people with no parents and no children
      - 'all families' - all families
      - 'unique surnames' - list of all unique surnames
      - 'people with media' - people who have media
      - 'media references' - all of the media
      - 'unique media' -
      - 'missing media' - media for which the file does not exist
      - 'media by size' -
      - 'list of people'-
    - 'URL' - and DATA is a URL
    - 'WIKI' - and DATA is a wiki page
    - 'Attribute' - and DATA is an attribute (eg, 'Nickname')
- **no_wrap()** - turn word wrap off DEPRECATED
- **set_wrap(BOOL)** - change word wrap

### Using Tags

Tags are the manner in which you format the text.

       tag = self.gui.buffer.create_tag("fixed")
       tag.set_property("font", "Courier 8")
       ...
       start, end = self.gui.buffer.get_bounds()
       self.gui.buffer.apply_tag_by_name("fixed", start, end)
       self.append_text("", scroll_to="begin")

## GUI Interface

- [Widget Gramplet example](wiki:Gramplets_development#Widget_Gramplet_example)
- [Cairo Clock Example](wiki:Gramplets_development#Cairo_Clock_Example)

### Widget Gramplet example

Occasionally, you might have to dive down to the graphical objects that compose a Gramplet.

- gui
  - gui.buffer
  - gui.textview
  - **gui.get_container_widget()**

If you wanted to put an arbitrary gtk object into the main area of a Gramplet, then you need to replace the standard textview object with your own. Here is the basic structure:

    # File: Widget.py
    from gettext import gettext as _
    from gramps.gen.plug import Gramplet
    from gi.repository import Gtk

    class WidgetGramplet(Gramplet):
        def init(self):
            self.gui.WIDGET = ### Some Widget Constructor ###
            self.gui.get_container_widget().remove(self.gui.textview)
            self.gui.get_container_widget().add_with_viewport(self.gui.WIDGET)
            self.gui.WIDGET.show()

    # File: Widget.gpr.py

    register(GRAMPLET,
             id= "Widget Gramplet",
             name=_("Widget Gramplet"),
             description = _("Widget Gramplet example"),
             authors = ["John Smith","Sam Jones"],
             authors_email = ["jsmith@example.com","user@noemail.invalid"],
             height=100,
             expand=False,
             gramplet = 'WidgetGramplet',
             gramplet_title=_("Widget"),
             version = '0.0.1',
             gramps_target_version = "6.0",
             fname="Widget.py",
             )

#### Gramps 3.x and older

    # File: Widget.py
    from gettext import gettext as _
    from gramps.gen.plug import Gramplet
    import gtk

    class WidgetGramplet(Gramplet):
        def init(self):
            self.gui.WIDGET = ### Some Widget Constructor ###
            self.gui.get_container_widget().remove(self.gui.textview)
            self.gui.get_container_widget().add_with_viewport(self.gui.WIDGET)
            self.gui.WIDGET.show()

    # File: Widget.gpr.py
    register(GRAMPLET, 
             id= "Widget Gramplet", 
             name=_("Widget Gramplet"), 
             height=100,
             expand=False,
             fname="Widget.py",
             gramplet = "WidgetGramplet",
             gramps_target_version = "3.4",
             gramplet_title=_("Widget"),
             )

### Cairo Clock Example

![[_media/ClockGramplet-addon-dashboard-detached-example-60.png|Clock Gramplet - shown detached from Dashboard]]

In fact, with Python, GTK, and cairo, you can make your own widgets that do pretty much anything and look very nice.

Here is an example adding a Cairo Clock (which really keeps time)

- With GTK+3 & Gramps
  - Github code: \[<https://github.com/gramps-project/addons-source/tree/maintenance/gramps>/ClockGramplet ClockGramplet\]
  - Manual Download: \[<https://github.com/gramps-project/addons/blob/master/gramps>/download/ClockGramplet.addon.tgz?raw=true ClockGramplet.addon.tgz\]

{{-}}

## GUI Options

- **add_option(OPTION)**
  - OPTION is one of the menu options in [gramps/gen/plug/menu](https://github.com/gramps-project/gramps/tree/master/gramps/gen/plug/menu) eg:
    - NumberOption
    - EnumeratedListOption
    - StringOption
    - ColorOption
    - TextOption
    - BooleanOption
    - FilterOption
    - PersonOption
    - FamilyOption
    - NoteOption
    - MediaOption
    - PersonListOption
    - PlaceListOption
    - SurnameColorOption
    - DestinationOption
    - StyleOption
    - BooleanListOption
- **build_options()**
- **save_options()**
- **get_option_widget(TEXT)**
- **get_option(TEXT)**

## Predefined Properties

There are a number of preset properties:

- dbstate
  - dbstate.db
    - dbstate.db.connect(SIGNAL, METHOD)
    - dbstate.db.get_person_from_handle(HANDLE)
    - dbstate.get_active_person()
- uistate

## Persistence

- gui
  - gui.data
- **on_load()**
- **on_save()**
- **save_text_to_data()**
- **load_data_to_text()**

## Advanced Settings

- `force_update` : set True to have the gramplet update, even when minimized

Calling the `update()` method of a gramplet causes its `main()` method to be called repeatedly in the background until it returns False.

Most gramplets will contain a `main()` method that runs quickly and always returns False.

Gramplets that have more intensive processing will use the `main()` method as a generator which will be run multiple times in the background. It will return True until it has finished processing then it will return False.

This background task can be controlled with the `pause()` and `resume()` methods. Additionally there is an `interrupt()` method which will cancel execution of the background task, and `update_all()` which will run the entire task in the foreground immediately.

Gramplets that should be updated in response to changes in the database should connect to the appropriate signals.

Gramplets such as a news gramplet could be updated by adding a refresh button or running the `update()` method at regular intervals.

## Learning More

To learn more about writing a Gramplet, it is suggested to look at the existing Gramplets. You can see a complete list of the Gramplet source code here:

- [Gramps Master (development fork) Gramplets](https://github.com/gramps-project/gramps/tree/master/gramps/plugins/gramplet)
- **[Gramps 6.0 Gramplets](https://github.com/gramps-project/gramps/tree/maintenance/gramps52/gramps/plugins/gramplet)**
- [Gramps 5.2 Gramplets](https://github.com/gramps-project/gramps/tree/maintenance/gramps52/gramps/plugins/gramplet)
- [Gramps 5.1 Gramplets](https://github.com/gramps-project/gramps/tree/maintenance/gramps51/gramps/plugins/gramplet)
- [Gramps 5.0 Gramplets](https://github.com/gramps-project/gramps/tree/maintenance/gramps50/gramps/plugins/gramplet)
- [Gramps 4.2 Gramplets](https://github.com/gramps-project/gramps/tree/maintenance/gramps42/gramps/plugins/gramplet)
- [Gramps 3.4 Gramplets](https://github.com/gramps-project/gramps/tree/maintenance/gramps34/src/plugins)

Click on a filename, to view the source code of that Gramplet.

- [master/gramps/gen/plug/\_gramplet.py](https://github.com/gramps-project/gramps/blob/master/gramps/gen/plug/_gramplet.py) - Base class for non-graphical gramplet code.

# See also

- [CallbackManager](https://www.gramps-project.org/docs/gen/gen_utils.html?module-gramps.gen.utils.callback#gramps.gen.utils.callman.CallbackManager) - a key tool that enables event handling and function execution based on specific triggers or events of a tree database.
- [Callback](https://www.gramps-project.org/docs/gen/gen_utils.html?highlight=signals#module-gramps.gen.utils.callback) in `signals#module-gramps.gen.utils`
- [Addons development](wiki:Addons_development) - for Gramps 4.2 and later
  - [Addons development old](wiki:Addons_development_old) - for Gramps 3.2 to 4.1
- [Writing a plugin](wiki:Writing_a_plugin) - for Gramps version 3.2 and earlier
- Discourse support forum :
  - [How can I make a .gpr.py registration that is compatible with 4.x and 5,2](https://gramps.discourse.group/t/how-can-i-make-a-gpr-py-registration-that-is-compatible-with-4-x-and-5-2/5290)
  - [Add a Custom Filter to a Gramplet Configuration options](https://gramps.discourse.group/t/looking-for-an-example-of-a-gramplet-with-a-custom-filter-configuration-option/5967)

[*](wiki:Category:Addons) [Category:Developers/General](wiki:Category:Developers/General) [Category:Developers/Tutorials](wiki:Category:Developers/Tutorials) [Category: Plugins](wiki:Category:_Plugins) [Category:Gramplets](wiki:Category:Gramplets)
