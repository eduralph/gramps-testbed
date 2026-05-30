---
title: Report API
categories:
- Developers/Reference
- GEPS
- Plugins
- Reports
- Stub
managed: false
source: wiki-scrape
wiki_revid: 128028
wiki_fetched_at: '2026-05-30T18:18:27Z'
---

The [Simple Document API interface](wiki:Report_API) is for easy presentation of the data and can be used with [Simple Access API](wiki:Simple_Access_API).

In Gramps there are five different types of reports.

- Text report
- Graphical report
- Graph
- Book
- Web pages

Only Text reports, Graphical reports and Graphs use the Report (Document) API, since Web reports write their output directly into files, while Book reports are simply combination of Text reports and Graphical reports.

## Common API

At the moment the combination of textual and graphical elements within one document is not supported (for future plans refer to Report API redesign), thus Text and Graphical reports are implemented via separate APIs, though they have a common part. This common part is implemented in the [BaseDoc class](http://www.gramps-project.org/docs/gen/gen_plug.html#gen.plug.docgen.basedoc.BaseDoc), which contains among others basic document opening, closing, and stylesheet handling methods. It also stores the physical description of a page (sheet of paper in print).

### Page

![[_media/Doc_paper.png]] Description of the paper, which every report will be rendered on, is stored by an instance of the [PaperStyle class](http://www.gramps-project.org/docs/gen/gen_plug.html#gen.plug.docgen.paperstyle.PaperStyle). This instance is available via the `BaseDoc.paper_style` class attribute. The chosen PaperStyle is given to the document generator at initialization, and is handled by the reporting framework.

The `PaperStyle` holds information on the size of the paper ([PaperSize class](http://www.gramps-project.org/docs/gen/gen_plug.html#gen.plug.docgen.paperstyle.PaperStyle) instance), the size of the margins, and the orientation of the paper. Use the proper accessor methods to get the values. To get the metrics of the usable area of a paper (page without the margins) one can also use the [PaperStyle.get_usable_width](http://www.gramps-project.org/docs/gen/gen_plug.html#gen.plug.docgen.paperstyle.PaperStyle.get_usable_width) and [PaperStyle.get_usable_height](http://www.gramps-project.org/docs/gen/gen_plug.html#gen.plug.docgen.paperstyle.PaperStyle.get_usable_height) convenience methods. Width and height are always given according to the orientation of the paper, thus width is always the horizontal, and height is always the vertical dimension.

Text reports do not need to care about paper properties, as the document generator (or the external viewer) paginates the report according to those properties. While, on the other hand, graphical reports do need to take paper properties into account when creating graphical elements, i.e. they should not draw on the margins.

The origin of the coordinate system is the top left corner of the usable area.

{{-}}

## Text document API

The specification of the Textdoc API is [here](https://gramps-project.org/docs/gen/gen_plug.html#gramps.gen.plug.docgen.textdoc.TextDoc)

The interface for adding media objects is as follows:

     add_media_object(name, align, w_cm, h_cm, alt='', style_name=None, crop=None)[source]

        Add a photo of the specified width (in centimeters).
        Parameters: 

            name – filename of the image to add
            align – alignment of the image. Valid values are ‘left’, ‘right’, ‘center’, and ‘single’
            w_cm – width in centimeters
            h_cm – height in centimeters
            alt – an alternative text to use. Useful for eg html reports
            style_name – style to use for captions
            crop – image cropping parameters

Note that because of the structure of these documents, Images are only allowed as children (i.e. following) Document or Cell.

This interface is used in the following reports:

| Report | Builtin | align | style_name | how called |
|----|----|----|----|----|
| Detailed Ancestral Report | Builtin | right | DDR-Caption | via gen/plug/report/utils.py |
| Detailed Descendant Report | Builtin | right | DDR-Caption | via gen/plug/report/utils.py |
| Individual Complete Report | Builtin | right | None | direct |
| Book (Title Page) | Builtin | center | None | direct |
| Person Everything | Addon | single | PE-Level%d | direct |
|  |  |  |  |  |

None of the reports use 'alt'. It is understood (from looking at the code in odfdoc.py) that **left** and **right** alignment should cause the text to wrap around the media object, while for **single** alignment, there should be no text on either side of the media object.

Since style_name should be used as the style for the caption (i.e. the **alt** string) it should also be used for the image itself. Otherwise the caption would not be below the picture.

As at December 2014, output appears as follows:

| Format | right | center | single |
|----|----|----|----|
| HTML | **OK** Picture on right, text wrapped round it | ? | Picture on left margin, text not wrapped |
| RTF | Picture on left margin, text not wrapped | ? | **OK** Picture aligned with previous paragraph, text not wrapped |
| ODF | **OK** Picture on right, text wrapped round it | ? | Picture centred, text not wrapped |
| PDF | Picture on right, text not wrapped | ? | Picture on left margin, text not wrapped |
|  |  |  |  |

## Draw document API

## Graph document API

[Category:Developers/Reference](wiki:Category:Developers/Reference) [R](wiki:Category:GEPS) [Category:Plugins](wiki:Category:Plugins) [A](wiki:Category:Reports)
