---
title: Gramps 6.0 Wiki Manual - FAQ/zh
categories:
- Zh:Documentation
managed: false
source: wiki-scrape
wiki_revid: 128626
wiki_fetched_at: '2026-05-30T21:01:44Z'
lang: zh
---

本附录包含在邮件讨论和论坛中经常出现的问题的列表。本列表并不一定完整。如果你希望添加问题/答案到列表中，请将你的建议发送到gramps-devel@lists.sourceforge.net

也可以考虑阅读以下内容：

- [How do I...](wiki::Category:How_do_I...)
- [Gramps Tutorials](wiki::Category:Tutorials)

## 常见问题

### 什么是Gramps?

Gramps是一套基因搜索和分析管理系统。换言之，它是一个个人基因程序，依赖于你电脑的功能，允许你存储，编辑和搜索基因的数据。请参照[About](wiki:Gramps:About).

### 如何获取程序，收费多少？

Gramps不收取任何安装 [installed](wiki:Installation)费用。Gramps是一个开源程序，遵守GNU通用协议。你可以获取源代码，并且可以将程序和源代码分发给其他人。

### Gramps是否支持其他语言?

支持，现在Gramps已经被翻译成了23种语言, 请参照 [Gramps translations](wiki:Gramps_translations).

### 如何保存备份?

使用最新版本的Gramps！从2.2.5版本开始，软件支持自动备份数据的功能。

备份你的数据并保存在安全的地方十分重要。Gramps有一种特殊的可携带的文件格式，它小巧且容易识别，以`.gramps` 作为文件后缀。

你可以将你的备份文件实时拷贝到保存位置（比如，U盘）。【注意： .gramps 文件是一个压缩文件。双击将会打开Gramps程序。如果查看XML文件选择他们并用解压缩工具（比如ark,gunzip）打开，之后你可以解压缩出可读取的XML文件，具体请参照 [details](wiki:Generate_XML#How_do_I_uncompress_the_file?)】。

Gramps 支持快速后台备份，当有错误出现时允许保存。如果安装了正确的软件包，你可以使用修改的程序。

其他方法就是备份隐藏的的目录*./gramps*. 这个目录位于linux系统的主目录下。备份你的目录将会备份你的数据库和修改的内容。

**不要在GEDCOM中保存备份**。并非Gramps存储的信息可以在GEDCOM中保存。因此，一次导入/导出操作 从Gramps--\>GEDCOM--\>Gramps，可能意味着**丢失**数据。请使用 `.gramps` 文件格式备份！ [details](wiki:Gramps_and_GEDCOM)

**不要以GRDB格式备份**. GRDB 是一种数据库,它有可能依赖于某些计算机 (但是可能不能在某些电脑上读取数据).对GRDB文件的微小损坏也可能不能修复。请使用 `.gramps`文件格式备份!

### Gramps 是否支持 Unicode 字体?

是否支持非罗马字的Unicode字体？

支持，Gramps内部支持Unicode (UTF-8), 因此所有的字母可以在全域内使用。虽然某些PDF/PS文档你需要与gnome-print或者openoffice配合使用，所有报告都支持Unicode字体。

## 安装

### 在linux，solaris，或者FreeBSD 下安装都需要哪些条件?

Gramps 是一种[GTK](http://en.wikipedia.org/wiki/Gtk) 应用程序. Gramps 需要安装 [pygtk](http://en.wikipedia.org/wiki/Pygtk) 库安装在系统上.一旦所有条件满足，Gramps就可以启动了。如果GNOME与python绑定安装在系统上，Gramps将会有额外的功能。Gramps计划推荐2.8版本以上的GTK。

### Gramps 是否可以在Windows系统下安装？

[<code>Linux Genealogy CD</code>](wiki:Linux_Genealogy_CD)` 可以作为一个启动光盘，即使你的电脑是Windows系统，你也可以运行Linux和Gramps。`

[<code>Windows installer</code>](wiki:Windows_installer)` 也已经可以下载了，虽然我们还没有足够的人手提供对windows系统的支持。 `[<code>windows mailing list</code>](wiki:Contact)

也可以使用，我们也会尽我们所能解决相关问题。

请参照 [Gramps_and_Windows](wiki:Gramps_and_Windows) 了解在对windows系统中使用的提示集合。

### Gramps 是否支持Mac系统

Fink项目已经为Gramps预留了一些接口给旧版本的OS X系统。Mac操作系统的接口并非由Gramps项目直接对应。主要原因是Gramps的开发者中没有能使用Mac系统的，而且Mac系统也不是免费软件。

现有版本的Gramps不像是由Fink项目维护的，请联系Fink项目了解更多信息。其实，一些用户有一些体会在[had success](wiki:Mac_OS_X) 无论是在本地模式安装还是使用X11并应用一些Fink工具包安装。

### Gramps 所需最低配置？

我们建议最低显卡像素为 800x600 。 对于版本 Gramps 3.1，内存需求已经被削减，它可以有效的运行在256MB内存的系统中。如果系统有512MB的内存，则可以同时运行200，000人的数据。对于典型的数据库，数据库所占的磁盘空间相应的也变大了。针对120,000人来讲，你必须考虑有530MB的数据库空间。图片应该分开存放，因此大容量的硬盘空间十分有必要。

### 如何升级 Gramps?

GNU/Linux 操作系统能够为你解决升级问题。如果它不能升级，那么你需要向你所使用的GNU/Linux操作系统的用户咨询相关问题。

windows用户需要手动升级。

(incomplete answer)

## 首选项

### 我可以将日期格式修改为‘日 月 年’吗？

可以，在选项中修改("编辑-\>首选项")的Gramps日期到所期望的格式(比如：YYYY-MM-DD 或者 日 月 年)，并制作报告。可是使用全局日期选项。

## Collaboration-Portability

### Gramps 是否与其他家谱软件兼容？

Gramps 努力维护与[GEDCOM](wiki:GEDCOM)的兼容性（通用的记录族谱信息的格式）。我们有导入和导出的过滤器可以允许Gramps读写 GEDCOM 文档。

事实上，GEDCOM的标准并未能得到很好的执行 -- 每个家谱软件都有它喜爱的GEDCOM文档标准。而我们也不断学习新的标准，不断更新导入/导出过滤器。然而，一旦发现未知的标准请咨询[user feedback](wiki:Contact)。请随时联系我们，并告知关于Gramps不支持的GEDCOM格式，我们将会尽我们努力改进。

### Gramps 是否可以读取其他族谱软件创建的文件？

请参照前文。

### Gramps 所输出文档是否可以被其他族谱软件支持？

请参照前文。

### Gramps 支持哪些格式？

最好的标准就是什么都不缺。Gramps已经被验证支持以下类型的GEDCOM格式： GEDCOM5.5, Brother's Keeper, Family Origins, Family Tree Maker, Ftree, GeneWeb, Legacy, Personal Ancestral File, Pro-Gen, Reunion, and Visual Genealogie.

### 我如何从另外一个族谱程序导入数据到Gramps？

最好的方式是新建一个家庭树，在菜单中选择导入选项。你选择由其他程序生成的GEDCOM文件，并导入。

### 我是否可以将Gramps安装在Linux 网页服务器上，并通过网页来访问它？

This would enable my relations worldwide to access and update it. While Gramps can generate web sites, it does not provide a web interface that allows for editing. If this is a requirement, then [GeneWeb](http://geneweb.org) or [PhpGedView](http://phpgedview.sourceforge.net) are programs more likely to meet your needs. However, you may wish to ask yourself the following questions:

1.  Do I really want relatives or other people to directly edit my genealogy database?
2.  Do I implicitly trust, without verification, any data that people may enter?
3.  Do these people have the same understanding of good genealogy practice that I have?

A better approach may be to provide a web form interface that allows others to enter data that is then held for your examination. You can then decide if the information should be entered into your database.

You may also want to consider the effects of possible downtime of your site if you cannot afford yourself a premium webhosting service.

## 报告单

### Gramps 是否能为我的家族打印一个家谱树？

可以，不同的人对家谱树的理解不同。一些人认为家谱树应该是一张图表，从祖先开始列出所有的后代和家庭。 其他人认为家谱树应该是一张图表，从个人向上回溯列出所有的祖先和家庭。然后其他人认为是表格，文字报告等等。

Gramps可以生成任何以上形式的表格，和很多其他不同的图标与报告。而且，插件结构使得游湖可以创建自己的插件，实现新的报表，图表或者搜索工具。

### Gramps可以输出何种格式的报告单？

文本报告单： HTML,PDF,ODT,LaTeX 和RTF格式。 图形报告单（图表与图）：PostScript,PDF,SVG,ODS 和GraphViz格式。

### 我如何更改报告的默认语言？

报告单的语言与你所安装的linux系统有关。你可以安装扩展语言包，请参照[Howto:Change the language of reports](wiki:Howto:Change_the_language_of_reports)

### Gramps是否与Internet 兼容？

Gramps 可以存储WEB地址并引导浏览器打开。 它可以导入你从互联网下载的数据。它可以将数据导出以便于你通过互联网传输。Gramps兼容互联网常用的标准格式（如JPEG, PNG, and GIF images, MP3, OGG, 和 WAV sound files, QuickTime, MPEG, 以及 AVI movie files, 等)。除此以外，就很少是家谱软件可以作的了。

### 我是否可以创建定制的报告单/过滤器/其他什么的？

可以。这当中包含很多等级的定制类型。一种是创建或者修改使用过的报告模板。允许你调整字体，颜色，和一些报告单的排版等。你可以用Gramps的报告对话框修改所显示的报告的内容格式。 除此之外，你可以建立你自己的过滤器---这个对于要找到你所设定的标准的人很有用。你可以整合这些过滤器，建立一个新的，更复杂的过滤器。最后，你可以选择建立你自己的插件。这些可能是新的报告单，搜索工具，导入/导出过滤器等等。 前提是假设你有关于python的编程知识。

### 为何non-Latin 字符在PDF/PS的报告单种显示为乱码？

这是由内嵌的PS和PDF格式的字体局限性造成的。 打印非希腊字母的问题，使用打印...在报告单对话框中选择。这将使用 `gnome-print`池，支持PS和PDF的创建，也就是直接打印。（注意：你可能需要单独安装Gnome-print）。

如果文档仅仅包含Latin文本，PDF选项将会生成与gnome-print相比的一个体积小的PDF，因为未加入字体信息。

### 我希望为Gramps撰写我所喜爱的报告单。我该怎么做？

最简单的方式 The easiest way to contribute to reports, filters, tools, etc. is to copy an existing Gramps report, filter, or tool. If you can create what you want by modifying existing code -- great! If your idea does not fit into the logic of any existing Gramps tool, you will need to write your own plugin from scratch. Help is available on the [Developers Portal](wiki:Portal:Developers), or on the [Developers mailing list](wiki:Contact): gramps-devel@lists.sourceforge.net.

To test your work in progress, you may save your plugin under \$HOME/.gramps/plugins directory and it should be found and imported on startup. The correctly written plugin will register itself with Gramps, create menu item, and so on.

If you are happy with your plugin and would like to contribute your code back to the Gramps project, you are very welcome to do so by contacting us at gramps-devel@lists.sourceforge.net

## Database - Gramps file formats

### What is the maximum database size (bytes) Gramps can handle?

Gramps has no hard limits on the size of a database that it can handle. Starting with 2.0.0 release, Gramps no longer loads all data into memory, which allows it to work with a much larger database than before. In reality, however, there are practical limits. The main limiting factors are the available memory on the system and the cache size used for BSDDB database access. With common memory sizes these days, Gramps should have no problem using databases with [tens of thousands of people](wiki:Gramps_Performance).

### Gramps可以处理多少人的数据库？

参照之前的内容。这取决于你电脑的内存多少？ 请参照 [Gramps Performance](wiki:Gramps_Performance).

### 我的数据库很大。是否有办法将所有的数据读入内存？

从版本2.0.0开始，Gramps不再将所有数据读入内存，它可以运行比以前更大的数据库。Gramps数据库所用的文件格式是`.grdb`

### 我是否可以从一个NFS的数据库上运行Gramps

可以

### 可移动的含义是什么？

Gramps 3 的数据库（.grdb文件）十分依赖于创建文件的软件的版本。比如，你不能将你的Gramps数据在拷贝到不同的操作系统下（或者不同版本的操作系统下使用），并希望能够读取你的数据。这些数据时“非可移动的"。因此你不能期望依赖这些格式的备份，你应该时时导出数据到可移动形式的格式。现有两种可选的格式：GEDCOM和Gramps XML（.gramps 或者.gpkg）。但是仅仅Gramps XML被推荐使用，因为它将保存你所有的数据。

### Why is the database format (GRDB) not portable?

The biggest issue with Gramps portability lies with 'transactions'. With Gramps 2.2, we added support for atomic transactions to protect data. With atomic transactions, multiple changes are committed as a single unit. Either all the changes make it, or none of the changes make it. You are never left in a situation with a partial set of changes. A side benefit of using transactions is that database access (reads and writes) are faster.

The problem with transactions (at least using BSDDB) is that it does not allow all the data to be stored in a single file. Logging files are needed to keep track of things. These logging files are kept in a DB Environment directory. We need a separate directory for each file, otherwise the log files can interfere with each other.

In 2.2, we keep the log files under the ~/.gramps/<path> directory, creating a unique directory for each database. The problem is that your GRDB file needs the log files, which are in a different directory. Copying the GRDB file is only copying a portion of the database.

## Bugs and requests

### What do I do if I have found a bug?

The best thing you can do is to fix the bug and send the patch to gramps-devel@lists.sourceforge.net :-)

If that is not possible, you should [submit a bug report](wiki:Using_the_bug_tracker)

A good bug report would include:

1.  Version of gramps you were using when you encountered the bug (available through Help → About menu item).
2.  Language under which gramps was run (available by executing `echo $LANG` in your terminal).
3.  Symptoms indicating that this is indeed a bug.
4.  Any Traceback messages, error messages, warnings, etc, that showed up in your terminal or a in separate traceback window.

Most problems can be fixed quickly provided there is enough information. To ensure this, please follow up on your bug reports. Then we will have a way of contacting you should we need more information.

- Gramps should be a .... type of application

It is obvious that Gramps absolutely needs to become a (client-server/web-based/PHP/weblog/Javascript/C++/distributed/KDE/Motif/Tcl/Win32/C#/You-name-it) application. When is this going to happen?

The surest way to see it happen is to get it done by yourself. Since Gramps is free/open source, nobody prevents you from taking all of the code and continuing its development in whatever direction you see fit. In doing so, you may consider giving your new project another name to avoid confusion with the continuing Gramps development. If you would like the Gramps project to provide advice, expertise, filters, etc., we will gladly cooperate with your new project, to ensure compatibility or import/export options to your new format of a project.

If, however, you would like the Gramps project to adopt your strategy, you would need to convince Gramps developers that your strategy is good for Gramps and superior to the present development strategy.

## 添加与编辑数据库

### residence 与address的区别

residence（住所） 是某人在某个时间段生活过的地方.address（地址）是住所的名称，被期望用于投递的地方。因此每个住所都可以有一个地址，如果有意义的话。

### 我如何更改儿女们的次序？

儿女的次序可以通过在 [Family Editor](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Relationships_View) 菜单中实现，具体可通过拖放或者上下移动按钮实现。

### 我如何更改配偶们的次序？

配偶可以被重新排序，是在 [Relationship View](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Relationships_View) 工具条中选择 'Reorder' 按钮。

[Category:Zh:Documentation](wiki:Category:Zh:Documentation)
