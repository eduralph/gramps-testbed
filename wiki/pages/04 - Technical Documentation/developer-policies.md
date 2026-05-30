---
title: Developer policies
categories:
- Developers/General
managed: false
source: wiki-scrape
wiki_revid: 104316
wiki_fetched_at: '2026-05-30T18:10:57Z'
---

This document collects the different policies the Gramps developer community has adopted.

## Coding policies

### License

Gramps is a GPLv2 licensed application with the possibility to use a later version of the GPL (GPLv3). There are no plans at the moment to move to GPLv3 and drop GPLv2. See [Project License](wiki:Project_License) for details.

### Coding style

Follow the Gramps [Programming guidelines](wiki:Programming_guidelines) - which mostly refer to PEP8 with a few additions. Gramps CI checks PRs for compliance using the [Black](https://github.com/psf/black) formatter.

All source files shall include conforming [Source file headers](wiki:Source_file_headers).

### GUI design

User interfaces shall conform to the agreed upon [UI style](wiki:UI_style).

### Acceptable changes

You should follow the [roadmap](wiki::Category:Developers/Roadmap) set out for the next release. Only minor features or new reports/gramplets/... can still be added to the roadmap after it has been made official. Add your changes to the [roadmap](wiki::Category:Developers/Roadmap) (on this wiki and in the bug tracker) so others are notified what you work on. Seek approval for your changes via the *gramps-devel* mailing list.

## Commit policies

### General

Read [Committing policies](wiki:Committing_policies)

### Becoming an official developer

The road to become an official developer is as follows:

- Fix bugs on the bug tracker and participate in the *gramps-devel* mailing list.
- Accept the guidance from existing developers. If you do not agree with them, you need to convince them. To do that, first consider coding what is asked for and pointing out the weakness afterward, i.e. let the code speak for you.
- Take up a feature request after assuring yourself (e.g. via the *gramps-devel* mailing list) the feature will probably be accepted by the developers. Let your code be reviewed.
- Once you come to the conclusion your code needs little change before commit, ask the technical architect (Nick) to send you an invitation to join the GitHub *Developers* team. If you have not had contact with the technical architect yet, ask one of the other developers to vouch for you.
- Even after you obtained commit rights, consider a review of your code by other developers by submitting a pull request or using the bug tracker (send reminder) or the *gramps-devel* mailing list.

[Category:Developers/General](wiki:Category:Developers/General)
