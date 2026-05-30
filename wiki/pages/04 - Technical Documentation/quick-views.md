---
title: Quick Views
categories:
- Developers/General
- Developers/Tutorials
- Plugins
- Reports
- Views
managed: false
source: wiki-scrape
wiki_revid: 126284
wiki_fetched_at: '2026-05-30T18:11:54Z'
---

![[_media/QuickViewReport-EditPerson-context-menu-popup-default-60.png|Quick View context menu on Person Editor]]

**Quick Views** (previously called *Quick reports* but show up in "Available Gramps Update for Addons" as *Quickreport*) are reports that are available in the context menu's of person, family, et cetera. There are a set of [builtin Quick Views](wiki:Gramps_{{man_version}}_Wiki_Manual_-_Reports_-_part_8#Quick_Views) that can be expanded with addon QuickView type plugins.

People with limited coding knowledge should be able to make them.

## Introduction

Many users want to produce a report quickly for their specific needs, but are hindered by the fact they do not want to learn Python fully, nor the intricacies of a complicated program like Gramps.

For them, a tool was constructed and introduced in Gramps 3.0:

- the  - short textual reports that the user can register with Gramps, so they automatically appear in the context menu's.

Accompanying this, a [simple database access](wiki:Simple_Access_API) and simple document interface has been constructed, so as to hide as much complexity as possible.

## Where to store my Quick View

A Quick View is normally composed of two files in its own subdirectory, that are stored under your *[User](wiki:Gramps_{{man_version}}_Wiki_Manual_-_User_Directory)* plugins directory. Go into your home folder and go to the hidden subdirectory **.gramps**. In this directory you will find the **plugins** subdirectory. Just add your plugin there, and it will appear within Gramps.

For the terminal users, you can get there as follows:

`cd ~/.gramps/grampsxx/plugins`

- See [Wiki Manual Appendix D - User Directory](wiki:Gramps_{{man_version}}_Wiki_Manual_-_User_Directory)

## Examples

How better than to learn something than by example?

### Example 1

#### Code

![[_media/PersonView-PeopleListView-example-with-context-menu-60.png|Quick View context menu on Person View]] ![[_media/QuickViewReport-Siblings-example-60.png|Quick View Report example result output]]

Here it goes. We want a report to show all siblings of a person.

That is, brothers and sisters from **all** families the person is part of.

The Quick Views report then needs the following folder and files to be created:

- Create a folder named: `siblings2` located in the [Gramps user plugins folder](#Where_to_store_my_Quick_View).
  - [<code>siblings2.gpr.py</code>](#siblings2.gpr.py)
  - [<code>siblings2.py</code>](#siblings2.py)

<span id="siblings.gpr.py"></span>

##### siblings2.gpr.py

You first need a Gramps registration (`*.gpr.py`) file so create a python file named `siblings2.gpr.py` and add the following content:

    #------------------------------------------------------------------------
    # File: siblings.gpr.py
    #------------------------------------------------------------------------

    register(QUICKREPORT, 
        id    = 'siblings2',
        name  = _("Siblings2 - Example Quick View"),
        description =  _("Display a person's siblings."),
        version = '0.1',
        gramps_target_version = '6.0',
        status = STABLE,
        fname = 'siblings2.py',
        authors = ["Your Name Here"],
        authors_email = ["Your @ Email address here"],
        category = CATEGORY_QR_PERSON,
        runfunc = 'run'
      )

<span id="siblings.py"></span>

##### siblings2.py

Now create a python file named `siblings2.py` and add the following content:

    #------------------------------------------------------------------------
    # File: siblings2.py
    #------------------------------------------------------------------------

    from gramps.gen.simple import SimpleAccess, SimpleDoc
    from gramps.gui.plug.quick import QuickTable
    from gramps.gen.const import GRAMPS_LOCALE as glocale
    _ = glocale.translation.gettext

    def run(database, document, person):
        """
        Loops through the families that the person is a child in, and display
        the information about the other children.
        """

        # setup the simple access functions
        sdb = SimpleAccess(database)
        sdoc = SimpleDoc(document)

        # display the title
        sdoc.title(_("Siblings of %s") % sdb.name(person))
        sdoc.paragraph("")

        # grab our current id, so we can filter the active person out
        # of the data

        gid = sdb.gid(person)


        stab = QuickTable(sdb)
        sdoc.header1(_("Siblings"))
        stab.columns(_("Person"), 
                     _("Gender"), 
                     _("Date"))

        # loop through each family in which the person is a child
        for family in sdb.child_in(person):

            # loop through each child in the family
            for child in sdb.children(family):

                # only display if this child is not the active person
                if sdb.gid(child) != gid:
                    stab.row(child,
                            sdb.gender(child),
                            sdb.birth_date(child))
                    document.has_data = True
        stab.write(sdoc)

#### Analysis: registering the report

Let's analyse the [siblings2.gpr.py](wiki:Quick_Views#siblings2.gpr.py) file above. We start at the bottom where the report is registered with **register**. This is the function Gramps will look for in your file. You need to give:

- = a unique name: a name Gramps identifies the plugin with, don't use spaces or strange symbols. In this case, we add a '2' to the name to avoid conflicts with the builtin .

- [](https://github.com/gramps-project/gramps/blob/892fc270592095192947097d22a72834d5c70447/gramps/gen/plug/_pluginreg.py#L159-L171) = a special constant indicating where the report will be shown. You can use **CATEGORY_QR_PERSON** to see the report on person editor and view, or **CATEGORY_QR_FAMILY** to see the report on family editor or view. (CATEGORY_QR_DATE is for reports that can be embedded in other reports since there is no "Date" category.)

- = the function you create in this plugin and that Gramps will execute when the user selects your Quick view report in the menu

- = the name of the report as it will appear in the menu

- [](https://github.com/gramps-project/gramps/blob/892fc270592095192947097d22a72834d5c70447/gramps/gen/plug/_pluginreg.py#L58-L69) = is your report **Stable**, **Unstable**, **Experimental** and **Beta**

- = a description of what your plugin does. This appears in a tooltip over the menu

- = your name

- = your email, so people can congratulate you with your work, or ask for bug fixes...

And beginning with Gramps 5.2 version, there are [additional registration properties](https://github.com/gramps-project/gramps/pull/1451):

- = a webpage that will be opened when using the Help

- [](https://github.com/gramps-project/gramps/blob/892fc270592095192947097d22a72834d5c70447/gramps/gen/plug/_pluginreg.py#L71-L76) = filtering options: ‘All’, ‘Developer’ and ‘Expert’.

- = name of person currently maintaining the addon, if different from the author_name

- = email of person currently maintaining the addon, if different from the author_email

- [](https://github.com/gramps-project/gramps/blob/892fc270592095192947097d22a72834d5c70447/gramps/gen/plug/_pluginreg.py#L297-L299), [](https://github.com/gramps-project/gramps/blob/892fc270592095192947097d22a72834d5c70447/gramps/gen/plug/_pluginreg.py#L300-L303), [](https://github.com/gramps-project/gramps/blob/892fc270592095192947097d22a72834d5c70447/gramps/gen/plug/_pluginreg.py#L304-L306) = if the addon has prerequisites.

#### Analysis: the run function

Now lets analyse the [siblings.py](wiki:Quick_Views#siblings.py) file.

If the user clicks in the quick view report menu on your report, the run function is executed with the following three parameters:

`run(database, document, person)`

So, your report receives from Gramps the currently opened database name on which to work, the document on which to write, and the person of the object the user is on. For a person quick view report, this is a person, for family, a family.

In this example, the function called is

`def run(database, document, person):`

#### Analysis: accessing the data

Now that your plugin runs, you need to open the database, start the document, access data, and write it out. We do this using the [Simple Database API](wiki:Simple_Access_API).

So, the following code:

    # setup the simple access functions
    sdb = SimpleAccess(database)
    sdoc = SimpleDoc(document)

prepares everything. Then we write a title on the document, an empty line under it, and a header, with the title, paragraph and header function:

    # display the title
    sdoc.title(_("Siblings of %s") % sdb.name(person))
    sdoc.paragraph("")

Note that we use an underscore (`_`) to indicate every string that requires translation, which comes from the line:

    from gramps.gen.ggettext import gettext as _

Everything is set up, now we write out the lines with all the siblings, leaving out the active person himself, as he is in the title field!

    # grab our current id, so we can filter the active person out
    # of the data

    gid = sdb.gid(person)

    # loop through each family in which the person is a child
    for family in sdb.child_in(person):

        # loop through each child in the family
        for child in sdb.children(family):

            # only display if this child is not the active person
            if sdb.gid(child) != gid:
                stab.row(child,
                         sdb.gender(child),
                         sdb.birth_date(child))
                document.has_data = True
    stab.write(sdoc)

Here, the easy access classes from the [Simple Access API](wiki:Simple_Access_API) have been used to quickly achieve what we want.

### Example 2

A second example can be found in the Gramps code. See [all_events.py](https://github.com/gramps-project/gramps/blob/master/gramps/plugins/quickview/all_events.py). In this report, all events for a person are printed, and all events for a family. Two Quick View reports are hence registered, one for person, and one for family.

## Notes

The possibilities are enormous. If you are an experienced programmer, there is no need to limit yourself to the simple database API. Also, if you make a real report, you can at the same time register a Quick view report with default settings.

See: [<https://github.com/gramps-project/gramps/tree/master/gramps/plugins/quickview>](https://github.com/gramps-project/gramps/tree/master/gramps/plugins/quickview)

# See also

- [Gramps_{{man version}}_Wiki_Manual_-_Reports_-_part_8#Quick_Views](wiki:Gramps_{{man_version}}_Wiki_Manual_-_Reports_-_part_8#Quick_Views)

# Addon Development Tutorials and Samples

- [Develop an Addon Gramplet](wiki:Gramplets_development) (add a [custom filtering option](https://gramps.discourse.group/t/looking-for-an-example-of-a-gramplet-with-a-custom-filter-configuration-option/5967))
- [Develop an Addon Rule](wiki:Develop_an_Addon_Rule) for custom filters
- [Develop an Addon Tool](wiki:Develop_an_Addon_Tool)
- [Develop an Addon Quick View](wiki:Quick_Views)
- Develop an Addon Report ([tutorial](wiki:Report-writing_tutorial), [samples](https://gramps.discourse.group/t/sample-report-for-new-developers/3046))
- [Adapt a builtin Report](wiki:Adapt_a_builtin_Report)

[Category:Developers/General](wiki:Category:Developers/General) [Category:Developers/Tutorials](wiki:Category:Developers/Tutorials) [Category: Plugins](wiki:Category:_Plugins) [Category:Reports](wiki:Category:Reports) [Category:Views](wiki:Category:Views)
