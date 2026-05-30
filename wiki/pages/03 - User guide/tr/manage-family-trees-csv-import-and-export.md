---
title: 'Gramps 6.0 Wiki Manual - Manage Family Trees: CSV Import and Export/tr'
categories:
- Documentation
- Gramps Examples
- Stub
managed: false
source: wiki-scrape
wiki_revid: 119802
wiki_fetched_at: '2026-05-30T20:55:52Z'
lang: tr
---

{{#vardefine:chapter\|6}} {{#vardefine:figure\|0}} Bu bölüm, Gramps'ı **Virgülle Ayrılmış Değerler E-tablosu (CSV)** formatı ile kullanmakla ilgilidir.

- [Gramps CSV içe aktarma](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/tr#Gramps_CSV_içe_aktarma)
- [Virgülle Ayrılmış Değerler E-tablosu (CSV) dışa aktarma](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/tr#Virgülle_Ayrılmış_Değerler_E-tablosu_(CSV)_dışa_aktarma)

Mevcut liste görünümünü bir Elektronik Tabloya(\*.ODT) veya CSV dosyasına da [aktarabilirsiniz](wiki:Gramps_6.0_Wiki_Manual_-_Settings/tr#Dışa_Aktar_Görünümü).

## Gramps E-tablo İçe/Dışa Aktarma

Bu biçim, bir veri tablosunu bir kerede içe/dışa aktarmanıza olanak tanır. E-tablo, Virgülle Ayrılmış Değerler (CSV) biçiminde olmalıdır. Çoğu elektronik tablo programı bu biçimi okuyabilir ve yazabilir. Elle yazmak da kolaydır. Bu, mevcut verilerle birleştirmeye izin veren tek Gramps içe aktarma biçimidir.

Bu biçim için üç ana kullanım vardır:

1.  Temel Gramps verilerinizi bir elektronik tablo biçiminde dışa aktarabilir, bir metin veya elektronik tablo programıyla düzenleyebilir ve değişiklikleri ve eklemeleri Gramps'a geri aktarabilirsiniz. Bu, doldurmaları için başkalarına göndermek veya tam Gramps uygulamanız olmadığında yola çıkmak için kullanışlıdır.
2.  Yeni verileri Gramps veri tabanınıza aktarabilirsiniz. Örneğin, veri tabanınıza ekleyeceğiniz bir grup yeni insan varsa, ancak tek tek eklemek istemiyorsanız onları bir elektronik tabloya yazmanız ve ardından hızlı bir şekilde hepsini birden içe aktarmanız daha kolay olabilir. Bu, başka bir uygulamadan veya web'den kesip yapıştırdığınız büyük miktarda veriye sahipseniz kullanışlıdır. Bunun bir örneği, Anlatı Web Sitesini bir elektronik tabloya yükleyerek [Gramps veri tabanınızı geri yüklemektir](wiki:Narrative_Website_Import/tr).
3.  Ayrıca bir dizi düzeltme ve eklemeyi de içe aktarabilirsiniz. Bir rapor yazdırdığınızı ve düzeltmeleri işaretlediğinizi varsayalım. Her düzeltmeyi bir elektronik tablonun bir bölümü yaparsanız, "düzenlemeleri komut dosyası haline getirebilir" ve ardından hepsini bir kerede yürütebilirsiniz.

## Dışa aktar

![[_media/ExportAssistant-ExportOptions-CSV-defaults-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Export Assistant - Export Options - wizard dialog (showing defaults for "Comma Separated Values Spreadsheet(CSV)") with highlight Bottom section for File format specific options]]

Veritabanınızı dışa aktarmak için:

1.  Gramps'ı başlatın

2.  menüsünden seçin.

3.  penceresinde 'yi seçin.

4.  penceresinde **Virgülle Ayrılmış Değerler E-tablosunu (CSV)** seçin

5.  penceresinde.

    1.  Üst bölümde, soy ağacınıza hangi süzgeçlerin uygulanacağını seçin
    2.  Onay kutularından, dışa aktarmaya dahil edilecek öğeleri (kişiler, evlilikler, çocuklar, yerler) ve başlıkların kullandığınız dile çevrilip çevrilmeyeceğini seçin.

{{-}}

Soyağacı verilerinizin seçilmiş bir dizi alanı, aşağıda açıklanan biçimde bir .csv dosyasına kaydedilecektir. Ayrıca, verilerin düzenlenip tekrar okunabilmesi ve böylece veri tabanının güncellenebilmesi için kişilere ve ailelere atıfta bulunulmaktadır.

Boş olacak bazı sütunlar var, özellikle not ve kaynak sütunları. Bunlar, içe aktarma için notlar alabilmeniz için elektronik tabloda listelenmiştir, ancak notlar bu araçla hiçbir zaman dışa aktarılmaz.

Verileriniz yerleri, kişileri, evlilikleri ve çocukları temsil eden dört bölüme ayrılmıştır. Dışa aktarılan alanlar ve sütun adları şunlardır:

Places  
Place, Title, Name, Type, Latitude, Longitude, Code, Enclosed_by, Date

<!-- -->

Individuals  
Person, Lastname, Firstname, Callname, Suffix, Prefix, Title, Gender, Birthdate, Birthplace (or Birthplaceid), Birthsource, Baptismdate, Baptismplace (or Baptismplaceid), Baptismsource, Deathdate, Deathplace (or Deathplaceid), Deathsource, Burialdate, Burialplace (or Burialplaceid), Burialsource, Note

<!-- -->

Marriages  
Marriage, Husband, Wife, Date, Place (or Placeid), Source, Note

<!-- -->

Families  
Family, Child

The first column in each area is the Gramps ID. That is what will tie your edits back to the correct data, so don't alter those data. Load this file into your favorite spreadsheet using comma separated, double-quote text delimited, and Text format (any encoding for now). Then you can add or correct data, and save it back out, keeping the same format. You can then import the data back on top of your old data and it will be corrected.

. .

## İçe aktar

To import your data:

1.  Use the file from above, or create a spreadsheet (described [below](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees:_CSV_Import_and_Export#Example_CSV_with_multiple_areas)) with genealogical data
2.  Start Gramps
3.  Create a new Family Tree
4.  Select from the menu
5.  Select the **Comma Separated Values Spreadsheet (CSV)** file and then select the button

The merge part of this code will only add or update information to your database, and it always assume that the spreadsheet data is the correct version.

If you load this spreadsheet into LibreOffice, make sure you select each column as type **Text** rather than **Standard**. Standard will reformat your dates and numbers. Also, if you use Excel, you will probably want to select all cells once opened, and change the format of the cells to **Text**.

The spreadsheet is data made up of columns. Each column should have at the top of it the name of what type of data is in the column. The first column in each area is the Gramps ID reference. You must use special names for the columns. They are:

### Yerler

    place - a reference to this place
    title - title of place
    name - name of place
    type - type of place (eg, City, County, State, etc.)
    latitude - latitude of place
    longitude - longitude of place
    code - postal code, etc.
    enclosed_by - the reference to another place that encloses this one
    date - date that the enclosed_by place was in effect

### Kişiler

    person -  a reference to be used for families (marriages, and children) 
    grampsid - to assign a Gramps id to the person
    firstname - a person's first name
    surname/lastname - a person's last name
    callname - a common name (nickname) for the person
    prefix - surname prefix (von, de, etc)
    suffix - a suffix of a person's name (Jr., Sr.)
    title - a person's title (Dr., Mr.)
    gender - male or female (you should use the translation for your language)
    note - a note for the person's record

    birthdate - date of birth
    birthplace - place of birth
    birthplaceid - place id of birth
    birthsource - source title for birth

    baptismdate - date of baptism
    baptismplace - place of baptism
    baptismplaceid - place id of baptism
    baptismsource - source title of baptism

    deathdate - date of death
    deathplace - place of death
    deathplaceid - place id of death
    deathsource - source title for death
    deathcause - cause of death

    burialdate - date of burial
    burialplace - place of burial
    burialplaceid - place id of burial
    burialsource - source title of burial

    occupationdate - date of occupation
    occupationplace - place of occupation
    occupationplace_id - place id of occupation
    occupationsource - source title of occupation
    occupationdescr - description of occupation

    residencedate - date of residence
    residenceplace - place of residence
    residenceplace_id - place id of residence
    residencesource - source title of residence

    attributetype - type of attribute
    attributevalue - value of attribute
    attributesource - source title of attribute

### Evlilikler

    marriage - if you want to reference this from a family, you'll need a matching name here
    husband/father/parent1 - the reference of the person above who is the husband 
                             (for female parent1, you'll need to put gender in the person area, 
                             or edit it later in gramps)
    wife/mother/parent2 - the reference of the person above who is the wife 
                             (for male parent2, you'll need to put gender in the person area, 
                             or edit it later in gramps)
    date - the date of the marriage
    place - the place of the marriage
    placeid - the place id of the marriage
    source - source title of the marriage
    note - a note about the marriage/wedding

### Aileler

    family - a reference to tie this to a marriage above (required)
    child - the reference of the person above who is a child
    source - source title of the marriage
    note - a note about the family
    gender - male or female (you should use the translation for your language) 
             [You can put gender here, or in person above]

## Ayrıntılar

Column names are not case-sensitive. You may use any combination of the columns, in any order. (**Actually, you have to at least have a surname and a given name when defining a person, you have to have a marriage and child columns when defining children, and places need a place reference, but that is it.**) The column names are the English names given (for now) but the data should be in your language (including the words "male" and "female").

Top-to-bottom order is important in that if you want to reference something in one area to another, the definition MUST come first. For example, if you want to define families of people, the individuals must be defined before the families. The same applies to places. So it is usually best to put the Places data first, people next, then marriages and families.

Each of these can go in its own area in a spreadsheet. There is no limit to the number of areas in a sheet, and each area can have any number of rows. Leave a blank row between "areas". Just make sure that areas are not next to each other; they must be above and below one another.

You can have multiple areas of each kind on a spreadsheet. The only limitation is that if you refer to a person, you must do that in a row lower than where that person is described. Likewise, if you refer to a marriage, you must do that in a row lower than where the marriage is described. References to enclosed_by places must already exist in the database, or be defined in rows above in the spreadsheet.

If you use the 'grampsid' as a way to assign specific ids, be *very* careful when importing to a current database. Any data you enter will **overwrite** the data assigned to that grampsid. If you use ids in the place, person, marriage, or family columns that are surrounded by brackets (for example '\[I0001\]'), the values you use will be interpreted as grampsids as well. If you are adding **new** items, you are encouraged to avoid use of the bracket format or grampsid columns, so as to avoid accidentally overwriting your data. If you are mixing the bracket (or grampsid) methods with plain references (no brackets), put the plain referenced data after the bracket referenced data.

If you are entering the data in a text file, and if you wish to have a comma inside one of the values, like "Clinton, Co., MO" then you need place the entire value in double-quotes and put the first double-quote right after the preceding comma. For example:

    marriage, parent1, parent2, place
    m1, p1, p2,"Clinton, Co., MO"
    m2, p3, p4,"Havertown, PA"

A spreadsheet program will do this automatically for you.

Here is an example spreadsheet in LibreOffice, but any spreadsheet program should work.

![[_media/Gramps-csv-example1.csv-LibreOffice-Calc--example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}]] {{-}}

    ,,,,,,,,,
    ,"Firstname","Surname","Callname","Gender","Prefix","Suffix","Title","Note","Grampsid"
    ,"Douglas","Test","Doug","male","Von","Sr.","Dr.","This is not related","I0007"
    ,"Laura","Test",,"female",,,,,

{{-}} Notice that the data need not begin in the first column, nor in the first row.

And here is the resulting data in Gramps:

![[_media/FamilyTree-example-imported-gramps-csv-example1.csv-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}]]

{{-}}

### Birden çok alana sahip CSV örneği

Here is an example of a CSV text spreadsheet with multiple areas:

    Place, Title, Name, Type
    [P0001], Michigan, Michigan, State
    L1, Canada, Canada, Country
    L2, USA, USA, Country

    Firstname, Surname, Birthdate, Birth place id
    John,      Tester,  11/11/1965, L1
    Sally,     Tester,  01/26/1973, L1

    Person, Firstname, Surname, Birthdate,    Birth place id
    p1,     Tom,       Smith,   22 Jan, 1970, [P0001]
    p2,     Mary,      Jones
    p3,     Jonnie,    Smith
    p5,     James,     Loucher
    p6,     Penny,     Armbruster
    [P0002],Tim,       Sparklet

    Marriage, Husband, Wife
    m1,       p1,      p2
    m2,       p5,      p6

    Family, Child
    m1,     p3
    m1,     p6
    m2,     [P0002]

If you cut and paste that into a file (or use the [Addon:Import Gramplet](wiki:Addon:ImportGramplet)), you can import it directly.

A date can be any valid Gramps date, including dates formats like "26 JAN 1973" or "26.1.1973".

If you make your references be Gramps IDs inside square brackets, then you can refer to people already in the database, like this:

    Person,    Firstname, Lastname
    joe's boy, Harry,     Smith

    Family,  Child
    [F1524], joe's boy

    Husband, Wife
    [I0123], [I0562]

    firstname, surname
    Timothy, Jones

    place, enclosed_by
    [P0001], [P0002]

This example would create and add Harry Smith to the previously existing family in Gramps, family F1524.

Also, this example would marry two previously existing people, I0123, and I0562.

This also creates a person named Timothy Jones who is not related to anyone.

Finally, this also make place P0001 be enclosed by place P0002.

### E-tablodan CSV örneği

![[_media/Gramps-csv-example3.ods-LibreOffice-Calc-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}}]]

Using Gramps [Example.gramps](wiki:Example.gramps) for this example. The children already exist in the Family Tree. So you can enter an entire generation (8 names with marriage dates) into LibreOffice Calc.

Notice that you can use numbers or strings as the reference names between areas. In the person area, I used the numbers 1 through 8. That made it easy to refer to them in the second area of marriages. The marriages are labeled with the letters A through D.

Also note that in the spreadsheet the children in the third area are existing people in Gramps as indicated by the brackets around the Gramps IDs.

Saving as CSV and importing into Gramps produces the far right-hand column in the tree.

![[_media/FamilyTree-example-imported-gramps-csv-example3.csv-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Saving as CSV and importing into Gramps produces the far right-hand column in the tree.(Highlighted in yellow)]] {{-}} Contents of CSV file `gen4-test.csv`

    ,,,
    ,,,
    "Person","Firstname","Lastname",
    1,"Peter","Blank",
    2,"Anna Maria","Kiefer",
    3,"Georg","Schmidt",
    4,"Barbara","Goering",
    5,"Johann","Kiefer",
    6,"Fides","Federer",
    7,"Sebastian","Schelli",
    8,"Magdelena","Schlegel",
    ,,,
    ,,,
    "Marriage","Husband","Wife","Date"
    "A",1,2,"28 jan 1712"
    "B",3,4,"4 may 1732"
    "C",5,6,02/07/1930
    "D",7,8,17/08/1927
    ,,,
    "Family","Child",,
    "A","[I0104]",,
    "B","[I0105]",,
    "C","[I0972]",,
    "D","[I0973]",,

### Ayrıca bakınız

- [Addon:Import (text) Gramplet](wiki:Addon:ImportGramplet) 3rd party addon by Doug Blank - an interactive version of the [CSV Import](wiki:Gramps_{{man_version}}_Wiki_Manual_-_Manage_Family_Trees:_CSV_Import_and_Export)

[C](wiki:Category:Documentation) [CSV import/Export](wiki:Category:Gramps_Examples)
