---
title: Report-writing tutorial
categories:
- Addons
- Developers/General
- Developers/Tutorials
- Plugins
- Reports
managed: false
source: wiki-scrape
wiki_revid: 129095
wiki_fetched_at: '2026-05-30T18:11:59Z'
---

This tutorial covers the basics of writing a simple report using the Gramps report infrastructure. It covers the process of handling options, building a document and creating the report.

The goals of this report are to create a database summary report. It will include the following information in the report:

- The number of people in the database
- The number of males and females
- The number of unique surnames
- The most common surname

## Overview

Before going into details, it is useful to note that the report should have two basic parts. This is explained on the [Addons development](wiki:Addons_development) page, that the source code goes into two different files:

1.  the Gramps Plugin Registration (*\*.gpr.py*) file e.g.: `report.gpr.py`
2.  and the main source code file (*\*.py*) e.g.: `report.py`

### report.gpr.py

Registration statement  
This initializes the report by a single call to the [`register()`](https://gramps-project.org/docs/gen/gen_plug.html#gramps.gen.plug._pluginreg.register) function. It is trivial, but without it your report will not become available to Gramps, even if it is otherwise perfectly written.

A report can potentially be generated as a standalone report, as a Gramps Book item, and as a command line report. The registration determines which modes are enabled for a given report. The report class does not have to know anything about the mode. The options class is there to provide options interface for all available modes.

- [Report-writing_tutorial#Registering_the_report](wiki:Report-writing_tutorial#Registering_the_report)

### report.py

Report class  
This is the code that takes data from the Gramps database and organizes it into the document structure. This structure can later be printed, viewed, or written into a file in a variety of formats. This class uses the [docgen](https://gramps-project.org/docs/gen/gen_plug.html#module-gramps.gen.plug._docgenplugin) interface to abstract away the output format details.

Options class  
This is the code that provides means to obtain options necessary for the report using a variety of available mechanisms.

## Document interface

The [Report Generation](wiki:Report_Generation) article provides an overview of the 'docgen' interfaces that are available for outputting documents.

The [Report API](wiki:Report_API) article provides more details about the interfaces.

The developer [docgen](https://gramps-project.org/docs/gen/gen_plug.html#module-gramps.gen.plug._docgenplugin) api documentation provides a detailed specification of the interfaces.

Gramps attempts to abstract the output document format away from the report. By coding to the [docgen](https://gramps-project.org/docs/gen/gen_plug.html#module-gramps.gen.plug._docgenplugin) class, the report can generate its output in the format desired by the end user. The document passed to the report (`self.doc`) could represent an HTML, OpenDocument, PDF or any of the other formats supported by the user. The report does not have to concern itself with the output format details, since all details are handled by the document object.

A document is composed of paragraphs, tables, and graphics objects. Tables and graphics objects will not be covered in this tutorial.

The report defines a set of paragraph and font styles, along with their default implementation. The user can override the definition of each style, allowing the user to [customize the report](wiki:Gramps_{{man_version}}_Wiki_Manual_-_Settings#Customize_report_output_formats). Each paragraph style must be named uniquely, to prevent collisions when printed in a book format. It is recommended to prefix each paragraph style with a three letter code unique to the report.

Paragraph and font styles are defined in the `make_default_style()` function of the options class. The paragraphs are grouped into a `StyleSheet`, which the `make_default_style()` function defines. For the example report (`DbSummary`), the paragraph styles are defined as below:

    def make_default_style(self, default_style):

        # Define the title paragraph, named 'DBS-Title', which uses a
        # 18 point, bold Sans Serif font with a paragraph that is centered

        font = docgen.FontStyle()
        font.set_size(18)
        font.set_type_face(docgen.FONT_SANS_SERIF)
        font.set_bold(True)

        para = docgen.ParagraphStyle()
        para.set_header_level(1)
        para.set_alignment(docgen.PARA_ALIGN_CENTER)
        para.set_font(font)
        para.set_description(_('The style used for the title of the page.'))

        default_style.add_style('DBS-Title',para)

        # Define the normal paragraph, named 'DBS-Normal', which uses a
        # 12 point, Serif font.

        font = docgen.FontStyle()
        font.set_size(12)
        font.set_type_face(docgen.FONT_SERIF)

        para = docgen.ParagraphStyle()
        para.set_font(font)
        para.set_description(_('The style used for normal text'))

        default_style.add_style('DBS-Normal',para)

## Defining the classes

### Report class

The user's report class should inherit from the [Report](https://www.gramps-project.org/docs/gen/gen_plug.html#gramps.gen.plug.report._reportbase.Report) class contained within the `gramps.gen.plug.report` module. The constructor should take three arguments (besides class instance itself, usually denoted by 'self' name):

- Gramps database instance
- options class instance
- user class instance

The first is the database to work with. The second is the instance of the options class defined in the same report, see next section. The third is an instance of the User class, used for interaction with the user. Here's an example of a report class definition:

    from gramps.gen.plug.report import Report

    class ReportClassName(Report):
        def __init__(self, database, options_class, user):
            Report.__init__(self, database, options_class, user)

The Report class's constructor will initialize several variables for the user based off the passed values. They are:

self.doc  
The opened document instance ready for output. This is of one of the [DocGen's Generator](https://gramps-project.org/docs/gen/gen_plug.html#module-gramps.gen.plug.docgen.basedoc) types, and is **not** a normal file object.

self.database  
The [DbReadBase](https://gramps-project.org/docs/gen/gen_db.html#gramps.gen.db.base.DbReadBase) database object.

self.options_class  
The [ReportOptions](https://www.gramps-project.org/docs/gen/gen_plug.html#gramps.gen.plug.report._options.ReportOptions) class passed to the report.

You'll probably need a start-person for which to write the report. This person should be obtained from the `options_class` object through the [PersonOption](https://gramps-project.org/docs/gen/gen_plug.html#gramps.gen.plug.menu._person.PersonOption) class which will default to the active person in the database. Anything else the report class needs in order to produce the report should be obtained from the `options_class` object. For example, you may need to include the additional code in the report class constructor to obtain any options you defined for the report.

Report class **must** provide a `write_report()` method. This method should dump the report's contents into the already opened document instance.

    def write_report(self):
        self.doc.start_paragraph("ABC-Title")
        self.doc.write_text(_("Some text"))
        self.doc.end_paragraph()

The rest of the report class is pretty much up to the report writer. Depending on the goals and the scope of the report, there can be any amount of code involved. When the user generates the report in any mode, the class constructor will be run, and then the `write_report()` method will be called. So if you wrote that beautiful method listing something really important, make sure it is eventually called from within the `write_report()`. Otherwise nobody will see it unless looking at the code.

### Options class

In theory Options class should derive from [ReportOptions](https://www.gramps-project.org/docs/gen/gen_plug.html#gramps.gen.plug.report._options.ReportOptions) class. But in pratice for a common report the [MenuReportOptions](https://www.gramps-project.org/docs/gen/gen_plug.html#gramps.gen.plug.report._options.MenuReportOptions) class is used instead, which will abstract most of the lower-level widget handling. In this tutorial we'll assume that Options class is derived from [MenuReportOptions](https://www.gramps-project.org/docs/gen/gen_plug.html#gramps.gen.plug.report._options.MenuReportOptions).

#### Defining parameters of the report

To define options for your report, you need to override `MenuReportOptions.add_menu_options()` method. Then [MenuReportOptions](https://www.gramps-project.org/docs/gen/gen_plug.html#gramps.gen.plug.report._options.MenuReportOptions) class will present the user with a standard menu interface for running the report. You may generate a menu using one or more of the classes available in [`gramps.gen.plug.menu`](https://www.gramps-project.org/docs/gen/gen_plug.html#module-gramps.gen.plug.menu._menu) package such as [BooleanListOption](https://www.gramps-project.org/docs/gen/gen_plug.html#gramps.gen.plug.menu._booleanlist.BooleanListOption) class. Also you may use standard Gramps options from [`gramps.gen.plug.report.stdoptions`](https://github.com/gramps-project/gramps/blob/dba1e4e5555694194836d2934542e30c0f75d1b6/gramps/gen/plug/report/stdoptions.py) module. For example:

    def add_menu_options(self, menu):
            """
            Add options to the menu for this report.
            """
            category_name = _("Report Options")
            what_types = BooleanListOption(_('Report for'))
            what_types.add_button(_('Males'), True)
            what_types.add_button(_('Females'), True)
            what_types.add_button(_('Unknown gender'), True)
            what_types.add_button(_('Other'), True)
            menu.add_option(category_name, "what_types", what_types)

            stdoptions.add_localization_option(menu, category_name)

In this example `category name` is used to generate tab "Report Options" on the report parameter entry dialog.

Object `what_types` of class [BooleanListOption](https://www.gramps-project.org/docs/gen/gen_plug.html#gramps.gen.plug.menu._booleanlist.BooleanListOption) is created that presents the user with a group of check boxes, one is created for each call to [what_types.add_button()](https://gramps-project.org/docs/gen/gen_plug.html#gramps.gen.plug.menu._booleanlist.BooleanListOption.add_button). Finally the object is added to the menu with [menu.add_option()](https://gramps-project.org/docs/gen/gen_plug.html#gramps.gen.plug.menu._menu.Menu.add_option).

Function `stdoptions.add_localization_option()` adds to the same `menu` a standard Gramps option for localizing the report into a different locale from the UI locale.

Then to access the selected values once the user runs the report, you make a call the menu object from within the report's `__init__()` method. For example, to access the "what_types" that are selected from the menu above you would add the following code:

        def __init__(self, database, options_class, user):

            Report.__init__(self, database, options_class, user)

            what_types_option = options_class.menu.get_option_by_name('what_types')
            self.what_types = what_types_option.get_selected()

            self.set_locale(
                options_class.menu.get_option_by_name("trans").get_value())

In the example, `what_types_option` instance is retrieved by the [options_class.menu.get_option_by_name()](https://gramps-project.org/docs/gen/gen_plug.html#gramps.gen.plug.menu._menu.Menu.get_option_by_name) method. The string passed to the method must match the name you passed as the second argument to [menu.add_option()](https://gramps-project.org/docs/gen/gen_plug.html#gramps.gen.plug.menu._menu.Menu.add_option) when you created the menu. Then a list of the selected item titles is retrieved with [what_types_option.get_selected()](https://gramps-project.org/docs/gen/gen_plug.html#gramps.gen.plug.menu._booleanlist.BooleanListOption.get_selected) and stored as a instance variable `self.what_types` for later use.

The standard Gramps option for localizing the report has name "trans". Its value is passed to [`Report.set_locale()`](https://www.gramps-project.org/docs/gen/gen_plug.html#gramps.gen.plug.report._reportbase.Report.set_locale) method that creates `self._()` method for the locale chosen by the report's user. It is then used by `write_report()` (see below).

#### Defining user-adjustable paragraph styles

If the report uses the user-adjustable paragraph styles the default definitions for the styles must be defined here by overriding method [make_default_style()](https://www.gramps-project.org/docs/gen/gen_plug.html#gramps.gen.plug.report._options.ReportOptions.make_default_style), to form a 'default' style sheet:

    def make_default_style(self, default_style):
        f = docgen.FontStyle()
        f.set_size(10)
        f.set_type_face(docgen.FONT_SANS_SERIF)
        p = docgen.ParagraphStyle()
        p.set_font(f)
        p.set_description(_("The style used for the person's name."))
        default_style.add_style("ABC-Name",p)

## Implementation

### Defining the ReportOptions class

In this tutorial, the report has two options. The first, called `what_types`, allows a user to choose whether the counts of persons whose gender is Male, Female, Unknown or Other are shown in the report. The second is the standard Gramps option that allows the user to choose the locale for the report different from UI locale. It is added by calling `stdoptions.add_localization_option()` method. These two options are added in the overridden `add_menu_options()` method.

To define two unique styles for the report: DBS-Title and DBS-Normal the method `make_default_style()` is overridden too. Both styles are added by calling `default_style.add_paragraph_style()` method.

So create now file **report.py** and copy there the above code.

### Defining the Report class

The actual implementation of the `DbSummaryReport` is rather simple. To initialize the class the parent `Report.__init__()` routine is called and then values of the options entered by the user are extracted from `options_class` parameter which is of class `DbSummaryOptions`. An instance variable `self.what_types` is assigned a list of names of check boxes selected by the user. Then `self.set_locale()` method is called with the value of the locale to be used to run the report.

All the work is done in the `_count()` method. It uses a [`self.database.iter_people()`](https://www.gramps-project.org/docs/gen/gen_db.html#gramps.gen.db.generic.DbGeneric.iter_people) to iterate through [`Person`](https://www.gramps-project.org/docs/gen/gen_lib.html#module-gramps.gen.lib.person) objects and gathers some simple statistics. The only thing of any complication is the determination of the most common surnames. A python dictionary is used to store the number of times each surname is used. Each time a surname is encountered, the value in the dictionary is incremented. The results are then loaded into a list and sorted in the reverse order `slist.sort(reverse=True)`, allowing us to find the most common names by looking at the first entries in the list.

Finally `write_report()` method outputs the data collected in accordance with the options selected by the report user. Note that the strings being used in the report (such as "Report Options", "Males" etc) have already been used somewhere else in Gramps and have already been translated into various languages. Thus the content of our report as well as its parameters are already translated!

Append the above code to the **report.py** file

### Registering the report

- Registration is set into a *<name>.gpr.py* file
- The registration consists from a single call to [register()](https://www.gramps-project.org/docs/gen/gen_plug.html#gramps.gen.plug._pluginreg.register) function
- Registration should define internal `id` of the report (preferably, single string with non-special ascii characters, usable for report identification from the command line and in the options storage, as well as for forming sane filename for storing its own styles).
- It should also define the report's...
  - `category` (text/graphics/code)
  - translatable `name` (the one to display in menus)
  - If the report requires an active person to run, then `require_active` should be set to `True`.
  - The `report_modes` argument is set to a list of zero or more of the following modes:
    - REPORT_MODE_GUI (available for Gramps running in a window, graphical user interface)
    - REPORT_MODE_BKI (available as a book report item)
    - REPORT_MODE_CLI (available for the command line interface)
  - Finally, both `reportclass` and `optionsclass` names should be passed to registration.

Descriptions of the other arguments of [register()](https://www.gramps-project.org/docs/gen/gen_plug.html#gramps.gen.plug._pluginreg.register) function can be found [here](https://www.gramps-project.org/docs/gen/gen_plug.html#module-gramps.gen.plug._pluginreg). Here's the registration statement for our report:

    from gramps.gen.plug._pluginreg import *
    from gramps.gen.const import GRAMPS_LOCALE as glocale
    _ = glocale.translation.gettext

    register(REPORT,
             id='RWT_ID',
             name=_("Report-writing tutorial"),
             description=_("Produces a simple database summary"),
             version='1.0',
             gramps_target_version='6.0.6',
             status=STABLE,
             fname='report.py',
             authors=["John Doe"],
             authors_email=["jdoe@example.com"],
             category=CATEGORY_TEXT,
             require_active=False,
             reportclass='DbSummaryReport',
             optionclass='DbSummaryOptions',
             report_modes=[REPORT_MODE_GUI, REPORT_MODE_CLI]
             )

Copy the above code into **report.gpr.py** file.

#### Remark regarding book report mode

To turn a report into one that will work as a book report, you add REPORT_MODE_BKI to the list of `report_modes` above. Also you have to add additional code to `write_report()` method of the Report class, similar to the code below:

    from gen.plug.docgen import IndexMark

    # Write the title line. 
    # Set in INDEX marker so that this section will be identified 
    # as a major category if this is included in a Book report.

    title = self._('My Report')
    mark = IndexMark(title, INDEX_TYPE_TOC, 1)
    self.doc.start_paragraph('MYREPORT-section')
    self.doc.write_text(title, mark)
    ...

See an existing book reports for more details. DO NOT copy the above code into **report.py** file since we do not intend to use our report in Book mode.

## Manually installing your report

Install in the plugins directory of your Gramps user directory. Go to ~/.local/share/gramps/gramps60/plugin directory (or similar for your version of Gramps) and create there RWT subdirectory. Then copy into RWT both **report.py** and **report.gpr.py** files.

## Example output

Start Gramps and your tutorial report will be available from the reports menu as

![[_media/Rwt_menu.png]]

Run the report and this is what the output looks like

![[_media/Example_RWT_ID.jpg]]

## See also

- [Report API](wiki:Report_API)
- [Substitution Values](wiki:Gramps_{{man_version}}_Wiki_Manual_-_Reports_-_part_2#Substitution_Values) (Pre-defined formatting of tree data for reports)
- [Report Generation](wiki:Report_Generation) (describing output format options)
- [Gramps Data Model](wiki:Gramps_Data_Model)
- Discourse forum discussion: [Sample Report for new developers](https://gramps.discourse.group/t/sample-report-for-new-developers/3046)

[*](wiki:Category:Addons) [Category:Developers/General](wiki:Category:Developers/General) [Category:Developers/Tutorials](wiki:Category:Developers/Tutorials) [Category:Plugins](wiki:Category:Plugins) [Category:Reports](wiki:Category:Reports)
