---
title: Gramps 6.0 Wiki Manual - What's new?/pl
categories:
- Pl:Dokumentacja
managed: false
source: wiki-scrape
wiki_revid: 119670
wiki_fetched_at: '2026-05-30T19:37:29Z'
lang: pl
---

This section gives an overview of changes since Gramps version 3.3. These changes are also detailed later in this manual. Users of Gramps version 3.3 are encouraged to review this section to be sure to take advantage of these new features.

# Zanim uaktualnisz

Before you upgrade, make sure your family tree data is secure. The best way to do this is:

1.  Start Gramps 3.3
2.  Open your family tree
3.  Export the family tree to the *gramps xml* format or the *gramps xml package* format (which includes your photographs and other media files associated with your family tree data). Export your tree via menu .
4.  Close this family tree and repeat the above steps for any other family trees you have
5.  Keep the resulting file(s) in a safe place

For more information, please review [Backing up a Family Tree](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Backing_up_a_Family_Tree).

After properly safeguarding your data, proceed to install Gramps 6.0. Use your operating system's regular installation process to do this. It is also best to uninstall Gramps 3.3 before installing Gramps 6.0, or make sure you install Gramps 6.0 in a different location.

After you install Gramps 6.0, you can open your existing family trees and continue working. In case of problems (e.g., after a complete system upgrade), use the backup file(s) created above to recreate your family tree(s).

# Visible changes to the core

Changes visible after the migration: interface, data.

## Citations (formerly Source References)

The principal changes are that:

- Citations can be shared and
- Citations can have media object attached to them.

It is possible to use Gramps in the same way as at Gramps version 3.3, if you do not want or need to take advantage of the new features:

- The Sources view looks almost the same as the old Sources view (but with the addition of a disclosure triangle for sources that have citations),
- The buttons for [adding sources](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_2#Editing_information_about_events) to information like events are the same as before,
- The selector for choosing an existing source looks the same (although with the addition of disclosure triangles to allow a citation to be chosen),
- The new 'Citation' editor looks (and behaves) almost exactly the same as the old 'Source Reference Editor',

Only if a user particularly wants to share citations between objects do they need to be aware of the change. The change is also intended to be entirely compatible with GEDCOM.

See [GEPS_023:_Storing_data_from_large_sources](wiki:GEPS_023:_Storing_data_from_large_sources) for an explanation of the rationale behind the new features.

If you have an existing Gramps database which you are upgrading to Gramps 6.0, after the upgrade process, Gramps will suggest that you might like to merge citations that are the same and refer to the same source. Unless you have specifically recorded different information (for example different notes) on old Source References that are the same, you should probably use the tool.

When you start using Gramps, if you want to share a citation, then you would click on the and in the dialogue, you would select the appropriate source and then citation. Clicking would take you to the editor, but you will probably just click , because the citation and source are both shared.

## Editors

- The citation editor is very little changed from the former Source Reference Editor:

![[_media/SourceRef-to-CitationEditor.png|Figure 1.1]]

As shown, the main change is that the Citation can have a Gallery of images, Data fields, and also has (back-)references because it is a separate primary object.

- Improvements on image selection feature.

<!-- -->

- New 'Default family relationship' option value (Preferences)

<!-- -->

- Add some accelerator keys on toogle buttons without labels. See also [#Accessibility](#Accessibility).

## Importowanie Gedcom

**GEDCOM import error/warnings report**. bug tracker: [1](http://www.gramps-project.org/bugs/view.php?id=5599) - provide a report of GEDCOM errors and warnings after import to show the user what information has not been imported.

![[_media/GEDCOM-import-report-result-example-50.png|Fig 1.2 Import report]]

The report (shown above) details most of the lines that were either ignored or could not be understood. The contents of the line (or lines where there are continuation lines) are also shown. In some cases, the lines may not be exactly what is contained in the input GEDCOM file, because the line is reconstructed following some processing.

In addition to this report, some improvements have been made to GEDCOM import to process more of the input file. Some data has been imported into Gramps data elements even when they are not exactly the same as the GEDCOM data elements. Because the format of GEDCOM, and the format that Gramps uses are different, there are inevitably some pieces of data that cannot be imported.

More details of the mapping from GEDCOM to Gramps are now provided. See [Gedcom import](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#GEDCOM_import).

# Zmiany we wtyczkach

Everything about the plugins: import/export, gramplets, views, reports, tools.

## Importowanie/Eksportowanie

- Citations support on file formats

<!-- -->

- Improvements on Gedcom file format support

## Raporty

- output file formats

Improvements : RTF, ODF, LaTeX, cairo (PDF, Print...)

- support image sections on textual reports

<!-- -->

- Citation support and source review (NarrativeWeb report, etc ...)

<!-- -->

- Paper options

Consistency rules on paper values, orientation and file format (options set by user)

### Książki

- Improvements

<!-- -->

- Alphabetical Index and Table Of Contents (TOC) features on book report

### Raporty szczegółowe

- Improvements, bug fix, consistency on age calculation, etc ...

### NarrativeWeb

- Media gallery, thumbnails

<!-- -->

- hyperlink menu for screen readers and braille writers

## Widoki

The sources view has been enhanced with a new tree view (Fig 1.3) that also shows citations below the source, in addition to the existing flat view (Fig 1.4)

![[_media/SourcesCategory-CitationTree-View-example-60.png|Fig. 1.3 Sources (Citation Tree) view]] ![[_media/Sources-category-list-view-42.png|Fig. 1.4 Sources view]] {{-}}

There is also a new Citations view (Fig 1.5).

![[_media/CitationsCategory-CitationView-List-example-60.png|Fig. 1.5 Citation view]] {{-}}

- Size adjustments on Main, Navigation, Bottom and Side bars

## Narzędzia

- A new tool for merging our citation records: MergeCitations.

<!-- -->

- Review on some *Repair Family Tree* tools

# Under the hood changes

Technical stuff (gui/gen).

## Dostępność

- Better ATK support

<!-- -->

- Improve consistency on Editors: [Accessibility](wiki:Accessibility).

## Menadżer dodatków

- Review, improvements

## Command Line Interface

- Argumenty/flagi

Improvements, consistency, optional translation

## Format plików i baza danych Gramps XML

- Citations support
- Gramps XML is now idempotent[2](http://en.wikipedia.org/wiki/Idempotence).

Exporter does not change records order any more, making easier to look at differences between versions/revisions.

## User classes

Reports and tools have *user* classes. These classes provide a means to interact with the user in an abstract way. These classes should be overridden by each respective user interface to provide the appropriate interaction (eg. dialogs for GTK, promts for CLI).

# Further info

More informations.

## Roadmap

- [Roadmap](wiki:Roadmap): [3.3.2](http://www.gramps-project.org/bugs/roadmap_page.php?version_id=28), [6.0.0](http://www.gramps-project.org/bugs/roadmap_page.php?version_id=30), [trunk](http://www.gramps-project.org/bugs/roadmap_page.php?version_id=25)

## Zmiany

- [6.0.0](http://www.gramps-project.org/bugs/changelog_page.php?version_id=30), [trunk](http://www.gramps-project.org/bugs/changelog_page.php?version_id=25)

[Category:Pl:Dokumentacja](wiki:Category:Pl:Dokumentacja)
