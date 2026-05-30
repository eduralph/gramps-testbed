---
title: Brief introduction to Git
categories:
- Developers/General
- Stub
managed: false
source: wiki-scrape
wiki_revid: 129797
wiki_fetched_at: '2026-05-30T18:10:38Z'
---

The Gramps project uses the [Git](https://en.wikipedia.org/wiki/Git) version control system to help synchronize changes to source code from various developers, tracking changes, managing releases, etc. You are probably here because you want to do one of two things with Git; either:

- Download the latest maintenance source version or the development version, or else
- [Submit a Pull Request (PR)](wiki:Brief_introduction_to_Git#Send_your_contribution_without_rights_to_push) with the changes (if you don't have write access) or upload your changes (if you have write access to the repository).

## Install Git on your system

Follow steps on Git's web site to [install Git](https://git-scm.com/install/), then [configure your Git settings](#Configure_Git_settings).

### Linux

- Debian/Ubuntu: `sudo apt-get install git`
- Fedora: `yum install git-core`

### Microsoft-Windows

- Microsoft-Windows: Download git from here <https://git-scm.com/download/win>

### Apple Mac OS X

- **Mac OS X (Intel)**: Download git from here <https://git-scm.com/download/mac>
- **Mac OS X (PPC)**: Although the git download is called '[`git-2.xx.x-intel-universal-mavericks.dmg`](https://sourceforge.net/projects/git-osx-installer/files/)', implying that this is a universal binary, in fact only the installer is universal, the binary to be installed in actually intel only. On a PPC you will need to build git manually. Follow the instructions here: <http://jnorthr.wordpress.com/2013/03/29/building-a-git-client-1-8-2-on-apple-imac-ppc-osx-10-5-8/>. I think you will also need some additional tools like 'msgfmt'. I don't think this is installed by the Apple development tool Xcode, but fortunately I have it either via fink which I installed some time ago, or via MacPorts which I installed more recently.

  
Mac OS X (PPC) Eclipse. If you are using Eclipse on a PPC, then there may be missing components for installing the latest version of EGit, depending on your version of Eclipse. If you have the Helios version of Eclipse, then you will not be able to install the latest EGit because you will get *requires 'org.eclipse.team.core 3.6.100' but it could not be found*. Installing EGit version 2.0 from <http://download.eclipse.org/egit/updates-2.0> should work if you uncheck the EGit Import Support feature when selecting what to install. You will obviously lose the Import Support feature. See [here](http://stackoverflow.com/questions/15281273/dependency-fail-installing-egit-on-eclipse-indigo). You will probably need to do *git config core.filemode false* to get round [this bug](https://bugs.eclipse.org/bugs/show_bug.cgi?id=307560) as suggested [here](http://stackoverflow.com/questions/1257592/how-do-i-remove-files-saying-old-mode-100755-new-mode-100644-from-unstaged-cha).

If you use Eclipse then will need to locally ignore the Eclipse files as suggested at section 4.2 [here](https://www.vogella.com/tutorials/EclipseGit/article.html#create-gitignore-file).

`cd ~/`  
`touch .gitignore`  
`echo ".metadata" >> .gitignore`  
`echo ".project" >> .gitignore`  
`echo ".pydevproject" >> .gitignore`  
`echo "windows" >> .gitignore`

### Configure Git settings

Git includes your name and email address in commits. To configure them, use the following commands:

`git config --global user.name "John Smith"`  
`git config --global user.email john@example.com`

Git will automatically convert line endings for you. Use the following settings:

`git config --global core.autocrlf true  # Windows`  
`git config --global core.autocrlf input  # Linux/Mac`

Git can invoke your favorite editor for commit messages, rebasing etc.

`git config --global core.editor "'C:\Program Files (x86)\Notepad++\notepad++.exe' -multiInst -notabbar -nosession -noPlugin"  # Windows`  
`git config --global core.editor "vim"  # Linux`

## Obtaining a copy of the Gramps repository

The description below is for a single working folder at `~/Gramps`. If you are working on a plugin, the folder name should be `addons-source` at the https://github.com/gramps-project/addons-source.git

### Using HTTPS Protocol

To obtain a copy of the Gramps repository, type the following in the command line (doesn't require a GitHub account):

`git clone https://github.com/gramps-project/gramps.git Gramps`

You should see the downloading progress reported in your terminal.

### Using SSH Protocol

If you have a GitHub account, use you can ssh if you wish, or continue to use HTTPS protocol with your GitHub credentials or a Personal Access Token:

`git clone git@github.com:gramps-project/gramps.git Gramps`

You will need a [SSH Key](https://help.github.com/articles/generating-ssh-keys/) in order to authenticate using this method. **Before you accept any host keys, make sure you [verify the SSH fingerprint](https://help.github.com/articles/what-are-github-s-ssh-key-fingerprints/)** of github.com.

You can check your connection by:

`ssh -T git@github.com`

which should return:

`Hi `<name>`! You've successfully authenticated, but GitHub does not provide shell access.`

Once the clone is complete, you have a local copy of the Gramps code with Git configured to use this as the 'origin'. You can see this by:

`git remote -v`

which should return:

`origin https://github.com/gramps-project/gramps.git (fetch)`  
`origin https://github.com/gramps-project/gramps.git (push)`

If you have 'push rights' to the Gramps repository, (members of the 'developers' group have this), then you are good to go. If not, then you will have to establish your own github account and use that for a place to publish your contributions. This is not needed until (or unless) you desire to contribute more than a simple patch to Gramps.

You should sign up for an account on <https://github.com>. GitHub is free to use for public and open source projects like Gramps. You should create a repository on github that can receive your pushed contributions. The examples below assume that is also called 'gramps'. See <https://help.github.com/articles/creating-a-new-repository/>

Once you have that set up, you should set up a second remote tied to your local repository. My personal arrangement is to change the name of the original tie to the remote Gramps github repository to 'upstream' and make the tie to my personal github repository 'origin':

`git remote set-url --push upstream cannot_push`  
`git remote set-url --fetch upstream https://github.com/gramps-project/gramps.git`  
`git remote set-url --push origin https://github.com/my-name/gramps.git`  
`git remote set-url --fetch origin https://github.com/my-name/gramps.git`

When done, you can check the results:

`git remote -v`

which should return:

`origin https://github.com/my-name/gramps.git (fetch)`  
`origin https://github.com/my-name/gramps.git (push)`  
`upstream https://github.com/gramps-project/gramps.git (fetch)`  
`upstream cannot_push (push)`

## Branches

Branches are the particular group of code sources associated with a Gramps version, enhancement, bug fix etc. When making changes to Gramps, it is important to understand where you are starting from (which version of Gramps) and what you are trying to do.

### Types of branches

When you clone the Gramps repository, a branch called *master* will be created for you. This contains the latest development version of Gramps. Gramps maintains different branches in several categories:

- *master* - There is only one *master* branch. All new feature development happens in the *master* branch. New releases never come from the *master* branch.

<!-- -->

- *maintenance* - There are many maintenance branches, though usually only one or two are active. A maintenance branch is created from the *master* branch when all the features for a release are complete. New features are not committed to maintenance branches. Releases only come from active maintenance branches; a branch is no longer active when no further releases are planned for it. Inactive branches should not have any changes committed to them. The purpose of maintenance branches is to allow the line of code to stabilize while new features are added in the *master* branch. In order to prevent regressions (fixed bugs reoccurring in later releases) the current maintenance branch is regularly merged into the *master* branch.

<!-- -->

- *geps* - These are meant for development of [Gramps Enhancement Proposals](wiki:Portal:Enhancement_Proposals). Most of the time GEPS are developed in the *master* branch. Occasionally a GEP will require extensive reworking or long periods when the code base is ususable. In these cases a branch in *geps* can be used as a temporary development area. Once the hard work is done the change should be merged into the trunk and the *geps* branch should be removed. *geps* branches should follow the naming convention *gep-\<###\>-<descriptive text>* e.g. *gep-013-server*. Please read the [#Working with development branches](#Working_with_development_branches) section for help with managing these branches.

Tags are created for each Gramps release. The first two digits of the Gramps version number are reserved to indicate the maintenance branch the code came from. The last digit indicates the revision from that maintenance branch. For example, 5.0.4 would indicate the 5th release from the 5.0 branch (5.0.0, 5.0.1, 5.0.2, 5.0.3, 5.0.4).

Here is a hypothetical example: Imagine that the current version of Gramps is 8.3.2. A new series of features has been added in the *master* branch and are ready for release. A new maintenance branch is created from the *master* branch named 8.4 (or possibly 9.0 depending on the nature of the new features). New features continue to be added in the *master* branch that will not be included in the 8.4 series of releases, but will be included in the 8.5 series. Bug fixes continue to occur in the 8.4 branch until the code is deemed worthy of release. At that time, a release is tagged from the 8.4 maintenance branch and named 8.4.0. Some time after the release of 8.4.0, some bugs are found and fixed in the 8.4 maintenance branch. Those bug fixes are released as 8.4.1.

## Stable version

There are several versions of the Gramps source code in Git. The development branch for small changes and bug fixes is

*`maintenance/gramps`*

By default, the remote server you cloned the Gramps repository from is called *origin*, unless you changed the setup as described above. In that case it is *upstream*.

To see a list of branches on the server, type:

`git remote show upstream`

To create a local branch which tracks a branch on the server, use:

`git checkout -b gramps`` upstream/maintenance/gramps`

This is known as a "tracking" branch.

To list the available branches, type:

`git branch`

The current branch is marked by an asterisk.

To switch to another branch, type:

`git checkout `<branch>

To look at any stable release version, and create a new local branch off of it, type:

`git checkout `<tag>` -b `<new_local_branch_name>

The following configuration option simplifies pushing a branch back to the server:

`git config --global push.default upstream`

You can then use:

`git push`

While it is certainly possible to do your contributions directly in the particular branch you start from, whether it be 'master' 'maintenance/gramps' or something else, it is more usual to create a branch of your own for each significant change. That way you can work on each separately, and change from one to the other without getting the changes intermixed.

For example if you are creating a new report you might want to call the branch 'gen-report'. If you are basing this off of the 'master' branch, then you would start by:

`git checkout master         # this ensures your work is based on master branch`  
`git checkout -b gen-report  # this creates a new branch 'gen-report' based on master but separate.`

You can create many such branches and switch between them with 'git checkout <yourbranch>' as long as you save your work via 'commit' (described below) before making the switch.

### Alternative approach

For an alternative approach see [Multiple Working Folders](wiki:Brief_introduction_to_Git#Multiple_Working_Folders).

## Basic Work Flow

The basic work flow after you've checked out the repository is update, develop, commit, update again, push. To update the current checked out Gramps branch (master in this case) from Gramps github, run

`git pull --rebase upstream master`

If you are working on a branch of your own creation ('mybranch'), based off of master, and currently have 'mybranch' checked out, I prefer to run

`git fetch upstream           # copies the latest stuff from Gramps on github`  
`git rebase upstream/master   # shift my work to be 'on top' of other peoples work`

As a general rule *always* use `git pull --rebase` to avoid creating unnecessary merge commits. Note that one must have no uncommitted edits on that branch when running `git pull`.

The differences between "git pull" and git pull --rebase" is explained well [here](http://stackoverflow.com/a/3357174/2615612).

You make your changes next with your preferred editor, debugging the code locally.

To see exactly what you have changed from the original (master in this case):

`git diff master`

To see changes since your last commit:

`git diff`

To review your change files before a commit, type:

`git status`

To stage and commit your changes locally, use the following commands:

`git add *    # the '*' adds every changed file to the stage, or you can specify a single file`  
`git commit`

Which will bring up the default \$EDITOR (or the editor you setup with 'git config' above) to create a commit message. If you are fixing a bug, the first line of the commit message should be the bug number and title, otherwise a brief statement of purpose. Skip a line and describe what you did.

- All developers should read Gramps [Committing policies](wiki:Committing_policies)

If the commit is a minor change that can be described entirely in the subject, you can instead use:

`git commit -am "message describing the nature of the change"`

Try to keep your commits digestible and understandable. A large changeset can be broken into several commits that "tell a story" about how the changeset moves the program from its old behavior to its new one.

To push your changes to the Gramps repository, you need to have cloned the Gramps source code with ssh, and have push access to the Gramps repository (the Gramps admins can give you this, [Brian Matherly or Nick Hall](wiki:Contact)). If you don't have push access continue in the next section below. First update again to make sure that you can fast-forward the repository, then push:

`git pull --rebase`  
`git push`

If someone else has made changes that interfere with yours, you will get a conflict error when you pull. You will have to resolve that conflict and re-commit (you can use `git commit --amend` if it affects only the last *unpushed* commit) before git will push successfully.

Since uploading is a potentially dangerous operation, most people do not obtain write access to the git repository. You can use one of two approaches to this, either make a 'patch' (useful for small bug fixes), or you can make a 'Pull Request' (PR).

See the [make a patchfile](wiki:Brief_introduction_to_Git#Making_a_patchfile) or [Making a PR](wiki:Brief_introduction_to_Git#Making_a_PR) sections for details.

  
Also see: [Getting started with Gramps master](wiki:Getting_started_with_Gramps_master).

### Making a patchfile

When dealing with a patch, you create a new bug on the [bug tracker](https://www.gramps-project.org/bugs) and attach a patch to it.

The [bug tracker](https://www.gramps-project.org/bugs) has a drop down at the top right to allow a choice among the projects under the Gramps Bugtracker; the default project shown is **All Projects**. Choose the project **Gramps** and submit an issue.

A patchfile is a text file with your changes which can be sent by email to somebody, or posted/uploaded to the bug tracker (against a bug you are fixing or a feature request which you are solving for instance), etc...

These instructions tell how to make a patchfile against the *master* branch, so that your changes are added to the next major release of Gramps. (To make a patchfile against a branch the process is similar, with some slight changes.)

First create a new branch to work in:

`git checkout -b fix`

Then use your favorite editor to change whatever file(s) you want. Add the files you have changed to the staging area and commit them.

Obtain the latest changes from the server.

`git checkout master`  
`git pull --rebase`

Next, rebase your fix again the *master* branch. This will ensure that your patch will apply cleanly.

`git rebase master fix`

This will leave you in the fix branch.

Finally, create a patchfile, using:

`git format-patch master --stdout > fix.patch`

You now have a patchfile that can be sent by email, or attached to a bug report. The patch can be applied using the 'git apply' command.

<span id="Making a PR">

### Making a Pull Request (PR) on Github

</span> If your changes or submission is more substantial, (or you will be making lots of them), you are encouraged to use the PR (Pull Request) method of making submissions. PRs allow the developers to easily see your proposed changes, download them and test them outside of the main code base, and see the results of automated testing. Github also has a comments area for each PR that allows you to describe in detail what you are trying to achieve, and for others to respond to your work.

To make a PR, you must first 'push' your work to a publicly view-able repository. We will continue to assume that github is used for this, and that you have your own account set up with a 'gramps' (or 'addons-source') repository as your remote 'origin', as was described earlier.

Again, to minimize the chance of collisions with other peoples work;

`git checkout mybranch        # unless you are already there`  
`git fetch upstream           # copies the latest stuff from Gramps on github`  
`git rebase upstream/master   # shift my work to be 'on top' of other peoples work`

If you have done multiple commits while working on you code and they don't really make sense separately or contain intermediate attempts that are not reflected in the final result, you should probably clean up your work. There are several ways to do this, but I like to use the 'interactive rebase'. Start with:

`git log`

which will list all the commits starting with the most recent. The list is potentially enormous, but you probably will only need to look at the first screen or so. (Type 'q' to quit) An example log is shown:

`commit defcda798145769f89189b95b202d5d0067f59c1`  
`Author: prculley <paulxxxx@gmail.com>`  
`Date:   Sat Dec 8 11:08:48 2016 -0600`  
`   messed up and need to fix this`  
`commit 2359633198ef50072d2bb6ca25f923718fab02d8`  
`Author: prculley <paulxxxx@gmail.com>`  
`Date:   Wed Dec 7 11:52:21 2016 -0600`  
`   bug 8333; fix merge issue with Person Tree View`  
`commit 5ad32042c6f808918cbbf540091e52e4ac4a9b28`  
`Author: Paul Franklin <pfxxxx@gmail.com>`  
`Date:   Wed Dec 21 22:24:48 2016 -0800`  
`   move two methods down slightly (to better check a forthcoming change)`

Find the first commit *after* your own commits and copy (at least) the first 5-6 characters of the long hash string. Then do an interactive rebase;

`git rebase -i 5ad320`

Something like the following should appear in your editor with your commits at the top:

`pick 2359633 bug 8333; fix merge issue with Person Tree View`  
`pick defcda7 messed up and need to fix this`  
`#`  
`# Rebase 5ad3204..defcda7 onto 5ad3204 (2 command(s))`  
`#`  
`# Commands:`  
`# p, pick = use commit`  
`# r, reword = use commit, but edit the commit message`  
`# e, edit = use commit, but stop for amending`  
`# s, squash = use commit, but meld into previous commit`  
`# f, fixup = like "squash", but discard this commit's log message`  
`# x, exec = run command (the rest of the line) using shell`  
`# d, drop = remove commit`  
`#`  
`# These lines can be re-ordered; they are executed from top to bottom.`  
`#`  
`# If you remove a line here THAT COMMIT WILL BE LOST.`  
`#`  
`# However, if you remove everything, the rebase will be aborted.`  
`#`  
`# Note that empty commits are commented out`

In the example above, I want to merge the two commits into a single one, and keep only the original commit message. So I use the 'f' option on the second pick (change the 'pick defcda7' to 'f defcda7'), save the file and exit the editor.

Once that is complete, you can finally push the results to github at your own account:

`git push origin mybranch`

The next stop is at github itself. Grab your web browser and navigate to your account and your repository and the 'branches' tab https://github.com/yourname/gramps/branches. You should see your newly 'pushed' branch ('mybranch') listed with a 'New Pull Request' button on the right.

You can then fill out the PR form. You might have to select the Gramps 'base' branch you are basing on if it is different than 'master', this will be evident if you see "Can’t automatically merge". Add any comments you have on your work. And push the 'Create Pull Request' button.

#### Send your contribution without rights to push

You can [fork](https://help.github.com/articles/fork-a-repo/) the Gramps repository and create a [pull request](https://help.github.com/articles/using-pull-requests/). Otherwise check it into Git if you obtained the [permission to do push](#Obtaining_a_copy_of_the_Gramps_repository).

Since syncing a fork can create unwanted commits, you may need to [rebase](https://github.com/edx/edx-platform/wiki/How-to-Rebase-a-Pull-Request) your pull request first. Remember to replace edx and master with the actual names of the remote repository (upstream) and the branch you're working on.

- [Making a Pull Request (PR) on Github](wiki:Brief_introduction_to_Git#Making_a_Pull_Request_.28PR.29_on_Github)

#### To PR or not to PR

Note from Nick Hall - 27 Feb 2024

Generally pull requests are preferred, but there are a few exceptions:

- Translations. Before Weblate, a translation maintainer was allowed to commit translation updates directly without a PR. This is still the case for addons. The reason behind this was that it was unlikely that the PR would be reviewed.
- Package maintenance. We allow package maintainers to make changes in the directory related to the package that they maintain.
- Releases. PRs are not required for commits relating to a release.
- Branch merges. I don’t make a PR when merging bug fixes from a maintenance branch into the master branch.

## Working with development branches

Creating branches with Git is quick and easy.

Here is a quick crib sheet:

### Creating a branch

To create a branch from the *master* branch:

`git checkout master`  
`git branch gep-014-fab-feature`

To make this branch available on the server use:

`git push origin gep-014-fab-feature`

### Merging changes from the branch back into the *master* branch

When you are ready to merge your changes back into the *master* branch:

`git rebase master`  
`git checkout master`  
`git merge gep-014-fab-feature`  
`git push`

### Removing branches

It is important that branches are removed once they have been merged into the trunk or have been abandoned. To remove a branch:

`git branch -d gep-014-fab-feature`

To remove a branch from the server, use:

`git push origin :gep-014-fab-feature`

The developers reserve the right to remove branches that have been dormant for more than 1 year.

### Applying a fix to another branch

If you write a fix for an old maintenance branch, you may need to also apply it to the current maintenance branch.

To apply a commit from the gramps42 branch to the gramps50 branch:

`git checkout gramps50`  
`git cherry-pick fix`

Then you may have to fix things that could not be applied due to conflicts. The patch program would mark the conflicts with the \<\<\<\<\<\<, ======, and \>\>\>\>\>\> signs. You will then need to push your changes.

If you apply a small fix that applies cleanly to another branch, it can be done like this (assuming you've just committed the fix to gramps42 in a single commit):

`git checkout gramps50`  
`git diff gramps42^ gramps42 | git apply`

If \`git apply' fails, nothing will be changed in the working copy, and you can try to resolve the conflicts by cherry-picking, or manually saving the diff result, using the "patch" program, and resolving the conflicts.

### Searching in a specific branch

The GUI search in GitHub only indexes the active branch in the code base. If you want to search for a string in a specific branch, use Git instead of the GUI.

Using issue as an example, the following examples show how to search for a term in various branches. The output shows that v5.1.3 introduced a change related to that string:

`> git grep "Default Person" master`  
`master:NEWS:* Change GUI references to ‘Home Person’ instead of ‘Default Person’`  
`master:po/pl.po:#~ “active person to the Default Person.”`

`> git grep "Default Person" v5.2.3`  
`v5.2.3:NEWS:* Change GUI references to ‘Home Person’ instead of ‘Default Person’`  
`v5.2.3:po/pl.po:#~ “active person to the Default Person.”`

`> git grep "Default Person" v5.1.6`  
`v5.1.6:NEWS:* Change GUI references to ‘Home Person’ instead of ‘Default Person’`  
`v5.1.6:po/pl.po:#~ “active person to the Default Person.”`

`> git grep "Default Person" v5.1.2`  
`v5.1.2:po/pl.po:#~ “active person to the Default Person.”`

`> git grep "Default Person" v5.1.3`  
`v5.1.3:NEWS:* Change GUI references to ‘Home Person’ instead of ‘Default Person’`  
`v5.1.3:po/pl.po:#~ “active person to the Default Person.”`

There are several options you can use with the grep command which you can see by adding “–help”.

### Workflow

Before switching to another branch it is useful to remove untracked files created by the build process. You can do this with the following command:

`git clean -dxf`

## Useful Tips

### Getting help

Git has excellent man pages. You can view the manual page for a Git command, by using one of the following:

`git help `<verb>  
`git `<verb>` --help`  
`man git-`<verb>

For example, to get help on the 'git log' command, type:

`git help log`

### Configuration settings

You can set your default editor with:

`git config --global core.editor `<editor>

To enable colored command line output, use:

`git config --global color.ui auto`

### Saving uncommitted work while you do something in another branch

Sometimes you are not ready to commit your work but you still want to do work in another branch. You may want to read up on:

`git worktree  # used to have another copy of the repository in another directory of your machine.`  
`git stash     # used to temporarily 'stash' uncommitted work on a 'stack'`  
`git stash pop # used to 'pop' the latest stashed item (can also be used to move uncommitted files to another branch if you forgot to switch before editing`  
`git stash -p  # interactive selection of stash items (if you want to stash some uncommitted work, but not other)`

### Checking out someone else's PR to test

On the github page for the PR, next to the 'Merge Pull Request' button, is a hotlink for 'command line instructions'; it gives the actual 'git checkout' line for this.

### Making merges (when there are rebase conflicts) easier

A tool which shows a 3-way merge can be helpful in determining what needs to be done. First configure git for the tool of choice (kdiff3 for windows shown here):

`git config --global merge.tool kdiff3`  
`git config --global mergetool.kdiff3.cmd "C:/Program Files/KDiff3/kdiff3.exe"  # Windows`  
`git config --global --add mergetool.kdiff3.trustExitCode false`

Then when a merge conflict comes up you can:

`git mergetool`

### Some procedural recommendations

1.  Always do `git pull --rebase` before pushing changes to the server. If necessary get advice about handling conflicts.
2.  Always do `git status` and look for staged files that are unexpected or unintended. This is a \*very important\* sanity check.

And here are a couple of incidental suggestions  

- Avoid grouping unrelated changes; better to divide into separate commits for the following reasons: a better log entry; easier troubleshooting/reverting. (and probably more).

<!-- -->

- Similar to above, it may be better to make small incremental changes than one big one (if possible). Interim changes should not introduce breakage, of course. For instance, if you change code in gramps/ and do associated translation changes in po/, you might want to commit the changes in po/ in a commit following the commit(s) with the changes in gramps/.

<!-- -->

- logs are important -- please give some thought to the log message. All developers should read the [Committing policies](wiki:Committing_policies).

### Browse Git

An alternative to the command line tools to view the Git repository is the [online interface](https://github.com/gramps-project/gramps).

## Multiple Working Folders

Using a single working folder as described above entails context switching when developing across multiple branches. For example:

- develop and test changes on the gramps41 branch,
- commit or stash the changes,
- clean to remove untracked files created by the development process,
- checkout the master 'branch',
- build (python setup.py build),
- cherry pick the changes from the gramps41 branch into the master 'branch',
- test and if necessary develop the changes to master,
- commit or stash the changes.

If the changes are all OK, then they can pushed to the GitHub repository.

An alternative is to clone the GitHub repository for each branch, but although git saves local disk space by using hard links for locally cloned repositories, keeping the local repositories in sync is complex.

The problem is well explained [here](https://www.finik.net/2010/10/24/multiple-working-folders-with-single-git-repository/) as is the solution, which is to create copies of the working directories only.

This can be done using either the builtin `git worktree` command since Git 2.5.0 or by a script that is in the git 'contrib' directory [git-new-workdir](http://nuclearsquid.com/writings/git-new-workdir/) for older versions of Git. Note that `git worktree` supports windows out of the box.

### git-new-workdir

Assuming that the directory structure would be:

`~`  
`+-Gramps `  
`  +-repository`  
`    +-.git`  
`      +- etc`  
`  +-gramps34`  
`  +-gramps40`  
`  +-gramps41`  
`  +-gramps42`  
`  +-gramps50`  
`  +-gramps51`  
`  +-gramps52`  
`  +-master`

The approach would be:

- clone from the GitHub repository:

`mkdir Gramps`  
`cd Gramps`  
`mkdir repository`  
`cd repository`  
`git clone git@github.com:gramps-project/gramps.git`

- then create the various working copies:

`# git-new-workdir path/to/repository   path/to/new/workingdir   branch`  
`git-new-workdir   ~/Gramps/repository  ~/Gramps/gramps34        maintenance/gramps34`  
`git-new-workdir   ~/Gramps/repository  ~/Gramps/gramps40        maintenance/gramps40`  
`git-new-workdir   ~/Gramps/repository  ~/Gramps/gramps41        maintenance/gramps41`  
`git-new-workdir   ~/Gramps/repository  ~/Gramps/gramps42        maintenance/gramps42`  
`git-new-workdir   ~/Gramps/repository  ~/Gramps/gramps50        maintenance/gramps50`  
`git-new-workdir   ~/Gramps/repository  ~/Gramps/gramps51        maintenance/gramps51`  
`git-new-workdir   ~/Gramps/repository  ~/Gramps/gramps52        maintenance/gramps52`  
`git-new-workdir   ~/Gramps/repository  ~/Gramps/master          master`

You will then need to build the source, but this only needs to be done once, and the 'clean' step is not needed. See [Run from source](wiki:Getting_started_with_Gramps_development#Run_Gramps_from_the_source) and [running](wiki:Running_a_development_version_of_Gramps) which describes the process for 'gramps 3.4 and before' as well as after. For example:

`cd ~/Gramps/gramps41`  
`python setup.py build`

### git worktree

Although from Git 2.5 (Q2 2015) a replacement for contrib/workdir/git-new-workdir was [builtin](http://stackoverflow.com/questions/6270193/multiple-working-directories-with-git/30185564#30185564) to git, it is recommended that you use the 'recipe' above instead of the builtin, in order to ensure that the repository is in the right place, and in view of the warning below.

WARNING. Using the builtin 'git worktree' may not be supported by Eclipse (as at Dec 2017), see [Bug 477475 - git 2.5 worktree support](https://bugs.eclipse.org/bugs/show_bug.cgi?id=477475). This has apparently been fixed as of 7 Sep 2024 in JGit 7 see [Eclipse JGit: Java implementation of Git 7.0.0](https://projects.eclipse.org/projects/technology.jgit/releases/7.0.0)

## git2cl

The Gramps project does not keep a ChangeLog file under source control. All change history is captured by git automatically when it is committed. A ChangeLog file is generated from the git commit logs before each release using [git2cl](wiki:Brief_introduction_to_SVN#How_to_use_git2cl). Developers should take care to make useful commit log messages when committing changes to git. Please read the [Committing policies](wiki:Committing_policies) for details.

### How to use git2cl

Starting with Gramps 3.0.0, we no longer have a `ChangeLog` file.

Instead, the list of changes is generated automatically using the standard `git2cl` script.

Note that `git2cl` is not included in the base installation of Git. With a Debian-based distro such as Ubuntu, you can get `git2cl` as follows:

`sudo apt-get install git2cl`

There typically are two `ChangeLog` files needed for releases; one in the main directory, and one in the `po` directory. You can generate these files with the following commands:

`git log gramps-4.0.1.. --pretty --numstat --summary --no-merges | git2cl > ChangeLog`  
`git log gramps-4.0.1.. --pretty --numstat --summary --no-merges -- po | git2cl > po/ChangeLog`

## External links

- [Git](http://git-scm.com/)
- [Git Book](http://git-scm.com/book)
- [GitHub SSH Keys](https://help.github.com/articles/generating-ssh-keys/)
- [GitHub SSH Key Fingerprints](https://help.github.com/articles/what-are-github-s-ssh-key-fingerprints/)

[B](wiki:Category:Developers/General)
