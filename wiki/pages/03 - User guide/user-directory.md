---
title: Gramps 6.0 Wiki Manual - User Directory
categories:
- Documentation
managed: false
source: wiki-scrape
wiki_revid: 126954
wiki_fetched_at: '2026-05-30T11:44:33Z'
---

{{#vardefine:chapter\|D}} {{#vardefine:figure\|0}} This appendix documents the location of the **Gramps [User Directory](wiki:Gramps_Glossary#user_directory)**. That directory, or folder, is stored at different locations due to

- differences in operating systems
- your username, i.e. the account with which you've logged into your computer. Where *<username>* is shown below it should be replaced by your username.
- user configuration

\_\_TOC\_\_

## New and old default locations and fallback behavior

In Gramps 6.0, on every operating system, the default location of the user directory changed. New and old default user directory locations for each OS are given below. If Gramps 6.0 and later detects a user directory in the old default location, it will use that directory and not create one in the new default location. Otherwise, it will create a user directory in the new default location.

## [POSIX](wiki:Gramps_Glossary#posix) - style systems

The default user directory location for Gramps in a [POSIX](https://wikipedia.org/wiki/Posix)-style [environment](https://wikipedia.org/wiki/Filesystem_Hierarchy_Standard) was changed in Gramps 5.2

`/home/`*`<username>`*`/.local/share/gramps`

In Gramps 5.1 and earlier, the user directory on a POSIX-style environment was

`/home/`*`<username>`*`/.gramps`

This is true for [BSD](https://wikipedia.org/wiki/Bsd), [Linux](https://wikipedia.org/wiki/Linux), [Solaris](https://wikipedia.org/wiki/Solaris_(operating_system)) and [Unix](https://wikipedia.org/wiki/Unix).

For brevity, you can use tilde notation. The path above can be simplified to

`~`*`<username>`*`/.local/share/gramps`

or, to avoid referring to the username,

`~/.local/share/gramps`

You can also use the [**\$HOME** environment variable](http://www.linfo.org/home_directory.html). Although Gramps will not recognize environment variables in paths internally, you can use them in a terminal or in scripts. Using **\$HOME**, the path above can be simplified to

`$HOME/.local/share/gramps`

### Flatpak

If you installed Gramps via the Flatpak route, an additional user directory is created in a different location:

`$HOME/.var/app/org.gramps_project.Gramps/data/gramps`

However, if there is also a user directory from previous versions that were installed directly (not via Flatpak), Gramps will continue to use that directory for some purposes.

So if you are trying to locate user files in an installation where Flatpak has superseded another kind of installation (e.g. from a Linux repository), it's important to consider both locations.

## macOS

![[_media/macos_200x200.png]] The default user directory location for Gramps on macOS, both the [Mac OS X:Application package](wiki:Mac_OS_X:Application_package) and [built from source](wiki:Build_from_source#Mac_OS_X), is (similar to other POSIX systems) (changed in 5.2)

`/Users/`*`<username>`*`/.local/share/gramps`

In Gramps 5.1 and earlier, the user directory for the Gramps [Mac OS X:Application package](wiki:Mac_OS_X:Application_package) was

`/Users/`*`<username>`*`/Library/Application Support/gramps`

but the user directory for [Gramps built from source on macOS](wiki:Build_from_source#Mac_OS_X) was (similar to other POSIX systems)

`/Users/`*`<username>`*`/.gramps`

### Accessing hidden directories in macOS

macOS filenames, including directories, starting with "." (period) do not show up in Finder. Access the Gramps user directory in any of these ways:

- In Finder, navigate to the directory which contains the hidden file or directory you want to see and type command-shift-. (period). All of the hidden files and directories in that directory will be shown.
- Click on [](https://osxdaily.com/2011/08/31/go-to-folder-useful-mac-os-x-keyboard-shortcut/) in the Finder, and type

`~/.gramps`

  
in the resulting macOS dialog box.

- Open a terminal window using the Terminal application and type

`ln -s ~/.gramps ~/Documents/Gramps`

which will make Finder show the directory as a folder in your Documents folder named "Gramps". (You can replace "Gramps" with whatever name you wish, but use a \\ before any spaces.)

## MS Windows

![[_media/windows_180x160.png]] The default **User Directory** location for any Gramps user data on a Windows 7 (and newer) system was changed in 5.2

`C:\Users\`*`%username%`*`\AppData\Local\gramps`

In Gramps 5.1 and earlier, the user directory for Windows 7 (and newer) was

`C:\Users\`*`%username%`*`\AppData\Roaming\gramps`

Alternately, you can use the **%LocalAppData%** [environment variable](https://wikipedia.org/wiki/Environment_variable#APPDATA) to avoid referring to the username. (We've chosen to use the username environment variable in the documentation for Windows rather than ***<username>*** used for documenting other OSes.) Although Gramps will not recognize environment variables for paths internally, you can use them within Windows to find Gramps user files. The path above can be simplified to:

`%LocalAppData%\gramps`

### Accessing hidden directories in MS Windows

On Microsoft Windows, filenames and folder for programs and userdata are [hidden](https://wikipedia.org/wiki/Hidden_file_and_hidden_directory) in the *File Explorer*. To make access to the Gramps user directory easy follow the following advice from Microsoft:

- [Show hidden files - Windows Help](https://support.microsoft.com/en-ca/help/14201/windows-show-hidden-files)

Like the **User Directory**, the location for programs/applications is also hidden from browsing with Windows Explorer.

The default location for an installation on a Windows 10 (and newer) system is

`C:\Program Files\GrampsAIO64-6.X.X`

{{-}}

## See Also

- [Command Line](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line) Configuration (config) option with [Environment Variables](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line#Environment_variables)
- [Switching from Breadcrumbs to a location text box](https://winaero.com/how-to-enter-file-location-manually-in-gtk-3-opensave-dialog/) using in GTK file dialogs
- Discourse forum threads :
  - [how to use Environment Variables in Gramps](https://gramps.discourse.group/t/how-to-set-the-base-path-from-media-relative-to-grampshome/481/2)
  - [Using Python Eval gramplet to list the Plugins folder path](https://gramps.discourse.group/t/manually-installing-addons/5696/5)
  - [Troubleshooting Gramps paths and environmental variables](https://gramps.discourse.group/t/troubleshooting-gramps-paths-and-environmental-variables/5692) with the [Python Evaluation](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Python_Evaluation) gramplet

<!-- -->

- 

[U](wiki:Category:Documentation)
