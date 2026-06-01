---
title: Addons development
categories:
- Addons
- Developers/General
- Developers/Tutorials
- Gramplets
- Plugins
- Reports
managed: false
source: wiki-scrape
wiki_revid: 131082
wiki_fetched_at: '2026-05-30T18:10:32Z'
---

If you are developing a [Third-party Addon](wiki:Third-party_Addons); this page documents the API, methods, and best practices for Gramps 4.2 and later. Developers should review the overarching policy for [contributing to Gramps](wiki:Howto:_Contribute_to_Gramps).

## What can addons extend?

Addons for Gramps can extend the program in many different ways. You can add any of the following [types](https://github.com/gramps-project/gramps/blob/master/gramps/gen/plug/_pluginreg.py) of addons:

- **Importer** (IMPORT) - adds additional file format import options to Gramps
- **Exporter** (EXPORT) - adds additional file format export options to Gramps
- **[Gramplet](wiki:Gramps_Glossary#gramplet)** (GRAMPLET) - adds a new interactive interface section to a Gramps view mode, which can be activated by right-clicking on the dashboard View or from the menu of the Sidebar/Bottombar in the other view categories.
- **Gramps [View <em>(mode)</em>](wiki:Gramps_Glossary#viewmode)** (VIEW) - adds a new view mode to the list of views available within a [View Category](wiki:Gramps_Glossary#view)
- **[Map Service](wiki:Map_Services)** (MAPSERVICE) - adds new mapping options to Gramps
- **Plugin lib** (GENERAL) - libraries that are present giving extra functionality. Can add, replace and or modifies builtin Gramps options.
- **[Quickreport<strong>/</strong>Quickview](wiki:Gramps_{{man_version}}_Wiki_Manual_-_Reports_-_part_8#Quick_Views)** (QUICKREPORT) - a view that you can run by right-clicking on object, or if a person quickview, then through the Quick View Gramplet
- **[Report](wiki:Gramps_{{man_version}}_Wiki_Manual_-_Reports_-_part_1)** (REPORT) - adds a new output report / includes **Website** - output a static genealogy website based on your Gramps Family Tree data.
- **[Rule](wiki:Gramps_{{man_version}}_Wiki_Manual_-_Filters#Add_Rule_dialog)** (RULE) - adds new [filter](wiki:Gramps_Glossary#filter) rules.
- **[Tool](wiki:Gramps_{{man_version}}_Wiki_Manual_-_Tools)** (TOOL) - adds a utility that helps process data from your family tree.
- **Doc creator** (DOCGEN)
- **Relationships** (RECALC)
- **Sidebar** (SIDEBAR)
- **[Database](wiki:Database_Backends)** (DATABASE) - add support for another database backend.
- **Thumbnailer** (THUMBNAILER)
- **Citation formatter** (CITE)

## Writing an addon

Writing an addon is fairly straightforward if you have just a little bit of Python experience. And sharing your addon is the right thing to do. The general steps to writing an addon and sharing your own addons are:

1.  [Develop your addon](#Develop_your_addon)
2.  [Create a Gramps Plugin Registration file (.gpr.py)](#Create_a_Gramps_Plugin_Registration_file)
3.  [Invite translation of your addon](#internationalization) into multiple natural languages
4.  [Package your addon](#Package_your_addon)
5.  [Document your addon](#List_and_document_your_addon_on_the_wiki) and publish it to the addon list
6.  [Register your addon with the Plugin Manager](#List_your_addon_in_the_Gramps_Plugin_Manager)
7.  [Announce it on the Gramps Forum](#Announce_the_addon) - Let users know it exist and how to use it.
8.  [Support it through the issue tracker](#Support_it_through_issue_tracker)
9.  [Maintain the code](#Maintain_the_code_as_Gramps_continues_to_evolve) as Gramps continues to evolve

We'll now expand upon each of these steps individually.

## Develop your addon

The [addons-source](http://github.com/gramps-project/addons-source) repository holds the source code for the addons with branches holding the version for different gramps. If you are working on an addon for gramps for the current Gramps public release, be sure to use the maintenance/gramps git branch, as the default is master branch for the developmental pre-release. (Currently gramps 6.1, which is not the typical target for addons.)

Example commands are shown below referring to the public release rather than the master branch.

The developers are currently merging changes to the most recent maintenance branch into master as necessary, so you don't have to do anything for that unless you are in a hurry.

The [addons-source](http://github.com/gramps-project/addons-source) git repository has the following structure, with the code for each addon in its own folder:

- /addons-source
  - /*IndividualNameOfAddon1*
  - /*IndividualNameOfAddon2*
  - ...

The [addons](http://github.com/gramps-project/addons) git repository holds built versions of the addons for each release of Gramps, and has the following structure:

- /addons
  - [/gramps42](https://github.com/gramps-project/addons/tree/master/gramps42)
    - /download
    - /listings
  - [/gramps50](https://github.com/gramps-project/addons/tree/master/gramps50)
    - /download
    - /listings
  - [/gramps51](https://github.com/gramps-project/addons/tree/master/gramps51)
    - /download
    - /listings
  - [/gramps52](https://github.com/gramps-project/addons/tree/master/gramps52)
    - /download
    - /listings
  - \[<https://github.com/gramps-project/addons/tree/master/gramps> /gramps\]
    - /download
    - /listings

### Get a local copy of Gramps and its addons

These steps show how to download the addon sources.

1.  Get an <https://github.com/join> account if you don't already have one.
2.  Request GIT write access for the <https://github.com/gramps-project/addons-source> project by emailing the [gramps-devel mailing list](wiki:Contact#Mailing_lists)

See also [git introduction](wiki:Brief_introduction_to_Git) for instructions on installing git and getting basic settings configured. Also [Connecting to GitHub with SSH](https://help.github.com/articles/generating-an-ssh-key/) will help with setting up credentials for GitHub. To fully build and advertise a new addon will require local copies of the three repositories, the 'addons-source', 'addons' and the main Gramps source 'gramps'.

This wiki assumes that all three git repositories local locations are put into the same base directory and named with the repository names in order for the make.py script commands to work as shown. From the base directory, run the following commands to create a copy of each repository. If you want to use SSH;

`git clone git@github.com:gramps-project/addons-source.git addons-source`  
`git clone git@github.com:gramps-project/addons.git addons`  
`git clone git@github.com:gramps-project/gramps.git gramps`

or if you want to use the HTTPS protocol:

`git clone https://github.com/gramps-project/addons-source.git addons-source`  
`git clone https://github.com/gramps-project/addons.git addons`  
`git clone https://github.com/gramps-project/gramps.git gramps`

To switch to a local copy of the gramps maintenance branch:

`cd addons-source`  
`git checkout -b gramps`` origin/maintenance/gramps`

or to work in the master branch:

`cd addons-source`  
`git checkout -b gramps61 origin/master`

### Other prerequisites

- Gramps uses Python version 3.2 or higher. You must have at least that version installed. If you have installed Gramps 4.2 or higher on your Linux system already, then a sufficient version of Python will be present. If you have more than one version of Python installed, then you must use the correct version for these scripts. On some systems, both Python 2.x and 3.x are installed. It is possible that the normal invocation of `python` starts up Python 2.x, and that to start up Python 3.x requires invoking with `python3` or `python3.4` etc. You can test the version by `python –version` or `python3 –version`. If this is so, replace any usage of 'python' in the examples below with the appropriate invocation.
- The make.py used in construction of the addons requires that the LANGUAGE environment variable be set to 'en_US.UTF-8'.
- The make.py used in construction of the addons requires that the GRAMPSPATH environment variable be set to your path to the Gramps source tree.
- intltool must be installed;

  
`sudo apt-get install intltool`

For example if your home directory is '/home/name' and you use the suggested path names, use

  
`GRAMPSPATH=/home/name/gramps LANGUAGE='en_US.UTF-8' python3 make.py ...`

to replace the `./make.py` in the examples below.

### Create your addon subdirectory

- Make a new project directory in addons-source:

  
`mkdir NewProjectName`

### Follow the development API for your tool

Create your NewProjectName.py and NewProjectName.gpr.py files.

Follow the development API for your tool, [report](wiki:Report-writing_tutorial), view, or [Gramplets development](wiki:Gramplets_development). Place all of your associated .py, .glade, etc. files in this directory. For general information on Gramps development see [Portal:Developers](wiki:Portal:Developers) and [Writing a Plugin](wiki:Writing_a_plugin) specifically.

### Test your addon as you develop

To test your addon as you develop it is suggested that you copy your NewProjectName plugin into your Gramps user plugin directory from your addon development directory, prior to testing. Or just edit in the Gramps user plugin directory until it is ready to publish, then copy back to your addon development directory.

Your installed Gramps will search this folder (and subdirectories) for .gpr.py files, and add them to the plugin list.

If you have code that you want to share between addons, you don't need to do anything special. Gramps adds each directory in which a .gpr.py is found onto the PYTHONPATH which is searched when you perform an import. Thus "import NewProjectName" will work from another addon. You should always make sure you name your addons with a name appropriate for Python imports.

### Commit your changes

To commit your changes so that others can see your addon source.

- Remove the files using the *clean* command that should not be added to GitHub (eg files(template.pot/ locale etc)):

  
`./make.py gramps`` clean NewProjectName`

- Add the project to the repository:

  
`git add NewProjectName`

- Commit it with an appropriate message

  
`git commit -m "A message describing what this addon is"`

Before committing additional edits to your addon, you should:

- to make sure that outside changes do not affect your commit

  
`git pull --rebase`

- only the files you changed should be in this list

  
`git status`

- Commit it with an appropriate message

  
`git commit -m "A message describing the changes"`

If you have been given 'push' rights to GitHub 'gramps-project/addons-source', and when you are sure you are done and want to publish to the repository:

- to make sure that outside changes do not affect your commit

  
`git pull --rebase`

`git push origin gramps`

Also you may want to [Package your addon](wiki:Addons_development#Package_your_addon) so it can be downloaded via the plugin manager.

### Config

Some addons may want to have persistent data (data settings that remain between sessions). You can handle this yourself, or you can use Gramps' builtin configure system.

At the top of the source file of your addon, you would do this:

`from config import config as configman`  
`config = configman.register_manager("grampletname")`  
`# register the values to save:`  
`config.register("section.option-name1", value1)`  
`config.register("section.option-name2", value2)`  
`...`  
`# load an existing file, if one:`  
`config.load()`  
`# save it, it case it didn't exist:`  
`config.save()`

This will create the file "grampletname.ini" and put in the same directory as the addon. If the config file already exists, it remains intact. The natural location for `.ini` files would be in the directory in which the addon is installed. (Using the main `gramps.ini` file for addon preferences could potentially lead to a conflict between addons.) Other locations and file formats are possible. [The Gramps architect recommends leaving this decision to the addon developer](https://gramps.discourse.group/t/add-option-for-boolean-options-in-gramplet/6371/19).

In the addon, you can then:

`x = config.get("section.option-name1")`  
`config.set("section.option-name1", 3)`

and when this code is exiting, you might want to save the config. In a Gramplet that would be:

`def on_save(self):`  
`    config.save()`

If your code is a system-level file, then you might want to save the config in the Gramps system folder:

`config = configman.register_manager("system", use_config_path=True)`

This, however, would be rare; most .ini files would go into the plugins directory.

In other code that might use this config file, you would do this:

`from config import config as configman`  
`config = configman.get_manager("grampletname")`  
`x = config.get("section.option-name1")`

### Localization

For managing translations that will be packaged with your addon (including extraction, gettext initialization, string marking, and `make.py` compilation), please see the dedicated [Addon Internationalization](wiki:Gramps_6.0_Wiki_Manual_-_Addon_Development_-_Internationalization) guide.

For general help on translating the core application, see [Translating Gramps](wiki:Translating_Gramps) and [Coding for translation](wiki:Coding_for_translation).

### Report plugins

The possible report categories are ([gen/plug/\_pluginreg.py](https://github.com/gramps-project/gramps/blob/892fc270592095192947097d22a72834d5c70447/gramps/gen/plug/_pluginreg.py#L141-L149)):

    #possible report categories
    CATEGORY_TEXT       = 0
    CATEGORY_DRAW       = 1
    CATEGORY_CODE       = 2
    CATEGORY_WEB        = 3
    CATEGORY_BOOK       = 4
    CATEGORY_GRAPHVIZ   = 5
    CATEGORY_TREE       = 6
    REPORT_CAT          = [ CATEGORY_TEXT, CATEGORY_DRAW, CATEGORY_CODE,
                            CATEGORY_WEB, CATEGORY_BOOK, CATEGORY_GRAPHVIZ, CATEGORY_TREE]

Each report category has a set of standards and interface. The categories CATEGORY_TEXT and CATEGORY_DRAW use the Document interface of Gramps. See also [Report API](wiki:Report_API) for a draft view on this.

The application programming interface or API for reports is treated at [Report-writing_tutorial](wiki:Report-writing_tutorial). For general information on Gramps development see [Portal:Developers](wiki:Portal:Developers) and [Writing a Plugin](wiki:Writing_a_plugin) specifically.

### General plugins

The plugin framework also allows you to create generic plugins for use. This includes the ability to create libraries of functions, and plugins of your own design.

#### Example: A library of functions

In this example, a file name library.py will be imported at time of registration (when Gramps starts):

    # file: library.gpr.py

    register(GENERAL, 
       id    = 'My Library',
       name  = _("My Library"),
       description =  _("Provides a library for doing something."),
       version = '1.0',
       gramps_target_version = '6.0',
       status = STABLE,
       fname = 'library.py',
       load_on_reg = True,
      )

The code in the file library.py will be imported when Gramps begins. You can access the loaded module in other code by issuing an "import library" as Python keeps track of files already imported. However, the amount of useful code that you can run when the program is imported is limited. You might like to have the code do something that requires a dbstate or uistate object, and neither of these is available when just importing a file.

If "load_on_reg" was not True, then this code would be unavailable until manually loaded. There is no automatic mechanism in Gramps to load GENERAL plugins automatically.

In addition to importing a file at startup, one can also run a single function inside a GENERAL plugin, and it will be passed the dbstate, the uistate, and the plugin data. The function must be called "load_on_reg", and take those three parameters, like this:

    # file: library.py

    def load_on_reg(dbstate, uistate, plugin):
        """
        Runs when plugin is registered.
        """
        print("Hello World!")

Here, you could connect signals to the dbstate, open windows, etc.

Another example of what one can do with the plugin interface is to create a general purpose plugin framework for use by other plugins. Here is the basis for a plugin system that:

- allows plugins to list data files
- allows the plugin to process all of the data files

First, the gpr.py file:


    register(GENERAL, 
      id    = "ID",
      category = "CATEGORY",
      load_on_reg = True,
      process = "FUNCTION_NAME",
      )

This example uses three new features:

1.  GENERAL plugins can have a category
2.  GENERAL plugins can have a load_on_reg function that returns data
3.  GENERAL plugins can have a function (called "process") which will process the data

If you (or someone else) create additional general plugins of this category, and they follow your load_on_reg data format API, then they could be used just like your original data. For example, here is an additional general plugin in the 'WEBSTUFF' category:

    # anew.gpr.py

    register(GENERAL, 
      id    = 'a new plugin',
      category = "WEBSTUFF",
      version = '1.0',
      gramps_target_version = '6.0',
      data = ["a", "b", "c"],
      )

This doesn't have load_on_reg = True, nor does it have a fname or process, but it does set the data directly in the .gpr.py file. Then we have the following results:

    >>> from gui.pluginmanager import GuiPluginManager
    >>> PLUGMAN = GuiPluginManager.get_instance()
    >>> PLUGMAN.get_plugin_data('WEBSTUFF')
    ["a", "b", "c", "Stylesheet.css", "Another.css"]
    >>> PLUGMAN.process_plugin_data('WEBSTUFF')
    ["A", "B", "C", "STYLESHEET.CSS", "ANOTHER.CSS"]

### Registered GENERAL Categories

The following are the published secondary plugins API's (type GENERAL, with the following categories):

#### WEBSTUFF

A sample gpr.py file:

    # stylesheet.gpr.py

    register(GENERAL, 
      id    = 'system stylesheets',
      category = "WEBSTUFF",
      name  = _("CSS Stylesheets"),
      description =  _("Provides a collection of stylesheets for the web"),
      version = '1.0',
      gramps_target_version = '6.0',
      fname = "stylesheet.py",
      load_on_reg = True,
      process = "process_list",
      )

Here is the associated program:

    # file: stylesheet.py

    def load_on_reg(dbstate, uistate, plugin):
        """
        Runs when plugin is registered.
        """
        return ["Stylesheet.css", "Another.css"]

    def process_list(files):
        return [file.upper() for file in files]

#### Filters

For example:

    register(GENERAL,
       category="Filters",
       ...
       load_on_reg = True
    )

    def load_on_reg(dbstate, uistate, plugin):
        # returns a function that takes a namespace, 'Person', 'Family', etc.

        def filters(namespace):
            print("Ok...", plugin.category, namespace, uistate)
            # return a Filter object here
        return filters

<span id=internationalization>

## List the Prerequistes your addon depends on

''In your gpr file, you can have a line like:

`depends_on = ["libwebconnect"],`

which is a list of plug-in identifier's from other gpr files. This example will ensure that [libwebconnect](wiki:Addon:Web_Connect_Pack#Prerequisites) is loaded before your addon. If that ID can't be found, or you have a cycle (circular import), then your addons won't be loaded. The Gramps architect summarizes: "The depends_on list is used to specify other plugins which the plugin depends on. These will be installed automatically."

example code used in the Addon:Web_Connect_Pack that references libwebconnect Prerequistes [RUWebPack.gpr.py#L17](https://github.com/gramps-project/addons-source/blob/1304b65a7d758bfe17339c26260473ac3e9c4061/RUWebConnectPack/RUWebPack.gpr.py#L17)

This means that common Prerequisites can be shared between addons. So that code can be maintained in its own gpr/addon file instead of synchronizing the maintenance of multiple copies across various silos.

Additional requirements properties were implemented in the [Registration Options](wiki:Gramplets_development#Register_Options) to specify prerequisites for plug-ins: [requires_mod (modules), requires_gi (GObject introspection) and requires_exe (executable).](https://github.com/gramps-project/gramps/blob/0f8d4ecd429431b4df64910962f8764af9ff1766/gramps/gen/plug/_pluginreg.py#L689-L719)

## Get translators to translate your addon into multiple languages

</span> If you [designed for localization](#Localization), the addon will begin supporting a single language. Make your addon inviting for volunteers to translate it into their native language.

- Initialize and update the `template.pot` for your addon:

  
`cd ~/addons-source`

`./make.py gramps`` init NewProjectName`

- You should edit the header of `template.pot` with your information, so it gets copied to individual language files.
- Initialize a language for your addon (say French, fr):

  
`./make.py gramps`` init NewProjectName fr`

- Update it from gramps and other addons:

  
`./make.py gramps`` update NewProjectName fr`

- Edit the translations file manually:

  
`/NewProjectName/po/fr-local.po`

- Compile the language:

  
`./make.py gramps`` compile NewProjectName`

- Add or update your local language file, and commit changes:

  
`git add NewProjectName/po/fr-local.po`

`git commit NewProjectName/po/fr-local.po -m "Added fr po file"`

- If you have been given 'push' rights to GitHub 'gramps-project/addons-source', then;

  
`git push origin gramps`

## Package your addon

To create a downloadable package:

  
`./make.py gramps`` build NewProjectName` or

`./make.py gramps61 build NewProjectName` for the master branch.

This will automatically include the following files in your build:

- \*.py
- \*.glade
- \*.xml
- \*.txt
- locale/\*/LC_MESSAGES/\*.mo

Starting with Gramp 5.0, if you have additional files beyond those listed above, you should create a MANIFEST file in the root of your addon folder listing the files (or pattern) one per line, like this sample MANIFEST file. Include the Addon folder name in each line.

    Addon/README.md
    Addon/extra_dir/*
    Addon/help_files/docs/help.html

This will leave your 'addons-source' with untracked changes according to git. You should delete the 'NewProjectName/locale' directory. The updated 'NewProjectName/NewProjectName.gpr.py ' is ready to add and commit the next time you make other changes.

  
`rm –rf –v 'NewProjectName/locale'`

Then add the package to GitHub:

     cd '~/addons'
     git add gramps{{Stable_branch}}/download/NewProjectName.addon.tgz
     git commit -m "Added new plugin: NewProjectName"

or (for the master branch);

     cd '~/addons'
     git add gramps61/download/NewProjectName.addon.tgz
     git commit -m " Added new plugin: NewProjectName"

## List your addon in the Gramps Plugin Manager

To create a listing:

  
`cd '~/gramps-addons'` or wherever you have built your addon

`GRAMPSPATH=path/to/your/gramps/install ./make.py gramps`` listing NewProjectName`

or (for the master branch);

  
`cd '~/gramps-addons'` or wherever you have built your addon

`GRAMPSPATH=path/to/your/gramps/install ./make.py gramps61 listing NewProjectName`

That will create a series of files in the `../listings/` directory.

Then add the updated listing to GitHub:

     cd '~/addons'
     git add gramps{{Stable_branch}}/listings/*
     git commit -m "Added new plugin to listings: NewProjectName"

or (for the master branch);

     cd '~/addons'
     git add gramps61/listings/*
     git commit -m " Added new plugin to listings: NewProjectName"

## List and document your addon on the wiki

### List your addon

Add a short description of your addon to the Addons list by editing the current release listing eg: [6.0_Addons](wiki:6.0_Addons) or if the addon is meant for a future release [6.1_Addons](wiki:6.1_Addons) when available.

#### Example addon template

Examine the listing for other addons and refer to the [Addon list legend](wiki:Addon_list_legend) for details of on the meaning of each columns.

    |- <!-- Copy this section and list your Addon -->
    |<!-- Plugin / Documentation -->
    |<!-- Type -->
    |<!-- Image -->
    |<!-- Description -->
    |<!-- Use -->
    |<!-- Rating (out of 4) -->
    |<!-- Contact -->
    |<!-- Download -->
    |-

### Document your addon

Document the addon in the wiki using the page name format of examine the other addon support pages for the general format to use.

#### Example addon article

Consider including the following information:

    <!-- Copy this section to your Addon support page-->
    {{Third-party plugin}}<!-- This is a mediawiki template that expands out to display the standard addon message you see at the top of each addon page-->

    <!--sections only add if needed-->
    == Usage ==

    === Configure Options ===

    ==Features==

    == Prerequisites ==

    == Issues ==

    <!--default categories-->
    [[Category:Addons]]
    [[Category:Plugins]]
    [[Category:Developers/General]]

## Announce the addon

Join the [Gramps Forum](wiki:Contact#Forum) and announce it to the users with general information on why you created and how to use it.

## Support it through issue tracker

Become a user on the [Gramps MantisBT (Mantis BugTracker)](https://gramps-project.org/bugs/view_all_bug_page.php). and please check it regularly. There is no automated notification of issues (and possible feature requests) related to your addon when reported by users.

Users tend to not understand coding and they make assumptions. So be kind and guiding if a report is ambiguous or inaccurate. A negative remark from an addon developer or anyone can be very discouraging.

## Maintain the code as Gramps continues to evolve

Remember that Gramps addons exist for many reasons and there are many Gramps developers that do support addons in various ways (translations, triage, keeping in sync with master, download infrastructure, etc).

Some reasons why the addons exist; they provide:

- A quick way for anyone to share their work; the Gramps-project has never denied adding a addon.
- A method to continuously update and develop a stand-alone component, often before being officially accepted.
- A place for controversial plugins that will never be accepted into core, but are loved by many users (eg, Data Entry Gramplet).
- A place for experimental components to live.

## Example code adding common enhancements

- Copy all the Gramplet's output to a system clipboard via context pop-up menu : Enhancement request , [example pull](https://github.com/gramps-project/gramps/pull/1014/commits/72012e13b4ca15caca4b7f36fdb9702c1fd470fd)
- add a custom [View Mode](wiki:Gramps_Glossary#viewmode) toolbar icon via the `.gpr.py` : [Pull 1017 Discussion](https://github.com/gramps-project/gramps/pull/1017), [example Pull](https://github.com/gramps-project/gramps/pull/1017/commits/76e41d546d6ec519dd78fbe07f663135b5c79351)

# Resources

- [Git introduction](wiki:Brief_introduction_to_Git)
- [Getting started with Gramps development](wiki:Getting_started_with_Gramps_development)
- [Portal:Developers](wiki:Portal:Developers)
- [gramps.gen.plug.\_pluginreg Registration Module](https://gramps-project.org/docs/gen/gen_plug.html?highlight=include_in_listing#module-gramps.gen.plug._pluginreg)
- [PluginData in \_pluginreg.py](https://github.com/gramps-project/gramps/blob/master/gramps/gen/plug/_pluginreg.py#L55)

Gramps Addons site for Gramps 4.2 and newer  

- <https://github.com/gramps-project/addons-source> - Source code (Git)
- <https://github.com/gramps-project/addons> - downloadable .tgz files

Gramps Addons site for Gramps 4.1 and older  

- For 4.1.x and earlier, see [Addons development old](wiki:Addons_development_old).

# Addon Development Tutorials and Samples

- [Develop an Addon Gramplet](wiki:Gramplets_development) example code:
  - of a [custom filtering option](https://gramps.discourse.group/t/looking-for-an-example-of-a-gramplet-with-a-custom-filter-configuration-option/5967))
  - toolbar: Photo Tagging gramplet - [documentation](wiki:Addon:Photo_Tagging_Gramplet#Toolbar) ([source](https://github.com/gramps-project/addons-source/blob/bd1ce5cceb8b8a24ae5b612f311db42dfa0ed679/PhotoTaggingGramplet/PhotoTaggingGramplet.py#L233))
- [Develop an Addon Rule](wiki:Develop_an_Addon_Rule) for custom filters
- [Develop an Addon Tool](wiki:Develop_an_Addon_Tool)
- [Develop an Addon Quick View](wiki:Quick_Views)
- Develop an Addon Report ([tutorial](wiki:Report-writing_tutorial), [samples](https://gramps.discourse.group/t/sample-report-for-new-developers/3046))
- [Adapt a builtin Report](wiki:Adapt_a_builtin_Report)

[Category:Developers/General](wiki:Category:Developers/General) [Category:Developers/Tutorials](wiki:Category:Developers/Tutorials) [Category:Plugins](wiki:Category:Plugins) [Category:Reports](wiki:Category:Reports) [Category:Gramplets](wiki:Category:Gramplets) [*](wiki:Category:Addons)
