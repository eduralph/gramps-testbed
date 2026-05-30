---
title: Gramps 6.0 Wiki Manual - User Directory/he
categories:
- He:תיעוד
managed: false
source: wiki-scrape
wiki_revid: 118545
wiki_fetched_at: '2026-05-30T19:26:08Z'
lang: he
---

<div dir="rtl" lang="he" class="mw-content-rtl">

{{#vardefine:chapter\|D}} {{#vardefine:figure\|0}}

מטרת מקטע זה לתאר את האופן שמערכות ההפעלה השנות מתכתבות עם ספרית משתמש גרמפס.

\_\_TOC\_\_

## מערכות בסיגנון [POSIX](wiki:He:מילון_מונחי_גרמפס#posix)

מיקום ברירת המחדל של מחיצת משתמש גרמפס במערכות בסיגנון [POSIX](https://wikipedia.org/wiki/Posix) [סביבת־עבודה](https://wikipedia.org/wiki/Filesystem_Hierarchy_Standard), הוא:

<div dir="ltr">

`/HOME/`***<username>***`/.gramps`

</div>

למחיצה ניתן להגיע ממשורת הפקודה על ידי הזנת הפקודה הבאה:

<div dir="ltr">

***`<~username>`***`/.gramps`

</div>

הקישורים מעלה נכונים למערכות הפעלה מסוג [BSD](https://wikipedia.org/wiki/Bsd), [לינוקס](https://wikipedia.org/wiki/Linux), [סולריס](https://wikipedia.org/wiki/Solaris_(operating_system)), [יוניקס](https://wikipedia.org/wiki/Unix) ו[OS-X](https://wikipedia.org/wiki/Mac_OS_X%7Cמק) כאשר משתמשים ב[בניית מקOS X מהמקור](wiki:Build_from_source/he#Mac_OS_X).

לחלופין ניתן להשתמש ב־**\$HOME** [שווה ערך לספרית הבית](http://www.linfo.org/home_directory.html) על מנת להמנע מהזנת שם משתמש ארוך או מורכב. למרות שגרמפס לא יזהה מקבילות למחיצות לנתיבים באופן מובנה, ניתן להשתמש בהם בלינוקס למצויאת קבצי משתמש גרמפס. הנתיב ל **מחיצת משתמש גרמפס** ליעל הופשט לאחד מאלה:

<div dir="ltr">

`$HOME/.gramps`

</div>

או

<div dir="ltr">

`~/.gramps`

</div>

במערכת הפעלה מסוג מיקרוסופט וינדוס, התחביר ישתנה ויראה כך:

<div dir="ltr">

`$HOME\.gramps`

</div>

או

<div dir="ltr">

`~\.gramps`

</div>

### מק OS

![[_media/macos_200x200.png]] במחשבי אפל מק, שמות קבצים שמתחילים ב-"." לא יופיעו בחיפוש. לפשוט הגישה לספריית המשתמשי גרמפס, עדיף להשתמש במסוף Terminal, לפתוח חלון במסוף והקלד:

`ln -s ~/.gramps ~/Documents/Gramps`

פקודה זו תגרום למחפש (Finder) להציג את המחיצה כתיקייה בתיקיית המסמכים של המשתמש והיא תקבל את השם "Gramps". (ניתן כמובן להחליף את השם "Gramps" בכל שם אחר, אך חשוב לזכור להשתמש ב־"/" בשמות עם רווחים ("/" לפני הרווח יגרום לקוד לדלג על הרווח). לחלופין, ניתן פשוט להקיש על [](https://osxdaily.com/2011/08/31/go-to-folder-useful-mac-os-x-keyboard-shortcut/)\] והקליד את הפקודה הבאה:

<div dir="ltr">

`~\.gramps`

</div>

בתיבת דו־השיח שתופיע בהמשך לשימוש ב בשלב הקודם.

#### חבילת יישומון מק OS

[חבילת־יישומון](wiki:Mac_OS_X:Application_package) מתנהגת באופן שתואם יותר את תקני מק OS ומשתמשות במיקום ברירת מחדל למחיצה:

<div dir="ltr">

`/Users/`***`<~username>`***`/Library/Application Support/gramps`

</div>

## MS וינדוס

![[_media/windows_180x160.png]]בווידנוס מייקרוסופט שמות הקבצים והתיקיות של התוכניות ונתוני משתמשים [מוסתרים](https://wikipedia.org/wiki/Hidden_file_and_hidden_directory) ב*סייר הקבצים*. ניתן להקל על הגישה למחיצת משתמש גרמפס, זאת על פי העצה הבאה של מיקרוסופט:

- [הצג קבצים מוסתרים - עזרת ווינדוס](https://support.microsoft.com/en-ca/help/14201/windows-show-hidden-files)

מיקום ברירת המחדל למחיצת המשתמש (**User Directory** ) עבור כל נתוני גרמפס במערכת ווינדוס 7 ואילך, הוא:

<div dir="ltr">

`C:\Users\`***`<~username>`***`\AppData\Roaming\gramps`

</div>

המחרוזת ***\<~username\>*** בנתיב שלעיל הוא רק 'שומר־מקום' לשם המשתמש המסויים איתו התבצעה ההתחברות למערכת וינדוס.

לחלופין, ניתן למנף את **%AppData%** [משתני סביבת עבודה](https://wikipedia.org/wiki/Environment_variable#APPDATA) כדי להימנע מהתמודדות עם הסיבוכים של שמות משתמש פעילים. למרות שגרמפס לא יזהה משתני סביבה של נתיבים באופן מובנה, ניתן להשתמש בהם מתוך ווינדוס למציאת קבצי משתמש גרמפס. הנתיב ל**מחיצת משתמש גרמפס** שלעיל הופשט לכדי:

<div dir="ltr">

`%AppData%\gramps`

</div>

<hr />

כמו מחיצת המשתמש **User Directory**, מקום מחיצת היישומונים/תוכניות (programs/applications) מוסתרת גם היא בסייר הקבצים כברירת מחדל.

מיקום ברירת המחדל להתקנת תוכנת גרמפס במערכת ווינדוס 7 ואליך הוא:

<div dir="ltr">

`C:\Program Files\GrampsAIO64-5.X.X`

</div>

או

<div dir="ltr">

`C:\Program Files (x86)\GrampsAIO32-5.X.X`

</div>

{{-}}

## לקריאה נוספת

- אפשרויות תצור (config) [שורת פקודה](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line) באמצעות [משתני סביבת עבודה](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line#Environment_variables)
- [מעבר מפירורי לחם לתיבת מלל מיקום](https://winaero.com/how-to-enter-file-location-manually-in-gtk-3-opensave-dialog/) תוך שימוש ב־ GTK ב־ בדו־שיח קובץ
- ערוץ פורום דיסקורד : [כיצד להשתמש במשתני סביבה בגרמפס](https://gramps.discourse.group/t/how-to-set-the-base-path-from-media-relative-to-grampshome/481/2)

[Category:He:תיעוד](wiki:Category:He:תיעוד)
