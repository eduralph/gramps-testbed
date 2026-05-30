---
title: Brief introduction to SVN
categories:
- Developers/General
managed: false
source: wiki-scrape
wiki_revid: 124224
wiki_fetched_at: '2026-05-30T18:10:41Z'
---

<s>[<http://svn.code.sf.net/p/gramps/code/>](http://svn.code.sf.net/p/gramps/code/)</s>. No longer available see Github for code.  

This helps synchronizing changes from various developers, tracking changes, managing releases, etc. If you are reading this, you probably want to do one of two things with SVN: either download the latest source or the development version, or else upload your changes (if you have write access to the repository) or [make a patchfile](wiki:Brief_introduction_to_SVN#Making_a_patchfile) (if you don't have write access).

- All developers should read Gramps [Committing policies](wiki:Committing_policies)

## Types of branches

There are four kinds of branches in the Subversion Repository:

- *trunk* - There is only one trunk. All new feature development happens in the trunk. New releases never come from the trunk. The trunk for Gramps can be found here: <http://svn.code.sf.net/p/gramps/code/trunk>

<!-- -->

- *maintenance* - There are many maintenance branches. A maintenance branch is created from the trunk when all the features for a release are complete. New features are not committed to maintenance branch. Releases only come from maintenance branches. The purpose of maintenance branches is to allow the line of code to stabilize while new features are added in trunk. Maintenance branches can be found here: <http://svn.code.sf.net/p/gramps/code/branches/maintenance>

<!-- -->

- *geps* - These are meant for development of [Gramps Enhancement Proposals](wiki:Portal:Enhancement_Proposals). Most of the time GEPS are developed in the *trunk*. Occasionally a GEP will require extensive reworking or long periods when the code base is unusable. In these cases a branch in *geps* can be used as a temporary development area. Once the hard work is done the change should be merged into the trunk and the *geps* branch should be removed. *greps* branches should follow the naming convention *gep-\<###\>-<descriptive text>* e.g. *gep-013-server*. Please read the [#Working with development branches](#Working_with_development_branches) section for help with managing these branches.

<!-- -->

- *sandbox* - These are meant for experimentation purposes. If you want to explore some ideas or try out some changes that would break the *trunk* or prototype something that has not made it to a GEP you can create a *sandbox* branch. These should be short lived. As soon as you have finished please remove the branch. We reserve the right to remove any *sandbox* branch that has not been touched for 12 months. *sandbox* branches should use the following naming convention *<username>-<descriptive text>* e.g. *hippy-prototype-rss-idea*. Please read the [#Working with development branches](#Working_with_development_branches) section for help with managing these branches.

Release tags are created in the *tags* directory. The first two digits of the Gramps version number are reserved to indicate the maintenance branch the code came from. The last digit indicates the revision from that maintenance branch. For example, 3.0.4 would indicate the 5th release from the 3.0 branch (3.0.0, 3.0.1, 3.0.2, 3.0.3, 3.0.4).

Here is a hypothetical example: Imagine that the current version of Gramps is 8.3.2. A new series of features has been added in trunk and are ready for release. A new maintenance branch is created from trunk named 8.4 (or possibly 9.0 depending on the nature of the new features). New features continue to be added in trunk that will not be included in the 8.4 series of releases, but will be included in the 8.5 series. Bug fixes continue to occur in the 8.4 branch until the code is deemed worthy of release. At that time, a release is tagged from the 8.4 maintenance branch and named 8.4.0. Some time after the release of 8.4.0, some bugs are found and fixed in the 8.4 maintenance branch. Those bug fixes are released as 8.4.1.

## Stable version

- To download the source to a ~/gramps41 directory, you can use two methods to access the SVN repository:

1.  An http frontend to gramps SVN
2.  SVN access

- To upload your changes, you have to have developer access.

The second method requires that svn be installed on your system (Debian/Ubuntu: `apt-get install subversion`; Fedora: `yum install subversion`). With the SVN method, type the following in the command line if you **don't have a sourceforge account**:

`svn co http://svn.code.sf.net/p/gramps/code/branches/maintenance/gramps41 gramps41`

You should see the downloading progress reported in your terminal.

If you have a sourceforge account, use https instead:

`svn co https://svn.code.sf.net/p/gramps/code/branches/maintenance/gramps41 gramps41`

You will in this case be requested for your root keyring password which will store your sourceforge credentials, and next your password. If the user on your PC is not the same one as on sourceforge, leave password empty and press enter, you will then receive the option to enter a username first, and then the sourceforge password for that username.

If you would like to update your source tree after some time, execute the following command in the top directory of the gramps41 source tree:

`svn update`

To commit your changes, you need to have checked out the gramps code with https, and have commit access to the Gramps repository (the Gramps admin can give you this, [Brian Matherly or Benny Malengier](wiki:Contact)). Commit happens if execute:

`svn commit -m "message describing the nature of the change"`

Since uploading is a potentially dangerous operation, most people do not obtain write access to the SVN repository. In this case, create a patch, and commit this on the [ticket tracker](http://bugs.gramps-project.org). You can do this in the top gramps directory as follows:

`svn diff > mychanges.patch`

A developer can apply this patch then with the command:

`patch -p0 < mychanges.patch`

## Unstable development: "trunk"

  
Also see: [Getting started with Gramps Trunk](wiki:Getting_started_with_Gramps_Trunk).

### Obtain it

There are several versions of the gramps code in SVN.

The development branch for small changes and bug fixes is *gramps41* and *trunk* has been created for the ongoing unstable version.

If this talk of *branch* and *trunk* sounds confusing you might like to read the list message [explaining branch and trunk](http://sourceforge.net/mailarchive/message.php?msg_id=19238907).

*'Replace in the commands here*https*by*http'' if you do not have a sourceforge account.

To checkout a copy of the possibly unstable trunk to ./trunk:

`svn co https://svn.code.sf.net/p/gramps/code/trunk trunk`

To checkout a copy of the last branch Gramps 4.0 ./gramps40:

`svn co https://svn.code.sf.net/p/gramps/code/branches/maintenance/gramps40 gramps40`

To checkout a copy of the last branch Gramps 3.4 ./gramps34:

`svn co https://svn.code.sf.net/p/gramps/code/branches/maintenance/gramps34 gramps34`

To checkout a copy of the last branch Gramps 3.3 ./gramps33:

`svn co https://svn.code.sf.net/p/gramps/code/branches/maintenance/gramps33 gramps33`

To checkout a copy of the last branch Gramps 3.2 ./gramps32:

`svn co https://svn.code.sf.net/p/gramps/code/branches/maintenance/gramps32 gramps32`

To checkout a copy of the last branch Gramps 3.1 ./gramps31:

`svn co https://svn.code.sf.net/p/gramps/code/branches/maintenance/gramps31 gramps31`

To checkout a copy of the older stable Gramps 3.0 ./gramps30:

`svn co https://svn.code.sf.net/p/gramps/code/branches/maintenance/gramps30 gramps30`

To checkout a copy of the older stable Gramps 2.2 ./gramps22:

`svn co https://svn.code.sf.net/p/gramps/code/branches/maintenance/gramps22 gramps22`

### Prepare gramps40 and trunk

Now go into the `trunk` directory and type

`python setup.py build`

### Prepare gramps34 and before

The old versions of Gramps use autotools, so you need to run

`./autogen.sh`  
`make`

#### Building with Fedora 8 - 10

These are the packages you need:

`yum install intltool gnome-doc-utils gettext subversion rcs`

#### Windows

This step appears unnecessary on windows? See [Installation#Building_from_source](wiki:Installation#Building_from_source)

### Run the development version

As you should not install the development version, how can you try it out? The current Python version required to run Gramps trunk is officially python2.7 as of July 2012.

#### Option 1: run from source repo

Here, we use the code in `trunk` directory to run Gramps. This means that compiled python files will be stored there. This is not ideal, but the easiest way to develop Gramps, as changes are immediately picked up by the code.

Copy the const.py file created in build to your source directory if you want to use your source directory to work with Gramps:

`cp build/lib.linux-$(uname -m)-2.7/gramps/gen/const.py gramps/gen/const.py`  
`python Gramps.py`

*Note*: the `lib.linux-$(uname -m)-2.7` folder name vary depending on your system (i686 or x86_64).

That is it. If you installed some dependencies of Gramps in non-default positions, you need to indicate with PYTHONPATH where they can be found, and with LD_LIBRARY_PATH where link libraries can be found. Eg, if you install GTK and spell checking from source too, you will need something like:

` PYTHONPATH=/usr/local/lib/python2.7/site-packages/ LD_LIBRARY_PATH=/usr/local/lib python Gramps.py`

#### Option 2: use the build code

Here, we use the code build in `trunk/build` directory to run Gramps. For compiled programs this is the only way, but for Gramps nothing is compiled. It is not bad however to keep your code separated from your execution, as deleting the build directory is easy. After a code change in your source, you then need to run however `python setup.py` again to update the build direcotry. To run Gramps from build, do

` cd trunk/build/lib.linux-$(uname -m)-2.7/`  
` python -c 'from gramps.grampsapp import main; main()'`

Again, it might be needed to set with PYTHONPATH where dependencies can be found, and with LD_LIBRARY_PATH link libraries, see option 1.

If you point your PYTHONPATH to the build directory, you can actually run Gramps from a random directory. Like this:

`cd`  
`PYTHONPATH=~/gramps-trunk/build/lib.linux-$(uname -m)-2.7/ python -c 'from gramps.grampsapp import main; main()'`

So, more general:

`cd`  
`PYTHONPATH=~/gramps-trunk/build/lib.linux-$(uname -m)-2.7/:/usr/local/lib/python2.7/site-packages/ LD_LIBRARY_PATH=/usr/local/lib  python -c 'from gramps.grampsapp import main; main()'`

If the build directory is in your PYTHONPATH, you can also just execute the grampsapp.py module. So this will work too:

`cd ~/gramps-trunk/build/lib.linux-$(uname -m)-2.7/gramps`  
`PYTHONPATH=~/gramps-trunk/build/lib.linux-$(uname -m)-2.7/ python grampsapp.py`

or again more generally

`PYTHONPATH=~/gramps-trunk/build/lib.linux-$(uname -m)-2.7/:/usr/local/lib/python2.7/site-packages/ LD_LIBRARY_PATH=/usr/local/lib python grampsapp.py`

**Note**: At the time of writing, only the last, so using grampsapp.py works, as not all imports in Gramps have been converted to relative or absolute imports. This conversion will be finished by end of 2012 however.

### Where for bugs?

The [bug tracker](http://bugs.gramps-project.org) has in the right top angle different projects. Choose project *trunk* and submit an issue.

### Making a patchfile

If you do not have write access to the repository, you can make a patchfile with your changes. This is a text file which can then be sent by email to somebody, or posted/uploaded to the bug tracker (against a bug you are fixing or a feature request which you are solving for instance), etc.

These instructions assume SVN is installed on your system (Debian/Ubuntu: `apt-get install subversion`; Fedora: `yum install subversion`).

These instructions tell how to make a patchfile against trunk, so that your changes are added to the next major release of Gramps. (To make a patchfile against a branch the process is similar, with some slight changes.)

So first checkout a copy of the trunk to ./trunk:

`svn co https://svn.code.sf.net/p/gramps/code/trunk trunk`

Then use your favorite editor to change whatever file(s) you want.

To then use SVN to make a patchfile, first go to the top of your changed tree

`cd /path-to-your-gramps/trunk`

and then tell SVN to record/document/itemize the changes to your edited file(s)

`svn diff > ~/some-descriptive-name.patch`

with the resulting file being the patchfile you just made.

If you want to add a new text file, such as a new python module, you can include that in your patchfile by first doing, e.g.,

`svn add dir1/dir2/newfile.py`

before you do the "svn diff" as described above. (This method does not work for non-text files such as image files; be warned.)

Note also that if you add a file in this manner, depending on what was added and where it was added, you may also have to modify the corresponding Makefile.am file.

(Who is I? - I do not know how to make a patchfile which documents a deleted file which "patch" will then correctly delete. (If you know how, please add it here.) When SVN version 1.7 is released (scheduled for 1Q2011 as I write this), then there will be a "svn patch" command which should do that. (Pat SVN 1.7 is out this is the link talk about [1](http://svnbook.red-bean.com/en/1.7/svn.ref.svn.c.patch.html))

## Working with development branches

If you are using a *geps* or *sandbox* branch you need to take care when merging changes from the *trunk* and back to the *trunk*. Please take a few minutes to read the \[<http://svnbook.red-bean.com/en/1.5/svn.branchmerge.basicmerging.html>\| Basic Merging\] section of the Subversion book.

**IMPORTANT:** please use an svn client that is version 1.5 or newer. The merge tracking functionality only became available in 1.5. If you use an earlier client you will have to deal with all the revision tracking of merges by hand - not fun.

**IMPORTANT:** if you see a message that talks about *from foreign repository* it is probably because your working copy was checked out from an <http://> url but you are merging from a <https://> url or visa versa. Just be consistent about why you use. Don't merge *from foreign repository* because svn will not be able to manage the revisions correctly.

Here is a quick crib sheet:

### Creating a branch

To create a branch from the *trunk*:

`svn copy https://svn.code.sf.net/p/gramps/code/trunk https://svn.code.sf.net/p/gramps/code/branches/geps/gep-014-fab-feature`

### Merging *trunk* changes into the branch

You should do this regularly so that you don't have a nasty job of resolving loads of conflicts when you come to merge your changes back into the *trunk*:

`cd gep-014-fab-feature`  
`svn merge https://svn.code.sf.net/p/gramps/code/trunk`

**NOTE** you will see some modification to files that you are not expecting. If you look at these you will find that they are modifications to svn properties. These are used by the merging tool to keep track of what changes have already been applied.

### Merging changes from the *branch* back into the *trunk*

When you are ready to merge your changes back into the *trunk*:

First make sure you have all the *trunk* changes in your branch:

`cd gep-014-fab-feature`  
`svn merge https://svn.code.sf.net/p/gramps/code/trunk`  
`svn commit -m "meaningful message"`

Then move over to a working copy of the *trunk* and merge in your branch:

`cd trunk`  
`svn merge --reintegrate https://svn.code.sf.net/p/gramps/code/branches/geps/gep-014-fab-feature`  

Now build it, test it, convince yourself that it all works and then commit the changes:

`svn commit -m "All the changes for GEP-014"`

Now you **must** delete your branch. You can recreate it later if you need to but svn can not cope with doing another merge --reintegrate from the same branch:

`svn remove https://svn.code.sf.net/p/gramps/code/branches/geps/gep-014-fab-feature`

### Removing branches

It is important that branches are removed once they have been merged into the trunk or have been abandoned. To remove a branch:

`svn remove https://svn.code.sf.net/p/gramps/code/branches/geps/gep-014-fab-feature`

The developers reserve the right to remove branches that have been dormant for more than 1 year.

## Useful things to know

### Subversion commands

`svn help add`

`svn help commit`

`svn help log`

Adding files to repositories requires you to set some properties to the files and to have a [sourceforge account](http://apps.sourceforge.net/trac/sitedocs/wiki/Subversion). See `svn help propset`. You can use the `propget` on existing files to see how you should add it. A convenient way is to add common files to your `~/.subversion/config` file, eg in my config I have:

`[miscellany]`  
`enable-auto-props = yes`  
  
`[auto-props]`  
`*.py = `[`svn:eol-style=native;svn:mime-type=text/plain;svn:keywords=Author`](svn:eol-style=native;svn:mime-type=text/plain;svn:keywords=Author)` Date Id Revision`  
`*.po = `[`svn:eol-style=native;svn:mime-type=text/plain;svn:keywords=Author`](svn:eol-style=native;svn:mime-type=text/plain;svn:keywords=Author)` Date Id Revision`  
`*.sh = `[`svn:eol-style=native;svn:executable`](svn:eol-style=native;svn:executable)  
`Makefile = `[`svn:eol-style=native`](svn:eol-style=native)  
`*.png = `[`svn:mime-type=application/octet-stream`](svn:mime-type=application/octet-stream)  
`*.svg = `[`svn:eol-style=native;svn:mime-type=text/plain`](svn:eol-style=native;svn:mime-type=text/plain)

#### Workflow

Before switching to another branch it is useful to remove untracked files created by the build process. You can do this with the following commands in that branch directory[2](http://www.jukie.net/bart/blog/svn-clean):

`   svn status --no-ignore | awk '{print $2}' | xargs rm -rf`  
`   svn revert -R .`  
`   svn update`

### Ignore files

You should on creation of new directories set the <svn:ignore> property:

`svn propedit `[`svn:ignore`](svn:ignore)` src/new_dir/`

and there set at least:

`*.pyc`  
`*.pyo`  
`Makefile`  
`Makefile.in`

### svn2cl

The Gramps project does not keep a ChangeLog file under source control. All change history is captured by Subversion automatically when it is committed. A ChangeLog file is generated from the SVN commit logs before each release using [svn2cl](wiki:Brief_introduction_to_SVN#How_to_use_svn2cl). Developers should take care to make useful commit log messages when committing changes to Subversion. Here are some guidelines:

- Try to make a descriptive message about the change.
- Use complete sentences when possible.
- When committing a change that fixes a bug on the tracker, use the bug's number and summary as the message.
- When committing a patch from a contributor, put the contributor's name and e-mail address in the commit message.
- It is not necessary to put the names of the files you have modified in the commit message because Subversion stores that automatically.

#### How to use svn2cl

Starting with Gramps 3.0.0, we no longer have a `ChangeLog` file.

Instead, the list of changes is generated automatically using the standard `svn2cl` script.

Note that `svn2cl` is not included in the base installation of subversion. With a Debian-based distro such as Ubuntu, you can get `svn2cl` as follows:

`sudo apt-get install subversion-tools`

or

`sudo apt-get install svn2cl`

There typically are two `ChangeLog` files needed for releases; one in the main directory, and one in the `po` directory. You can generate these files with the following commands:

`cd gramps30`  
`svn2cl --reparagraph --include-rev --authors=src/data/authors.xml`  
`cd po`  
`svn2cl --reparagraph --include-rev --authors=../src/data/authors.xml`

### SVN Commit Tips

#### Some procedural recommendations

1.  Always do *svn up* before a commit, and look especially for conflicts marked 'C'. If necessary get advice about handling conflicts.
2.  Always do *svn st* and look for modifications 'M' that are unexpected or unintended. This is a \*very important\* sanity check. Checking the '?'reports for forgotten additions is also worth remembering.
3.  Recommeded to explicitly name commit targets via 'svn ci X Y Z ..', but if you do simply 'svn ci' (or use a utility commit script), it is especially important to:
    1.  check advisory (2)
    2.  quit (no save) your edit session if you see a filename you did not expect -- svn will prompt whether you want to abort or commit without a log entry (say 'abort').

And here are a couple of incidental suggestions  

- avoid grouping unrelated changes; better to divide into separate commits for the following reasons: a better log entry; easier troubleshooting/reverting. (and probably more).

<!-- -->

- similar to above, it may be better to make small incremental changes than one big one (if possible). Interim changes should not introduce breakage, of course.

<!-- -->

- logs are important -- please give some thought to the log message: the ideal first sentence would be short, meaningful, and suggestive. Include a tracker issue \#NNNN there, if appropriate. Additional explanation is encouraged if it would be something you yourself would appreciate when reading it six months from now. If relevant, emphasize impact of change from user's point of view.

#### svn merge

If you do a change in a branch, you need to do the same change in trunk. You can create a patch on the branch with

`svn diff > mypatch.patch`

and then apply the same patch on trunk.

`patch -p0 < mypatch.patch`

There is a more convenient way though: use svn merge. For this you commit your changes in the branch, and write down the revision number, eg a commit in branch :

`Transmitting file data ..`  
`Committed revision 12345.`

Now you apply this change in branch to trunk as follows. Go into your trunk working branch, and there type the command:

`svn merge -c  12345 `[`https://svn.code.sf.net/p/gramps/code/branches/maintenance/gramps`](https://svn.code.sf.net/p/gramps/code/branches/maintenance/gramps)

The change will then be obtained and applied, after which you can commit trunk.

### Browse svn

An alternative to the command line tools to view the svn repository is the [online interface](http://sourceforge.net/p/gramps/code/).

## External links

- [Apache™ Subversion®](http://subversion.apache.org/)
- [Version Control with Subversion](http://svnbook.red-bean.com/)
- [Source control in ten minutes: a Subversion tutorial](http://www.clear.rice.edu/comp314/svn.html)

[B](wiki:Category:Developers/General)
