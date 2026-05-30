---
title: Gramps 6.0 Wiki Manual - What's new?
categories:
- Documentation
managed: false
source: wiki-scrape
wiki_revid: 127149
wiki_fetched_at: '2026-05-30T11:44:37Z'
---

{{#vardefine:chapter\|1}} {{#vardefine:figure\|0}}

This section gives an overview of changes since the Gramps 5.2 version. This is an *enhancement* release. So changes include new features as well as bug fixes. These changes are also detailed later in this manual. Users of Gramps upgrading from earlier versions are encouraged to review this section in older [user manuals](wiki:User_manual) to be sure to take advantage of these new features when they start using version 6.0. Search for the lightning bolt of the "" tagged sections.

### Preliminary change list

**Gramps documentation is created be volunteers, so user documentation is published incrementally *after* the release goes public.** (For selected key items, the documentation will be marked with "''</small>" to make searching easier.) The WikiContributors write not only from their experience exploring the features, but also by looking a development objectives, feature requests, status reports and Pull Request notes. If you are an explorer too, the announcements below are partially linked to those reference documents. Explore freely and share your experience to help guide others.

#### From the Announcements

From the **[Announcements](https://gramps.discourse.group/c/gramps-announce/5)** section of the **[Gramps community support Discourse forum](https://gramps.discourse.group/t/welcome-to-the-gramps-discourse-forum/7)**:

- [6.0.5](https://github.com/gramps-project/gramps/releases/tag/v6.0.5) - a new maintenance release, released 2025-09-06.
- [6.0.4](https://github.com/gramps-project/gramps/releases/tag/v6.0.4) - a new maintenance release, released 2025-08-10.
- [6.0.3](https://github.com/gramps-project/gramps/releases/tag/v6.0.3) - a new maintenance release, released 2025-06-18.
- [6.0.2](https://github.com/gramps-project/gramps/releases/tag/v6.0.2) - a new maintenance release, released 2025-06-15.
- [6.0.1](https://github.com/gramps-project/gramps/releases/tag/v6.0.1) - a new maintenance release, released 2025-04-18.
- [6.0.0](https://github.com/gramps-project/gramps/releases/tag/v6.0.0) - a new major release, released 2025-03-19.
- [v6.0.0-rc2](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-rc2) - an experimental pre-release, released 2025-03-16
- [v6.0.0-rc1](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-rc1) - an experimental pre-release, released 2025-03-03
- [v6.0.0-beta2](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-beta2) - an experimental pre-release, released 2025-02-13
- [v6.0.0-beta1](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-beta1) - an experimental pre-release, released 2025-02-05

Discussions from the developers about the future 6.0 release:

- [Understanding Gramps 6.0](https://gramps.discourse.group/t/understanding-gramps-6-0/6652) By Doug Blank - Development - Roadmap

<!-- -->

- Toolbar usability improvement shows text under icons by default.[1](https://gramps.discourse.group/t/gramps-6-0-defaults/6990/3)

## Before you upgrade

***Before*** you upgrade, make sure your family tree data is secure. The best way to do this is:

1.  Start your existing version of Gramps (Gramps 4.2/5.0/5.1/5.2)
2.  Open your family tree
3.  Back up the family tree to the *gramps xml* format or the *gramps xml package* format (the *gramps xml package* includes your photographs and other media files associated with your family tree data). Backup your tree via menu .
4.  Close this family tree and repeat the above steps for any other family trees you have
5.  Keep the resulting file(s) in a safe place

For more information, please review [Backing up a Family Tree](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Backing_up_a_Family_Tree). Note [what will not be included during a backup](wiki:Template:Backup_Omissions).

After properly safeguarding your data, proceed to install Gramps 6.0 using your operating system's regular installation process. In most cases, this will ensure that the new Gramps 6.0 installation will not clash with your older version of Gramps. However, it may be safer to uninstall Gramps 3.4 before installing Gramps 6.0, or make sure you install Gramps 6.0 in a different location. This is always necessary if you are installing from the source code. For more information on installing Gramps 6.0, please see [Downloading the latest Gramps](wiki:Download)

After you install Gramps 6.0, you can open your existing family trees and continue working. In case of problems (e.g., after a complete system upgrade), import the backup file(s) created above to recreate your family tree(s).

## Visible changes to the core

Changes visible after the migration: interface, data.

### Data Model

Details of changes to the [data model](wiki:Gramps_Data_Model) (if any):

1.  No change

<hr>

- A Family Tree **cannot be opened** in Gramps 3.4/4.0/4.1/4.2 and Gramps 6.0 without upgrade.

<!-- -->

- A downgrade can only be accomplished by exporting XML and importing to the previous version.

<!-- -->

- A Gramps XML file generated by Gramps 3.4/4.0/4.1 is **not identical** to one generated by Gramps 6.0.

<!-- -->

- Gramps 6.0 is now **python3** only

See [detailed changes](wiki:Database_Formats#Detailed_Changes) for more details on internal database.

### Primary changes

- SQLite is now the default database backend rather than BSDDB. You can still choose to use [alternative database](wiki:Relational_database_comparison) backends. BSDDB remains available as a standard alternative. For power users, PostgreSQL and MongoDB are available as experimental third-party addons.

The developers believe that SQLite may have fewer database corruptions that prevent easy recovery.

- 

### GUI

- 

### Place

- ability to search alternate place names when selecting place

### Reports, Tools, Gramplets

- 

### Import/Export

- 

### New Addons

- 

## Under the hood changes

Technical changes.

- Numerous changes relating to support for other database backends (SQLite, PostgreSQL, MongoDB etc.).

### Dependencies

## Further information

### Miscellaneous

### Localization

- Updated translations

#### Third-Party Addons

- [Weblate for Third-Party Addons Translation](https://gramps.discourse.group/t/weblate-translation-for-addons-experiment-needs-testers/6964)

### Roadmap

- Explore the Release Notes for [previous releases of Gramps](wiki:Previous_releases_of_Gramps)
- See projected items related to Gramps [next version.](https://gramps-project.org/bugs/roadmap_page.php)
- [Gramps Enhancement Proposals (GEPS)](wiki::Category:GEPS) - See **Released** column for new items implemented in Gramps 6.0
- [6.0 Roadmap](wiki:6.0_Roadmap) - wiki

### Changelog

- See items related to Gramps [6.0](https://gramps-project.org/bugs/changelog_page.php) on the Gramps issue tracker.

<!-- -->

- See additional information see the changelogs for the maintenance releases of Gramps:
  - Gramps [6.0.5](https://github.com/gramps-project/gramps/releases/tag/v6.0.4)
  - Gramps [6.0.4](https://github.com/gramps-project/gramps/releases/tag/v6.0.4)
  - Gramps [6.0.3](https://github.com/gramps-project/gramps/releases/tag/v6.0.3)
  - Gramps [6.0.2](https://github.com/gramps-project/gramps/releases/tag/v6.0.2)
  - Gramps [6.0.1](https://github.com/gramps-project/gramps/releases/tag/v6.0.1)
  - Gramps [6.0.0](https://github.com/gramps-project/gramps/releases/tag/v6.0.0)
  - Gramps [6.0.0-rc2](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-rc2)
  - Gramps [6.0.0-rc1](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-rc1)
  - Gramps [6.0.0-beta2](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-beta2)
  - Gramps [6.0.0-beta1](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-beta1)

Compare GitHub commits from \[<https://github.com/gramps-project/gramps/compare/v5.2.4>...v6.0.1 Gramps 5.2.4 to 6.0.1\] {{-}}

### What Was *Once* New

The [Previous Release](wiki:Previous_releases_of_Gramps) page includes links to bullet lists of changes in major releases and maintenance releases over the years.

However, the **What's New?** pages in the superseded version of the wiki manual for each major releases can provide greater detail:

- [Version 5.2](wiki:Gramps_5.2_Wiki_Manual_-_What%27s_new%3F)
- [Version 5.1](wiki:Gramps_5.1_Wiki_Manual_-_What%27s_new%3F)
- [Version 5.0](wiki:Gramps_5.0_Wiki_Manual_-_What%27s_new%3F)
- [Version 4.2](wiki:Gramps_4.2_Wiki_Manual_-_What%27s_new%3F)
- [Version 4.1](wiki:Gramps_4.1_Wiki_Manual_-_What%27s_new%3F)
- [Version 4.0](wiki:Gramps_4.0_Wiki_Manual_-_What%27s_new%3F)
- [Version 3.4](wiki:Gramps_3.4_Wiki_Manual_-_What%27s_new%3F)
- [Version 3.3](wiki:Gramps_3.3_Wiki_Manual_-_What%27s_new%3F)
- [Version 3.2](wiki:Gramps_3.2_Wiki_Manual_-_What%27s_new%3F)

A compact overview of enhancements was first added to the manual in 2010. For the first 3 years of the wiki, it was necessary to review the entire manual.

### Downloadable manual

Version 6.0 - downloadable manual

- [English PDF](wiki::File:Gramps6.0UserManual.pdf)

We do not list every single bug fix or smaller improvement on this page. To get a more complete list of changes, you should look at the [commit history](https://github.com/gramps-project/gramps/commits/maintenance/gramps60) for each release. {{-}}

[Category:Documentation](wiki:Category:Documentation)
