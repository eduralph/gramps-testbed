---
title: Programming guidelines
categories:
- Developers/General
- Developers/Quality Assurance
managed: false
source: wiki-scrape
wiki_revid: 131054
wiki_fetched_at: '2026-05-30T18:11:51Z'
---

In a multi-programmer environment, it is important to follow common coding guidelines to make sure the code remains maintainable.

## Coding style

### PEP8

- Write [PEP 8](https://www.python.org/dev/peps/pep-0008/) compatible code! This is important to have a consistent, readable codebase.
  - it is not explicit in PEP8, but we like a space after a comma

### Tabs

- Do not use TABs. Use space characters. In Gramps we use 4 spaces for indentation. This does not mean you must set your TAB stops to 4. TABs and indents are not the same thing. Most editors have a configuration option to set indentation and TAB stops. Be careful to just set the **indentation** to 4, which automatically means it has to be **spaces**. TABs are still necessary, in Makefiles for example, and they **have to** be equivalent to 8 spaces, **always**. To summarize:
  - uses spaces, no TABs
  - indentation is 4
  - TAB stops (if any) are at position 9,17,25,... (first column is 1)

### Members names

- Private class functions (functions that cannot be called outside the class) should be preceded with two underscores.
- Protected functions (functions that can only be called by the class or derived classes) should be preceded with one underscore.

<!-- -->

    def __private_function(self):
        pass
     
    def _protected_function(self):
        pass

### Callbacks

Names of callbacks should be prefixed by 'cb\_'. For example, `cb_my_callback`.

`pylint` does not check that arguments are used when methods are named in this way. This is useful to avoid the `pylint` warning: 'W0613: Unused argument <arg>'.

### Imports

The top module is called gramps, and it has following submodules:

- gen
- cli
- gui
- plugins

The other dirs should not contain code, or are for testing.

Within a submodule, only relative imports are allowed of the own submodule (so starting with . or with a module of the own directory), and absolute imports of other submodules (so starting with `gramps.`)

Generally (i.e. this is guidance, not a inviolable rule) imports should be grouped into three main sections: Python, GTK etc. and Gramps. Not all sections are required, include only those that apply. Other sections, or further grouping can be used if the developer thinks this will be useful. It may be useful to put imports in alphabetical order, but a logical order is also acceptable and may be preferable in some cases. It will often be useful to precede each main section with comment headers as in the following example:

    # -------------------------------------------------------------------------
    #
    # Standard Python modules
    #
    # -------------------------------------------------------------------------
    import os
    import logging

    # -------------------------------------------------------------------------
    #
    # GTK/Gnome modules
    #
    # -------------------------------------------------------------------------
    from gi.repository import Gtk

    # -------------------------------------------------------------------------
    #
    # Gramps modules
    #
    # -------------------------------------------------------------------------
    from gramps.gen.db.base import DbReadBase
    from .mymodule import MyClass

Where existing code has not followed this guidance, it will not normally be necessary to change the code to follow this guidance.

## Class headers

- Each class should have a simple header to help mark it in the file. This is not used for documentation - it is used to help find the class when multiple classes exist in the same file.

<!-- -->

    #------------------------------------------------------------
    #
    # MyClass
    #
    #------------------------------------------------------------

## Docstrings

- Python provides a docstrings to document classes and functions. If the class is a class used by others (such as the [gen lib](http://www.gramps-project.org/docs/gen/gen_lib.html#module-gen.lib) classes), the docstrings should follow the restructuredtext ([rst](http://docutils.sourceforge.net/docs/user/rst/quickstart.html#structure)) format. This allows us to extract [API](http://www.gramps-project.org/docs/) documentation [using Sphinx](wiki:Devhelp#See_also), a documentation generator for Python code.

<!-- -->

- Aside from adding doc strings to classes and functions, also the api generating rst files must be edited so as to extract the documentation. These files are in the [docs directory](https://github.com/gramps-project/gramps/tree/master/docs), for info read the [/docs/README.txt](https://github.com/gramps-project/gramps/blob/master/docs/README.txt) file.

  
More info

- [Sphinx for python](http://www.sphinx-doc.org/en/stable/markup/)
- [doc with Sphinx](http://www.sphinx-doc.org/en/stable/rest.html)

Classes that are not core reusable classes do not have to follow this format (although we encourage you do), but should be documented using docstrings.

    class MyClass:
        """
        MyClass is a sample class.
        """
       
        def my_function(self):
            """
            The my_function task serves no purpose whatsoever.
            """
            pass

## Black

Gramps CI checks for code formatting compliance using [Black](https://github.com/psf/black).

Black can be installed as a [Python PIP package,](https://pypi.org/project/black/) as a plugin/integration to many IDEs, or as a [standalone tool](https://github.com/psf/black/releases/) on the system. Follow the [usage instructions](https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html) on the Black docs to validate your file changes. Doing this prior to creating the Pull Request ensures that it will pass the lint check.

If code in a PR violates formatting rules the PR fails the CI check, and cannot be merged. Code which requires changes is shown in the Checks tab in the Lint panel. Make changes required to make the lint check pass. Sometimes the changes are not visible because they are white space violations, so look carefully. When using Black locally, use the same version as the CI system to ensure formatting consistency.

## Pylint

- Run `pylint` on your code before checking in.
- New files shall have a Pylint score of 9 or higher, but not enforced by CI tools as Black formatting is.
- Any changes to existing files with a Pylint score lower than 9 shall not reduce the Pylint score. It is expected that over time, this policy will cause all files to eventually have a score of 9 or higher.

Note that you must run `pylint` in the `gramps` directory. If import errors still occur, add a PYTHONPATH. Example usage:

` me@laptop:~/programs/master/src$ PYTHONPATH=plugins/lib/ pylint --reports=y plugins/mapservices/googlemap.py`

Set reports to **n** to have less output. Information on the meaning of codes can be found here:

- [All codes, PyLint 1.1.0](http://pylint-messages.wikidot.com/all-codes) Messages: and what they're trying to tell you
- [Pylint current stable](https://pylint.readthedocs.io/en/stable/user_guide/messages) documentation - now generally has a bit more detail that the older version

## Best practices

- Maintain good code hygiene by following coding guidelines and running code analysis and formatting tools locally

<!-- -->

- Always develop with [language translation](wiki:Coding_for_translation) in mind

<!-- -->

- Reduce dependencies (imports) between files.

<!-- -->

- Think on [Accessibility](wiki:Accessibility).

[Category:Developers/General](wiki:Category:Developers/General) [Category:Developers/Quality Assurance](wiki:Category:Developers/Quality_Assurance)
