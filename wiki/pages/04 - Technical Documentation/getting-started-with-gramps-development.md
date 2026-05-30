---
title: Getting started with Gramps development
categories:
- Developers/General
- Developers/Tutorials
- Stub
managed: false
source: wiki-scrape
wiki_revid: 97692
wiki_fetched_at: '2026-05-30T18:10:58Z'
---

This tutorial aims to help you get started initially with Gramps development and shows you a general overview of what you need to know when working with the Gramps source code. The following will help you setup a development environment and explain where to find the files you need.

This tutorial assumes that you are using GNU/Linux (but it might help under another OS) and that you know the basics of Python programming language.

# Set up your environment

## Linux: Optional : set up a development environment

If you run your development version of Gramps as the usual user, it will show all your usual Gramps family trees, so loading one by mistake is possible and a bug may result in losing productive data. To prevent this, you could use a [GRAMPSHOME](wiki:GRAMPSHOME) environment variable to create a separate folder for productive data, see [Run Gramps from a portable drive](wiki:Run_Gramps_from_a_portable_drive) for more information.

Here are some options you may choose to prevent this. If you have enough resources, I recommend using VirtualBox.

### VirtualBox

[VirtualBox](https://www.virtualbox.org/) is an open source virtualisation solution. Install it, run it and you have a virtual PC in your PC. Network connection works out of the box without extra configuration needed. Install your favorite Linux distribution and start hacking Gramps in a fully separated environment.

### Chroot

You may also use a [`chroot`](https://wikipedia.org/wiki/Chroot) to result in a similar separation as virtualbox.

If you use Ubuntu, you can set up the chroot environment following these instructions: [Creating a basic Ubuntu chroot](https://help.ubuntu.com/community/BasicChroot)

If you use Gramps in a chroot jail with another Linux distribution, please add information here.

You should then have a working chroot environment in `/var/chroot` (or whichever location you chose). Enter it with

`sudo chroot /var/chroot `

This means that within this directory, applications cannot access files without the chroot jail, i.e. your Gramps install within the directory cannot destroy another install of Gramps in your usual home directory.

From a shell within your chroot directory, just clone the Git repository into the chroot folder as usual. Please note that before running the autogen-Script for generating makefiles, you may need to get some packages:

`apt-get install python intltool libglib2.0-dev gedit`

### Another user

You may also simply do your development as another user, so you won't access your usual `~/.gramps` database when testing.

You can also create an alias account with the same user and group IDs, but with a different login name and different home directory, typically, a subdir of the real user's home directory. This gives the benefit of less disk usage, and no permission boundary between the two account aliases. On the other hand, if you are afraid of malicious code within gramps purposefully breaking out and wreaking havoc on your real home account's `.gramps`, this method is too weak for you. For regular development scenario, though, this setup certainly does suffice.

This is what the cloning looks like in my `/etc/passwd`:

`vassilii:x:1000:1000:Vassilii Khachaturov,,,:/home/vassilii:/bin/bash`  
`v:x:1000:1000:Vassilii Khachaturov,,,:/home/vassilii/pub:/bin/bash`

Create symlink to the dotfiles you want to reuse. Obviously, don't do this for *`.gramps`*! Something like (inside `~vassilii/pub`):

`ln -s ../.bashrc ../.mozilla ../.ratpoisonrc ../.gitconfig .`

You can use the alias account in a standalone matter (X session under it), or just inside a terminal window (su - <name of the alias account>). All the build, install, and test run of gramps should be done under this account. This will preserve your normal account's .gramps.

Having obtained the gramps source tree, as the first build step, do

`./autogen.sh -- --prefix=/home/vassilii/pub/local`

(**replace /home/vassilii/pub/ with the actual aliased home directory!!!**)

After you build and install (no root needed! you install under the local prefix), check that the right (locally built) gramps is on your PATH. Tweak your shell profiles as needed.

### None of above

## Mac OS X

In order to develop (or even use) Gramps on an Apple Macintosh, you must first install all of the prerequisite libraries and their headers. There are three choices for this:

1.  [Gtk-OSX](http://live.gnome.org/Gtk%2BOSX),
2.  [MacPorts](http://www.macports.org), or
3.  [Fink](http://www.finkproject.org).

Full instructions for building Gramps for each is provided here:

1.  [Mac OS X:Build from source:Application package](wiki:Mac_OS_X:Build_from_source:Application_package),
2.  [Mac OS X:Build from source:MacPorts](wiki:Mac_OS_X:Build_from_source:MacPorts), or
3.  [Mac OS X:Build from source:fink](wiki:Mac_OS_X:Build_from_source:fink).

The last only works with X11, which is no longer included in OS X but can be installed separately. MacPorts can be built with/for either X11 or OS X's native Quartz graphics backend, and Gtk-OSX is exclusively for Quartz.

## Windows

In order to develop (or even use) Gramps on Windows, you must first install a development environment and all of the prerequisite libraries and their headers. [Gramps_for_Windows_with_MSYS2](wiki:Gramps_for_Windows_with_MSYS2)

Full instructions for building Gramps is provided here: [Building_Gramps_AIO_cx_freeze-based](wiki:Building_Gramps_AIO_cx_freeze-based)

## Install a text editor

Choose the text editor you like to work with. If your favourite text Editor is not listed you can add it and describe how to set it up here.

### Eclipse + PyDev

[Eclipse](http://www.eclipse.org/downloads/) with [PyDev](http://www.pydev.org/manual_101_install.html) brings an integrated IDE for Python. To run it, you have to do a few steps configuration:

- First, you have to set the path to your python interpreter:
  - Go in the menu **Window \> Preferences...**;
  - Then choose **PyDev \> Interpreters \> Python Interpreter**.
  - Click **New...** to create a link to your Python executable (for example */usr/bin/python3.5*).

<!-- -->

- Next, you have to set up a PyDev project:
  - Go in the menu **File \> New \> Project...**;
  - Choose **PyDev Project**
  - Project name could be *Gramps*
  - Uncheck **Use defaults** and choose **~/gramps-master** as the project directory.
  - Project type is **Python 3.5**
  - Interpreter is the one you created at the first step above
  - And then you can press **Finish**.

You are now ready to start coding!

### PyCharm

[PyCharm](https://www.jetbrains.com/pycharm/) is not Free Software like Eclipse is. But seems to be recognizing more Python syntax and feels faster on my box. I unpacked the distribution, launched bin/pycharm.sh script, and it just worked. 'File » Open Directory' and selected the "Gramps/src" directory in my local checked out Git WD, and things work from there.

'Version Control » Update Project' automatically syncs up with the Git repository.

### Emacs or Vim

Experienced Unix-like users and developers will often use one of these editors. They're available with virtually all distributions of modern Unix-like systems.

### The Eric Python IDE

[Eric](https://eric-ide.python-projects.org/) is a python editor. It has everything you need (code completion, python shell, ...)

### Geany

[Geany](https://www.geany.org/) is a nice development Editor. One feature I like is that it will automatically recognise python code and list Symbols in a side bar, allowing to jump quickly in your code.

Install it and you can start coding !

Note, you can also get [instant documentation for python modules](https://wiki.geany.org/howtos/pydocw).

### SPE

[SPE](http://pythonide.stani.be/) or Stani's python editor, is a python editor. It is somewhat more powerfull than Eric (quick access to code fragments, extensive search, ...) but can be unstable on some setups. Try it to know.

### Scribes

[Scribes](http://scribes.sourceforge.net/) is a text editor written in python and Gtk, that uniquely blends simplicity with well researched powerful functions.

### Kate

[Kate](https://kate-editor.org/) works well as a general editor for Python. It also recognizes key words of Python and marks them in colours. Kate is a Linux KDE desktop program. Of course, it also works on gnome installations.

### Idle

**Idle** is a handy simple editor that takes advantage of the interpreter features of Python. Often Idle comes with Python packages. Idle works well in Linux and other OS's, including the "dominant OS". If you install Windows version of Python, you will probably install from the same package Idle. One feature of Idle tends to confuse newcomers: Idle main window is NOT used for program writing, but for displaying the results. Notice that there is a Python tutorial, automagically installed with Idle on a Windows box. It is worth noting that the Tutorial gives quite extensive introduction into Python and is authored by the originator of Python: Guido van Rossum.

## Get the source tree

To get the source tree, you will need Git. Please read the dedicated tutorial [Brief introduction to Git](wiki:Brief_introduction_to_Git) for details.

You can also use a graphical Git tool like "[gitk (The Git repository browser)](https://git-scm.com/docs/gitk/)" or "[git-gui ( A portable graphical interface to Git)](https://git-scm.com/docs/git-gui/)".
python3 wiki/tools/scrape_wiki.py \
  --seed "Gramps_6.0_Wiki_Manual_-_Gramplets" \
  --prefix "Gramps_6.0_Wiki_Manual_-_Gramplets" \
  --target-dir "wiki/pages/04 - Technical Documentation" \
  --max-pages 1
**This tutorial now assumes you have cloned the Gramps repository into a directory called `~/Gramps`. If not, you have to change this path when it is used below.**

## Run Gramps from the source

To test that you did all well, you may want to run Gramps from your downloaded Git tree. This is explained in the [Running a development version of Gramps](wiki:Running_a_development_version_of_Gramps); here are the quick steps:

For the internationalization code to work, you need to have the translation tools.

On Debian, just run (as root) - ('''Only if Debian installs Gramps 4.0+ as Gramps version!):

`apt-get build-dep gramps`

On Fedora 20+, you will need:

`yum install intltool gettext git-core rcs`

Build Gramps with:

`cd ~/Gramps`  
`python setup.py build`

To run Gramps, type:

`python Gramps.py`

Dependencies

If you have an "GExiv2 Module Not Loaded" you should install it with

`sudo apt install gir1.2-gexiv2-0.10`

The same for the "osmGpsMap module not loaded, Geography functionality will not be available"

`sudo apt install gir1.2-osmgpsmap-1.0`

## Correct Translation in development

Warning: you will not be able to load translations on /usr/local/share/locale, because you will load /usr/share/locale, which could be translations for stable release (set on grampsapp.py). You may generate a custom launcher by adding this line:

`export GRAMPSI18N=/usr/local/share/locale`

if you want to use an other path, you may add this line:

`export GRAMPSI18N=@prefix@/share/locale`

on current gramps.sh.in (source file) before installation.

# Browse the source code

- For further information see: [Gramps 4.x File Layout Organization](wiki:Gramps_4.x_File_Organization)

# Develop

Before you start developing, read

- [Programming guidelines](wiki:Programming_guidelines)
- [UI style](wiki:UI_style)
- [Brief introduction to Git](wiki:Brief_introduction_to_Git)
- [Using database API](wiki:Using_database_API)
- [API Code Documentation](https://www.gramps-project.org/docs/) - Gramps current release.
- [Devhelp](wiki:Devhelp) - How to include [Gramps API](https://gramps-project.org/docs/) into the Devhelp index.
- [Committing policies](wiki:Committing_policies)

[Category:Developers/Tutorials](wiki:Category:Developers/Tutorials) [G](wiki:Category:Developers/General)
