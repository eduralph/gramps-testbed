---
title: What to do for a release
categories:
- Developers/General
- Developers/Packaging
managed: false
source: wiki-scrape
wiki_revid: 131324
wiki_fetched_at: '2026-05-30T18:18:56Z'
---

Note that the main use of this page will be for making a normal "minor" release. If you are making a "major" release (e.g. x.y.0) then you will need to update this page first, to change the numbers. But if you are only making an "alpha" or "beta" release, some steps may be skipped, or altered slightly.

Note also that there are additional necessary [Post release](wiki:What_to_do_for_a_release#Post-release) tasks which are related to making a new release. For instance, the wiki will require making a new release-section and updating ["General" version templates](wiki:Template:Version_Templates#General). For the making a new release-section on the bug tracker. Or when making new Debian and Mac and Windows [packaging](wiki::Category:Developers/Packaging), they will need to be coordinated with the appropriate [package maintainers](wiki:Team#Package_Maintainers) and updating the corresponding [Versions](wiki::Category:Versions) : [Templates](wiki:Template:Version_Templates).

## Pre-release

### Agree a release timetable

Co-ordinate with the [package maintainers](wiki:Team#Package_Maintainers) to agree a release timetable. For a major release there may be a schedule on the [Roadmap](wiki:5.2_Roadmap)

### Announce a feature freeze

For a major release, announce a feature freeze on the *gramps-devel* mailing list. This will usually be about 4 weeks before the release date.

### Translation update

The translation template should be updated, if necessary, just before the string freeze is announced.

- Check for new files since the last release:

` cd po`  
` intltool-update -m `

  
That will create a file called `missing`in the `po` directory if there are new files that need to be scanned for translatable strings. Examine each of the files listed in `missing`, adding each to `POTFILES.in` if it contains translatable string constants and to `POTFILES.skip` if it does not.

- Generate a new template file:

` python update_po.py -p # makes a new gramps.pot template file`  
` git diff gramps.pot`

  
Examine the changes. If they're all just comments about where a string is found you need not commit the change (so the next line will restore the official file, instead of the one you just made):

` git restore gramps.pot`

  
If there have been changes on `msgid` entries, you'll need to commit `gramps.pot` and ask translators to update their `.po` files before you can make a release:

` git add gramps.pot`  
` git commit -m "Update translation template for new release"`  
` git push`

  
After updating the `pot` file, push the changes and wait for Weblate to update the `po` files. Merge the corresponding pull request from Weblate.

- Check current translation files:

` python update_po.py -k all`

  
There should be very few warnings and no fatal errors. Warnings related to new languages using default values in their headers are acceptable. All fatal errors should be fixed.

Also see:

- [Template:Gramps_translations#INCOMPLETE_TRANSLATIONS](wiki:Template:Gramps_translations#INCOMPLETE_TRANSLATIONS) - Update if any translation needs to be added or excluded due to not meeting the minimum 70% completion requirement.

### Announce a string freeze

For a major release, announce a string freeze on the *gramps-devel* mailing list and on Weblate. This will usually be about 2 weeks before the release date.

In the *Program* component on Weblate, select "Manage⟶Post announcement" from the menu. Enter an *Expiry date* the day before the release date, and select the *Notify users* checkbox to send a notification to all subscribed users.

## Prepare your repository

- Check out the current stable branch:

` git checkout maintenance/gramps`

  
That branch name assumes that you're using the same name as the Github repository; if you're not (perhaps you don't use `maintenance` in the name) use your local name.

- Make sure that your local copy is clean:

` git status`

  
If you have any uncommitted changes, either commit them now or stash them until after you've completed the release.

- Clean up any untracked files and make sure that the local repo is up to date:

` git clean -fdx`  
` git pull --rebase`

  
If you had commits that hadn't been pushed yet they'll show up as "applying" messages in the output of this command. If that's the case re-run the tests and push as usual.

- Build and test to make sure that everything works, then clean the repo of all build products.

### Check the About box year

Check if the year in the box needs to be updated

eg:

`  `*`© 2007-2025 The Gramps Developers`*` `

to

`  `*`© 2007-`**`2026`**` The Gramps Developers`*`.`

Found in `gramps/gen/const.py`

### API docs update year

If needed in the file:

docs/conf.py

Update the year for the copyright.

`copyright = '2001-2026, The Gramps Project'`

### Update Classifier in pyproject.toml

Change [Classifier](https://pypi.python.org/pypi?%3Aaction=list_classifiers) to the appropriate one in [pyproject.toml](https://github.com/gramps-project/gramps/blob/maintenance/gramps61/pyproject.toml) (master is always the first one)

    Development Status :: 1 - Planning
    Development Status :: 2 - Pre-Alpha
    Development Status :: 3 - Alpha
    Development Status :: 4 - Beta
    Development Status :: 5 - Production/Stable

Check if any additional language classifier needs to be added also.

## Release name

Refer to (and update) the [list of previous releases](wiki:Previous_releases_of_Gramps).

Previously you needed to select an appropriate name but we have not named releases for several years now. You will still need to add the release though, including things like its relevant color.

- [Suggestions](wiki:Talk:Previous_releases_of_Gramps) : For Gramps 5.0 `Just remember that you're standing on a planet that's evolving`

## Changelog and NEWS file

[Section *2a*](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html#section2) of the **G**eneral **P**ublic **L**icense says that if you distribute a modified version of a program: *you must cause the modified files to carry prominent notices stating that you changed the files and the date of any change*.

Note that the below means the *previous* version, not the one you're about to release (which is the `..`).

`git log v``.. --pretty --numstat --summary --no-merges | git2cl > ChangeLog`  
`git log v``.. --pretty --numstat --summary --no-merges -- po/*.po | git2cl > po/ChangeLog`  
`git add ChangeLog`  
`git add po/ChangeLog`

- Edit and update the `NEWS` file using the new ChangeLog entries as a guide. If this is the first branch in a new series there will be no NEWS file, so look at a previous release and mimic the format.

Commit the NEWS file:

`git add NEWS`  
`git commit -m "Update ChangeLog and NEWS files"`

## Working on VERSION

- Modify [`gramps/version.py`](https://github.com/gramps-project/gramps/blob/master/gramps/version.py). Update `VERSION_TUPLE` to the new version and set `DEV_VERSION` to indicate an official release:

`VERSION_TUPLE = (4, 2, ...)`

`- DEV_VERSION = True`  
`+ DEV_VERSION = False`

- Add an entry to the [org.gramps_project.Gramps.metainfo.xml.in](https://github.com/gramps-project/gramps/blob/maintenance/gramps52/data/org.gramps_project.Gramps.metainfo.xml.in) file.

<!-- -->

- Save the changes:

`git commit -am "Release Gramps ``"`

- Check that the version number is correct:

`python Gramps.py -v`

- If everything looks good, push the changes:

` git push origin maintenance/gramps`

- If that fails then someone pushed a commit while you were working. Return to [Prepare your repository](wiki:What_to_do_for_a_release#Prepare_your_repository) and start over.

## Create a tag

Create the release tag; note the **v** leading the actual tag.:

`git tag -am "Tag ``" v`

## Push to repository

Push the changes to the repository:

`git push origin v`

### Update DEV_VERSION to indicate a development version

Revert change on `DEV_VERSION` in `gramps/version.py` so that the git revision is appended to the reported version in non-release builds:

`- DEV_VERSION = False`  
`+ DEV_VERSION = True`

Save change:

`git commit -am "Set to development version"`  
`git push`

### Github

- Github generates a tarball automatically when we push a tag.
- Go to [Github](https://github.com/gramps-project/gramps) and log in if necessary.
- Select **NN Releases** from the line of items just above the thick line (**NN** is the number of releases so far).
- Find the tag you just pushed and click it, or click the "Draft a new release" button.
- Copy the NEWS file contents into the **Write** tab. You can use the **Preview** tab to check your formatting.
- Add the sh256sum of the source distribution to the bottom of the release notes.

You can obtain the sha256sum with the following command:

`git archive --format=tar --prefix=gramps-`` v`` | gzip | sha256sum`

Alternatively, download it and use:

`sha256sum gramps-``.tar.gz`

- Click **Publish Release** at the bottom of the edit area when you're satisfied with the contents.

### SourceForge

- Go to [the SourceForge files page](https://sourceforge.net/projects/gramps/files/) and log in if necessary.
- Click on **Stable** or **Unstable** depending on the class of the release you're making.
- Click **Add Folder** and name the directory for the release version. Click "'Create'". Click your new folder to enter it.
- You can either download the GitHub-generated tarball or create one locally:

` python -m build --sdist`

- Click **Add File** and drag the tarball to the drop area on the web page.
- Copy the release notes from GitHub into a file called README.md and upload it.

## Announcing the new release

- update mantisdb(Bug/issue database) and enable the new version via Admin:Projects item for reporting issues. (You will need a high-enough status on the bug tracker in order to do this, so you can ask an appropriate person if you aren't.)
- announce on gramps-announce@lists.sourceforge.net, gramps-devel@lists.sourceforge.net and gramps-users@lists.sourceforge.net (You will need to be a member of all three lists first, to send to them.)
- announce on the Discourse forum in the "[Announcements](https://gramps.discourse.group/c/gramps-announce)" category.
- announce on Gramps [blog](https://gramps-project.org/blog/blog/) (File under: [Gramps Releases](https://gramps-project.org/blog/category/releases/) and [News](https://gramps-project.org/blog/category/news/)) (not needed for an alpha or beta release)
- update [News](wiki:News) section on this wiki (not needed for an alpha or beta release)
- update the list of [previous releases](wiki:Previous_releases_of_Gramps)
- update reference to the new version on the [wiki template](wiki:Template:Version) <small></small> (not needed for an alpha or beta release)
- Verify other ["version" Wiki templates](wiki::Category:Versions) values: Last version, Stable version, etc.
- update [HeadlineNews](wiki:HeadlineNews) (not needed for an alpha or beta release)
- update {{version-released}} [date template](https://gramps-project.org/wiki/index.php/Template:Version-released) for the [Download](wiki:Download) pages <small></small> (not needed for an alpha or beta release)
- change the Matrix room title and IRC channel title (not needed for an alpha or beta release)
- update the version number at [Wikipedia](https://en.wikipedia.org/wiki/Gramps_(software)) (not needed for an alpha or beta release)

## Post-release

- merge forward the `NEWS` file

# See also

- Category [Versions](wiki::Category:Versions) : [Template](wiki:Template:Version_Templates)
- Building a distribution to share as on the [Download](wiki:Download) page

  
![[_media/Windows_32x32.png]] [Building Gramps AIO cx freeze-based](wiki:Building_Gramps_AIO_cx_freeze-based) - Updating the MS-Windows All-In-One package

- [Brief introduction to Git](wiki:Brief_introduction_to_Git)
- [Running a development version of Gramps](wiki:Running_a_development_version_of_Gramps)
- [:Category:Developers/Packaging](wiki::Category:Developers/Packaging)
- [:Category:AppData](wiki::Category:AppData) - Screenshots used by Appdata - Debian
- [.dtd and .rng](wiki:.dtd_and_.rng)
- [Rollover for the Wiki](wiki:Rollover_for_the_manual) - for major and feature releases. No rollover for maintenance releases.
- [List of pages linked to Bug Report template](wiki:Special:WhatLinksHere/Template:Bug) - verify the reported issues still apply to the new release. Leave links in place for any issue fixed in maintenance releases. Simply add notations for the version where the fix was applied. Remove links for fixed issues in Rollovers.

# External links

- <https://github.com/gramps-project>
- <https://gramps-project.org/cpanel>
- <https://sourceforge.net/projects/gramps/>

[Category:Developers/General](wiki:Category:Developers/General) [Category:Developers/Packaging](wiki:Category:Developers/Packaging)
