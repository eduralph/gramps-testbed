---
title: Translating Gramps
categories:
- Developers/General
- Translators/Categories
managed: false
source: wiki-scrape
wiki_revid: 110144
wiki_fetched_at: '2026-05-30T18:18:40Z'
---

Tips for translators of the Gramps program.

The page [coding for translation](wiki:Coding_for_translation) may also be of interest to translators.

Please read [A Translators Guide to Git](wiki:A_Translators_Guide_to_Git)

## Gettext file format

### Header

*msginit* is a GNU utility, called on /po directory, which generates a header for gettext file template : **gramps.pot**.

`"Project-Id-Version: PACKAGE VERSION\n"`  
`"Report-Msgid-Bugs-To: \n"`  
`"POT-Creation-Date: 2004-12-30 10:52-0500\n"`  
`"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"`  
`"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"`  
`"Language-Team: LANGUAGE <LL@li.org>\n"`  
`"MIME-Version: 1.0\n"`  
`"Content-Type: text/plain; charset=CHARSET\n"`  
`"Content-Transfer-Encoding: 8bit\n"`  
`"Plural-Forms: nplurals=2; plural=(n != 1);\n"`

- *Project-Id-Version* : this is the name and version of the package. Fill it in if it has not already been filled in by xgettext.
- *Report-Msgid-Bugs-To* : this has already been filled in by xgettext. It contains an email address or URL where you can report bugs in the untranslated strings:
  - Strings which are not entire sentences, see the maintainer guidelines in Preparing Strings.
  - Strings which use unclear terms or require additional context to be understood.
  - Strings which make invalid assumptions about notation of date, time or money.
  - Pluralisation problems.
  - Incorrect English spelling.
  - Incorrect formatting.
- *POT-Creation-Date* : this has already been filled in by xgettext.
- *PO-Revision-Date* : You don't need to fill this in. It will be filled by the PO file editor when you save the file.
- *Last-Translator* : fill in your name and email address (without double quotes).
- *Language-Team* : fill in the English name of the language, and the email address or homepage URL of the language team you are part of. Before starting a translation, it is a good idea to get in touch with your translation team, not only to make sure you don't do duplicated work, but also to coordinate difficult linguistic issues. In the Free Translation Project, each translation team has its own mailing list. The up-to-date list of teams can be found at the Free Translation Project's [homepage](http://translationproject.org/), in the "Teams" area.

### msgid / msgstr / comment / fuzzy

`#: gramps.py:10`  
`#, fuzzy`  
`msgid "File not found"`  
`msgstr ""`

- text after *\#* provides a comment.
  - The file reference and the line number after *\#:*
  - A comment on code or the main string (*msgid*) after *\#.*
  - A comment on your translation (*msgstr*) after *\#*

This will help translator but is optional for having a translation.

- *\#, fuzzy* could be added because string is not up-to-date. It means that there was a change somewhere (a string has been added, removed or modified) and *xgettext* did a guess on what the translation should be. This guess is most likely not entirely correct, but it is often very close.

*fuzzy* strings are ignored, english string (*msgid*) will be used ! Need to correct/validate entry on your translation editor.

- msgid is the string, present on gramps' code
- msgstr is your translation string

## Tips for translators

### Getting started

1.  Always save your translations in UTF-8 encoding **without [BOM](https://en.wikipedia.org/wiki/Byte-order_mark)** ([take care with *NotePad*](http://achilles-keep-moving.blogspot.de/2011/10/msgfmt-fatal-error-with-utf-8-with-bom.html))
2.  Don't overwrite the English strings, your translation should be below the original string
3.  Take heed on special characters. You must have the same number of and types as the original string.
4.  Verify spelling and grammar on your translation.
5.  Don't translate "too freely". Your translation should be as close match to the original as possible
6.  Be consistent with your translations. If you decide on a specific word/phrase for something, stick to that throughout the translation.
7.  If possible, try the translation before sending

Translating Gramps into a new language means translating English strings used in the Gramps interface. To put it shortly, this amounts to

1.  obtaining the gramps.pot file with the strings to be translated,
2.  translating the strings in the template, and
3.  getting the translated file uploaded into the Gramps Git repository.

Another avenue of translation is translating the documentation. This is a different and lengthy process and it is described in our [Translating the Gramps User manual](wiki:Translating_the_Gramps_User_manual) page. Here we will concentrate on the interface translation only.

### Obtaining gramps.pot

- Download `gramps.pot` from Gramps Git repository, see [the introduction to Git](wiki:Brief_introduction_to_Git).

You can also download files by browsing via [GitHub web interface](https://github.com/gramps-project/gramps).

- Look for `gramps.pot` in the **po** directory.

### Translating messages

- Copy `gramps.pot` to the file named `lang.po`, according to the language you are translating into (`fr.po` for French, `ru.po` for Russian, etc.)
- Use [GTtranslator](http://gtranslator.sourceforge.net) (GNOME, windows), [KBabel](http://i18n.kde.org/tools/) (KDE), [Lokalize](http://userbase.kde.org/Lokalize) (KDE, windows), Emacs po-mode, [Virtaal](http://virtaal.translatehouse.org) (GNU/Linux, Mac, windows), [poedit](http://www.poedit.net/) (GNU/Linux, OSX, windows), or any similar tool designed for translating `.po` files. If you do not like any of these tools, you can use any text editor to translate messages. If using vim, properly setting the "langmap" option will significantly speed up your work.
- Even though Gramps uses UNICODE (UTF-8) for its character set, you may use your native character set for your translation. Just make sure you specify the character set you are using in the `Content-Type` line in the `.po` file. Gramps will handle the conversion to UNICODE.
- If there are non ASCII characters in the original English string, try to preserve them by copying them, if applicable.

### Context

As an extension to standard gettext, strings in Gramps can have a context prefix. This prefix should **not** be translated, and just be deleted in the translation. More info and an example [further down](#Translation_context).

As a special context, you will see the manual context, <abbr title="exempli gratia - Latin phrase meaning 'for example'">e.g.</abbr>, :

`'manual|Editing_Dates'`

these strings should only be translated if a **wiki user manual** is available in your language, <abbr title="exempli gratia - Latin phrase meaning 'for example'">e.g.</abbr>, in Dutch :

`'Datums_aanpassen' `

The string refers to a section, <abbr title="exempli gratia - Latin phrase meaning 'for example'">e.g.</abbr>, [Editing_Dates](wiki:Gramps_4.1_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_1#Editing_dates) in Dutch becomes [Datums_aanpassen](wiki:Gramps_4.1_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_1/de#Daten_bearbeiten).

### Testing your `.po` file

In the `po` directory run the command:

    make

If there are errors in your po file, this will fail and give you an error message. You should correct these errors. If you have trouble understanding the error, try to run the next test, which might give a more verbose output.

#### check_po

In the `po` directory run the command:

`./check_po --skip-fuzzy lang.po `

or

`python check_po --skip-fuzzy lang.po > lang`

where lang is your language code. This will give you errors in your translation, information on badly translated phrases, ... the output could resemble something like this..

`File:               nl.po`  
`Template total:     3816`  
`PO total:           3671`  
`Fuzzy:              125`  
`Untranslated:       12`  
`%s mismatches:      0`  
`%d mismatches:      2`  
`%() name mismatches:9`  
`%() missing s/d:    0`  
`Runaway context:    0`  
`XML special chars:  0`  
`Last character:     15`  
`Shortcut in msgstr: 16`  
`PO Coverage:        99.67%`  
`Template Coverage:  95.89%`  
`Localized at:       97% (previous gramps.pot)`

If you get *previous gramps.pot*, then you are not using the last *gramps.pot*, see [update your translation](#Updating_your_translation). *fuzzy* and untranslated strings will be ignored, Gramps will use main strings in english.

`-------- %d mismatches --------------`

You can see that there are 3816 strings to be translated and the coverage is around 96 %. There are still 12 untranslated strings and some 120 fuzzies. The last one can be ok, but should be checked. Additional information shows <abbr title="exempli gratia - Latin phrase meaning 'for example'">e.g.</abbr>, that in 15 strings there is a mismatch with the 'last character':

`-------- last character not identical ---------`  
`msg nr: 98, lineno: 602`  
`msgid "Could not make database directory: "`  
`msgstr "Kon geen gegevensbestandsmap aanmaken"`

This is very valuable information, because you can easily see what the problem is, even if you do not understand the language! Clearly the last characters must be ": "

#### statistics

In the `po` directory run the command:

    msgfmt --statistics lang.po

or

    msgfmt.exe --statistics lang.po

where lang is your language code. This should not throw an error. Basically this gives the same info in a condensed format: 3533 translated messages, 125 fuzzy translations, 12 untranslated messages.

#### GNU \`gettext' utilities

[GNU \`gettext' utilities](http://www.gnu.org/software/gettext/) provides a few stand-alone programs to massage in various ways the sets of translatable strings, or already translated strings:

`msgattrib - attribute matching and manipulation on message catalog`  
`msgcat - combines several message catalogs`  
`msgcmp - compare message catalog and template`  
`msgcomm - match two message catalogs`  
`msgconv - character set conversion for message catalog`  
`msgen - create English message catalog`  
`msgexec - process translations of message catalog`  
`msgfilter - edit translations of message catalog`  
`msgfmt - compile message catalog to binary format (.po->.mo)`  
`msggrep - pattern matching on message catalog`  
`msginit - initialize a message catalog`  
`msgmerge - merge message catalog and template`  
`msgunfmt - uncompile message catalog from binary format`  
`msguniq - unify duplicate translations in message catalog`

For checking syntax (header, format, domain) :

`msgfmt -c nl.po`

`msgfmt.exe -c nl.po`

For checking keyboard accelerators (underscore) :

`msgfmt --check-accelerators=_ nl.po`

`msgfmt.exe --check-accelerators=_ nl.po`

- Some experimentations and customizations, with these GNU gettext utilities for gramps' translation strings, were tested with success some years ago. You can still get an overview via an ancien ['setup.py' stand-alone script for an addon (5.1 branch)](https://raw.githubusercontent.com/gramps-project/addons-source/refs/heads/maintenance/gramps51/lxml/setup.py) or the [setup one at the top of the addons-sources repository](https://raw.githubusercontent.com/gramps-project/addons-source/refs/heads/maintenance/gramps60/setup.py).

#### Gettext lint

[Gettext lint](http://gettext-lint.sourceforge.net/) is a collection of tools for checking the validity, consistency and spelling of PO. Some python scripts do not work anymore with last expat version.

#### Pology (KDE)

[Pology](http://pology.nedohodnik.net/) is a Python library and collection of command-line tools for in-depth processing of PO files, the translation file format of the GNU Gettext software translation system. Pology functionality ranges from precision operations on individual PO messages, to cross-file operations on large collections of PO files. Pology is used by the [KDE](http://websvn.kde.org/trunk/l10n-support/pology/) translation teams for checking syntax.

#### Translate Toolkit

[Translate Toolkit](http://translate.sourceforge.net/wiki/toolkit/index) is a collection of useful tools for localisation. It can help to improve the quality of your localisation, including tools to help check, validate, merge and extract messages from your localizations.

### Save as .mo file

If possible and when you are finished translating, go to **File -\> Save as...** to generate a *.mo* file for testing syntax.

- Under poedit, you can set to always compile a *.mo* file when saving changes by clicking **File -\> Preferences** and on the **Editor tab** check the **Automatically compile *.mo* file on save box**. A dialog will warn you if there is a syntax error on your *.po* file.

<!-- -->

- Lokalize, GTranslator also provide a syntax check when saving. If an error occured we can navigate to messages which contain errors.

Please, enable this feature to avoid errors on compilation process.

### Formatting (compiling) `.po` file

- Currently, [formatting (msgfmt) is performed during build time](wiki:Coding_for_translation#How_it_works), so you should not have to worry about it. The translated `.po` file is the product of your work. However, try to [check syntax](wiki:Translating_Gramps#Save_as_.mo_file) before any commit.

### Send your contribution

Check it into Git if you obtained the permission to do so.

The following configuration option simplifies pushing a branch back to the server:

`$ git config --global push.default upstream`

Otherwise you can fork gramps repository with a Github account and pull a merge request.

See:

### Updating your translation

If you have submitted a translation, it may well be that after some weeks/months, new strings are added to Gramps, implying you need to update your translation file.

Assuming you have obtained originally the Gramps source tree as explained in [Brief introduction to Git](wiki:Brief_introduction_to_Git). Now:

- Update your Gramps tree from Git. This can be done by executing the command
      git pull --rebase

  from the root Gramps directory. This will download an updated `gramps.pot` file.
- Use your outdated translation to translate the strings that did not change:
      msgmerge lang.po gramps.pot -o newlang.po

  or

      msgmerge --no-wrap lang.po gramps.pot -o newlang.po

  where `lang` is your language code. The `--no-wrap` option will prevent changes due to automatic word wrapping, use it if your previous po file was constructed like that. The `--no-wrap` options allows for more readable Git diffs.
- Check fuzzy messages and translate all untranslated messages in `newlang.po`. When you are sure everything is right, rename `newlang.po` as `lang.po` and check it into Git as you did with the original file.
- If command `msgmerge` is not available on your system, you have to install the `gettext` package. For [windows users](http://wiki.wxpython.org/index.cgi/Internationalization#How_to_get_gettext_tools_for_Win32).
- To back-port translations, <abbr title="exempli gratia - Latin phrase meaning 'for example'">e.g.</abbr>, to merge master branch translations onto an earlier branch, do this on the earlier branch (assuming gramps.pot is updated):

<!-- -->

    msgmerge -C lang.po master-lang.po gramps.pot -o newlang.po

. Then resolve the fuzzies as usual.

There is also the make target that does the following:

- Create new `gramps.pot` template from the source code files

`  cd po`  
`  ./genpot.sh or python update_po.py -p see `[<code>differences between tools</code>](wiki:Talk:Translation_environment4)`.`

- Updates each `po` file in the source tree

It may be an overkill for you, but if you feel like using it, you can run:

`  cd po`  
`  python update_po -m all  `

in the `po` directory. This assumes that you have already successfully configured the source. Note, this command ignores `--no-wrap` option, so not practical for Git diffs.

### Testing your update

You can test your update easily with the above mentioned **check_po** file. If you downloaded this file, just do:

`python check_po --skip-fuzzy newlang.po`

If everything is ok, the output will be something like this:

`File:               newlang.po`  
`Template total:     3075`  
`PO total:           3075`  
`Fuzzy:              0`  
`Untranslated:       0`  
`%s mismatches:      0`  
`%d mismatches:      0`  
`%() name mismatches:0`  
`%() missing s/d:    0`  
`Runaway context:    0`  
`XML special chars:  0`  
`Last character:     0`  
`Shortcut in msgstr: 0`  
`PO Coverage:        100.00%`  
`Template Coverage:  100.00%`

### Installing your translation

You want to use the new translation immediately, and systemwide? You can by installing just the contents of the po directory, but you will need to build the source first, so:

`./autogen.sh`  
`make`  
`cd po`  
`make --prefix=/usr install     #as root !`

This should install your translations to */usr/share/locale/{lang}/LC_MESSAGES/gramps.mo*, with {lang} being your language. You could of course copy your files manually to that dir with the gramps.mo name.

Make sure you only install from within the po directory, or you will install the development version of Gramps, which is not supported and for testing only!

#### Running the master branch with your translation

The i18n data are often under *../share/locale* according to the default prefix.

So you can use:

`python setup.py build`  
`python setup.py install     #as root !`

This will install the .mo files under *../share/locale/xx/LC_MESSAGES*, according to the default prefix set.

or

`python setup.py build`  
`python setup.py install --root=/home/joe/gramps`  
`                        --prefix="/home/joe/gramps4" `  
`                        --enable-packager-mode     #as simple user !`

This will install Gramps and translations under your */home/...* directory.

##### \$GRAMPSI18N (for your locale)

Actually you don't even need to install the files in order to test them. This is useful because you can develop Gramps without needing superuser privileges. Bear in mind the Gramps i18n process goes something like this when you use the master branch:

- when you type `python build` in the source tree root (/home/user/Gramps <abbr title="exempli gratia - Latin phrase meaning 'for example'">e.g.</abbr>) all the po/\*.po files are compiled into build/mo/{lang}/\*.mo files.
- when you type `python install` inside the po directory, these .mo files are copied to {prefix}/share/locale/{lang}/LC_MESSAGES as gramps.mo files.

But you can change the place where Gramps looks for these files by altering the environment variable \$GRAMPSI18N. So you could also for instance do something like this and avoid the `python setup install` step: (if you are using csh or tcsh the syntax would be a little different)

` [user@localhost /home/user/Gramps]$ mkdir -p po/en_GB/LC_MESSAGES`  
` [user@localhost /home/user/Gramps]$ cp po/en_GB.gmo po/en_GB/LC_MESSAGES/gramps.mo`  
` [user@localhost /home/user/Gramps]$ cd gramps`  
` [user@localhost /home/user/Gramps/src]$ GRAMPSI18N=$PWD/../po LANG=en_GB.UTF-8 python gramps.py`

##### gramps.sh

On a gramps launcher (copy from *`{prefix}/bin/gramps`*) you can set :

`export GRAMPSDIR=/...`  
`export GRAMPSI18N=/...`

Where the environment variable *\$GRAMPSDIR* is the path to your *gramps* directory.

Where the environment variable *\$GRAMPSI18N* is the path to your *gramps locale* directory.

##### Just testing your translation

If you don't want to compile all translations, you may save your *.po* file as *.mo* file, or use *msgfmt* utility on /po directory:

`msgfmt -o gramps.mo your_lang.po`

`msgfmt.exe -o gramps.mo your_lang.po`

this will create a *gramps.mo* file, a compiled version of your *.po* file. Put it on your translation path (*see above*).

## Hard to translate phrases

Some things are just hard to translate. Below are a few of the more difficult items, along with some suggestions on how to handle them.

### Gramps terminology

There are terms with special significance in computer software. The terms are often creatively awkward constructs in English... just so the term is more unique and stands out in a sentence. Translating the words literally or substituting a translation of the underlying concept may not be workable. It may be necessary to become *creative* and substitute a similarly awkward (and short!) label in your target language.

The labels of some Gramps core concepts or interface elements hold that higher level of significance. These must be translated consistently between the User Interface and the Wiki. (Inconsistent translations will confuse the users.)

*Example:* The **[Active Person](wiki:Gramps_Glossary#active_person)** in Gramps is not a person with a healthy amount of vigorous physical exercise. Instead, it is the record from the [People](wiki:Gramps_Glossary#people) [Category](wiki:Gramps_Glossary#category) that is the focal center of reference for display & change. Neither would translate into a memorable label.

The [Gramps Glossary](wiki:Gramps_Glossary) is a good resource for understanding the context and significance of such terms. If you translate the Glossary and then alphabetize the translated terms, also leave an ID SPAN with the untranslated English term. This allows hotlinks from untranslated pages to work in unison with translated hotlinks.

If it becomes necessary to be *creative* translating a term, please add a [language specific](wiki:Translating_Gramps#Language_specific_pages) reference page for your language. This helps other Translators share your style of creativity.

### LDS terminology

The Church of Jesus Christ of Latter Day Saints (a.k.a. Mormons) maintains a lot of genealogy data. In the United States, they are probably the non-government organization with the most detailed records available. Genealogical research is important to the Mormon church. They are responsible for defining the [GEDCOM](wiki:GEDCOM) format.

The LDS Church has some specific terminology that can present difficulty in translating. There are two approaches to handling the information.

1.  If the LDS Church has a presence in your country, contact the LDS Temple in your area and ask them what the correct terminology is in your native language
2.  If the LDS Church does not have a presence in your country, it would probably be safe to simply not translate the phrases.

These terms include:

1.  LDS Ordinance names:
    - Sealed to Parents
    - Sealed to Spouse
    - LDS Baptism
    - Endowment
2.  LDS Status names for Ordinances:
    - Child
    - Cleared
    - Completed
    - Infant
    - Pre-1970
    - Qualified
    - Stillborn
    - Submitted
    - Uncleared
    - BIC (Born In the Covenant)
    - DNS (Do Not Submit)
    - Canceled
    - DNS/CAN (Do Not Submit/Previous sealing cancelled)

## Advanced issues

### Format line parameters

Format line parameters such as %s and %d **should not** be translated. The order of these parameters **should not** be changed. Examples:

English:

`   Long widowhood: %s was a widow %d years.`

Translation (using Backward English as an example :-):

`   Gnol doohwodiw: %s saw a wodiw %d sraey.`

Named format line parameters such as %(something)s and %(something)d also **should not** be translated. Feel free to change the order of named parameters to correctly phrase the message in your language. Also, use hints provided by the names. Examples:

English:

`   Baptized before birth: %(male_name)s`  
`           born %(byear)d, baptized %(bapyear)d.`

Translation into Backward English:

`   Dezitpab erofeb htrib: %(byear)d`  
`           nrob %(male_name)s, dezitpab %(bapyear)d.`

In the above example, the verb "born" should be in masculine form (if verbs in your language have gender, that is), since the person born is apparently a male.

Sometimes those %(something)s are positioned in a text without spaces, like in the example below:

English:

`   This person was baptised%(endnotes)s.`

Translation into Backward English:

`   Siht nosrep saw desitpab%(endnotes)s.`

### Translation context

In some cases, two different concepts can be expressed by the same word in English and yet require different translations. For example, the **title of the book** and the nobility **title of the person** are expressed by the same **Title** word. However, in other languages different words are needed to describe the book title and the person's title.

To mitigate such problems, a context can be added to the translation string. A context-enabled string has a vertical line separating the context from the string:

`book|Title`  
`person|Title`

The correct translation **should not** include either the context or the separator. The context is to give the translator idea of what the string means. However, **both the context and the separator must not be in the translated string**, so in backward english the above is translated into

`Eltitkoob`  
`Eltitnosrep`

If you are a Gramps translator and need a developer to help you add a context to the Gramps source files, please ask for it on the gramps-devel list.

#### Translation context in GUI labels

If there is a string in the Glade GUI (i.e., in a .glade source file) that requires the translation context, it's impossible to have it translated statically. In this case, one needs to add runtime code to the corresponding dialog initialization to override the label string with the text obtained with an sgettext call. I.e.,

- Verify the relevant widget has a meaningful id in the .glade file (as opposed to a silly autogenerated one). Modify the id if needed and make sure no existing code used the old widget id! <abbr title="exempli gratia - Latin phrase meaning 'for example'">e.g.</abbr>, change

<object class="GtkLabel" id="label3">

  
into

<object class="GtkLabel" id="place_name_label">

- Add a context to the translatable string in the .glade file. This way, when you look at the POT file or a PO file derived from it, you see a reference to this place, along with the actual place in the .py file(s) which also has the same context string. <abbr title="exempli gratia - Latin phrase meaning 'for example'">e.g.</abbr>, change

<property name="label" translatable="yes">`Name:`</property>

  
into

<property name="label" translatable="yes">`place|Name:`</property>

- In the corresponding dialog initialization, add code to set the string to the correct translation during runtime, <abbr title="exempli gratia - Latin phrase meaning 'for example'">e.g.</abbr>,:

  
globally in the file:

`PLACE_NAME = _('place|Name:')`

  
in the MergePlace.\_\_init\_\_ method:

`       for widget_name in ('name_btn1', 'name_btn2'):`  
`           self.get_widget(widget_name).set_label(PLACE_NAME)`

  
The exact method to call on the Gtk control will be different based on the actual GUI element affected. <abbr title="exempli gratia - Latin phrase meaning 'for example'">e.g.</abbr>, a GtkButton has a set_label method, whereas a GtkLabel has a set_text.

- Regenerate the POT, translate the new PO strings, and test your work.

### Plural forms

There was requests for [plural forms](http://www.gnu.org/software/gettext/manual/html_node/gettext_150.html#Plural-forms) support.

First, translators need to check if information is available on .po header :*"Plural-Forms:\n"*. (See [samples](http://translate.sourceforge.net/wiki/l10n/pluralforms))

1.  msgid contains the singular string in english
2.  msgid_plural contains the plural string in english
3.  msgstr\[0\] contains the singular translated version (for 1 and sometimes 0, set on header)
4.  msgstr\[1\] contains the plural version (for 1 + 1 = 2 )
5.  msgstr\[2\] contains the plural form (for 2 + 1 = 3)

- For language with one form (singular=plural, *Plural-Forms: nplurals=1; plural=0*), like Chinese, Hungarian or Turkish:

`msgid "%d second"`  
`msgid_plural "%d seconds"`  
`msgstr [0] "%d 秒"`

- For language with one plural form (*Plural-Forms: nplurals=2; plural=n != 1;*), like english:

`msgid "%d hour"`  
`msgid_plural "%d hours"`  
`msgstr [0] "%d hour"`  
`msgstr [1] "%d hours"`

- For language with more plural forms (like Czech):

`msgid "%d second"`  
`msgid_plural "%d seconds"`  
`msgstr [0] "%d sekunda"`  
`msgstr [1] "%d sekundy"`  
`msgstr [2] "%d sekund"`

As a final check, please do ensure that the following command does not throw any errors:

`msgfmt -c filename.po`

### Translating mnemonics keys(Keyboard Shortcut keys)

Mnemonics are accelerator keys (also known as Keyboard Shortcut keys) you find in labels, accessible by pressing the key together with the mnemonic. You see then in the translated text with a low line, <abbr title="exempli gratia - Latin phrase meaning 'for example'">e.g.</abbr>, '\_Help' is shown as 'Help' with an underline under the H, and can be put to focus/selected by pressing .

It is nice if mnemonics on a screen are unique, but it is not required. If you use twice the same mnemonic, the user must press repeatedly the accelerator to switch between the different entries. However, note the following rule:

- "If duplication of access keys in a window is unavoidable, you should still refrain from duplicating the access keys for any of these buttons that appear in the same window: , , , or ."

So you should check in your language what the mnemonic key is for those buttons, and avoid using the same in translated text

Capital letters are no problem though, underlining <abbr title="exempli gratia - Latin phrase meaning 'for example'">e.g.</abbr>, G will work just fine as the letter does not write over the line.

### Translating relationships

Translating relationships is not done within the `.po` files, except for occasional `father` and `mother` strings here and there in the interfaces and reports. Complete translation of all relationships for the language/culture is done inside a relationship calculator plugin.

In short, the need for a plugin comes from the impossibility to translate "first cousin twice removed" in languages such as, <abbr title="exempli gratia - Latin phrase meaning 'for example'">e.g.</abbr>, German or Russian. See the [Relationship Calculator](wiki:Relationship_Calculator) page for details on why and how to create such a plugin.

### Translating dates

Handling date translation is not entirely done within the `.po` files. Complete handling of date translation for each language/culture is done inside a dedicated date handler module.

The need for a separate module comes from the requirements to handle culture-specific parsing and displaying of dates. For example, the month and day order is different between most European countries and the US. Also, each language has its own set of acceptable modifier and qualifiers for the date: things like "from X to Y" or "between X and Y" may have different word order. Same with "around", "calculated", "estimated". Add to this calendar names, and you have a compelling need for a dedicated module. See the [Date Handler](wiki:Date_Handler) page for details on why and how to create such a module.

## Translating man pages

You can also translated the man pages into your own language.

For the development version (master branch) you can find the required starting files under the directory data/man. You will find the files

- Makefile.am
- gramps.1.in

First off all you must make a directory for your language under data/man.

`cd data/man`

and do

`mkdir xx`

where xx is your languagecode (fr for French, sv for Swedish, etc.) You should use Git. See [the introduction to Git](wiki:Brief_introduction_to_Git).

Next step is to copy the Makefile.am and gramps.1.in from data/man to your new directory. Translate all relevant strings in the data/man/xx/gramps.1.in file. Change the file data/man/xx/Makefile.am:

- add the line mandir = @mandir@/xx
- change the line && CONFIG_FILES=data/man/xx/\$@ \$(SHELL)

Next step: change the file data/man/Makefile:

- add xx to the line SUBDIRS = fr nl sv

The final step is to alter the file *Configure.in*:

- add data/man/xx/Makefile to the line AC_CONFIG_FILES(\[

All changes must be committed and pushed to the server:

`git commit -am "Add man page for xx"`  
`git push`

You should see no errors when you run the

`./configure`  
`make`  
scripts.

`sudo make install`

This will put the gramps.1.gz file into /usr/local/share/man/xx/man1 directory. You could also use a prefix. Then you do:

`sudo make --prefix=/usr/share install`

To see the result of your work, do:

`man -L xx gramps`

## Translating wiki manual

To enable the weblink for help when pressing the button in the Gramps program, you need to have or edit the `MANUALS` variable to contain your language code locale in the:

[display.py](https://github.com/gramps-project/gramps/blob/master/gramps/gui/display.py) file for Gramp 4.x or greater

or

GrampsDisplay.py file for Gramps 3.x or earlier

On approximately line 41 of that file, you may see:

`#list of manuals on wiki, map locale code to wiki extension, add language codes`  
`#completely, or first part, so pt_BR if Brazilian portugeze wiki manual, and`  
`#nl for Dutch (nl_BE, nl_NL language code)`  
`MANUALS = {`  
`   'nl' : '/nl',`  
`}`

These entries map a language code to the extension used on the wiki, so to add french, change this too:

`MANUALS = {`  
`   'nl' : '/nl',`  
`   'fr':  '/fr',`  
`}`

- Every '`manual|...`' entry in the `gramp.pot` file refers to a section in the manual, so make sure to use good section headings so this does not change too much over time.

Note that reports/tools link to a section in the page with the same name as the report name in Gramps.

- You should be able to edit directly on wiki or using tools like [txt2po](http://translate.sourceforge.net/wiki/toolkit/txt2po) or [po4a](http://po4a.alioth.debian.org/). Also previous gettext file for the manual and [Translation Memory](http://en.wikipedia.org/wiki/Translation_memory) may help you to upgrade deprecated/old gettext files. <abbr title="exempli gratia - Latin phrase meaning 'for example'">e.g.</abbr>, store existing entries from */usr/share/locale*.

## Language specific pages

Check out the pages which cover some aspects of translation into a specific language, such as the glossary.

- [Finnish](wiki:Translation_into_Finnish)
- [French (Français)](wiki:Translation_into_French)
- [Russian](wiki:Translation_into_Russian)
- [Hebrew](wiki:Translation_into_Hebrew)

## Translating addon plugins

- See [Third-party addons for Gramps](wiki:Addons_development#Get_translators_to_translate_your_addon_into_multiple_languages).

[Category:Translators/Categories](wiki:Category:Translators/Categories) [Category:Developers/General](wiki:Category:Developers/General)
