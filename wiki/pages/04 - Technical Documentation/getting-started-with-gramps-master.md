---
title: Getting started with Gramps master
categories:
- Developers/General
managed: false
source: wiki-scrape
wiki_revid: 113284
wiki_fetched_at: '2026-05-30T18:11:33Z'
---

Gramps (previously called *trunk* when using SVN) is the newest version of Gramps, but it is under development. You can help by trying this version and reporting feedback and bugs. Before embarking on this you should first read this page.

You should not *install* Gramps as that will overwrite your regular Gramps. However, you can download and compile locally, largely without interfering with your regular Gramps. Subtle interactions are easy to resolve for developers.

## Precautions

Gramps should only be used on a copy of your Family Tree data! Here is a step-by-step guide to doing this:

1.  Start your old version of Gramps
2.  Export your data using the Gramps Package
3.  Quit your old version of Gramps
4.  Start Gramps
5.  Create a new Family Tree
6.  Import the Gramps package from step 2

## Can I run my older version of Gramps with this new version?

Yes. See installation notes below.

## I have a suggestion or have found a bug. What do I do?

Please make a note of your Feature Request, or your bug here: <https://gramps-project.org/bugs/> This is one of the most important things you can do to help the state of Gramps.

## Can I help with Gramps ?

Yes! You could:

1.  Help write documentation on how to use Gramps . See [Gramps X.x User Wiki Manual](wiki:User_manual) and [translating/updating the manual](wiki:User_manual_translations)
2.  Help translate Gramps into another language. See [Internationalization](wiki:Portal:Translators)
3.  Test and follow-up on issues in the tracker. See <https://gramps-project.org/bugs/>
4.  Donate money to Gramps. See [Gramps Support](wiki:Gramps:Site_support)

## Installing Gramps 

Now that you have read all of the precautions, you are ready to begin exploring Gramps .

See [running Gramps from source](wiki:Getting_started_with_Gramps_development#Run_Gramps_from_the_source) for details to make the code work.

## Running parallel versions of  and branches

As stated in **Installing Gramps** , you can only have a dedicated gramps.mo file on /usr/share/local/xx/.. . If you want to have both the and branches version with separate translations, consider using some **[Virtual Machines](http://en.wikipedia.org/wiki/Comparison_of_platform_virtualization_software)**.

## See also

- [GRAMPSHOME](wiki:GRAMPSHOME)
- [Getting started with Gramps development](wiki:Getting_started_with_Gramps_development)
- [Installation alternatives](wiki:Installation_alternatives)

[Category:Developers/General](wiki:Category:Developers/General)
