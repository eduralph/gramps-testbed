---
title: Using the bug tracker
categories:
- Developers/General
- Developers/Quality Assurance
- Troubleshooting
managed: false
source: wiki-scrape
wiki_revid: 125932
wiki_fetched_at: '2026-05-30T18:18:48Z'
---

This bug/issue tracker allows users and developers to log new issues and track them as they progress. Please take some time to read the issue tracker instructions below and read **[how to create a good bug report](wiki:How_to_create_a_good_bug_report)**. Also, have a look at **[known issues](wiki:Known_issues)** and **[common problems](wiki:Common_problems)**.

## Quick recommendations

When composing a problem (bug) report for Gramps:

- Be ***precise***
- Be ***clear**:* explain how to reproduce the problem, step by step, so others can reproduce the bug, or understand the request.
- Include only ***one problem per report***
- Include any relevant links and ***examples***

## Report a bug

### 1. Login

To report a bug or raise a feature request, you must have a login account on the **Gramps bug tracker** *([powered by MantisBT](https://www.mantisbt.org/))*:

- [](https://bugs.gramps-project.org) to your account at <https://gramps-project.org/bugs/login_page.php> , or;
- Select [](https://gramps-project.org/bugs/signup_page.php) or visit the following link to create a new login account: <https://gramps-project.org/bugs/signup_page.php> .

Due to periodic SPAMbot activity, New Account requests might require human pre-approval. Be aware that this means that it might take up to 12 hours before a confirmation email is sent when creating a user account. Only after clicking on the link in the confirmation email can you submit bugs. Your email address will be handled confidentially.

{{-}}

#### How Do I Change My Profile Picture on MantisBT

MantisBT (the open source issue tracker used by the Gramps project) automatically uses your [Gravatar service profile](https://gravatar.com/) based on your registered email address. {{-}}

### 2. Search wiki and existing bugs

![[_media/Search_box_for_existing_bugs.png|Search Box]] Sometimes the behavior being observed might seem odd, yet as-designed. So the first step is to search the wiki to see what the documented behavior is. If you're still not sure, ask the [Gramps community on Discourse.](https://forum.gramps-project.org/)

If it still appears to be a bug, perhaps the bug you want to report has been reported before. To check this, click on [](https://gramps-project.org/bugs/view_all_bug_page.php). The top of the page is reserved for filters, which you set. Normally the default filters are just fine. Under these filters, there is a box. Enter the terms best describing the bug, and click to search. If you have an error message, try pasting a part of the error, to see if it is has been reported already.

If the bug is already reported, read over the bug report, and see if you can add to the information. If so, you can leave a note with extra information to help the developers. {{-}}

### 3. Submit new bug

![[_media/Report_issue_buttons_Gramps_bugs.png|&#39;Report Issue&#39; buttons.]] Click on one of the buttons, and enter the required information, see below on how to select the project to which the bug belongs. Be verbose, the developers are bad at mind reading. We shall mercilessly close the bugs which have no meaningful information at all, such as \#. Do not forget to list the Gramps version you are using. You can check this in Gramps by clicking in the Gramps program the Help menu, option About. {{-}}

#### How to proceed

![[_media/Dropdown-Choose-Project-GrampsBugtracker.png|Choose Project - selection list]] The first step in submitting an issue on the tracker is to determine which project it belongs to on the issue tracker from the **Select Project** box, use the **Choose Project** drop down list to select the "project" for the bugs. "Projects" are a way to categorize issues. There are two types of projects in the issue tracker, **Feature Requests** and **Gramps**:

- The **Feature Requests** project is a place for recording requests for new features.
  - If the issue represents functionality that does not currently exist in Gramps, then the issue should be filed under the **Feature Requests** project.

<!-- -->

- The **Gramps** project is a place for recording all issues with Gramps.
  - If the issue represents a problem with functionality that has been released in a stable release or a problem with functionality that only exists in the master branch, then the issue should be filed under the Gramps project.

<!-- -->

- For bug reports and feature requests relating to Gramps Web, see [\| Get Help - Gramps Web](https://www.grampsweb.org/help/)

{{-}}

#### Enter Issue Details

![[_media/Enter_Issue_Details_page_Gramps_bugs.png|Enter Issue Details - page]] The page is where you share with the developers what your issue or feature request is.

Try and complete all the relevant sections as well as you can and be prepared to answer follow up questions if your report needs clarification. Here's a concise guide on **[How to create a good bug report](wiki:How_to_create_a_good_bug_report)** for Gramps which will greatly increase the chances of reproducibility and thus being fixed.

##### Filling out the page

- Select Profile
  - Gramps runs on multiple operating systems, so it's important to know which operating system and version you are reporting an issue against. This is where you provide that information. MantisBT allows you store multiple profiles in your Account so that you can pick the appropriate one, which is handy if you run Gramps on different system configurations.
- Product Version
  - The projects with names that look like **Gramps x.x.X** are where issues are reported that apply specifically to a maintenance branch (see [Types of Branches](wiki:Brief_introduction_to_Git#Types_of_branches)). A separate project exists for each maintenance branch.
  - For recording issues that *only* apply to the master branch in Git (see [Types of Branches](wiki:Brief_introduction_to_Git#Types_of_branches)), use next un-released version e.g.: 6.1.0 as shown on the \[<https://gramps-project.org/bugs/roadmap_page.php>\| MantisBT Roadmap\].
- Addon Version
  - If you are reporting a bug in an third-party addon, use the [<strong>Addon Manager</strong>](wiki:Gramps_{{man_version}}_Wiki_Manual_-_Navigation#Using_the_Addon_Manager...) or [<strong>Plugin Manager</strong>](wiki:Gramps_{{man_version}}_Wiki_Manual_-_Plugin_Manager) (or even the [Enhanced Plugin Manager - addon](wiki:Addon:Plugin_Manager)) to find the version of the addon and include it in the report.

{{-}}

## Useful MantisBT bug tracker Syntax codes

The following are useful [MantisBT bug tracker](http://www.mantisbt.org/) syntax codes you can use:

- Using *`#`* before a bug number writes a link to the bug. eg: *`#1`* becomes
- Use *`@`* before a user name to mention a person (note: user names with embedded spaces are not supported)
- Using *`~`* before a comment number writes a link to the comment, same as : *`{url}#c{comment number}`*. eg: *`~3`* becomes [1](https://gramps-project.org/bugs/view.php?id=1#c3)
- To link a GitHub Pull Request in the bug tracker, use *`p:gramps:nnnn:`* where *`nnnn`* is the PR number. (This only applies to the main gramps repository, not add-ons.)
- To link a GitHub Pull Request in the bug tracker, for Gramps addons-source paste the full Github link.

### Limited HTML tags

- A [limited set](https://github.com/mantisbt/mantisbt/blob/55fb5721ea7d980557da484390db5c6003b63cd0/config_defaults_inc.php#L1979) of [HTML tags](https://www.w3schools.com/tags/) can be used in the text field:
  - `<p> </p>` to define a paragraph.
  - `<li>` to defines a [list item](https://www.w3schools.com/tags/tag_li.asp) used with:
    - `<ul>` unordered lists
    - `<ol>` ordered lists
  - `<br>` to insert a single line break.
  - `<pre> </pre>` to add preformatted text, that is displayed in a fixed-width font, and it preserves both spaces and line breaks.
  - `<i> </i>` usually displays text in *italics*.
  - `<b> </b>` shows **bold** text
  - `<u> </u>` Underline a misspelled word
  - `<em> </em>` It renders as emphasized text.
  - `<strong>` It defines important text.

## See also

- [How to create a good bug report](wiki:How_to_create_a_good_bug_report)
- [Known issues](wiki:Known_issues)
- [Common problems](wiki:Common_problems)
- Help the Gramps project [Bug triage](wiki:Bug_triage)

MantisBT.org reports providing user-oriented (*not* admin) documentation

- [0005070](https://www.mantisbt.org/bugs/view.php?id=5070): I have written \[MantisBT\] quick-start documentation \[.doc, .pdf, .swx\] if you’re interested
- [0008939](https://www.mantisbt.org/bugs/view.php?id=8939): Lifecycle model \[Visio\] for a report in MantisBT

[Category:Developers/General](wiki:Category:Developers/General) [Category:Developers/Quality Assurance](wiki:Category:Developers/Quality_Assurance) [Category:Troubleshooting](wiki:Category:Troubleshooting)
