---
title: Gramps 6.0 Wiki Manual - What's new?/he
categories:
- He:מדריך למשתמש
- He:תיעוד
managed: false
source: wiki-scrape
wiki_revid: 129550
wiki_fetched_at: '2026-05-30T18:51:11Z'
lang: he
---

<div dir="rtl" lang="he" class="mw-content-rtl">

חלק זה סוקר בסקירה כללית את כלל השינויים בתוכנה מאז גרסת גרמפס 5.1 (שינויים אלה מפורטים גם בהמשך המדריך). לכל אלו שמשדרגים מגרסאות קודמות או ישנותמקטע זה מציג סקירה כללית של השינויים מאז גרסה 5.2 של גרמפס. זוהי גרסת *שדרוג* (enhancement). לכן השינויים כוללים תכונות חדשות וכן תיקוני תקלים. שינויים אלה מפורטים גם בהמשך מדריך זה. מומלץ למשתמשים שׁמשדרגים לגרמפס מגרסאות מוקדמות יותר לעיין במקטע זה גם ב־[מדריכי המשתמש](wiki:User_manual) הישנים, כדי לוודא שנעשה שימוש בתכונות החדשות כאשר מתחילים להשתמש בגרסה 6.0. יש לחפש את סמל הברק במקטעים שׁמסומנים בתג "".

### רשימת שינויים מקדימה

**תיעוד גרמפס נכתב על־ידי מתנדבים, לכן תיעוד למשתמשים מתפרסם טיפיו טיפין ובהדרגה *לאחר* שהגרסה מתפרסמת לציבור הרחב.** (לפריטים מרכזיים נבחרים, התיעוד יסומן ב־"''</small>" כדי להקל על החיפוש.) מתנדבי התמיכה באתר הוויקי כותבים לא רק מתוך ניסיונם בעת חקירת התכונות החדשות, אלא גם תוך עיון בתיעוד יעדי פיתוח, בקשות תכונות חדשות, בדוחות מצב ובהערות לבקשות משיכה (Pull Request). לכל מי שעניין לחקור גם כן, ההכרזות שלהלן מקושרות חלקית למסמכים שאוזכרו. אפשר לחקור בחופשיות ולשתף תובנות כדי לסייע בהכוונת אחרים.

#### מתוך ההכרזות

מתוך מקטע **[Announcements](https://gramps.discourse.group/c/gramps-announce/5)** של **[פורום התמיכה הקהילתי של גרמפס ב־Discourse](https://gramps.discourse.group/t/welcome-to-the-gramps-discourse-forum/7)**:

- [6.0.5](https://github.com/gramps-project/gramps/releases/tag/v6.0.5) – גרסת תחזוקה חדשה, שׁשוחררה ב־2025-09-06.
- [6.0.4](https://github.com/gramps-project/gramps/releases/tag/v6.0.4) – גרסת תחזוקה חדשה, שׁשוחררה ב־2025-08-10.
- [6.0.3](https://github.com/gramps-project/gramps/releases/tag/v6.0.3) – גרסת תחזוקה חדשה, שׁשוחררה ב־2025-06-18.
- [6.0.2](https://github.com/gramps-project/gramps/releases/tag/v6.0.2) – גרסת תחזוקה חדשה, שׁשוחררה ב־2025-06-15.
- [6.0.1](https://github.com/gramps-project/gramps/releases/tag/v6.0.1) – גרסת תחזוקה חדשה, שׁשוחררה ב־2025-04-18.
- [6.0.0](https://github.com/gramps-project/gramps/releases/tag/v6.0.0) – מהדורה ראשית חדשה, שׁשוחררה ב־2025-03-19.
- [v6.0.0-rc2](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-rc2) – מהדורת קדם ניסיונית, שׁשוחררה ב־2025-03-16.
- [v6.0.0-rc1](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-rc1) – מהדורת קדם ניסיונית, שׁשוחררה ב־2025-03-03.
- [v6.0.0-beta2](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-beta2) – מהדורת קדם ניסיונית, שׁשוחררה ב־2025-02-13.
- [v6.0.0-beta1](https://github.com/gramps-project/gramps/releases/tag/v6.0.0-beta1) – מהדורת קדם ניסיונית, שׁשוחררה ב־2025-02-05.

דיונים מצד המפתחים על גרסה 6.0 העתידית:

- [Understanding Gramps 6.0](https://gramps.discourse.group/t/understanding-gramps-6-0/6652) מאת Doug Blank – פיתוח – מפת־דרך

<!-- -->

- שיפור שימושיות סרגל כלים מציג מלל מתחת לסמלים כברירת מחדל.[1](https://gramps.discourse.group/t/gramps-6-0-defaults/6990/3)

# לפי שמשדרגים

***לפני*** השדרוג, יש לוודא שנתוני אילן־היוחסין מאובטחים. הדרך הטובה ביותר לעשות זאת היא:

1.  להפעיל את הגרסה הקיימת של גרמפס (גרמפס 4.2‏/5.0‏/5.1‏/5.2)
2.  לפתוח את אילן־היוחסין
3.  לגבות את אילן־היוחסין לתסדיר *gramps xml* או לתסדיר *gramps xml package* (תסדיר *gramps xml package* כולל גם תצלומים וקובצי מדיה נוספים שׁקשורים לנתוני אילן־היוחסין). יש לגבות את האילן באמצעות התפריט .
4.  לסגור את אילן־היוחסין ולחזור על השלבים שלעיל עבור כל אילן־יוחסין נוסף שקיים
5.  לשמור את הקבצים שׁנוצרו במקום בטוח ומרוחק (כגון אחסון בענן)

למידע נוסף, מומלץ לעיין ב[גיבוי אילן־יוחסין](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/he#גיבוי_אילן־יוחסין). יש לשים לב ל[מה שלא ייכלל במהלך גיבוי](wiki:Template:Backup_Omissions/he).

לאחר אבטחה תקינה של הנתונים, יש להתקדם להתקנת גרמפס 6.0 באמצעות תהליך ההתקנה הרגיל של מערכת ההפעלה. ברוב המקרים, תהליך זה יבטיח שהתקנת גרמפס 6.0 החדשה לא תתנגש עם הגרסה הישנה של גרמפס. עם זאת, ייתכן שבטוח יותר להסיר את התקנת גרמפס 3.4 לפני התקנת גרמפס 6.0, או לוודא שגרמפס 6.0 מותקנת במיקום אחר. הדבר נדרש תמיד כאשר ההתקנה מתבצעת מקוד־המקור. למידע נוסף על התקנת גרמפס 6.0, ניתן לעיין ב[הורדת גרסת גרמפס העדכנית ביותר](wiki:Download/he).

לאחר התקנת גרמפס 6.0, ניתן לפתוח את אילנות־היוחסין הקיימים ולהמשיך בעבודה. במקרה שׁעולות בעיות (לדוגמה, לאחר שדרוג מערכת מלא), יש לייבא את קובצי הגיבוי שׁנוצרו לעיל כדי ליצור מחדש את אילנות־היוחסין.

{{-}}

## שינויים גלויים בליבה

שינויים שׁנראים לאחר השדרוג: מנשק, נתונים.

### מודל נתונים

פרטי שינויים ב־[מודל הנתונים](wiki:Gramps_Data_Model) (אם יש):

1.  אין שינוי

<hr>

- לא ניתן **לפתוח** אילן־יוחסין ב־<span dir="ltr">Gramps 3.4/4.0/4.1/4.2</span> וב־<span dir="ltr">Gramps 6.0</span> ללא שדרוג.

<!-- -->

- ניתן לבצע הורדה־בגרסה (downgrade) רק באמצעות ייצוא <span dir="ltr">XML</span> ויבוא אל הגרסה הקודמת.

<!-- -->

- קובץ <span dir="ltr">Gramps XML</span> שׁנוצר ב־<span dir="ltr">Gramps 3.4/4.0/4.1</span> **אינו זהה** לקובץ שׁנוצר ב־<span dir="ltr">Gramps 6.0</span>.

<!-- -->

- <span dir="ltr">Gramps 6.0</span> הוא כעת **python3** בלבד

למידע נוסף על מסד הנתונים הפנימי, ראו [שינויים מפורטים](wiki:Database_Formats#Detailed_Changes).

### שינויים עיקריים

- <span dir="ltr">SQLite</span> הוא כעת מנגנון מסד הנתונים כברירת מחדל במקום <span dir="ltr">BSDDB</span>. עדיין ניתן לבחור ב־[מנגנוני מסד נתונים חלופיים](wiki:Relational_database_comparison). <span dir="ltr">BSDDB</span> עדיין זמין כחלופה תקנית. למשתמשים מתקדמים זמינים <span dir="ltr">PostgreSQL</span> ו־<span dir="ltr">MongoDB</span> כתוספי צד־שלישי ניסיוניים.

המפתחים סבורים של־<span dir="ltr">SQLite</span> עשויים להיות פחות שיבושי מסד נתונים שׁמונעים שחזור קל.

- 

### מנשק

- 

### מקום

- יכולת לחפש שמות מקום חלופיים בעת בחירת מקום

### דוחות, כלים וגרמפלטים

- 

### יבוא/יצוא

- 

### תוספים חדשים

- 

## שינויים מאחורי הקלעים

שינויים טכניים.

- שינויים רבים שׁקשורים לתמיכה במנגנוני מסד נתונים אחרים (<span dir="ltr">SQLite</span>, <span dir="ltr">PostgreSQL</span>, <span dir="ltr">MongoDB</span> ועוד).

### תלויות

## מידע נוסף

### שונות

### התאמה לשפה

- תרגומים שעודכנו

#### תוספים מצד־שלישי

- [Weblate for Third-Party Addons Translation](https://gramps.discourse.group/t/weblate-translation-for-addons-experiment-needs-testers/6964)

### מפת־דרכים

- אפשר לעיין בהערות השחרור של [מהדורות קודמות של גרמפס](wiki:Previous_releases_of_Gramps)
- אפשר לראות פריטים חזויים שׁקשורים לגרמפס [בגרסה הבאה.](https://gramps-project.org/bugs/roadmap_page.php)
- [הצעות שדרוג לגרמפס (GEPS)](wiki::Category:GEPS) - יש לעיין בעמודת **Released** לפריטים חדשים שׁיושמו בגרמפס 6.0
- [6.0 Roadmap](wiki:6.0_Roadmap) - ויקי

### יומן שינויים

- פריטים שׁקשורים לגרמפס: [6.0](https://gramps-project.org/bugs/changelog_page.php) במעקב הסוגיות של גרמפס.

<!-- -->

- מידע נוסף: אפשר לעיין ביומני השינויים של מהדורות התחזוקה של גרמפס:
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

השוואת התחייבויות (<span dir="ltr">commits</span>) ב־GitHub: \[<https://github.com/gramps-project/gramps/compare/v5.2.4>...v6.0.1 Gramps 5.2.4 to 6.0.1\] {{-}}

### מה שהיה *פעם* חדש

דף [מהדורות קודמות](wiki:Previous_releases_of_Gramps) כולל קישורים לרשימות תבליטים של שינויים במהדורות ראשיות ובמהדורות תחזוקה לאורך השנים.

עם זאת, דפי **What's New?** במדריך הוויקי של הגרסה שׁהוחלפה עבור כל מהדורה ראשית יכולים לספק פירוט רב יותר:

- [גרסה 5.2](wiki:Gramps_5.2_Wiki_Manual_-_What%27s_new%3F)
- [גרסה 5.1](wiki:Gramps_5.1_Wiki_Manual_-_What%27s_new%3F)
- [גרסה 5.0](wiki:Gramps_5.0_Wiki_Manual_-_What%27s_new%3F)
- [גרסה 4.2](wiki:Gramps_4.2_Wiki_Manual_-_What%27s_new%3F)
- [גרסה 4.1](wiki:Gramps_4.1_Wiki_Manual_-_What%27s_new%3F)
- [גרסה 4.0](wiki:Gramps_4.0_Wiki_Manual_-_What%27s_new%3F)
- [גרסה 3.4](wiki:Gramps_3.4_Wiki_Manual_-_What%27s_new%3F)
- [גרסה 3.3](wiki:Gramps_3.3_Wiki_Manual_-_What%27s_new%3F)
- [גרסה 3.2](wiki:Gramps_3.2_Wiki_Manual_-_What%27s_new%3F)

סקירה תמציתית של שדרוגים נוספה לראשונה למדריך בשנת 2010. בשלוש השנים הראשונות של הוויקי היה צורך לעיין בכל המדריך.

### מדריך להורדה

גרסה 6.0 - מדריך להורדה

- [PDF באנגלית](wiki::File:Gramps6.0UserManual.pdf)

איננו מפרטים בדף זה כל תיקון תקל או שיפור קטן. כדי לקבל רשימה שלמה יותר של שינויים, יש לעיין בהיסטוריית ההתחייבויות (<span dir="ltr">commit history</span>) ב־[ענף התחזוקה](https://github.com/gramps-project/gramps/commits/maintenance/gramps60) עבור כל מהדורה.

{{-}}

[Category:He:מדריך למשתמש](wiki:Category:He:מדריך_למשתמש) [Category:He:תיעוד](wiki:Category:He:תיעוד)
