---
title: Gramps 6.0 Wiki Manual - Manage Family Trees/he
categories:
- 'He: מדריך למשתמש'
- He:תיעוד
- Stub
managed: false
source: wiki-scrape
wiki_revid: 127178
wiki_fetched_at: '2026-05-30T19:18:45Z'
lang: he
---

<div dir="rtl" lang="he" align="justify" class="mw-content-rtl">

{{#vardefine:chapter\|5}} {{#vardefine:figure\|0}} סקירה מעמיקה של השימוש היומיומי בגרמפס. פרק זה מביא סקירה מפורטת של ניהול אילנות־יוחסין, וכן של שיתוף נתונים עם חוקרי יוחסין נוספים.

## ייצירת אילן־יוחסין חדש

![[_media/Menubar-FamilyTrees-overview-example-51_he.png|איור: {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} תפריט עליון - "אילנות־יוחסין" - תצוגה מקדימה]]

לייצירת אילן־יוחסין חדש, יש לבחור בתפריט , או להשתמש בלחצן הכלים , או להפעיל את קיצור המקשים . פעולה זו תפתח את חלון ניהול .

יש להקיש על לחצן כדי להוסיף ערך חדש לרשימת אילנות־היוחסין. לשינוי שם ברירת־המחדל (למשל: `Family Tree 1`), יש לבחור את השם ולהקיש על לחצן , ואז להקליד שם חדש.

לפתיחת אילן־יוחסין ריק, יש לבחור את השם ברשימה ולהקיש פעמיים או לבחור בלחצן .

{{-}}

![[_media/FamilyTrees-ManageDatabases-icon-toolbar-60.png|איור: {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} ניהול מסדי־נתונים – סמל בלחצן כלים (מקביל לתפריט )]]

{{-}}

![[_media/ConnectToARecentDatabase-icon-toolbar-60.png|איור: {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} התחברות למסד־נתונים אחרון – תפריט נפתח מהתפריט]]

{{-}}

### חלון ניהול אילנות־יוחסין

![[_media/FamilyTreesManager-window-example-60.png|איור: {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} חלון ניהול אילנות־יוחסין]]

הקשה על תפתח את חלון , שמאפשר לעבוד עם אילנות־יוחסין ולנהל אותם.

באמצעות חלון מנהל אילנות־יוחסין ניתן ליצור אילן־יוחסין חדש, לשנות את שמו של אילן קיים, למחוק אילן־יוחסין, לטעון אותו או להציג מידע אודותיו. כל שמות אילנות־היוחסין מופיעים ברשימה. אם אילן־יוחסין פתוח כעת, תופיע סמליל בעמודת המצב ליד שמו. נוסף לכך מוצגים סוג מסד־הנתונים והתאריך והשעה של הגישה האחרונה לאילן.

- — יצירת אילן־יוחסין חדש.

- — הצגת מידע על אילן־היוחסין הנבחר.

- — מחיקת אילן־היוחסין הנבחר; יוצג אזהרה עם בקשת אישור סופית.

- — שינוי שם של אילן־היוחסין הנבחר.

- — סגירת אילן־היוחסין הנבחר.

- — המרת אילן־יוחסין נבחר. אפשרות זו זמינה רק עבור מסדי־נתונים מסוג [BSDDB](wiki:Gramps_Glossary/he#bsddb) הישנים. למידע נוסף: [המרת אילן־יוחסין מ־BSDDB ל־SQLite](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/he#המרת_אילן־יוחסין_BSDDB_ל־SQlite).

- — תיקון אילן־היוחסין הנבחר, אם גרמפס זיהה בעיה.

- — אפשרות זו זמינה רק אם מותקן [GNU Revision Control System](http://www.gnu.org/software/rcs/)‏ (RCS).

- — פעולה משלימה ל; זמינה רק עם התקנת [RCS](http://www.gnu.org/software/rcs/).

- — פתיחת עזרה עבור מקטע זה.

- — סגירת חלון מנהל אילנות־יוחסין.

- — טעינת אילן־היוחסין הנבחר.

{{-}}

## פתיחת אילן־יוחסין

לפתיחת אילן־יוחסין, יש לבחור בתפריט או להקיש על לחצן שבסרגל הכלים. יופיע חלון , ובו יוצגו כל אילנות־היוחסין שגרמפס זיהה. בעמודת תופיע סמלית של תיקייה פתוחה ליד כל אילן־יוחסין שנטען כעת.

יש לבחור את אילן־היוחסין הרצוי, ולהקיש על לחצן . לחלופין, ניתן לבצע הקשה כפולה על שם האילן ברשימה.

לפתיחה מהירה של אילן־יוחסין שנפתח לאחרונה, יש לבחור באפשרות או להשתמש בחץ הקטן לצד לחצן שבסרגל הכלים, ולבחור מתוך הרשימה.

### מצב לקריאה בלבד

לתשומת לב: תפריט הכלים לא יהיה זמין במצב זה. {{-}}

### <big>▼</big> התחברות למסד־נתונים שנפתח לאחרונה

![[_media/ConnectToARecentDatabase-icon-toolbar-60.png|איור {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} התחברות למסד־נתונים שנפתח לאחרונה – סמל תפריט נפתח בסרגל הכלים]]

כדי לפתוח אילן־יוחסין שהיה בשימוש לאחרונה, יש לבחור באפשרות התפריט או ללחוץ על לחצן החץ למטה <big>▼ </big> שלצד לחצן סרגל הכלים ולבחור את אילן־היוחסין מהרשימה. {{-}}

#### אזהרת "לא ניתן לטעון אילן־יוחסין אחרון"

![[_media/Could-not-load-a-recent-Family-Tree-warning-60.png|איור {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} אזהרת "לא ניתן לטעון אילן־יוחסין אחרון"]]

אם אילן־היוחסין שנבחר מתוך הרשימה אינו זמין, תוצג האזהרה הבאה:

**לא ניתן לטעון אילן־יוחסין אחרון.**

*אילן־היוחסין אינו קיים, מאחר שנמחק.* {{-}}

## שמירת שינויים באילן־היוחסין

גרמפס שומר את השינויים מיד עם החלתם. משמעות הדבר היא שכל לחיצה על הלחצן **** בעת שימוש בגרמפס, השינויים נרשמים ונשמרים באופן מיידי. אין פקודה נפרדת ל**שמירה**.

ניתן להסיג שינויים שבוצעו על־ידי בחירה בתפריט ****. שימוש בפקודה זו מספר פעמים ברצף, כל שינוי אחרון יוסג צעד־אחר־צעד. כדי להחזיר מספר פעולות יחד, ניתן להשתמש בתפריט ****.

כדי להחזיר את אילן־היוחסין למצב שבו היה בעת פתיחתו, יש לבחור בתפריט ****. (פעולה זו דומה ליציאה מתוכנות אחרות מבלי לשמור שינויים.) תוצג חלונית אזהרה ****.

לשמירת עותק של אילן־היוחסין בשם אחר, יש לייצא אותו ולאחר מכן לייבא אותו לתוך אילן־יוחסין בשם החדש. לתכלית זו מומלץ להשתמש בתסדיר מאגר הנתונים **גרמפס XML**.

## פתיחת מסד נתונים מסוג GEDCOM או XML

ניתן לפתוח מסדי נתונים מסוימים שלא נשמרו בתסדיר הקבצים של גרמפס באופן ישיר, באמצעות שורת הפקודה. מידע נוסף נמצא בעמד [הפניה למתגי פתיחה בשורת הפקודה](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/he#אפשרויות_פתיחה). בין התסדירים הנתמכים כלולים קבצי XML ו־GEDCOM. עם זאת, יש לקחת בחשבון שכאשר מדובר בקבצים גדולים יחסית, עלולות להתעורר בעיות ביצועים, ובמקרה של קריסה — ייתכן שתתרחש פגיעה בנתונים. לפיכך, עדיף במקום זאת ליצור אילן־יוחסין חדש בגרמפס (כלומר מסד נתונים ריק  חדש) ולייבא לתוכו את הנתונים מקובצי ה־XML או GEDCOM.

{{-}}

## מחיקת אילן־יוחסין

יש לבחור את אילן־היוחסין אותו מעונינים להסיר, ולהקיש על לחצן . פעולה זו תביא ל**מחיקה מוחלטת** של האילן, ללא אפשרות לשחזור הנתונים. **לפני כל מחיקה**, מומלץ לשקול יצירת גיבוי של הנתונים באמצעות יצוא לתסדיר Gramps XML ושמירת הקובץ. {{-}}

## שינוי שם אילן־יוחסין

ניתן לשנות את שם אילן־היוחסין (או ארכיון שלו) על־ידי בחירת האילן הרצוי והקשה על לחצן . אפשרות נוספת היא ללחוץ ישירות על השם ברשימת האילנות. בכל מקרה, יש להקליד את השם החדש כדי שהשינוי ייכנס לתוקף.

{{-}}

## גיבוי אילן־יוחסין

הדרך הבטוחה ביותר לגבות אילן־יוחסין בגרמפס היא לייצא אותו ללא הגבלת פרטיות ומסננים, לתסדיר **גרמפס XML** (או **חבילת גרמפס XML** כדי לכלול גם את כל פריטי המדיה שבגלריה) ולהעתיק/להעביר את הקובץ שנוצר למקום ממשי מרוחק ובטוח, לדוגמה באחסון ענן או על גבי החסן נייד בבית קרוב משפחה.

### דו־שיח גיבוי

![[_media/MakeBackup-GrampsXML-Backup-52_he.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} ליצירת גיבוי בחירה מתפריט ב]]

אל חלון דו־שיח ניתן להגיע מתפריט . חלון הדו־שיח כולל את אפשרויות התיצור הבאות:  
– ניתן להזין את הנתיב שבו יאוחסנו הגיבויים בעת יצירת גיבוי באופן ידני או באמצעות הלחצן כדי להעלות את דו־השיח .  
– נתן להזין שם קובץ גיבוי באופן ידני או להשתמש בשם הקובץ שנוצר באופן אוטומטי.  
– ניתן לבחור *לכלול* או **לא לכלול** (ברירת מחדל) את כל קובצי המדיה שבגלריה באילן־היוחסין.  
{{-}}

- ניתן להשתמש בתכונת הארכיון (כמתואר בסעיף הבא) כדי ליצור ואחסן צילום־חטף של אילן היוחסין . ניתן להשתמש בצילמי־חטף אלה כגיבויים פשוטים, תכונה זו שימושית במיוחד אם יש כוונה לנסות פעולות מסויימות שאולי יהיה צורך לבטל מאוחר יותר. יחד עם זאת אין להשתמש בשיטה זו לביצוע גיבויים תקניים, מכיוון שצילום־חטף כזה לא ישרוד במצב של קריסת כונן קשיח או את רוב ה'אסונות' האחרים שעלולים לפקוד מחשב.

<!-- -->

- *למשתמשים מתקדמים:* כל מסד נתונים מאוחסן במחיצת משנה משלה, בסבבות דמוי לינוקס במחיצת ‎~/.gramps. למרות שניתן לבצע גיבוי ידני על ידי גיבוי של מחיצה זו, זה לא מומלץ. מומלץ בחום להשתמש בגיבוי XML של גרמפס במקום זאת.

### גיבוי בעת יציאה

בלשונית העדפות , ניתן להגדיר את גרמפס כך שייווצר גיבוי בכול יוצא מגרמפס. לתשומת לב הגיבוי שייוצר הוא רק לאילן־היוחסין הפעיל (הפתוח). אם אילן־יוחסין נסגר לפני היציאה מגרמפס, לא ייוצר קובץ גיבוי.

- [הגדרות אילן יוחסין](wiki:Gramps_6.0_Wiki_Manual_-_Settings/he#אילן־יןחסין)

### גיבוי אוטומטי

בלשונית העדפות , ניתן להגדיר את גרמפס כך שייצןר גיבוי באופן אוטומטי, כל 15, 30 או 60 דקות.

לקריאה נוספת:

- [הגדרות אילן יוחסין](wiki:Gramps_6.0_Wiki_Manual_-_Settings/he#אילן־יוחסין)
- [הגדרה מתקדמת של שם קובץ גיבוי](wiki:Gramps_6.0_Wiki_Manual_-_Settings/he#Advanced_backup_filename_setting) – דפוס שמות שם קובץ הגיבוי ניתן אףהוא להגדרה.
- [השמטות גיבוי](wiki:Template:Backup_Omissions/he) – מה לא כלול בקובצי הגיבוי

## ארכוב אילן־יוחסין

ניתן להשתמש בלחצן כדי לשמור עותק של אילן־היוחסין לפני ביצוע שינויים משמעותיים, וכך לאפשר חזרה לגרסה ידועה.

ליצירת ארכיון:

![[_media/ManageFamilyTrees-Archive-RevisionComment-example-60.png|איור {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} דוגמה לארכיון אילן־יוחסין]] טעינת אילן־היוחסין המבוקש. הקשה על לחצן בסרגל הכלים (כאשר מצביעים עליו מופיע המלל ). הקשה על אילן־היוחסין שנטען כעת; לחצן אמור להופיע. לחיצה על וניתן להזין בחלון הדו־שיח תיאור גרסת הארכיון.

לאחר יצירת הארכיון, ברשימת האילנות יופיע ליד אילן־היוחסין המקורי משולש הפונה ימינה. לחיצה על המשולש כדי להציג את שמות הארכיונים. (לחיצה חוזרת כדי לכווץ את רשימת הארכיונים). ניתן למחוק , לשנות את שמו ולהוציא אותו .

{{-}}

## חילוץ ארכיון אילן־יוחסין

![[_media/ManageFamilyTrees-Archive-Selected-to-Extract-example-60.png|איור {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} חלון ניהול "אילנות־יוחסין" – ארכיון נבחר ומוכן לחילוץ – דוגמה]]

כדי לשחזר גרסה מתוך ארכיון אילן־יוחסין, יש לסמן את פריט הארכיון הרצוי בחלון ניהול , ואז ללחוץ על לחצן .

{{-}}

![[_media/ManageFamilyTrees-Archive-Extracted-version-selected-example-60.png|איור {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} חלון ניהול "אילנות־יוחסין" – גרסת ארכיון שנבחרה וחולצה – דוגמה]]

הארכיון יחולץ אל אילן־יוחסין חדש שיופיע ברשימת האילנות.

שם האילן החדש ייגזר משם האילן המקורי ושם הארכיון, כגון:<שם האילן המקורי>:<שם הארכיון>.(למידע נוסף נא לעיין ב [ארכוב אילן־יוחסין](#ארכוב_אילן־יוחסין))

שיטה זו עשויה להועיל בשמירת עותק של גרסת אילן־יוחסין, שכן הארכיוניםש נוצרו נמחקים כאשר האילן המקורי נמחק, ו־**הם אינם נכללים בקובץ ייצוא בתסדיר XML של גרמפס**.

{{-}}

## שחרור נעילת אילן־יוחסין

![[_media/FamilyTreesManager-Dialog-ShowingLocked-Sample-50.png|איור {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} חלון ניהול &quot;אילנות־יוחסין&quot; – דוגמה: אילן נעול בשם &quot;Sample&quot;]] גרמפס היא תוכנה לניהול מסד נתונים עבור משתמש יחיד. בעת פתיחת אילן־יוחסין, גרמפס שומר קובץ lock בתיקיית־המשנה של האילן תחת תיקיית grampsdb שב[תיקיית המשתמש](wiki:Gramps_6.0_Wiki_Manual_-_User_Directory/he). קובץ זה מציין שכרגע נעשה שימוש באילן, וכולל את שם המשתמש והמתחם. גרמפס לא תאפשר לפתוח את אותו האילן בשני אדגמים בו זמנית במקביל. לעומת זאת, ניתן לפתוח אילן אחר באדגם נוסף.

אם אילן מסוים פתוח כבר, תופיע ליד שמו עִקּוּן נעילה (![[_media/22x22-gramps-lock.png]]) בעמודת המצב בחלון ניהול האילנות. סגירת האילן באדגם הראשון תביא למחיקת קובץ הנעילה, ותאפשר גישה לאילן באדגם השני.

אם תתאפשר פתיחת אותו אילן בשני אדגמים במקביל, הנתונים עלולים להינזק כתוצאה מכתיבה חופפת בין אדגמים.

#### למידע נוסף:

[שורת פקודה: אפשרות לשחרור נעילה](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/he#אפשרות_אילוץ_שחרור_נעילה)

### חלון שחרור נעילה: "האם לשחרר את הנעילה על מסד הנתונים \[שם אילן־היוחסין\]?"

![[_media/ErrorParsingArguments-dialog-DatabaseIsLocked-example-50.png|איור {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} חלון שגיאת ניתוח משתנים – דוגמה: מסד הנתונים נעול]]

במקרה הלא־שכיח שבו גרמפס קורס, האילן יישאר נעול (ויופיע סמל הנעילה ![[_media/22x22-gramps-lock.png]] בעמודת המצב ליד שמו).

שחרור נעילה במהלך אתחול:

אם בהעדפות מוגדרת האפשרות לפתוח אילן מסוים עם אתחול גרמפס, יופיע חלון שגיאה בשם "Error parsing arguments" המציין כי מסד הנתונים נעול. יש ללחוץ על , ואז לבחור בתפריט .

אחרת, עם אתחול גרמפס תופיע ישירות חלונית .

{{-}} ![[_media/Break-the-lock-on-the-database-Dialog-example-50.png|איור {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} חלון שחרור נעילה על מסד נתונים &quot;Sample&quot; – דוגמה]]

יש לבחור את האילן הנעול וללחוץ על . יופיע חלון אישור הנעילה: **האם לשחרר את הנעילה על מסד הנתונים \[שם אילן־היוחסין\]?**

לחיצה על לחצן תביא לעדכון החלונית כך שסמל הנעילה ייעלם.

לאחר מכן ניתן לבחור שוב באילן וללחוץ על כדי להמשיך בעבודה.

{{-}}

## תיקון אילן־יוחסין שניזוק

![[_media/FamilyTreesManager-Dialog-ShowingRedErrorStatusIcon-Sample-50.png|איור {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} חלון ניהול אילנות־יוחסין – דוגמה: אִילָן בשם "Sample" שניזוק ומוצג עם סמל שגיאה אדום בעמודת המצב]]

אם אילן־יוחסין ניזוק או הושחת באופן כלשהו, חלון ניהול אילנות־היוחסין של גרמפס יציג סמל שגיאה אדום בעמודת .

כדי שגרמפס ינסה לתקן את הנזק, יש לבחור את האילן וללחוץ על לחצן .

גרמפס ינסה לשחזר את אילן־היוחסין מתוך קובצי הגיבוי שנשמרו באופן אוטומטי בעת היציאה האחרונה מהתוכנה.

למידע נוסף:

- [תיקון אילן־יוחסין שניזוק](wiki:Recover_corrupted_family_tree/he) מתאם לגרסאות גרמפס ישנות יותר עד לגרסה 5.1.

{{-}}

## המרת אילן־יוחסין מסוג BSDDB ל־SQLite

![[_media/ManageFamilyTrees-Convert-the-database-dialog-example-51.png|איור {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} חלון המרה "האם להמיר את מסד הנתונים [שם אילן־היוחסין]?" עם חלונית "ניהול אילנות־יוחסין" ברקע]]

עד גרסה 5.1, גרמפס תמך במסד נתונים מסוג BSDDB, אם קיים עדין אילן־יוחסין ישן מסוג [BSDDB](wiki:Gramps_Glossary/he#bsddb) – כלומר ערך "סוג מסד נתונים" מציין BSDDB – גרמפס מאפשר לבצע המרת מסד הנתונים למסד נתונים מסוג SQLite. במקרה כזה לחצן בחלונית יהפוך לפעיל (אחרת הוא מופיע על רקע אפור, כלומר לא פעיל).

כאשר הכל מוכן, יש ללחוץ על , ואז יופיע החלון עם ההודעה: **האם להמיר את האילן למסד נתונים מסוג SQLite?**

ניתן לבחור כדי להפסיק או כדי להתחיל את התהליך. לאחר ההמרה, תוצג רשומה חדשה בחלונית "ניהול אילנות־יוחסין" עבור האילן המומר, עם ערך "סוג מסד נתונים" המציין SQLite.

יש לפתוח את האילן המומר ולגבות אותו.

לאחר מכן אפשר לשנות את שמו של האילן הישן (BSDDB) כך שיכלול את המילה "OLD" או למחוק אותו כדי למנוע בלבול. לאחר מכן ניתן לשנות את שם האילן החדש (SQLite) לשם המקורי.

{{-}}

## ייבוא נתונים

ייבוא מאפשר להעביר נתונים מתוכנות גנאלוגיה אחרות אל תוך אילן־יוחסין בגרמפס. גרמפס מסוגל לייבא נתונים מהתסדירים הבאים:

- [Gramps XML](#Gramps_XML_and_XML_Package_import) (סיומת קובץ `.gramps`) — תסדיר חילופין ייעודי של גרמפס, כקובץ מלל בלתי דחוס או דחוס באמצעות [gzip](https://wikipedia.org/wiki/Gzip)
- [חבילת Gramps XML](#Gramps_XML_and_XML_Package_import) (סיומת קובץ `.gpkg`) — תסדיר גיבוי דחוס בארכיון [.tar.gz](https://wikipedia.org/wiki/.tar.gz)
- [מסד נתונים מגרסה GRAMPS V2.x](#GRAMPS_V2.x_database_import) (סיומת קובץ `.grdb`)
- [גיליון אלקטרוני מסוג CSV](#Gramps_CSV_import) — ערכים מופרדים בפסיקים (סיומת `.csv`)
- [GEDCOM](#GEDCOM_import) (סיומת קובץ `.ged`) — תסדיר חילופין מקובל להעברת נתונים בין תוכנות גנאלוגיה
- GeneWeb (סיומת קובץ `.gw`) — [GeneWeb](https://en.wikipedia.org/wiki/GeneWeb) היא תוכנה גנאלוגית בעלת מנשק מבוסס־רשת
- Pro-Gen (סיומת קובץ `.def`) — [Pro-Gen](https://www.pro-gen.nl/gbhome.htm) תוכנה ותיקה שהייתה נפוצה במיוחד בהולנד ובצפון־מערב גרמניה. רבים השתמשו בה עוד משנת 1989. מדובר בתוכנה שהופעלה על DOS והותאמה בהמשך לעבודה תחת וינדוס 10
- vCard (סיומת קובץ `.vcf`) — תסדיר [כרטיס ביקור אלקטרוני](https://wikipedia.org/wiki/VCard) לפי תקן נפוץ
- ייבוא JSON (סיומת קובץ `.json`) — [JSON](https://www.json.org/) הוא תסדיר חילופין קל־משקל להעברת נתונים
- ייבוא SQLite (סיומת קובץ `.sql`) — תסדיר מסד נתונים של [SQLite](https://www.sqlite.org/fileformat.html)

{{-}}

### דו־שיח ייבוא אילן־יוחסין

![[_media/Importfamilytree-dialog-51_he.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} ייבוא אילן־יוחסין – דוגמת חלון דו־שיח]]

תחילה יש ליצור [אילן־יוחסין חדש וריק](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/he#Starting_a_new_Family_Tree), ולהזין שם לאילן־היוחסין. לאחר מכן מתפריט או באמצעות [צרוף המקשים](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/he#2) לפתיחת חלון דו־שיח **** לבחירת קובץ ולהתחיל בתהליך ייבוא נתונים מקובץ שנתקבל מתוכנה אחרת או כדי לשחזר קובץ גיבוי אילן־יוחסין של גרמפס שנשמר קודם (מגרסה ישנה יותר של גרמפס או מהגרסה הנוכחית).

![[_media/UndoHistoryWarning-Import-dialog-52.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} תיבת דו־שיח אזהרת ייבוא]] בעת ניסיון לייבא נתונים ל​​אילן־יוחסין שהוא ***לא ריק***, יפתח חלון דו־שיח . זוהי רק תזכורת לבצוע גיבוי לפני ייבוא, במקום זאת יש לייצור אילן־יוחסין חדש, אלא אם הכוונה היא למזג ביודעין נתונים משני אילנות־יוחסין.

גרמפס משתמש ב[ברר קבצים GTK](https://docs.gtk.org/gtk3/iface.FileChooser.html) לבחירת קובץ הנתונים לייבוא. אופן הניווט לקובץ מוכר וברור בדומה לשימוש במנהל הקבצים או סייר קבצים תקני.

אפשרות מצג ברירת המחדל לנתיב הקובץ היא להציג כל רמת מחיצה כלחצן בר הקשה [בסיגנון ניווט סימני־דרך](https://en.wikipedia.org/wiki/Breadcrumb_navigation). ניתן להזין את הנתיב בתיבת המלל שנועדה לעריכה על ידי שימוש בצרוף המקשים .

אפשרות על פי סיומת סוג הקובץ תזהה את תסדיר הקובץ ותמיר אותו לתסדיר מסד הנתונים המקורי. ניתן לעקוף זאת על ידי בחירה באחת מאפשרויות הזמינות כמו ****או ולסנן את רשימת הקבצים.

במקרים בהם נדרש לחזור על פעולת הייבוא ​​שוב ושוב (למטרת עדכונים שוטפים או להכללת מחקר יוחסין), ניתן [1068/5 להתאים את תיבת ־דו־השיח בהתאמה אישית](https://gramps.discourse.group/t/need-help-doing-a-cross-os-linux-mac-verification/) על ידי הוספת לחצנים לנתיבי המחיצות מסומנות על ידי הקשת עכבר ימנית על שם מחיצה ובחירה מהתפריט הצץ באפשרות .

{{-}}

### ייבוא מסד נתונים מסוג גרמפס V2.x

מסד נתונים של גרמפס V2.x (סיומת <span dir="ltr">.grdb</span>) — בגרסאות גרמפס שקדמו לגרסה 3.0, תסדיר מסד הנתונים הייעודי של גרמפס היה גרסה ייחודית של בסיס הנתונים Berkeley (כלומר [BSDDB](wiki:Gramps_Glossary/he#bsddb)), עם מבנה ייחודי של טבלאות נתונים. התסדיר היה בינרי ותלוי ארכיטקטורת־מעבד. הוא היה מהיר ויעיל מאוד, אך לא ניתן היה להעביר אותו בין מחשבים בעלי ארכיטקטורות בינאריות שונות (למשל i386 לעומת alpha).

ייבוא תסדיר גרמפס V2.x נתמך רק בגרסה ‪3.0.x‬ של גרמפס. ייבוא של V2.x לגרמפס ‪3.0.x‬ אינו גורם לאובדן נתונים.

#### העברת מסדי נתונים מגרמפס 2.2 לגרסה 3.x

כדי להעביר את הנתונים מגרסת גרמפס2.x לגרסה ‪6.0.x‬, יש לייבא תחילה את מסד הנתונים לגרסת גרמפס ‪3.0.x‬ מוקדמת, ואז לשמור את מסד הנתונים ולייבא אותו מחדש לגרסה ‪6.0.x‬, או לייצא אותו בתסדיר [XML](wiki:XML) מהגרסה המוקדמת ואז לייבאו מחדש בגרסה החדשה.

למידע נוסף והנחיות לייבוא מסדי נתונים של גרסה ‪2.x‬ לגרסה ‪3.x‬, לקריאה נוספת [מדריכי המשתמש של גרסאות קודמות של גרמפס](wiki:User_manual_translations/he).

{{-}}

### ייבוא גרמפס XML וחבילת XML

מסדי הנתונים מסוג [גרמפס XML](wiki:Gramps_XML/he) וחבילת [גרמפס XML](wiki:Gramps_XML/he) הם התסדירים המובנים של גרמפס. אין חשש לאובדן מידע בעת ייבוא (שחזור) או ייצוא נתונים בתסדירים אלו.

- ‏גרמפס [גרמפס XML](wiki:Gramps_XML/he) ‏(.gramps): קובץ ה־[XML/he](wiki:XML/he) של גרמפס הוא תסדיר חילופי הנתונים וגיבוי תיקני של גרמפס, ושימש גם כברירת מחדל לעבודה בגירסאות גרמפס הישנות (טרום גרסה 2.x). שלא כמו תסדיר .grdb של גרמפס V2.x, הוא בלתי תלוי בארכיטקטורה וניתן לקריאה אנושית. עם זאת, ייתכן שמסד הנתונים יכיל הפניות לעצמים מדיה חיצוניים (כלומר: שאינם מקומיים), ולכן אינו בהכרח נייד במלואו. לשם ניידות מלאה (כולל עצמי המדיה), מומלץ להשתמש בחבילת ה־[גרמפס XML](wiki:Gramps_XML/he) של גרמפס (.gpkg). מסד הנתונים XML של גרמפס נוצר על־ידי ייצוא הנתונים (באמצעות התפריט ) בתסדיר זה.

<!-- -->

- ‏חבילת [גרמפס XML](wiki:Gramps_XML/he) ‏(.gpkg): חבילת ה־[גרמפס XML](wiki:Gramps_XML/he) של גרמפס היא ארכיון דחוס המכיל את קובץ ה[גרמפס XML](wiki:Gramps_XML/he) ואת כל עצמי ה[מדיה](wiki:Gramps_Glossary/he#מדיה) (תמונות, קובצי שמע וכד') שמוזכרים במסד הנתונים. כיוון שהיא מכילה את כל עצמי המדיה, חבילה זו ניידת לחלוטין. החבילה נוצרת באמצעות ייצוא הנתונים (באמצעות התפריט ) בתסדיר זה.

בעת ייבוא מידע ממסד־נתונים אחר של גרמפס או מקובץ XML של גרמפס, יוצג תהליך ההתקדמות בסרגל ההתקדמות שבחלון הראשי של גרמפס. בסיום הייבוא, יוצג חלון משוב עם מספר העצמים שיובאו. אם המידע שיובא מקורו באותו אילן־יוחסין שבו הוא מיובא, יוצגו הצעות למיזוג נתונים; המיזוג **אינו** מתבצע אוטומטית. אם ברצונך למזג נתוני יוחסין בסיסיים באופן אוטומטי, ניתן לשקול שימוש בייצוא וייבוא מסוג גיליון אלקטרוני (CSV).

### ייבוא CSV בגרמפס

- תסדיר הגיליון האלקטרוני CSV של גרמפס מאפשר ייבוא וייצוא של תת־קבוצה מנתוני גרמפס בתסדיר גיליון פשוט. מידע נוסף ניתן למצוא בעמוד [ייבוא וייצוא CSV](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees:_CSV_Import_and_Export/he).

### ייבוא ​​GEDCOM

כפעולה מקדימה לייבוא קובץ נתונים, נדרש לייצור [אילן־יוחסין חדש ריק](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/he#Starting_a_new_Family_Tree). לאחר מכן לבחור מתפריט או על ידי שימוש ב[צרוף המקשים](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/he#2) לפתיחת חלון מחלון דו־שיח זה ניתן לבחור את קובץ ה־GEDCOM אותו מעונינים לייבא, כתלות בסוג קובץ ה־GEDCOM, ייתכן שתוצג התווית .

בעת ייבא מידע מקובץ GEDCOM, החלון הראשי של גרמפס יציג [סרגל התקדמות](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window/he#Status_Bar_and_Progress_Bar) תהליך הייבוא. כאשר ייבוא קובץ ה־​​GEDCOM יסתיים, חלון וחלון **** יוצגו חלונות אלו מציגים את תוצאות תהליך הייבוא או אזהרות הקשורות לנתוני הייבוא. {{-}}

#### דו־שיח קידוד GEDCOM

![[_media/GEDCOM-Encoding-dialog-52.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} קידוד GEDCOM – תיבת דו־שיח]]

תיבת דו־השיח תוצג כאשר קובץ GEDCOM המיובא מזדהה כקובץ בתסדיר קידוד ANSEL. לפעמים זה רק טעות בזיהוי קידוד הקובץ, אך אם לאחר שתהליך ייבוא קובץ ​​ה־GEDCOM הסתיים, והנתונים באילן־היוחסין מכילים תווים חריגים, יש לבטל את הייבוא ​​ולעקוף את ערכת התווים על ידי בחירת קידוד זמין שונה מרשימה הבחירה.

- **ברירת מחדל**
- ANSEL
- ANSI (iso-8859-1)
- ASCII
- UTF8

{{-}}

#### חלונית סטטיסטיקת ייבוא

![[_media/ImportStatistics-dialog-example-GrampXML-52.png|תרשים {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} – חלונית סטטיסטיקת ייבוא]] מציגה פרטים על סטטיסטיקת הייבוא. {{-}}

#### דו"ח ייבוא GEDCOM

![[_media/GEDCOM-import-report-result-example-50.png|תרשים {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} – דוח ייבוא GEDCOM, תוצאות לדוגמה.]]

**** מציג את מרבית השורות בקובץ GEDCOM שלא היו מובנות או שהתעלמו מהן במהלך הייבוא. ברוב המקרים מדובר בשורות שאינן חלק מהתקן GEDCOM 5.6.0 (למידע נוסף [תוספי GEDCOM](wiki:Addon:GEDCOM_Extensions)). הדוח מציג גם את מלל השורה (או שורות ההמשך, אם קיימות). בחלק מהמקרים ייתכן שהשורות לא יוצגו בדיוק כפי שהופיעו בקובץ המקורי, כיוון שגרמפס משחזר אותן לאחר עיבוד פנימי מסוים.

{{-}}

##### אודות הדוח

![[_media/Source-Note-GEDCOMImportNote-example-50.png|תרשים {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} – הערת ייבוא GEDCOM המציינת מידע שנשמט, מחוברת ל"מקור ← הערה" (נתונים מ־"GEDitCOM" – קבצי GEDCOM 5.5 Torture Test)]]

לגרמפס מודל־נתונים מתקדם יותר מזה של GEDCOM, ולכן לא כל המידע המופיע בקובץ GEDCOM ניתן לייבוא לתוך גרמפס. (למידע נוסף [גרמפס ו־GEDCOM](wiki:Gramps_and_GEDCOM/he).) החריגים העיקריים הם:

- חלק ממבני המאפיינים (Attributes) ב־GEDCOM ממופים למאפיינים בגרמפס, ולכן פריטי מידע רבים (GEDCOM Primitive Elements) אינם נשמרים.
- רכיבי DATA ברשומות מקור (SOURCE_RECORD) — המציינים אילו אירועים תועדו ומי היה הגוף הממונה — אינם מיובאים.
- אזכורים למקורות בתוך הערות אינם מיובאים.
- פריטי מידע רבים ב־GEDCOM אינם תואמים במדויק לשדות קיימים בגרמפס, ולכן הם נשמרים כמאפיינים () עם שמות המבוססים על תגי GEDCOM, למשל REFN, RFN, RIN, ו־AFN, וכן מידע מתוך רשומות HEAD, SUBM ו־SUBN.

כאשר מידע מסומן כ"נשמט", השמטתו תופיע בפלט הייבוא ותצורף גם כהערה () אל העצם הרלוונטי עם סוג מותאם־אישית: . לדוגמה, העצם מסוג מקור בצילום המסך המצורף.

כאשר מידע מסומן כ"נשמט בשקט", אין לכך אזכור בדוח, והוא גם לא נכלל בהערות. במצב הנוכחי מדובר כנראה בתקלה או חסר, ויש לדווח עליה.

{{-}}

#### מגבלות ייבוא GEDCOM

מקטע זה מפרט מידע מתסדירי GEDCOM שאין להם ייצוג ישיר בגרמפס, ואת האופן שבו גרמפס מתמודד עמם. למידע נוסף על מגבלות ייבוא (ויצוא) GEDCOM, למידע נוסף [גרמפס ו־GEDCOM](wiki:Gramps_and_GEDCOM).

##### HEADer, SUBMitter ו־SUBmissioN

לגרמפס אין ייצוג ישיר לנתונים אלו, ולכן המידע נשמר בעצמים אחרים. בהתאם ללהגדרה שנקבע בתפריט ההעדפות בחלון דו־השיח [הגדרות כלליות](wiki:Gramps_6.0_Wiki_Manual_-_Settings/he#כללי), ייתכן שגרמפס ייצור עצם ברירת־מחדל מסוג , שבו יישמר עיקר המידע, וכן המשויכים לו.

###### HEADer

רוב הנתונים משדות ה־HEADER נשמרים במקור ברירת־המחדל (או במאגר המשויך לו), לדוגמה:

| תגי GEDCOM                                  | אופן השימור בגרמפס          |
|---------------------------------------------|-----------------------------|
| +1 SOUR, +2 VERS, +2 NAME                   | נשמרים כפרטי המקור          |
| +2 CORP, +3 \<<ADDRESS_STRUCTURE>\>         | נשמרים במאגר של המקור       |
| +2 DATA, +3 DATE, +3 COPR                   | נשמרים במקור                |
| +1 DEST, DATE, TIME, SUBM, SUBN, FILE, COPR | נשמרים במקור                |
| +1 GEDC: VERS ו־FORM                        | שמורים במקור                |
| +1 CHAR, +2 VERS                            | שמורים במקור                |
| +1 LANG                                     | נשמר במקור                  |
| +1 PLAC, +2 FORM                            | נשמר כהגדרת פירוק שמות־מקום |
| +1 NOTE                                     | נשמר כהערה על המקור         |

###### SUBmissioN

רשומת ההגשה (SUBN) נשמרת כפריט במקור ברירת־המחדל. פרטי שדות כגון שם הקובץ, מספר דורות, מידע על מלל וכדומה נשמרים בהתאם.

###### SUBMitter

רשומות שולחים (SUBM) רבות עשויות להופיע, אך רק זו המקושרת ל־HEADER נחשבת לקובעת, ומשמשת לקביעת [בעלי מסג־הנתונים הנתונים](wiki:Gramps_6.0_Wiki_Manual_-_Tools/he#עריכת_מידע_בעלי_מסד־הנתונים). ניתן להעתיק אותה גם ללשונית [פרטי החוקר](wiki:Gramps_6.0_Wiki_Manual_-_Settings/he#חוקר).

שדות כגון , , נשמרים כמאגר, אך:

- קישורים למדיה (MULTIMEDIA_LINK) — מתעלמים מהם.
- שפות מועדפות (LANG) — מתעלמים מהם.
- מזהה רשום (RFN) ומספר מזהה אוטומטי (RIN) — מתעלמים מהם.

##### INDIVIDUAL_RECORD

רשומת אדם (INDI) מיובאת כעצם בגרמפס. חריגים:

- קישורים ל־SUBM, ANCI, DESI — מתעלמים.
- אליאס (ALIA) נשמר כקשר מסוג בשם "שם חלופי".
- מזהים (REFN ו־TYPE) נשמרים כ, אך כשיש כמה REFN, לא ברור תמיד מהו הסוג המתאים.

מבנה המאפיינים של אדם (INDIVIDUAL_ATTRIBUTE_STRUCTURE) מפוצל:

האירועים הבאים מטופלים כאירועים:

| תג GEDCOM | תיאור        |
|-----------|--------------|
| EDUC      | השכלה        |
| NMR       | מספר נישואין |
| OCCU      | עיסוק        |
| PROP      | נכסים        |
| RELI      | שיוך דתי     |
| RESI      | מגורים       |
| TITL      | תואר         |

המידע מצורף כ של האירוע. אם קיים TYPE עם תיאור נוסף, הוא יחליף את התיאור הקודם.

המאפיינים הבאים מיובאים כמאפיינים אישיים:

| תג GEDCOM | תיאור            |
|-----------|------------------|
| CAST      | מעמד             |
| DSCR      | תיאור פיזי       |
| INDO      | מספר מזהה לאומי  |
| NATI      | מוצא לאומי       |
| NCHI      | מספר ילדים       |
| SSN       | מספר ביטוח לאומי |

פרטים נוספים כגון תאריך, מקום, גיל וכו' מתעלמים.

##### FAM_RECORD

רשומת משפחה (FAM) מיובאת כעצם . חריגים:

- קישורים ל־SUBM — מתעלמים.
- מזהי משתמש (REFN ו־TYPE) נשמרים כ, אך ייתכנו בעיות זיהוי בהתאמה בין הסוג לערך.

##### SOURCE_RECORD

רשומת מקור (SOUR) מיובאת כעצם . אך:

- הנתונים המופיעים תחת DATA (אירועים, תאריכים, תחום שיפוט, סוכנות אחראית) — מתעלמים.

##### REPOSITORY_RECORD

רשומת מאגר (REPO) מיובאת כעצם . אך:

- מזהים REFN, TYPE ו־RIN — מתעלמים.

##### MULTIMEDIA_RECORD

רשומת מדיה (OBJE) מיובאת כעצם . אך:

- שדות מסוג BLOB ו־CONT — מתעלמים.
- מזהי משתמש REFN, TYPE ו־RIN — מתעלמים.
- שדות FILE לפי GEDCOM 5.6.0 נתמכים חלקית בלבד — קובץ מאוחר עשוי לדרוס קובץ קודם, ללא בדיקת שגיאות.

##### NOTE_RECORD

רשומת הערה (NOTE) מיובאת כעצם , אך:

- אזכורי מקור (SOURCE_CITATION) — מתעלמים.
- מזהים REFN, TYPE ו־RIN — מתעלמים.

## ייצוא נתונים

כדי לייצא נתונים, יש לבחור בתפריט או להשתמש בקיצור המקלדת [קיצור מקשים](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/he#) או במחשבי Apple Mac. פעולה זו תפתח את חלון הדו־שיח .

היצוא מאפשר לשתף את כל אילן־היוחסין (מסד־נתונים) או כל חלק ממנו עם חוקרים וגורמים אחרים, כמו כן מאפשר להעביר את הנתונים למחשב או תוכנה אחריפ.

גרמפס תומך בייצא נתונים בתסדירים הבאים:

- [גיליון נתונים מופרד בפסיקים (CSV)](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/he#Comma_Separated_Values_Spreadsheet.28CSV.29_export)
- [GEDCOM](#GEDCOM_export/he)
- [GeneWeb](#GeneWeb_export)
- [XML גרמפס](wiki:Gramps_XML/he) (אילן־יוחסין)
- [חבילת XML של גרמפס](wiki:Gramps_XML/he) (אילן־יוחסין ומדיה)
- [אילן־יוחסין למרשתת](#Web_Family_Tree_export)
- [vCalendar](#vCalendar_export)
- [vCard](#vCard_export)

תסדירי יצוא נוספים עשויים להיות זמינים באמצעות תוספים.

{{-}}

### דו־שיח סיען ייצוא

עמודי מנחים בבחירה של [תסדיר הקובץ ליצוא](#Choose_the_output_format), ולאחר מכן מאפשרים לקבוע את אפשרויות היצוא הייחודיות לאותו תסדיר קובץ. לאחר עמוד , תהליך היצוא יתבצע בהתאם לבחירות שנעשו. בכל שלב ניתן ללחוץ על לחצן כדי לשוב אחורה ולתקן בחירה קודמת, ואז להתקדם שוב כדי לבצע מחדש את היצוא.

- [שמירת הנתונים](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Saving_your_data)
- [בחירת תסדיר הקובץ](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Choose_the_output_format)
- [אפשרויות יצוא](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Export_options)
- [בחירת קובץ לשמירה](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Select_save_file)
- [אישור סופי](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Final_confirmation)
- [סיכום](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Summary)

#### Saving your data

![[_media/ExportAssistant-SavingYourData-wizard-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Export Assistant: "Saving your data" - wizard start page]]

General information about exporting from Gramps:

  
**Under normal circumstances, Gramps does not require you to directly save your changes. All changes you make are immediately saved to the database.**

<!-- -->

  
**This process will help you save a copy of your data in any of the several formats supported by Gramps. This can be used to make a copy of your data, backup your data, or convert it to a format that will allow you to transfer it to a different program.**

<!-- -->

  
**If you change your mind during this process, you can safely press the Cancel button at any time and your present database will still be intact.**

Select the button to continue.

{{-}}

#### Choose the output format

![[_media/ExportAssistant-ChooseTheOutputFormat-wizard-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Export Assistant - Choose the output format - wizard dialog]]

Select the file format to export your data to:

- [Comma Separated Values Spreadsheet (CSV)](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Comma_Separated_Values_Spreadsheet.28CSV.29_export)

- [GEDCOM](#GEDCOM_export)

- [GeneWeb](#GeneWeb_export)

- **Gramps [XML](wiki:Gramps_XML) (family tree)**(default)

- Gramps [XML](wiki:Gramps_XML) Package (family tree and media)

- [Web Family Tree](#Web_Family_Tree_export)

- [vCalendar](#vCalendar_export)

- [vCard](#vCard_export)

Then select the button to continue. {{-}}

#### Export options

![[_media/ExportAssistant-ExportOptions-CSV-defaults-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Export Assistant - Export Options - wizard dialog (showing defaults for "Comma Separated Values Spreadsheet(CSV)") with Bottom section for File format specific options]]

After you have adjusted your options in the two sections.

- Top unlabeled section: [Filters and privacy](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Filters_and_privacy)
- Bottom unlabeled section: [File format specific options](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#File_format_specific_export_options)

Make any changes you require and then select the button to continue.

{{-}}

##### Filters and privacy

In the top unlabeled section, Gramps allows you to export your selected Family tree into common file formats.

The following filters provide options that allow you to fine tune your export.

Filters allow you to export a limited amount of data, based on the criteria you select.

###### Privacy Filter:

  
Check this box to prevent ![[_media/22x22-gramps-lock.png]][private](wiki:Gramps_Glossary#private) records from being included in the exported file. (Checkbox checked by default)

###### Living Filter:

These option restrict data and help limit the information exported for living people. This means that all information concerning their birth, death, addresses, significant events, etc., will be omitted in the exported file. For example, you can choose to substitute the word **Living** for the first name (see your [settings](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Text)); you can exclude notes; and you can exclude sources for [living people](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive).

Sometimes, it is not always obvious from the data if someone is actually alive. Gramps uses an advanced algorithm to try to determine [if a person could still be alive](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive). Remember, Gramps is making its best guess, and it may not always be able to guess correctly all the time. Please double check your data.

Select from the following options:

- (default)

- 

- 

- 

###### Person Filter:

Select from the following options:

- (default)

- 

- 

- 

- 

- Create a custom filter by selecting the *Edit icon* to show the dialog.

###### Note Filter:

Select from the following options:

- (default)

- Create a custom filter by selecting the *Edit icon* to show the dialog.

###### Reference Filter:

Select from the following options:

- (default)

- 

##### File format specific export options

The bottom unlabeled section will only be shown depending on the file format chosen, you may find a number of file format specific export options to choose from listed underneath the *[Filters and privacy](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Filters_and_privacy)* section.

See the relevant section for each of file formats listed that have specific export options:

- [Comma Separated Values Spreadsheet (CSV)](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Comma_Separated_Values_Spreadsheet.28CSV.29_export)
- [Gramps XML (family tree)](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Gramps_XML_.28family_tree.29_export)

#### Select save file

![[_media/ExportAssistant-SelectSaveFile-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Export Assistant - Select save file - wizard dialog - example]]

Enter a export file `Untitled_1.`<file format extension>(default) and choose the folder location to save the export file to (normally your **Documents** folder.

Then select the button to continue.

If you don't have permission to save the file to that location you will see the warning dialog and then the Export Assistants wizard dialog, select the button and start the export again this time choosing a suitable folder. {{-}}

#### Final confirmation

![[_media/ExportAssistant-FinalConfirmation-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Export Assistant - Final confirmation - wizard dialog - example]]

The Export Assistants wizard dialog allows you to check the summarized details (Format/Name/Folder) of the export file to be created.

At this point you can press to revisit your options or to abort.

Or select the button to continue. {{-}}

#### Summary

![[_media/ExportAssistant-YourDataHasBeenSaved-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Export Assistant - Summary - wizard dialog - example]]

The Export Assistants wizard dialog shows the *Filename:* and confirms that you export data has been saved successfully and shows a reminder of the location the file was saved to.

Select the button to exit the Export Assistant. {{-}}

### Comma Separated Values Spreadsheet(CSV) export

![[_media/ExportAssistant-ExportOptions-CSV-defaults-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Export Assistant - Export Options - wizard dialog (showing defaults for "Comma Separated Values Spreadsheet(CSV)") with Bottom section for File format specific options]]

Comma Separated Values Spreadsheet(CSV): Allows exporting (and importing) a subset of your Gramps data in a simple spreadsheet format.

See [CSV Import and Export](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees:_CSV_Import_and_Export) for additional information and examples.

Comma Separated Values Spreadsheet(CSV) has the following [file format specific export options](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#File_format_specific_export_options):

- \-

- \-

- \-

- \-

- \- whether to Translate headers into the language currently being used.

{{-}} Also, see [Export (List) View](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Export_View) as Spreadsheet.

### GEDCOM export

Gramps allows you to export a database into the common legacy format.

export has no [file format specific export options](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#File_format_specific_export_options) but you can change the following:

- Make sure you add your information to create a valid GEDCOM file, this can be also be done with the tool.

For more information on the GEDCOM format see: :

- <https://en.wikipedia.org/wiki/GEDCOM>
- <https://www.familysearch.org/developers/docs/guides/gedcom>
- <https://www.familysearch.org/developers/docs/gedcom/>

See [Gramps and GEDCOM](wiki:Gramps_and_GEDCOM) for details of data which is not exported when exporting to GEDCOM (). {{-}}

### GeneWeb export

export will save a copy of your data to the GeneWeb genealogy format.

To find out more about GeneWeb and its format, visit:

- <http://www.geneweb.org>

has no [file format specific export options](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#File_format_specific_export_options) {{-}}

<span id="Export into Gramps formats"></span>

### Gramps XML (family tree) export

![[_media/ExportAssistant-ExportOptions-GrampsXMLFamilyTree-defaults-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Export Assistant - Export Options - wizard (showing defaults for "Gramps XML (family tree)") with highlight Bottom section for File format specific options]]

export (.gramps): This format is the standard format for data-exchange and backups (see the related .gpkg format below for full portability including media objects). Exporting into Gramps [XML](wiki:XML) format will produce a portable database. As XML is a text-based human-readable format, you may also use it to take a look at your data. Gramps guarantees you can open XML output of older versions of Gramps in newer version of Gramps (not the other way around though!).

If a media file is not found during export, you will see the same dialog you encounter with GEDCOM export.

has the following [file format specific export options](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#File_format_specific_export_options):

- \- option to allow Gramps to export a .gramps file, without compressing the file. (Checkbox is selected by default)

{{-}}

#### What's not included:

### Gramps XML Package (family tree and media) export

export (.gpkg): Exporting to the Gramps package format will create a compressed file that contains the Gramps XML database and copies of all associated media files. This is useful if you want to move your database to another computer or to share it with someone.

If a media file is not found during export, you will see the same dialog you encounter with GEDCOM export.

has no [file format specific export options](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#File_format_specific_export_options)

#### What's not included:

### Web Family Tree export

export creates a text file that can be used by the **Web Family Tree** program.

To find out more about Web Family Tree and its format, visit

- [`http://www.simonward.com/cgi-bin/page.pl?family/tree`](http://www.simonward.com/cgi-bin/page.pl?family/tree) - [linkrot](https://wikipedia.org/wiki/Link_rot). *see* [2016 **Internet Archive** snapshot](https://web.archive.org/web/20160316080343/http://www.simonward.com/cgi-bin/page.pl?family/tree)

has no [file format specific export options](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#File_format_specific_export_options) {{-}}

### vCalendar export

export saves information in the format used in many calendaring applications, sometimes called PIM for Personal Information Manager.

For more information on the vCalendar format see:

- <https://en.wikipedia.org/wiki/ICalendar#vCalendar_1.0>

has no [file format specific export options](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#File_format_specific_export_options) {{-}}

### vCard export

export saves information in a format used in many addressbook applications, sometimes called PIM for Personal Information Manager.

For more information on the vCard format see:

- <https://en.wikipedia.org/wiki/VCard>

has no [file format specific export options](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#File_format_specific_export_options) {{-}}

[Category:He: מדריך למשתמש](wiki:Category:He:_מדריך_למשתמש) [Category:He:תיעוד](wiki:Category:He:תיעוד)
