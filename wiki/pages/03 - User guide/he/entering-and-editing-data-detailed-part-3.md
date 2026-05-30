---
title: 'Gramps 6.0 Wiki Manual - Entering and editing data: detailed - part 3/he'
categories:
- He:מדריך למשתמש
- He:תיעוד
- Pages with broken file links
- Stub
managed: false
source: wiki-scrape
wiki_revid: 121710
wiki_fetched_at: '2026-05-30T19:15:44Z'
lang: he
---

<div dir="rtl" lang="he" class="mw-content-rtl">

{{#vardefine:chapter\|9.3}} {{#vardefine:figure\|0}}

The previous section offered you a detailed overview of how to enter and edit the main objects you see in Gramps. This section continues with other objects you encounter in Gramps.

## עורך שמות

חלון דו־שיח הוא למעשה חלון דו־שיח משנה של חלון אליו ניתן להגיע במספר דרכים:  
ממצג סוג־אב אנשים, מתפריט או על ידי הקשה על האדם הרצוי במצג רשימת אנשים ומלשונית במקטע . חלון דו־שיח זה הוא המקום שבו ניתן להוסיף מידע חדש או לעורך מידע קיים של אדם לרבות את כל רכיבי שמו של האדם, תוארו, שמותיו הפרטיים, שמות משפחה אותם נשאה לאורך ימי חייו, כינויים ושמות חיבה ואת שמו הפרטי המועדף.

דו־שיח נחלק למספר מקטעים:

1.  מקטע סוג שם – שם ניתן להזין את סוג השם
2.  מקטע שם פרטי – מאפשר הזנת כל שמותיו הפרטיים וכינוייו של אדם
3.  מקטע שם משפחה – נועד לשם משפחת האדם ומאפשר ניהול שמות משפחה מרובים ומרכבים
4.  מקטע כללי – שמאפשר את התאמת אופן המיון והקיבוץ של השמות, וטווחי תאריכים

{{-}}

### דו־שיח עורך שמות

![[_media/NameEditor-dialog-example-52_he.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} עורך שמות – דו־שיח – דוגמה]] בחלקו העליון של החלון ניתן להזין או לבחור את סוג השם (לדוגמה, שם בלידה, שם מנישואין וכדומה) מתוך רשימה נפתחת. לאחר שנבחר 'סוג' לשם, הוא יהיה חלק ממרכיבי השם במסד הנתונים. מקטע השדות הבא הם מרכיביהשם הפרטי, כאשר הקיבוץ התדיר ביותר הוא שם פרטי שניתן לאדם בלידה. המקטע הבא הוא מקטע שמות המשפחה. בתחתית החלון מקטע כללי שמכיל רכיבים שמאפשרים התאמה אישית למיון שמות, טווחי תאריכים לשמות, מקורות שמות והערות לשמות. {{-}}

#### סוג

- (`שם בלידה`ברירת מחדל) רשימה נפתחת של סוג השם מאפשרת לבחור את סוג השם מהרשימה. ניתן גם להזין ישירות [סוג מותאם אישית](wiki:Gramps_Glossary/he#סוגים_מותאם_אישית) בשדה זה.

- הקשה על סמל המנעול בפינה השמאלית העליונה של כדי למתג את סמן השומת השם כפרטית או ציבורית (גלויה). סימון הרשומה כפרטית תאפשר להשמיט את השם הזה (וכלל הנתונים הנלווים אליו) מלהופיע בדוחות (אם אפשרויות הפקת הדוח הוגדרו בהתאם).

{{-}}

#### שמות פרטיים

הקטע **שמות פרטיים** מכיל את כל רכיבי השם הפרטי אותם ניתן לאחסן במסד הנתונים של גרמפס:

- בשדה זה ניתן להזין כאן את כל השמות הפרטיים של אדם.

- זהו השם הפרטי החוקי מבין כל שאר השמות שלו, בו הוא נוהג להציג את עצמו ובו נוהגים אחרים לכנותו. לדוגמה, אדם ששמו ג'ון ריימונד סמית' שמשתמש בשם ריימונד, השם *ריימונד* יוזן בשדה זה. גם אם אדם זה משתמש ב*ריי* באופן שגרתי, זהו כינוי! ואותן יש להזין בשדה ולא בשדה זה. שכן "ריי" הוא לא השם המשפטי כפי שמופיע ברשומות (הסבר להלן). בגרמניה ובכמה מקומות אחרים, נהוג היה להדגיש בקו תחתון את מבין יתר השמות הפרטיים השונים (לקריאה נוספת [שם מועדף](wiki:Names_in_Gramps/he#שם_מועדף)).

- בשדה זה ניתן להזין כאן את התוארו של האדם, כגון דוקטור (או דר').

- במקרים בהם קיימת סיומת לשם הפרטי כגון ג'וניור (Jr.) או III (השלישי). יש להזין בשדה זה את סיומת השם.

- כינויים לרוב כוללים קיצורי שמות משפטיים נאותים של אדם שנתנו לו כשם 'חיבה' כגון 'גרג' ל'גרגורי' או 'מק' ל'מקלאוד' וכדומה (זאת בניגוד לשם צועדף לעיל). יש מקרים בהם הכינוי אינו נגזר ישירות משם תיקני כגון 'בוגי' או 'בוז'י', גם שמות כינוי אלו ככל שהם מזהים את האדם באופן מובהק ניתן להזין בשדה זה.

{{-}}

#### שמות משפחה

חלון מקטע מכיל את רכיבי שם משפחתו של אדם. גרמפס מאפשר לנהל מספר שמות משפחה לאותו אדם, שמות משפחה מרובים ושמות משפחה מורכבים.

- בסרגל הכלים שבראש החלון מוצגים הלחצנים הבאים: (הוספה, עריכה, הסרה, העברה מעלה, העברה מטה)

העמודות הבאות מוצגות:

- – קידומת לשם המשפחה, הקידומת לא משפיעה על מיון השמות ברשימות (כגון "דה" או "ואן").

- – החלק העיקרי של שם המשפחה של האדם.

- – משמש לעתים קרובות בתסדירי שמות משפחה שנגזרים משם האב או האם, לדוגמה שמה של הזמרת [דוטר](https://he.wikipedia.org/wiki/דוטר_(זמרת)).

- – מציין את סוג שם המשפחה זה והגזירה שלו.

- – פקד כפתור רדיו מציין אם שם המשפחה הוא השם הראשי.

בתחתית החלון מופיע השדה הבא:

- נועד למשפחות שמכונות בשגרה בכינוי בשפה מקומית (על פי שם החווה שלהם או עיסוקם).

לקריאה נוספת: [שמות בגרמפס](wiki:Names_in_Gramps/he#שמות) – מאמר ויקי. {{-}}

### עמוד לשונית עורך שמות

#### כללי

אפשרויות שמאפשרות להתאים קיבוץ, מיון והצגת מאפיינים מסוימים של שם זה, כמו גם לספק את התאריך המתאים למועד בו היה שם מסוים בשימוש האדם:

- השדה {{ man label\|קיבוץ בשם:}} מספק צומת קיבוץ חלופי עבור שם בתצוגת האדם, תוך עקיפת קיבוץ ברירת המחדל שמבוסס על שם משפחה.יכולת זו נדרשת בעיקר לקיבוץ שמות משפחה דומים – לדוגמה שמות רוסיים כמו **איבנוב** ו**איבנובה** נחשבים לזהים, למעט השוני במגדר שבא לידי ביטוי באיות שונה. לקריאה נוספת [קיבוץ שמות משפחה](wiki:Grouping_Surnames/he).
  -  כדי לאפשר הקלדה בשדה זה יש לסמן תיבת סימון זו. (תיבת הסימון לא מסומנת כברירת מחדל)

  
אנשים מוצגים לפי תסדיר השם שהוגדר בהעדפות (ברירת המחדל).

כאן ניתן לוודא שהאדם הזה מוצג לפי תסדיר שם מותאם אישית. *(ניתן לבחור תסדירים נוספים של שמות בלשונית או להתאים אישית באמצעות [עורך תסדיר שמות](wiki:Gramps_6.0_Wiki_Manual_-_Settings/he#עורך_תסדיר_שמות).)*

- The and determine how the name appears in the People View and the reports. The sort allows you to override the name pattern set in the Gramps preferences in the sorting of the name. For example, you suddenly have a branch of Swedish names with given and patronymic, but the rest of your database sorts names on Family name, Given. You can indicate here to sort this name always as Patronymic, Given.

  
Here you can make sure this person is sorted according to a custom name format. *(More name formats can be selected in the tab or customized using the [Display_Name_Editor](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display_Name_Editor).)*.

The allows you to say how the name is listed. You might, for example, want to sort a name in based on a person's given or surname, but still have the display show an honorific title before that name. *(More name formats can be selected in the tab or customized using the [Display_Name_Editor](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display_Name_Editor).)*

The Person Tree view groups people under the primary surname. You can override this by setting here a group value. You will be asked if you want to group this person only or all people with this specific primary surname.

- The can provide information on the validity of this name -- use date spans as necessary. The edit date icon opens the [Date Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_1#Editing_dates). Eg. for a Married Name, enter the date that the name is first used or the marriage date.

#### מובאות מקור

לשונית מציגה מידע על מקורות ומבאות לעינין שם זה ומספר פקדים שמאפשרים את טפלול המידע. החלק המרכזי מציג את רשימת כל המובאות והמקורות הללו שמאוחסנים במסד הנתונים. הלחצנים , ו־ מאפשרים להוסיף, לשנות ולהסיר מובאות לשם זה בהתאמה. לתשומת לב! הלחצנים ו־ יהפכו לזמינים לזמינים רק עם בחירת אזכור למקור מהרשימה.

לקריאה נוספת: [עורך מובאות](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2/he#עריכת_מובאות_מקור)

#### הערות

The tab displays any notes concerning the name. To add a note or modify existing notes simply edit the text in the text entry field.

More info: [Note Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed_-_part_2#Editing_information_about_notes)

## תכונות

When you add or edit an [Attributes](wiki:Attributes_in_Gramps) from the dialogs tab the dialog will be shown. {{-}}

### דו־שיח עורך תכונות

![[_media/AttributeEditor-dialog-default-60.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Attribute Editor - Dialog - default]] The top of the window shows the dialog title including the name of the person whose attribute is being edited. The central part of the window displays three notebook tabs containing different categories of available information. You can bring any tab to the top for viewing or editing by clicking on the appropriate tab heading. The bottom part has and buttons. Clicking the button at any time will apply all the changes made in all tabs and close the dialog window. Clicking the button at any time will close the window without applying any changes.

The top section allows editing of the most general information about the attribute:

- (`Identification Number`default) The name of an attribute you want to use. For example: *Height* (for a person), *Weather on this Day* (for an event), ... Use this to store snippets of information you collect and want to correctly link to sources. Attributes can be used for people, families, events, and media. The information can be typed in the appropriate text entry fields. The attribute name can also be selected from available choices (if any) listed in the drop-down menu.

- Toggle this to mark this attribute record as private or public. This will give you a chance to omit this attribute from being included in the reports if you choose so among the report generation options.

- Plain text description entry of the attribute. Eg. *1.8m, Sunny, or Blue eyes*.

{{-}}

### Attribute Editor tab pages

#### Source Citations

  
The tab displays information about citations and sources relevant to this attribute and controls allowing its modification. The central part displays the list of all such sources and citations references stored in the database. The buttons , , and allow you to correspondingly add, modify, and remove a source reference to this attribute. Note that the and buttons become available only when a citation/source reference is selected from the list.

#### הערות

  
The tab displays any notes concerning the attribute. To add a note or modify existing notes simply edit the text in the text entry field.

{{-}}

## כתובות

When you add or edit an address from the dialogs tab the dialog will be shown. {{-}}

### Address Editor dialog

![[_media/AddressEditor-dialog-default-60.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Address Editor - Dialog - default]] The dialog allows you to record a current address by recording the information in the appropriate text entry fields.

The top section of the dialog allows editing and entry of information about the address:

- Date at which the address is valid.

  - button

- The street of the address.

- button. Toggle this button to mark this address record as private or public. This will give you a chance to omit this address from being included in reports if you choose so among the report generation options.

- The locality name of the address.

- The state or county of the address in case a mail address must contain this.

- The village or city of the address.

- Country of the address.

- מיקוד.

- מספר טלפון מקושר לכתובת.

The bottom of the dialog has , and buttons. Clicking the button at any time will apply all the changes made in all tabs and close the dialog window. Clicking the button at any time will close the window without applying any changes. {{-}}

### Address Editor tab pages

The following tabs contain different categories of available information. You can bring any tab to the top for viewing or editing by clicking on the appropriate tab heading.

#### Source Citations

  
The tab displays information about sources relevant to this address and controls allowing its modification. The central part displays the list of all such sources and citations references stored in the database. The buttons , , and allow you to correspondingly add, modify, and remove a citation/source reference to this address. Note that the and buttons become available only when a source reference is selected from the list.

#### הערות

  
The tab displays any notes concerning the address. To add a note or modify existing notes simply edit the text in the text entry field.

{{-}}

## מיזוג רשומות

![[_media/PeopleCategory-Toolbar-MergeTheSelectedPersons-icon-example-60.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Merge the Selected Persons - Toolbar icon highlighted - example]] Sometimes several records in your family tree turn out to be describing the same object: same person, same place, or same citation/source. It could happen either when the data is entered twice by mistake, or when new information reveals that the two entries refer to the same person. It can also happen after importing a GEDCOM obtained from a relative, whose database overlaps with your existing data.

Whenever you detect duplicate records, merging them is a useful way of correcting the situation. {{-}}

### מיזוג אנשים

![[_media/MergePeople-dialog-default-example-60-he.png|איור {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} חלון הדו־שיח "מיזוג אנשים" – עם מקטע "בחירה מפורתת" פתוח – דוגמה]]

בעת העבודה עם מסדי נתונים גנאלוגי, ייתכן שתיווצר יותר מרשומה אחת עבור אותו אדם — לדוגמה, כאשר מוזנים נתונים כפולים ממקורות שונים או בעת יבוא מידע מקובץ אחר. כלי של גרמפס נועד לטפל במקרים כאלה, ומאפשר לאחד שתי רשומות של אנשים שנבחרו, תוך שמירה על כל המידע — גם אם הוא מופיע בצורה שונה בכל אחת מהרשומות.

פעולת המיזוג, מאפשרת בחירה ברשומה שתשמש כעיקרית, והמידע מהרשומה השנייה יישמר כנתונים חלופיים — לדוגמה: שמות חלופיים, הורים חלופיים, בני זוג חלופיים, ילדים חלופיים, ועוד. כלי זה מבטיח שלא יימחק מידע, אלא רק יאורגן מחדש כך שרק רשומה אחת תישאר פעילה, וכל הנתונים יאוחדו תחתיה.

כלי המיזוג מחייבת בחירת שני אנשים בדיוק, יש לבחור כדי לפתוח את חלון .

החלון מאפשר להחליט אם למזג את הרשומות שנבחרו. אם הוחלט שלא למזגן, אף על פי שהשמות בהן דומים, ניתן ללחוץ על לחצן כדי לסגור את החלון בלי לבצע שינויים.

ניתן לפתוח את השדה בתחתית משמאל כדי להציג מידע נוסף שבעזרתו ניתן להחליט איזו רשומה תוגדר כרשומה העיקרית במיזוג.

השדה בתחתית משמאל מציג מידע נוסף על האנשים שנבחרו למיזוג.

כדי לבצע את המיזוג, יש לבחור באמצעות לחצן הבחירה ![[_media/RadioButton_Selected.png]] את הרשומה שתשמש כמקור לנתונים העיקריים, ולאחר מכן ללחוץ על . הנתונים מהרשומה השנייה יישמרו כנתונים חלופיים.

למשל, כל השמות ברשומה השנייה יהפכו לשמות חלופיים ברשומה הממוזגת. בדומה לכך, הורים, זוגאים וילדים ברשומה השנייה יישמרו כהורים, זוגאים זוג וילדים חלופיים.

למידע נוסף:

- [איתור אנשים כפולים אפשריים](wiki:Gramps_6.0_Wiki_Manual_-_Tools/he#איתור_אנשים_כפולים_אפשריים)
- [פעולת מיזוג אנשים](wiki:Merging_people/he)

{{-}}

### מיזוג משפחות

![[_media/MergeFamilies-dialog-sections-expanded-example-51_he.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} מיזוג משפחות - &quot;בחירה מפורטת&quot; – דו־שיח – דוגמה]] לאחר סימון (בדיוק) שתי משפחות למיזוג (הגיוני למדי, שכן לא ניתן למזג רשימה בודדת), יש לבחור מהתפריט ב כדי לעורר את חלון דו־השיח .

חלון דו־השיח מאפשר לקבל החלטה האם להמשיך ולמזג את הרשומות שנבחרו או לאו. אם ההחלטה שהתקבלה היא שאין למזג את הרשומות, למרות שהן דומות, נא להקיש על ל סגירת הדו־שיח מבלי לבצע כל שינוי.

נא לבחור באחת משתי המשפחות שתהווה מקור נתונים עיקרי למשפחה החדשה. אפשרות שניה היא על ידי הרחבת שדה } וסימון את כפתורי־הרדיו הרצויים ומאפשרים מרחב בחירה עשיר יותר, כך לדוגמה ניתן לבחור בנפרד:

- מי מאבות שתי המשפחות ישמש כמקור הנתונים הראשי,
- מי מהאמהות תשמש כמקור נתונים ראשי,
- איזו משפחה (נבחרה על ידי Gramps ID) תהווה מקור נתונים אחרים ראשיים .

להמשיך במיזוג, נא בכפתורי־הרדיו המתאימים להגדרת מקורות הנתונים הראשיים עבור הרשומה המשפחתית הממוזגת. הקשה על תאשר את ביצוע פעולת המיזוג.

פעולת המיזוג מטפלת ברשומות באופן הבא:

- צאצאי שתי המשפחות יאוחדו למשפחה אחת ויופיעו ברשומות המשפחה החדשה.
- רשומות שני האבות ימוזגו ואירועים מרשומות האב המשני יקושרו לאב הראשי. שמות מרשומת האב המשני יהפכו לשמות חלופיים של האב הראשי.
- תהליך זהה מתרחש גם עם רשומות שתי אמהות המשפחות הממוזגות.
- האירועים הקשורים למשפחה המשנית (כמו נישואין או גירושין) יקושרו למשפחה הראשית.
- לסיום התהליך, רשומות המשפחה, האב והאם המשניים ימחקו ממסד הנתונים.

למעשה אין אובדן מידע או רשומות אלא סידור וקישור המידע בצורה אחרת. {{-}}

### מיזוג אירועים

![[_media/MergeEvents-dialog-example-default-60.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Merge Events - dialog - default example]] When exactly two events are selected, choose to invoke dialog.

The dialog allows you to decide on whether or not the selected records should be merged.

By expanding the field you can see additional information about the merge.

If you decide that the records should not be merged, despite similar titles, you may click to close the dialog without making any changes.

If you decide to proceed with merging, choose the appropriate radio button to specify:

- סוג
- תאריך
- מקום
- תאור
- מזהה גרמפס

to be used for the merged record, then click {{-}} ![[_media/MergeEvents-dialog-DetailedSelection-section-expanded-example-60.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Merge Events - &quot;Detailed Selection&quot; section expanded - dialog - example]] {{-}}

### מיזוג מקומות

![[_media/MergePlaces-dialog-example-default-60.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Merge Places - dialog - default example]] When exactly two places are selected, choose to invoke dialog.

By expanding the field you can see additional information about the merge.

The dialog allows you to decide on whether or not the selected records should be merged.

If you decide that the records should not be merged, despite similar titles, you may click to close the dialog without making any changes.

If you decide to proceed with merging, choose the appropriate radio button to specify:

- כותרת
- קו־אורך
- קו־רוחב
- מיקום
- מזהה

to be used for the merged record, then click . {{-}} ![[_media/MergePlaces-dialog-DetailedSelection-section-expanded-example-60.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Merge Places - &quot;Detailed Selection&quot; section expanded - dialog - example]] {{-}}

### מיזוג מקורות

![[_media/MergeSources-dialog-example-default-60.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Merge Sources - dialog - default example]] When exactly two sources are selected, choose to invoke dialog.

By expanding the field you can see additional information about the merge.

The dialog allows you to decide on whether or not the selected records should be merged.

If you decide that the records should not be merged, despite similar titles, you may click to close the dialog without making any changes.

If you decide to proceed with merging, choose the appropriate radio button to specify:

- Title
- Author
- Abbreviated title
- Publication information
- ID

to be used for the merged record, then click . {{-}} ![[_media/MergeSources-dialog-DetailedSelection-section-expanded-example-60.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Merge Sources - &quot;Detailed Selection&quot; section expanded - dialog - example]] {{-}}

### מיזוג מובאות

![[_media/MergeCitations-dialog-example-default-60.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} — &quot;מיזוג מובאות&quot; – חלון ברירת־מחדל – דוגמה]] כאשר בדיוק שתי מובאות מסומנות, ניתן לבחור ב כדי לפתוח את חלון .

בהרחבת השדה ניתן לצפות במידע נוסף על אודות פרטי המיזוג.

החלון מאפשר להחליט האם יש למזג את הרשומות שנבחרו.

אם הוחלט שלא למזג את הרשומות – חרף שמות דומים – ניתן ללחוץ על כדי לסגור את החלון ללא ביצוע שינויים.

אם הוחלט להמשיך במיזוג, יש לבחור את לחצן הבחירה המתאים כדי לקבוע אילו פרטים ישמשו ברשומת המובאה המאוחדת:

- עמוד/כרך
- תאריך
- רמת אמינות
- מזהה גרמפס (Gramps ID)

ולאחר מכן ללחוץ על .

לקריאה נוספת: [הכלי "מיזוג מובאות..."](wiki:Gramps_6.0_Wiki_Manual_-_Tools/he#מיזוג_מובאות) {{-}} ![[_media/MergeCitations-dialog-DetailedSelection-section-expanded-example-60.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} — &quot;מיזוג מובאות&quot; – חלונית &quot;בחירה מפורטת&quot; מורחבת – דוגמה]] {{-}}

### מיזוג מאגרים

![[_media/MergeRepositories-dialog-example-default-60.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Merge Repositories - dialog - default example]] When exactly two repositories are selected, choose to invoke dialog.

By expanding the field you can see additional information about the merge.

The dialog allows you to decide on whether or not the selected records should be merged.

If you decide that the records should not be merged, despite similar titles, you may click to close the dialog without making any changes.

If you decide to proceed with merging, choose the appropriate radio button to specify:

- Name
- Type
- Gramps ID

to be used for the merged record, then click {{-}} ![[_media/MergeRepositories-dialog-DetailedSelection-section-expanded-example-60.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Merge Repositories - &quot;Detailed Selection&quot; section expanded - dialog - example]] {{-}}

### מיזוג עצמי מדיה

![[_media/MergeMediaObjects-dialog-example-default-60.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Merge Media Objects - dialog - default example]] When exactly two Media Objects are selected, choose to invoke dialog.

By expanding the field you can see additional information about the merge.

The dialog allows you to decide on whether or not the selected records should be merged.

If you decide that the records should not be merged, despite similar titles, you may click to close the dialog without making any changes.

If you decide to proceed with merging, choose the appropriate radio button to specify:

- Title
- Path
- Date
- Gramps ID

to be used for the merged record, then click {{-}} ![[_media/MergeMediaObjects-dialog-DetailedSelection-section-expanded-example-60.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Merge Media Objects - &quot;Detailed Selection&quot; section expanded - dialog - example]] {{-}}

### מיזוג הערות

![[_media/MergeNotes-dialog-example-default-60.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Merge Notes - dialog - default example]] When exactly two notes are selected, choose to invoke dialog.

By expanding the field you can see additional information about the merge.

The dialog allows you to decide on whether or not the selected records should be merged.

If you decide that the records should not be merged, despite similar titles, you may click to close the dialog without making any changes.

If you decide to proceed with merging, choose the appropriate radio button to specify:

- Text
- Type
- Format
- Gramps ID

to be used for the merged record, then click {{-}} ![[_media/MergeNotes-dialog-DetailedSelection-section-expanded-example-60.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Merge Notes - &quot;Detailed Selection&quot; section expanded - dialog - example]]

{{-}}

[Category:He:מדריך למשתמש](wiki:Category:He:מדריך_למשתמש) [Category:He:תיעוד](wiki:Category:He:תיעוד)
