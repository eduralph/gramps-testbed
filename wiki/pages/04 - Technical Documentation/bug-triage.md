---
title: Bug triage
categories:
- Developers/General
- Developers/Quality Assurance
- Troubleshooting
managed: false
source: wiki-scrape
wiki_revid: 130270
wiki_fetched_at: '2026-05-30T18:10:44Z'
---

Help the Gramps project with bug triaging.  

Fixing a bug always starts with reproducing it, and many times the developer does not succeed in that. Making that possible is the aim of triage.

The bug/issue tracker for Gramps is located at the following URL: <https://gramps-project.org/bugs>

## Goals of Bug Triage

### What

The goal of bug triage is to make it easier for developers to do development by organizing the bug list for them. This means the developers are able to spend less time asking bug reporters what the problem is, confirming if it is still an issue in the latest master branch in [Git](wiki:Brief_introduction_to_Git).

Bug triage includes the reduction of open tickets, removal of stale/out of date tickets, and grouping of feature requests.

### How

![[_media/Mantisbt-valid-status-states.png|MantisBT valid Status states. * &quot;new&quot; * &quot;feedback&quot; * &quot;acknowledged&quot; * &quot;confirmed&quot; * &quot;assigned&quot; * &quot;closed&quot; * &quot;resolved&quot;]] Make sure you're using the **current**''' release of Gramps, using the master branch in [Git](wiki:Brief_introduction_to_Git) is usually best. From a clean install of Gramps attempt to reproduce the bug that is being reported. If you cannot reproduce the bug, post a comment as such - explaining the steps you took to reproduce the bug. If you encounter a different bug, file a new bug report for that problem if one has not been filed already.

- Read a bit of the [documentation of MantisBT](https://www.mantisbt.org/documentation.php) so you know what is possible.

<!-- -->

- Be familiar with the supported [Mantis bug tracker Syntax codes](wiki:Using_the_bug_tracker#Useful_Mantis_bug_tracker_Syntax_codes)

<!-- -->

- Make sure you have Gramps installed so you can test bugs and problems. Create a family tree and import the [example.gramps](wiki:example.gramps) file.

It would be beneficial to also run the master branch version of Gramps so as to test bugs that are in the master branch only.

- At the moment only projects Gramps 5.2, Gramps 6.0 and Gramps master are supported, so any bugs not closed or resolved in older versions must be resolved one way or the other:
  - "**<span style="background:Lime">resolved</span>**" in the meantime
  - does not apply anymore, state why and change the status to "**<span style="background:#C9CCC4">closed</span>**"
  - version no longer supported ([EOL](https://en.wikipedia.org/wiki/End-of-life_%28product%29) versions), [backup your family trees](wiki:How_to_make_a_backup) and install and try with the new version
    - See: [Previous releases of Gramps](wiki:Previous_releases_of_Gramps)
  - bug/problem still present, or move the bug to the correct project eg decide if it is a feature request?
  - too little information given, "**<span style="background:#e3b7eb">feedback</span>**" wanted from reporter
  - several issues in one bug, close it asking users to submit a single ticket per issue (or rename the bug for one issue, and ask to create new ones for the other),
  - other issues...

- For the supported projects, the bugs must be triaged: Duplicate bugs "**<span style="background:#C9CCC4">closed</span>**", set a better bug title so it is more clear for a developer what the bug is about, add extra information. Most important here is to try to duplicate the bug with the [example.gramps](wiki:example.gramps) file, as that is what the developer will spend a lot of time trying to do. Fixing a bug always starts with reproducing it, and many times the developer does not succeed in that. Making that possible is the aim of triage. Once a developer sees a bug in front of him, fixing it is often easier.

<!-- -->

- Then there is the feature request project. These must be organised somehow. It is best you look at some of those tickets and make a suggestion on how to organize it so that the feature requests remain useful. Also giving better titles is important here, closing duplicates. Don't be afraid to close something saying users must give a better worked out request (but be polite!).

<!-- -->

- Don't leave bugs in "**<span style="background:#FCBDBD">new</span>**" state if they're actually no longer **new**.

<!-- -->

- Bugs that are clearly not spam, and have enough info to start an investigation (even though they might turn out as a problem at submitter's end) should be made "**<span style="background:orange">acknowledged</span>**".

<!-- -->

- Those that other people are able to reproduce (or reason about their validity) should be "**<span style="background:yellow">confirmed</span>**".
  - If a feature request is valid also move it to "**<span style="background:yellow">confirmed</span>**". This only confirms it's a possibility and is not a guarantee that the Gramps project will develop and include it in a future release.

<!-- -->

- If the bug is blocked waiting for somebody's input, mark it as "**<span style="background:#e3b7eb">feedback</span>**".

<!-- -->

- If somebody is actively working on a bug, this is best expressed as "**<span style="background:#c2dfff">assigned</span>**". If you stop working on a bug, please remove it from **assigned** state.
  - If a developer has self assigned the issue and raised an associated pull request check that it includes a reference to the MantisBT issue as mentioned in the [Committing policies](wiki:Committing_policies#Create_a_pull_request) the pull request should be using one of the special keywords mentioned [Bug tracker integration for Git Pull request.](wiki:Committing_policies#Bug_tracker_integration)

### Resolving bugs for developers

This information is for the developers following up on the submitted issues.

The page of the bug tracker lists the bugs currently prioritized for the next releases. If you are looking for a bug to fix, this is a good place to start. Placement on the roadmap is controlled by the field for the bug. Special "X.Y.99" phony releases, such as "3.4.99" and "4.0.99", list bugs that we would eventually like to fix for the "X.Y" version, but don't really know the milestone yet. Bugs that really should hold up a release should be on the roadmap with a real release number, and should only be moved after giving a reason or heads up on the devel list [1](http://sourceforge.net/mailarchive/message.php?msg_id=31870820). If you fix a bug scheduled for a later milestone before a previous one is out, **please manually adjust the target release field before marking the bug resolved,** otherwise the roadmap display will be inaccurate [2](http://sourceforge.net/mailarchive/message.php?msg_id=31870821).

In general, when resolving an issue, it is always a good idea to add a note with the “commit hash” (also called the Git commit “reference” or “SHA”) of the commit that fixed the problem.

When resolving issues in a maintenance branch, one should always set the "" field to the version of the next release that will be made from that branch. This is done so that the issue properly appears in the page for that project.

Bugs in maintenance branch projects should not be marked as "**<span style="background:Lime">resolved</span>**" until the developer has committed the change into the corresponding maintenance branch. Additionally, it is the developers responsibility to make sure the change has been merged into the master branch.

### MantisBT permissions

If you don't have MantisBT permissions (the ability to change bugs' status from "new" to "feedback", "acknowledged","confirmed", "closed" or "resolved"), then feel free to ask on the [Gramps Forum](wiki:Contact#Official) developers section for someone to set the status for you (eg: "Could someone set bug \# to "closed" please?). Once you do this enough, feel free to ask for MantisBT permissions on the same Gramps Forum developers section .

## Status

See the summary page:

- <https://gramps-project.org/bugs/summary_page.php>

## Issues

With MantisBT:

- "Bugtracker" Make specific permission profile for people who are only triagers

## See also

- [How to create a good bug report](wiki:How_to_create_a_good_bug_report)
- [Known issues](wiki:Known_issues)
- [Common problems](wiki:Common_problems)

[Category:Developers/Quality Assurance](wiki:Category:Developers/Quality_Assurance) [Category:Developers/General](wiki:Category:Developers/General) [Category:Troubleshooting](wiki:Category:Troubleshooting)
