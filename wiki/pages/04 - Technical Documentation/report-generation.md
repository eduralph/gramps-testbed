---
title: Report Generation
categories:
- Developers/Reference
- GEPS
- Plugins
- Reports
managed: false
source: wiki-scrape
wiki_revid: 128797
wiki_fetched_at: '2026-05-30T18:18:32Z'
---

There are four categories of report:

- Text - ([TextDoc](wiki:Report_Generation#TextDoc))
- Draw - ([DrawDoc](wiki:Report_Generation#DrawDoc))
- Graphviz - ([GVDoc](wiki:Report_Generation#GVDoc))
- Web - (*Web reports work slightly differently to the others.*)

## Writing a report

When writing a report, the developer uses one of 3 report interfaces: TextDoc, DrawDoc and GVDoc. Abstract classes which define these interfaces can be found in the *[/gramps/gen/plug/docgen](https://github.com/gramps-project/gramps/tree/master/gramps/gen/plug/docgen)* folder. In this way reports are independent of the output format.

Documents are actually created using document generators. There is one document generator for each output format, which implements one or more of the report interfaces.

When a report is run, it calls the report methods in the appropriate document generator.

Book reports give the user a mechanism to include more than one report in a single document. Only Text and Draw reports are allowed in a book. The allowed output formats are determined by the document generators which implement both the TextDoc and DrawDoc interfaces.

Reports can be run in any of three modes: GUI, Command Line and Book. The report category and report modes are defined in the plugin data for the report.

The report interfaces are very different:

## TextDoc

This is used for creating text documents. It has a simple hierarchical structure:

`Document`  
`  Paragraph`  
`  Pagebreak`  
`  Table`  
`    Row`  
`      Cell`  
`        Paragraph`  
`        Image`  
`  Image`

The layout of the document elements is sequentially down the page, except for table cells which are obviously arranged in a row across the page.

Document elements such as titles and list entries are defined by paragraph styles.

Pagination is handled by the document generator or external program, except when a user inserts a manual pagebreak.

Index marks can be attached to text within a paragraph.

## DrawDoc

This is used for creating graphical documents. Its structure is almost flat:

`Document`  
`  Frame`  
`    Line`  
`    Polygon`  
`    Box`  
`    Text`

The document consists of frames which represent the drawing area on a page.

The document elements Line, Polygon, Box and Text are placed within the frame according to co-ordinates specified in the report. The report interface determines the precise layout making this type of report more complex to write.

## GVDoc

This is used for creating documents that represent mathematical graphs. A graph is a set of nodes, in which any two nodes can be joined by a line.

`Document`  
`  Subgraph`  
`    Node`  
`    Link`  
`    Comment`

The report interface allows nodes, links and comments to be defined, but not their layout. The layout is defined by the document generator or external program.

# See also

- [Report API](wiki:Report_API).

[Category:Developers/Reference](wiki:Category:Developers/Reference) [R](wiki:Category:GEPS) [Category:Plugins](wiki:Category:Plugins) [Category:Reports](wiki:Category:Reports)
