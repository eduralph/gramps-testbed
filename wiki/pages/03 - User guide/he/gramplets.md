---
title: Gramps 6.0 Wiki Manual - Gramplets/he
categories:
- He:תיעוד
- Pages with broken file links
- Stub
managed: false
source: wiki-scrape
wiki_revid: 127693
wiki_fetched_at: '2026-05-30T19:17:28Z'
lang: he
---

<div dir="rtl" lang="he" class="mw-content-rtl">

{{#vardefine:chapter\|12}} {{#vardefine:figure\|0}} מקטע זה מפורט את התכונות והיכולות הנספות ש**מתקעים מובנים** – גרמפלטס, מספקים למערכת גרמפס.

# <span id="מה_זה_גרמפלט?"></span>מה זה גרמפלט?

<span id="נגדרה"> ![[_media/DashboardCategory-DashboardView-default-gramplets-51_he.png|איור: {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} סוג־אב לוח מחוונים (מצג ברירת מחדל)]]

[גרמפלט](wiki:Gramps_Glossary/he#גרמפלט) הוא בעצם תוכנית (קוד) שנועד להרחבת יכולות או תכונות בתוכנית הליבה של גרמפס **בתקווה** שהן אכן משתלבות ופועלת בצורה חלקה בדומה לתכונה מובנית. מהיבט פונקציונאלי, גרמפלטים מספקים נקודת־מבט הידודית ומשלימה על נתוני אילן היוחסין שמשתנה במהלך הניווט, או; מאפשר הידודיות עם הנתונים הגנאלוגיים שלנו.

גרמםלטס שמכונים לעיתים גם [ווידג'יטס](http://wikipedia.org/wiki/Widget_engine), תוספים, מתקעים, תוכניות ורכיבי עזר ועוד, מוטמעים כחלק מתוכנית גרמפס והם ימצאו בעצמים שונים כמו **לוח מחוונים' '' או**סרגלי צד**ו**סרגל תחתון''' ובסוגי־אב ניווט אחרים. הפונקציונליות שמתקעים אלו מספקים עשויים בהחלט להוות ערך מוסף משמעותי במחקר גנאולוגי.</span>

## האם לא כל המתקעים גם גרמפלטים?

מה למעשה ההבדל בין גרמפלטים, דוחות, מבטים מהירים וכלים?

כל אלה הם סוגי **מתקעים**. כאש גרמפלטים הם תת־סוג של מתקעים עם דגש רב יותר על מנשק המשתמש. גרמפלטים מוסיפים **יכולת** או **תשקופות אחרת** למצג. ניתן להשתמש בהם לשיפור זרימת העבודה של מצג.

מתקעים אחרים נוטים להפריע בזרימת העבודה הרגילה בביצוע משימה אחרת והשימוש בהם הוא לסירוגין. מתקע עשוי ליצור תמונת מצב סטטית (אפילו בקשור חם) של הנתונים, לשמש לבצוע שינויים גורפים, או לספק יכולות ייבוא/ייצוא/פלטים חלופית.

כמה [מסוגי המתקעים](wiki:Gramps_6.0_Wiki_Manual_-_Plugin_Manager/he#סוגי_מתקעים) הנפוצים הם:

- דוחות - ספקים תסדיר פלט סטטי של הנתונים, בדרך כלל כמצג
- [מצג מהיר](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8/he#מצג_מהיר) - מספק רשימה הידודית קצרה שנגזרת בדרך כלל מהנתונים
- כלים - מספקים שיטות לעיבוד הנתונים
- גרמפלטים - מספקים מנשק ומצג דינמי לנתונים.

להבנה מעמיקה יותר של סוגי מתקעים השונים ניתן למין את [רשימת התוספים](wiki:6.0_Addons/he#רשימת_תוספים) לפי **סוג** ולבחון ב**תיאורים** את הניגודיות שמבחינה ביניהם.

את כמה מסוגי המתקעים הסטטיים יותר ניתן להרחיב כך שיפעלו באופן דינמי בדומה לגרמפלט.

מספר מתקעים התפתחו לכדי מגוון סוגים. חלקם הם רק 'מעטפות' שמרבדות יכולות נוספות סביב מתקעים אחרים. גרמפלט **מצג מהיר** אינו [סוג של תוסף תצוגה מהירה](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8/he#מצגים_מהירים), במקום זאת, הוא משמש כמעטפת שניתנת לעגינה ומציגה מתקע **מצג מהיר** ודוחפת את המתקע לרענן את הנתונים כשההקשר משתנה.

## להתחיל עם גרמפלטים

בעת הפעלת [סוג־אב לוח המחוונים](wiki:Gramps_6.0_Wiki_Manual_-_Categories/he#סוג־אב_לוח_מחוונים) לראשונה, יוצגו שני גרמפלטים המוגדרים כברירת מחדל: גרמפלט **** וגרמפלט ****.

החל מגרסה 4.2 של גרמפס, תכונות מסוימות של לוח המחוונים הורחבו לסוגי־אב ניווט אחרים, ולכן קיימים גרמפלטים **כלליים** וגרמפלטים **ייעודיים**.

גרמפלטים כלליים\*\* רלוונטיים לכל תצוגה... ונקודת המבט על הנתונים היא ביחס להקשר של האדם הפעיל ו/או האדם הביתי. ניתן לעגן אותם בכל תצוגת קטגוריית ניווט מבלי להפוך את התצוגה ללא חד משמעית. גרמפלטים ייעודיים\*\* זקוקים להקשר של תצוגות מסוימות כדי לתת הקשר לנקודת המבט שלהם על הנתונים. רשימת התפריט "הוסף גרמפלטים" תשתנה בהתאם לתצוגת הקטגוריה הפעילה ולגרמפלטים המותקנים.

- רשימה זו נותרה משינוי קודם של הוויקי. לא ברור היכן הפריטים משתלבים בדיון זה.
- גרמפלטים של הפניות אחוריות – מספקים נראות מיידית לנתונים ונוטים להיראות מדי פעם וקבורים במנשק... כמו בלשונית עורך עצם.
- גרמפלט סינון דומה לסרגל הצד הקודם של הסינון.
- מודלים נפוצים עבור הערות, גלריה, מקורות, ציטוטים, אירועים.
- גרמפלט ילדים בתצוגות אדם (גם קטגוריית תרשימים וקטגוריית קשרים), תצוגת משפחות.

## שימוש כללי ותיצור

![[_media/WelcomeToGramps-Gramplet-docked-in-dashboard-60.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dashboard Welcome Gramplet]] פקדי המכולה בגרמפלטים מסודרים מעט שונה מאשר במצג סוג־אב לוח המחוונים, סרגל הצד והסרגל התחתון. המודעות לאופן שבו מיכלי גרמפלט אלה שונים (וגם דומים) תאפשר להתמקד השגת היעדים וביצועם במהירות גבוהה זאת במקום לתהות מדוע הם מתנהגים מעט שונה.

הסיבה לשונות נובעת בעיקר מהבדלי עיתוי. גרמפלטים במצג סוג־אב לוח המחוונים מסודרים במספר עמודות שניתנות לתיצור במקור נוספו בגרסה 3 . סרגל הצד והסרגל התחתון [חלוניות מפוצלות](wiki:Split_Views/he) נבחרו מבין חידושים מאוחרים יותר שהוצעו ב־[GEPS 19](wiki:GEPS_019:_Improved_Sidebar_and_Split_Views). הם נבנו על סרגל הצד של המסנן של גרסת 3.3. המסנן הומר לגרמפלט'' ועוגן מראש בסרגל הצד.

[left|thumb|450pxאיור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} סרגל צד גרמפלט ברוכך בואך לא מעוגן](wiki:File:Welcome-Gramplet-detached-52.png) החלוניות המפוצלות מספקות שטח מסך מוגבל לעגינת גרמפלטים בסוגי־אב האחרים של הנווט. אבל, שלא כמו העמודות הרבות של מצג לוח המחוונים, כל חלונית מפוצלת חדשה היא עמודה אחת, שמאכלסת גרמפלט יחיד. (החלונית עדיין תומכת באכלוס גרמפלטים מרובים, היא פשוט משתמשת בלשוניות כדי להציג אותם אחד בכל פעם.)

גישת החלונית המפוצלת מפחיתה את הצורך במעבר בין מצגי סוגי־אב ... וזה מקל על הדרישות ממסד הנתונים.

![[_media/DashboardCategory-gramplet-detached-example-52.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Detached Gramplet in the Dashboard View]] עם זאת, ניתן לנתק את עגינת הגרמפלטים (לשחרר, להסיר)מכל אחד משלושת המיכלים כדי שאלו פשוט יצופו באופן חופשי. בעת ניתוק העגינה, לחצן שמתווסף בפינה השמאלית התחתונה יפתח את עמוד הגרמפלט באתר זה. לחיצה על לחצן  בפינה השמאלית העליונה יעגן מחדש גרמפלט מנותק. באופן דומה, לחיצה על לחצן   של גרמפלט מעוגן יסיר אותו מהחלונית.

### תצוגת לוח המחוונים

בלוח המחוונים, ניתן לגרור את לחצן המאפיינים של כל גרמפלט כדי לשנות את מיקומו באזור לוח המחוונים. לחיצה על לחצן זה מאפשרת להוציא את הגרמפלט ("לבטל עגינה") מלוח המחוונים ולהציג אותו בחלון עצמאי. חלון זה יישאר פתוח ללא קשר לדף הנוכחי (קשרים, תרשימים וכדומה). סגירת התצוגה המופרדת תחזיר את הגרמפלט ללוח המחוונים. אם תצאו מגרמפס עם גרמפלט פתוח, הוא ייפתח אוטומטית בהפעלה הבאה של התוכנה.

כאשר גרמפלט אחד או יותר מופרדים מלוח המחוונים, הם נשארים גלויים בעת מעבר לתצוגה אחרת (כגון תצוגת אנשים או תרשימים). באופן זה, ניתן להשתמש בגרמפלטים אלה כדי להוסיף פרטים ופונקציונליות לתצוגה מסוימת.

ניתן להוסיף גרמפלטים חדשים על ידי לחיצה ימנית על שטח פתוח בלוח המחוונים. לחיצה על לחצן מעל הגרמפלט תסיר אותו מלוח המחוונים.

### אפשרויות תיצור

![[_media/Menubar-View-overview-example-60.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} תפריט View]] ניתן גם לשנות את מספר העמודות על ידי שינוי ההגדרה בלשונית *,תסדיר גרמפלטים* בחלון *תיצור לוח מחוונים*. כדי לפתוח את החלון, לחיצה על לחצן ![[_media/Gramps-config.png]], בחירה מתפריט התצוגה או לחיצה על קיצור המקשים *תיצור מצג פעיל*. ![[_media/Whats-next-gramplet-configure-dashboard-60.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} בלשונית להגדרת גרמפלט]]

לכל גרמפלט שעוגן בלוח המחוונים תתווסף גם לשונית הגדרות. (ייתכן שלאותו גרמפלט לא יהיו אפשרויות הגדרה או לשונית כלל כאשר הוא מעוגן בסרגל הצד או בתחתית). לוח המחוונים מספק אפשרויות נוספות לכל גרמפלט, שמאפשרות לשנות את שמו, לקבוע גודל אנכי קבוע או למרב אותו אנכית בעמודה שלו. לשונית ההגדרות עבור גרמפלטים שמעוגנים בלוח המחוונים תציג לפחות אפשרויות בסיסיות אלה.

לחיצה כפולה על הכותרת של גרמפלט שעוגן בלוח המחוונים מאפשרת לשנות את כותרת התצוגה.

### סרגל צד המסך המפוצל וסרגל תחתון

![[_media/Bottombar-sidebar-drop-down-menu-60.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} גרמפלט מסכים מפוצלים שמציג תפריט סרגלגרמפלט בצורת ראש חץ כלפי מטה ללא תווית  לחצן תפריט נפתח]] כל אחת מחלוניות החלונות המפוצלים הללו היא למעשה מיכל לשוניות גרמפלט נערמות. כמו חלונות עם מקטע לשוניות, כל אחד מהם יכול להציג רק לשונית בודדת בכל פעם. אבל ניתן להוסיף לשוניות, לסדרן מחדש, לנתק עגינתן או להשבית אותן באופן דומה כפי שמתבצע בלוח המחוונים. עם זאת, במקום תפריט הקשר, בכל חלונית מפוצלת יוצג *ראש חץ כלפי מטה* לחצן תפריט נפתח שיציג את אותן אפשרויות ברשימה צצה.

להוספת גרמפלט ללשוניות הנערמות, יש לבחור אותו מתפריט המשנה .

<span id="undock gramplet">כדי לנתק עגינת לשונית, יש 'לתפוס' את כותרת הלשונית ולגרור החוצה מהחלונית המפוצלת. לעגינה מחדש, יש ללחוץ על לחצן או על הלחצן ה־</span>

כדי להסיר את הגרמפלט ממערום הלשוניות, יש לבחור אותו מתפריט המשנה . (לחלופין, לחצן הסגירה יהיה נגיש אם תיבת הסימון 'הצגת לחצן סגירה בלשיוניות גרפלט' בלשונית [תצוגה](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) העדפות נבחרה).

באופן תמוהה, אותם גרמפלטים עשויים להיות לשוניות במקטע החלון המפוצל האחר של מצג, אך הם מוגדרים כך שיציגו מידע בצורה שונה. חשוב להיות מודעים לכך שכל גרמפלט (בין אם הוא מעוגן כלשונית או 'צף' ללא עגינה) פוגע בביצועי גרמפס. לכן חשוב להשתמש בפחות גרמפלטים ורק באלו שנדרשים לביצוע המשימה שעל הפרק, זאת כדי לשמר את התגובתיות של גרמפס בצורה מיטבית.

רשימות הגרמפלטים שניתן להוסיף למערום הלשוניות בחלונית מפוצלת מסוננים לפי אלו שמתאימים לאותו סוג־אב.

#### ⚙ אפשרויות תיצור

![[_media/Menubar-View-overview-example-60.png|איור. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} תפריט מצג]]

בנוסף, ישנם מספר גרמפלטים של צד ג' שניתן להתקין ולהשתמש בקלות. אלה כוללים:

- גרמפלט חדשות - חדשות עדכניות, חדשות מגרמפס
- גרמפלט להזנת נתונים - לעריכת שם האדם הפעיל, תאריך ומקום לידה, תאריך ומקום פטירה, והוספת אנשים
- גרמפלט פיתון - מעטפת פיתון
- גרמפלט שאלות נפוצות - שאלות נפוצות
- גרמפלט הערות - הצגת ועריכת הערת של האדם הפעיל

לקריאה נוספת: רשימת [תוספים צד ג'](wiki:Third-party_Addons/he).

# תקציר גרמפלטים

תקציר על כל אחד מהגרמפלטים המובנים כברירת מחדל וסוגי־אב מצג בהן ניתן להשתמש בכל אחד מהם.

באופן עצמאי לכל מיכל ומצב סוג־אב מצג, ניתן להוסיף או להסיר את גרמפלטים באמצעות הפקדים הבאים:

- במצג סוג־אב לוח המחוונים, מתפריט ההקשר בלחיצת עכבר ימנית.
- בכל שאר סוגי־האב, דרך תפריטי בחירת הגרמפלט אותם ניתן להרחיב בלחיצה על לחצן (לחצן *ראש חץ כלפי מטה*) בסרגל התחתון או בסרגל הצד.

*אין אפשרויות תפריט יעודית להוספת גרמפלט. הסיבה לכך היא שגרמפלטים מתווספים לסרגל הצד או לסרגל התחתון של מצב המצג על פי הקשרם.* {{-}}

## רשימת גרמפלטים

הקשה כפולה על כותרת סוג־אב למיון הרשימה והצגת אפשרויות תפריט לגרמפלט זמינים לאותו סוג־אב. (התפריט הממשי יכלול גם גרמפלטים שהם למעשה [מתקעים צד ג'](wiki:6.0_Addons/he#רשימת_מתקעים)).

| גרמפלט | ![[_media/22x22-gramps-gramplet.png]] <small>לוח־מחוונים</small> | ![[_media/22x22-gramps-person.png]] <small>אנשים</small> | ![[_media/22x22-gramps-relation.png]] <small>קישרי קירבה</small> | ![[_media/22x22-gramps-family.png]] <small>משפחות</small> | ![[_media/22x22-gramps-pedigree.png]] <small>תרשימים</small> | ![[_media/22x22-gramps-event.png]] <small>ארועים</small> | ![[_media/22x22-gramps-place.png]] <small>מקומות</small> | ![[_media/22x22-gramps-geo.png]] <small>גאוגרפיה</small> | ![[_media/22x22-gramps-source.png]] <small>מקורות</small> | ![[_media/22x22-gramps-citation.png]] <small>מובאות</small> | ![[_media/22x22-gramps-repository.png]] <small>מאגרים</small> | ![[_media/22x22-gramps-media.png]] <small>מדיע</small> | ![[_media/22x22-gramps-notes.png]] <small>הערות</small> |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| id="0" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="1" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="2" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="3" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="4" \| |  | ✔ | ✔ | ✔ | ✔ | ✔ |  | ✔ | ✔ | ✔ |  | ✔ |  |
| id="5" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="6" \| |  | ✔ | ✔ | ✔ | ✔ |  |  | ✔ |  |  |  |  |  |
| id="7" \| |  | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |  | ✔ |  |
| id="8" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="9" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="10" \| |  | ✔ | ✔ |  | ✔ |  | ✔ | ✔ |  |  | ✔ |  |  |
| id="18a" \| |  |  |  |  |  |  | ✔ |  |  |  |  |  |  |
| id="18b" \| |  |  |  |  |  |  | ✔ |  |  |  |  |  |  |
| id="11" \| |  | ✔ | ✔ | ✔ | ✔ |  |  | ✔ |  |  |  |  |  |
| id="11a" \| |  | ✔ | ✔ | ✔ | ✔ |  |  | ✔ |  |  |  |  |  |
| id="12" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="13" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="14" \| |  |  | ✔ |  | ✔ |  |  |  |  |  |  |  |  |
| id="15" \| |  | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |  |
| id="16" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="17" \| |  |  |  |  |  |  |  |  |  |  |  | ✔ |  |
| id="21" \| |  |  |  |  |  |  |  |  |  |  |  | ✔ |  |
| id="19" \| |  | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |  |
| id="20" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="22" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="23" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="24" \| |  | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="25" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="26" \| |  | ✔ | ✔ |  | ✔ |  |  | ✔ |  |  |  |  |  |
| id="27" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="28" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="29" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="30" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="31" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="32" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="35" \| | ⚠ | ⚠ | ⚠ |  | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ | ⚠ |
| id="33" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="34" \| | ♦ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| id="xx" \| |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |

למידע מפורט יותר על השימוש בגרמפלטים מותקנים, נא לעיין ב[גרמפלטים](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/he#גרמפלטים). {{-}}

# תקצירי גרמפלטים

המקטע הבאה מציג סקירה קצרה על כל אחד מהגרפלטים שמופיעים בפרק זה

## תרשים מניפה דו כיווני

![[_media/2-WayFanChart-detached-gramplet-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} 2-Way Fan Gramplet]]

**לקריאה נוספת:** {{-}}

## גיל בפטירה

![[_media/AgeOnDate-Gramplet-detached-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Age On Date Gramplet - detached example]]

The Gramplet allows you to enter a [Calendar date](https://en.wikipedia.org/wiki/Calendar_date) in the entry field. If you select the the Gramplet will compute the ages for everyone in your Family Tree living on that Date and will show the results in a separate Quick View report dialog. The date must be entered in a calendar format that Gramps accepts eg: YYYY-MM-DD .

- No configuration options are available for this gramplet.

{{-}} ![[_media/AgeOnDate-Gramplet-QuickView-example-result-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Age On Date Gramplet - Quick View - result example]]

From the resulting Quick View report dialog you can sort by the Person, Age or Status columns. Right clicking the row opens a context menu that allows you to *Copy all* rows to the clipboard; or to *See the person details* in the Person Editor, or *Make the person active*.

{{-}}

- You can also drag a date to from [Calendar Gramplet](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Calendar) to the Gramplets entry field to enter that date.
- See also the [Third-party Addon](wiki:Third-party_Addons) [Date Calculator Gramplet](wiki:Addon:DateCalculator) which allows you to do date math.

{{-}}

## סטיסטיקת גילאים

![[_media/AgeStats-Gramplet-detached-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Age Stats Gramplet - detached example]]

The Gramplet shows statistics in the form of three text graphs grouped in 5 years age span breakdowns (use the vertical scroll bar to see the other two graphs):

- **Lifespan Age Distribution** - for all people having valid birth and death dates.
- **Father - *Child Age Diff Distribution*** - shows the age difference between child and father where both individuals have valid birth dates.
- **Mother - *Child Age Diff Distribution*** - shows the age difference between child and mother where both individuals have valid birth dates.

Rolling over a chart row will display a hint with the count of offspring matching the row's range.

Double-clicking a row in any of the statistics graphs opens a Quick Report of the offspring categorized by that row. You can sort the Quick Report by the Name, Birth Date and Name Type columns.

Right-clicking the Quick View report row displays a context menu for copying the list, opening the Person Editor or activating the person.

#### ⚙ אפשרויות תיצור

![[_media/AgeStats-Gramplet-configuration-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Age Stats Gramplet - from Charts Configuration tab defaults]] Adjustable graph scaling limits

- Maximum Age 1-150; (*110 default*)
- Maximum Age of mother at birth: 1-150; (*40 default*)
- Maximum Age of father at birth: 1-150; (*60 default*)
- Chart Width: 1-150; (*60 default*)

In the Dashboard View, the Gramplet may be detached by clicking the button.

### לקריאה נוספת

- An upgrade has been developed for the 6.0 version of Gramps.See the [screen capture](wiki::File:AgeStats-Gramplet-detached-51.png#Summary)

{{-}}

## אבות קדמונים

![[_media/Ancestors-Gramplet-detached-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ancestors Gramplet - detached example]]

Gramplet showing active person's ancestors. {{-}}

## תכונות

![[_media/Attributes-Gramplet-detached-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Attributes Gramplet]]

The Attributes Gramplet shows all of the attributes for the current, active person. Double click on the name of the attribute, and you will run a Quick View that shows all of the people that have that attribute, and the values for it. You can sort the Quick View by the attribute value by clicking on the column name. {{-}} ![[_media/Atttribute-Gramplet-QuickView-example-result-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Attributes Gramplet - Quick View example result]]

In the Quick View, highlight the entry to change the active person (which will then change the Attributes Gramplet), and double-click the Quick View entry to bring up the Edit Person dialog window. {{-}}

### מאפייני אדם

See [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) {{-}}

### מאפייני משפחה

See [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) {{-}}

### מאפייני ארועים

See [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) {{-}}

### מאפייני מקורות

See [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) {{-}}

### מאפייני מובאות

See [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) {{-}}

### מאפייני מדיה

See [Attributes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Attributes) {{-}}

## לוח־שנה

![[_media/CalendarGramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Calendar Gramplet - detached example]]

The **Calendar Gramplet** shows a monthly calendar.

Surrounding the label at the top left corner, the and buttons can be used to change the month.

Surrounding the label at the top right corner, the and buttons can be used to change the year.

Double-click a **day** to run the Quick View. The Quick View window shows up to 3 table sections, the events (if any exist) of: the exact date, other events on the same month/day in history, and events in that year.

You can also drag a day from the Calendar to the date fields (such as for the [Event Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#New_Event_dialog) or the [Age on Date Gramplet](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Age_on_Date)) to enter that date. Similarly, a calendar day may also be dragged to the [Clipboard](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Using_the_Clipboard) where it will be stored in a plain text format.

{{-}}

## צאצאים

![[_media/Children-Gramplet-detached-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Children Gramplet - detached example]]

Gramplet showing the active persons children.

[How do I change the order of children?](wiki:Gramps_6.0_Wiki_Manual_-_FAQ#How_do_I_change_the_order_of_children.3F) Use:

- The Family Editor [Children](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Children) tab to change the order of children in the family.
- The third party addon [Birth Order Tool](wiki:Addon:BirthOrderTool) which allows bulk updates of the children order.

{{-}}

### צאצאי אדם

See [Children](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Children)

Also shows the childs spouse if present. {{-}}

### צאצאי משפחה

See [Children](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Children) {{-}}

## מובאות

![[_media/Citation-Gramplet-detached-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Citation Gramplet - detached example]]

Gramplet showing the active persons citations. {{-}}

### מוברות אדם

See [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) {{-}}

### Family Citations

See [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) {{-}}

### Event Citations

See [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) {{-}}

### Place Citations

See [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) {{-}}

### Media Citations

See [Citations](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Citations) {{-}}

## Descendant Fan Chart

![[_media/DescendantFan-Gramplet-detached-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Descendant Fan (chart) Gramplet - detached example]]

Gramplet showing active person's direct descendants as a fan chart.

**See also:** {{-}}

## דורות ממשיכים

![[_media/Descendants-Gramplet-detached-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Descendants Gramplet - detached example]]

The Descendants Gramplet shows the direct descendants of the active person.

The order of the spouses and children is that given in the Gramps editor. To change the order of spouses, click on *Order* on the Relationship view. To change the order of children, [drag and drop](http://en.wikipedia.org/wiki/Drag-and-drop) them in the correct order in the Family edit window.

This Gramplet is based on the [Descendant Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Descendant_Report), available from the Textual Reports.

The Descendants Gramplet will update when you change the active person, or change family trees. It does not update automatically for edits or additions because this report is time-consuming to run.

Minimizing a Gramplet will prevent it from updating.

Moving the mouse over a person will show a tooltip summary which includes the death date. {{-}}

## Details

![[_media/Details-Gramplet-detached-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Details Gramplet - detached example]]

Gramplet showing details of the active person.

Provides a brief non editable summary of the selected person for example:

- *Name*: of person
- *Also Known As:*
- *Other Name:*
- *Father:*
- *Mother:*
- *Birth:*
- *Death:*
- *Burial:*

<!-- -->

- *Image*: If available the primary image will be shown to the right of the details, otherwise a cross will indicate the image is missing, you may double click the image to open it in an external viewer. To change the primary active image see: [Edit Person Editors - Gallery tab](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Gallery)

You may highlight and copy the individual text fields. {{-}}

### Person Details

See [Details](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Details) {{-}}

### Place Details

See [Details](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Details) {{-}}

### Repository Details

See [Details](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Details) {{-}}

## Encloses

![[_media/Encloses-Gramplet-detached-example-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Encloses Gramplet - detached example]]

Gramplet showing the locations of a place it encloses over time. {{-}}

- See also [Enclosed By](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Enclosed_By) tab

### Encloses Place Locations

See [Enclosed By](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Enclosed_By) {{-}}

## Enclosed By

![[_media/EnclosedBy-Gramplet-detached-example-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Enclosed By Gramplet - detached example]]

Gramplet showing the locations enclosed by a place over time. {{-}}

- See also [Enclosed By](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Enclosed_By) tab

### Enclosed By Place Locations

See [Encloses](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Encloses) {{-}}

## Events

![[_media/Events-Gramplet-detached-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Events Gramplet - detached example]]

Gramplet showing the events for the active person.

Double click a row to edit the event. {{-}}

### Person Events

See [Events](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Events) {{-}}

### Family Events

See [Events](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Events) {{-}}

## Events Coordinates

![[_media/EventsCoordinates-Gramplet-detached-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Events Coordinates Gramplet - detached example]]

Gramplet showing the events coordinates for the active person.

Double click a row to edit the event. {{-}}

## תרשים מניפה

![[_media/FanChart-detached-gramplet-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Fan Chart Gramplet]]

The Fan Chart Gramplet shows the direct ancestors of the active person in a circular format. It is similar to the Pedigree View, but shown around the center/active person, and further generations spiralling out.

Click on a parent in the chart and they will expand or contract above their child. Right-click on a person and you can:

- select that person to be the active person
- edit the person which allows through Person Editor add children to person's families
- select from among the person's relatives to be the active person
- add partners (families) to person
- copy name, birth and death of person into clipboard

Clicking in an open area (non-person) and dragging the mouse will allow you to rotate the chart about the center. You may also left-click and drag in the center to reposition the fan chart.

A black edge on the outer radius of the chart indicates more parents for that person. A black circle in the center indicates that the center person has children.

The Fan Chart Gramplet will update when you change the active person, or change family trees.

Minimizing a Gramplet will prevent it from updating.

**See also:** {{-}}

## FAQ

![[_media/FAQ-Gramplet-detached-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} FAQ Gramplet - detached example]]

The (Frequently Asked Questions) shows a list of common questions, and links to their answers from the Gramps Wiki (requires an internet connection).

This gramplet shows a manually curated list of **Frequently Asked Questions** hyperlinked to answers in articles of the Gramps wiki. The list is collated from new user postings to the [Gramps User maillist](wiki:Contact#Mailing_lists) that must be answered repeatedly.

The idea is to make the answers to the most common question easier to find, the primary objective is to let new users start using Gramps more quickly.

### See Also

- Bug Report : Dashboard FAQ links are obsolete (resolved)
- Bug Report : how to add/update FAQs

{{-}}

## מסנן

Gramplet providing a filter specific to the Category.

See also [Which filters in which Category?](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Which_filters_in_which_Category.3F) {{-}}

### Person Filter

![[_media/FilterGramplet-Person-detached-default-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Person - Filter Gramplet - detached - default]]

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) {{-}}

### Family Filter

![[_media/FilterGramplet-Family-detached-default-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Family - Filter Gramplet - detached - default]]

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) {{-}}

### Event Filter

![[_media/FilterGramplet-Event-detached-default-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Event - Filter Gramplet - detached - default]]

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) {{-}}

### Place Filter

![[_media/FilterGramplet-Place-detached-default-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Place - Filter Gramplet - detached - default]]

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) {{-}}

### Source Filter

![[_media/FilterGramplet-Source-detached-default-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Source - Filter Gramplet - detached - default]]

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) {{-}}

### Citation Filter

![[_media/FilterGramplet-Citation-detached-default-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Citation - Filter Gramplet - detached - default]]

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) {{-}}

### Repository Filter

![[_media/FilterGramplet-Repository-detached-default-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Repository - Filter Gramplet - detached - default]]

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) {{-}}

### Media Filter

![[_media/FilterGramplet-Media-detached-default-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Media - Filter Gramplet - detached - default]]

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) {{-}}

### Notes Filter

![[_media/FilterGramplet-Notes-detached-default-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Notes - Filter Gramplet - detached - default]]

See [Filter](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter) {{-}}

### גלריה

![[_media/Gallery-Gramplet-detached-example-60.png|איור {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} גרמפלט גלריה – תצוגה מנותקת]]

גרמפלט המציג עצמי מדיה. התמונה הראשונה היא עצם המדיה הראשי הפעיל, אשר משמש בדוחות וב.

ניתן להשתמש בתפריט ההקשר (הקשה ימנית) כדי לבחור באפשרות (דווח תקל )

הקשה כפולה על התמונה תפתח אותה ביישום ברירת־המחדל לצפייה בתמונות.

למידע נוסף:

- לשם שינוי עצם המדיה הראשי לדוחות וכדומה, יש להשתמש בלשונית שב.

{{-}}

#### גלריית אדם

ראו [גלריה](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/he#גלריה) {{-}}

#### גלריית משפחה

ראו [גלריה](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/he#גלריה) {{-}}

#### גלריית אירועים

ראו [גלריה](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/he#גלריה) {{-}}

#### גלריית מקומות

ראו [גלריה](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/he#גלריה) {{-}}

#### גלריית מקורות

ראו [גלריה](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/he#גלריה) {{-}}

#### גלריית מובאות

ראו [גלריה](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/he#גלריה) {{-}}

## Given Name Cloud

![[_media/GivenNameCloud-Gramplet-detached-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Given Name Cloud Gramplet - detached example]]

Like the [Surname Cloud Gramplet](#Surname_Cloud), the Given Name Cloud Gramplet shows the top most popular given names in your family tree. The size of the name indicates how popular it is. Mouse over the name to see the exact count, and the percent of people in the family tree that have that name.

The Gramplet splits up given names into words (broken up by spaces). For example "Sarah Elizabeth" would appear under both "Sarah" and "Elizabeth".

Double-click on the given name to bring up a Quick View of all of the matching people. {{-}}

## Image Metadata

![[_media/ImageMetadata-Gramplet-detached-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Image Metadata Gramplet - example]]

The Image Metadata Gramplet offers an interface to look at [Image Exif Metadata](https://en.wikipedia.org/wiki/Exchangeable_image_file_format) from your images (\*.jpg, \*.png. \*.tiff, \*.exv, \*.nef, \*.psd, \*.pgf). {{-}} See also the third party:

- [Addon:Edit Image Exif Metadata](wiki:Addon:Edit_Image_Exif_Metadata)

### Prerequisites

Once you have installed gexiv2, see above for directions to download and install this addon...

Pyexiv2 can be used from the command line interface (cli) as well, and from within a python script:

1.  import the pyexiv2 library
      
    from pyexiv2 import ImageMetadata, ExifTag
2.  specify your image
      
    image = ImageMetadata("/home/user/image.jpg")
3.  read the image
      
    image.read()

Exif, IPTC, XMP metadata reference tags can be found [here](http://www.exiv2.org/metadata.html).

Example:

  
image\["Exif.Image.Artist"\] \# Artist

Smith and Johnson's Photography Studio

<!-- -->

  
image\["Exif.Image.DateTime"\] \# DateTime

1826 Apr 12 14:00:00

<!-- -->

  
image\["Exif.Image.DateTime"\] = datetime.datetime.now() \# Add DateTime

<!-- -->

  
image.write() \# write the Metadata

### Usage scenario

The preferred way to use this addon is:

1.  install pyexiv2
2.  Install this addon
3.  Restart Gramps
4.  Click Views from the Menu bar, and select Media Views
5.  Open the Side Bar
6.  Slide the available empty right view to about half the screen.
7.  Right click text to the Side Bar tab, and select Add a Gramplet
8.  Select Image Metadata Gramplet
9.  Select an image from the left hand MediaView

{{-}}

## Media Preview

![[_media/MediaPreview-Gramplet-detached-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Media Preview Gramplet - detached example]]

Gramplet shows a preview of a single media object. {{-}} See [Media Category](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Media_Category)

## הערות

![[_media/Notes-Gramplet-detached-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Notes Gramplet - detached example]]

Gramplet showing the active persons notes.

See also:

- [Note Gramplet](wiki:Addon:NoteGramplet) - Third party Addon

{{-}}

### Person Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) {{-}}

### Family Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) {{-}}

### Event Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) {{-}}

### Place Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) {{-}}

### Source Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) {{-}}

### Citation Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) {{-}}

### Repository Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) {{-}}

### Media Notes

See [Notes](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Notes) {{-}}

## יוחסין

![[_media/Pedigree-Gramplet-detached-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pedigree Gramplet - detached example]]

The Pedigree Gramplet shows a compressed view of the active person's direct ancestors. It defaults to going back 100 generations. The names can be clicked to change the active person, right-click to edit the person. At the bottom of the Gramplet the number of people per generation is listed. Birth and death dates are shown next to each person's name. Double-click the Generation number to see the matching individuals.

Using the content of the Pedigree in another program requires a bit of effort Open a contextual pop-up menu by right-clicking anywhere in the gramplet except a hotlink. Or, you can begin a drag selection from the same inert areas. Copy the highlighted text the OS clipboard from that same context menu. (The keybinding for 'Copy' will not work.) When you paste the text into another text editing program, you may need change the font to a non-proportional font to preserve the indentation. Some online services collapse leading spaces when you post a chunk of text. Preserving the indentation for such services may require replacing doubled spaces with doubled placeholder characters... like periods/full stops.

#### ⚙ Configurable Options

- Maximum generations: 1 to 100 limit; (default: *100*)
- Show Dates checkbox; (default: *deselected*)
- Line Type menu: <abbr title="Unicode Transformation Format graphical symbols">UTF</abbr>, <abbr title="American Standard Code for Information Interchange text symbols">ASCII</abbr>; (default: *UTF*)

## מצג מהיר

![[_media/QuickView-Gramplet-Configuration-tab-52.png|איור: {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} גרמפלט "מצג מהיר" — תצוגה מנותקת]]

הגרמפלט מאפשר להפעיל תצוגה מהירה, והוא מתעדכן בכל מעבר בין אנשים. (בעת הוספת גרמפלט זה לראשונה, הוא תמך רק במצג מהיר מסוג־האב "אנשים", אך כיום נתמכים גם סוגי־אב נוספים).

ניתן להפעיל כל אחת מה[מצגים המהירים](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8/he#מצגים_מהירים) עבור אדם מסוים. {{-}}

![[_media/QuickView-Gramplet-detached-52.png|איור: {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} גרמפלט "מצג מהיר" — לשונית התצורה]]

אפשר לשנות את ההגדרות דרך לחצן האפשרויות (בפינה העליונה השמאלית של הגרמפלט), שגורם לניתוק הגרמפלט ופתיחתו בחלון חדש. יש לבחור בלשונית שבשורת הלשוניות העליונה, ולהציג את רשימת האפשרויות. לחיצה על תפעיל את השינויים. לאחר מכן ניתן לסגור את החלון ולהחזיר את הגרמפלט למקומו.

{{-}}

למידע נוסף למפתחים המעוניינים ליצור גרסה משלהם:

:\*[כיצד ליימור מצג מהיר](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_8/he#Making_your_own_Quick_view)

`   {{-}}`

## Records

![[_media/Records-Gramplet-detached-52.png|Fig {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Records Gramplet - detached example]]

The Records Gramplet shows a number of interesting facts about the records (mostly age related) from your database. The list shows the top three for each element.

- Person Records:
  - Youngest living person
  - Oldest living person
  - Person died at youngest age
  - Person died at oldest age
  - Person married at youngest age
  - Person married at oldest age
  - Person divorced at youngest age
  - Person divorced at oldest age
  - Youngest father
  - Youngest mother
  - Oldest father
  - Oldest mother
- Family Records
  - Couple with most children
  - Living couple married most recently
  - Living couple married most long ago
  - Shortest past marriage
  - Longest past marriage

{{-}} The list is not only interesting on its own, it is also a good sanity check of the data. For some items you have to fill in some additional information.

This following example shows that there was a marriage event (thus calculation of the offset) but none of the persons had a death event. Even if the date is not known, just enter a death event for one of the partners and the list will be corrected.

**Living couple married most long ago**

1.  van Dosselaere, Egidius and Rechters, Petronella (382 years, 1 month)
2.  de Richter, Petrus and Asscericx, Catharina (379 years, 9 months)

{{-}}

An identical [Records Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Records_Report) is also available.

## אזכורים

![[_media/References-Gramplet-detached-52.png|איור {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} גרמפלט אזכורים – דוגמה מופרדת (צפה)]] גרמפלט המציג את האזכורים של האדם הפעיל.

{{-}}

### אזכורי אדם

אזכורי אדם: גרמפלט המציג את האזכורים החוזרים (backlink) עבור אדם.

למידע נוסף: [אזכורים](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/he#אזכורים) {{-}}

### אזכורי משפחה

אזכורי משפחה: גרמפלט המציג את האזכורים החוזרים עבור משפחה.

למידע נוסף: [אזכורים](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/he#אזכורים) {{-}}

### אזכורי אירועים

אזכורי אירועים: גרמפלט המציג את האזכורים החוזרים עבור אירוע.

למידע נוסף: [אזכורים](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/he#אזכורים) {{-}}

### אזכורי מקום

אזכורי מקום: גרמפלט המציג את האזכורים החוזרים עבור מקום.

למידע נוסף: [אזכורים](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/he#אזכורים) {{-}}

### אזכורי מקור

אזכורי מקור: גרמפלט המציג את האזכורים החוזרים עבור מקור.

למידע נוסף: [אזכורים](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/he#אזכורים) {{-}}

### אזכורי מראי־מקום

אזכורי מראי־מקום: גרמפלט המציג את האזכורים החוזרים עבור מראי־מקום.

למידע נוסף: [אזכורים](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/he#אזכורים) {{-}}

### אזכורי מאגר

אזכורי מאגר: גרמפלט המציג את האזכורים החוזרים עבור מאגר.

למידע נוסף: [אזכורים](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/he#אזכורים) {{-}}

### אזכורי מדיה

אזכורי מדיה: גרמפלט המציג את האזכורים החוזרים עבור עצם מדיה.

למידע נוסף: [אזכורים](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/he#אזכורים) {{-}}

### אזכורי פתקים

אזכורי פתקים: גרמפלט המציג את האזכורים החוזרים עבור פתק.

למידע נוסף: [אזכורים](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/he#אזכורים) {{-}}

## קרובי משפחה

![[_media/Relatives-Gramplet-detached-52.png|Fig {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Relatives Gramplet - detached example]]

This Gramplet shows all direct relatives of the active person. It's intended use is as a navigation help, an alternative way to move through your family tree in Gramps . If you detach the Gramplet, and place it next to Gramps, it will allow you to use it to easily change the content of the current "Person view".

If you are working in the charts category Pedigree view, the active person is the left-most person. By clicking a name in the relatives Gramplet, you can easily change the active person, and all person view in the other window will update. As the relatives Gramplet shows all spouses, all children and all parents, this offers an alternative way of navigating your data.

The names in this Gramplet also allow you to call up the person editor directly, by right-clicking on any of the names.

The Relatives Gramplet can be added to the following categories:

- People Category
- Relationships Category
- Charts Category
- Geography Category (selected views only)

{{-}}

## Residence

![[_media/ResidenceGramplet-Person-detached-example-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Person - Residence Gramplet - detached - example]]

Gramplet showing residence events for the active person {{-}}

### Person Residence

See [Residence](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Residence) {{-}}

## Session Log

![[_media/SessionLog-Gramplet-detached-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Session Log Gramplet - detached example]]

The session log keeps track of activity in this session. It lists selected and edited objects.

Click a name once to make this person the active person. Double-click on a name or family brings up the page for that object. In addition, if you want to edit a person, but don't want to change the active person, you can right-click on the person's name.

This Gramplet is handy because you can very quickly change the active person, or edit the object, from the session list. {{-}}

### SoundEx

![[_media/SoundEx-Gramplet-detached-60_he.png|איור {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} גרמפלט SoundEx — דוגמה מנותקת המציגה תפריט הקשר]]

הגרמפלט יוצר קודי סאונדאקס לשמות אנשים באילן־יוחסין.

מחלון ניתן לבחור ערך מתוך התפריט הנשלף על־ידי לחיצה על החץ שמצביע מטה , או להקליד שם ישירות בשדה הקלט.

ניתן לבחור או להזין כל שם — לרבות שם שלא קיים באילן־היוחסין.

השדה מציג את התוצאה באופן אוטומטי. לדוגמה: הקוד עבור *Simpson* הוא *S512*.

ניתן להקיש הקשת עכבר ימנית על שדה כדי להעתיק את התוצאה.

לחצן ה מפנה לעמוד זה, ולחצן (או קיצור המקלדת ) לסגירת חלון . {{-}}

##### מהו SoundEx?

SoundEx הוא האלגוריתם הפונטי הידוע ביותר שמאפשר אינדוקס של מילים לפי הגייתן באנגלית. מנגנון סאונדאקס נתמך בחיפוש באמצעות [התאמת סאונדאקס של אנשים לפי שם](wiki:Gramps_6.0_Wiki_Manual_-_Filters/he#Soundex_match_of_People_with_the_.3Cname.3E), בגרמפלט , וככלי עזר בבדיקת התאמות במיזם .

הקוד של סאונדאקס הוא מפתח מקודד של שם־המשפחה לפי הצליל שלו ולא לפי האיות. שמות שנשמעים אותו דבר, אך מאויתים שונה, כגון SMITH ו־SMYTH, מקבלים את אותו הקוד ומקובצים יחד.

מערכת הקידוד פותחה לצורך מיפוי שמות־משפחה גם כאשר יש להן גרסאות כתיב שונות. היא יושמה לראשונה במפקד ארה"ב בשנת 1880. מדובר במפתוח לפי צליל, לא לפי סדר אלפביתי.

המאפיין העיקרי הוא קידוד שמות־משפחה לפי ההגייה, והמערכת קודמת לעידן המחשוב. היא נועדה לעזור לחוקרים לאתר שמות למרות ההגוון באיות.

בעת חיפוש, יש לחשב את הקידוד של שם־המשפחה כפי שבוצע על־ידי פקידי המִפקד.

מטבעו האלגוריתם תלוי בשפה. מובן שהוא דורש התאמה לשימוש בשפה שאיננה נכתבת באלפבית לטיני, וגם כאשר השפה נכתבת באלפבית לטיני, כללי ההגייה שלה עשויים להיות שונים מאלה של האנגלית.

באמצע שנות השישים פותח בישראל אלגוריתם סאונדקס לשמות עבריים, אך כלי זה בגרמפס **אינו מותאם לשפה העברית**.

- **כלל הקידוד הבסיסי של SoundEx:**

כל קוד סאונדאקס מורכב מאות ושלוש ספרות, כגון W-252. האות היא האות הראשונה בשם־המשפחה. הספרות מוקצות לשאר האותיות לפי הטבלה שלהלן. אם צריך, משלימים אפסים לסך ארבע תווים. אותיות נוספות מעבר לכך מושמטות.

דוגמאות:

- Washington → W-252 (W, 2 עבור S, 5 עבור N, 2 עבור G)
- Lee → L-000 (L + שלושה אפסים)

| מספר | אותיות תואמות          |
|------|------------------------|
| 1    | B, F, P, V             |
| 2    | C, G, J, K, Q, S, X, Z |
| 3    | D, T                   |
| 4    | L                      |
| 5    | M, N                   |
| 6    | R                      |

אותיות A, E, I, O, U, H, W, Y מושמטות מהקידוד.

- **כללים נוספים:**
  - אותיות כפולות נחשבות לאות אחת:
    - Gutierrez → G-362 (G, 3 עבור T, 6 עבור R הראשון, השני מושמט, 2 עבור Z)
  - אותיות עוקבות עם אותו קוד SoundEx נחשבות לאחת:
    - Pfister → P-236 (P, F מושמט, 2 עבור S, 3 עבור T, 6 עבור R)
    - Jackson → J-250 (J, 2 עבור C, K ו־S מושמטים, 5 עבור N, 0 נוסף)
    - Tymczak → T-522 (T, 5 עבור M, 2 עבור C, Z מושמט, 2 עבור K; מכיוון ש־A מפרידה בין Z ו־K, K מקודדת)
  - קידוד שמות עם קידומות (Van, Con, De, Di, La, Le): יש לקודד גם עם וגם בלי הקידומת, למעט Mc ו־Mac שאינן נחשבות לקידומת.
    - לדוגמה: VanDeusen → V-532 או D-250
  - תנועות כמפרידות עיצורים: אם תנועה מפרידה בין שני עיצורים עם אותו קוד, העיצור הימני מקודד.
    - Tymczak → T-522 (T, 5 עבור M, 2 עבור C, Z מושמט, 2 עבור K)
  - אם H או W מפרידים בין עיצורים עם אותו קוד, העיצור הימני אינו מקודד:
    - Ashcraft → A-261 (A, 2 עבור S, C מושמט, 6 עבור R, 1 עבור F)

למידע נוסף:

- [סאונדאקס באתר הארכיון הלאומי של ארה"ב](http://www.archives.gov/research/census/soundex.html).
- [סאונדאקס בויקיפדיה](https://he.wikipedia.org/wiki/סאונדקס)

{{-}}

## Statistics

![[_media/Statistics-Gramplet-detached-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Statistics Gramplet - detached example]]

The Statistics Gramplet runs a Statistics report. Double-click the phrases to bring up the matching items.

Following information is provided to you in this Gramplet:

- **Individuals**
  - Number of individuals
  - Males
  - Females
  - Individuals with unknown gender
  - Incomplete names
  - Individuals with missing birth dates
  - Disconnected individuals
- **Family information**
  - Number of families
  - Unique surnames
- **Media objects**
  - Individuals with media objects
  - Total numbers of media object references
  - Number of unique media objects
  - Total size of media objects
  - Missing Media Objects

As with all Gramplets if you click on the left hand side button you detach the window and if you add persons to your family tree, you will see the amount of individuals change dynamically.

The information given in this Gramplet is the same as in the [Database Summary Report](wiki:Gramps_6.0_Wiki_Manual_-_Reports_-_part_6#Database_Summary_Report) {{-}}

## Surname Cloud

![[_media/SurnameCloud-Gramplet-detached-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Surname Cloud Gramplet - detached example]]

The Surname Cloud Gramplet shows the top 100 (by default) used surnames. The name font size is proportional to the amount of people with the same name.

Double-click a surname to run the . This will open the window where you can find all people with a matching or alternate name. Person, birth date and name type are given.

If you mouse over the name you see the percentage of occurrence and total counts. {{-}} ![[_media/SurnameCloud-Gramplet-Configuration-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Surname Cloud Gramplet - Configuration tab shown]]

You can change the number of names displayed by configuring the view for this gramplet. {{-}}

## To Do

![[_media/ToDo-Gramplet-detached-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} To Do Gramplet - detached example]]

The **To Do Gramplet** displays a free form text area showing the contents of Note objects of the "To Do" type.

You can use this area to put some notes, remarks, things you should to get your research going. There are several other To Do programs (e.g. Tomboy e.a.) but these Gramplets are useful as the information stays within the Gramps database.

To Do Gramplets allow you to create notes and attach them to Gramps objects. For example, you can add a Person To Do Gramplet to the sidebar of the Person View. Notes added using this Gramplet will be attached to the currently active person. There is a To Do Gramplet for each Gramps primary object type. {{-}} See also the experimental [Third-party Addon](wiki:Third-party_Addons):

- [ToDo Notes Gramplet](wiki:Addon:ToDoNotesGramplet) available for the Dashboard that lists all To Do notes in the database, together with the object to which they are attached.

{{-}}

### Person To Do

See [To Do](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#To_Do) {{-}}

### Family To Do

See [To Do](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#To_Do) {{-}}

### Event To Do

See [To Do](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#To_Do) {{-}}

### Place To Do

See [To Do](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#To_Do) {{-}}

### Source To Do

See [To Do](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#To_Do) {{-}}

### Citation To Do

See [To Do](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#To_Do) {{-}}

### Repository To Do

See [To Do](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#To_Do) {{-}}

### Media To Do

See [To Do](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#To_Do) {{-}}

## Top Surnames

![[_media/TopSurnames-Gramplet-detached-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Top Surnames Gramplet - detached example]]

The Top Surnames Gramplet shows the top 10 (by default) used surnames.

The top ten is presented as follows:

- Surname
- percentage
- occurrences

The list gives you also the Total unique surnames in the database as well as the total number of people in your database.

Double-click a surname to run the . This opens the window, which gives the people with the surname you double-clicked.

A table is presented which shows all people with a matching name or alternate name. Person's name, ID, birth date and name type is given. {{-}}

Advanced:

- Change the number of names displayed by editing this section in `~/.gramps/gramps50/gramplets.ini`

{{-}}

## Uncollected Objects

![[_media/UncollectedObjects-Gramplet-detached-example-52.png|Fig {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Uncollected Objects Gramplet - detached example]]

The Gramplet is intended to list the low-level Python objects that are left around in memory and cannot be (easily) automatically deleted when they are no longer in use. Developers use it to try to identify the source of memory 'leaks', which cause Gramps to continually use more and more memory, the longer it is used.

Because the tool is trying to display objects that might still be getting deleted, it sometimes has some trouble. {{-}}

## Welcome

![[_media/Welcome-Gramplet-detached-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Welcome Gramplet - detached example]]

The **Welcome to Gramps!** Gramplet gives an introductory message to new users, and some basic instructions.

The welcome message describes what Gramps is, that the program is Open Source Software and how you start a [Family Tree](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees). {{-}}

## What's Next

![[_media/WhatsNext-Gramplet-detached-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} What's Next? Gramplet - detached example]]

The What's Next Gramplet displays a list of the "most urgent" information gaps in your family tree. It is based on the following assumptions:

- The Home Person defines the focus
- Searches for gaps begin with the Home Person's descendants and work up the tree
- The tree is expected to contain the given name, surname, birth date and place, and death date and place of each person
- You want to know parents, their marriage date and place, and - if divorced - divorce date and place of each family with married parents
- You want to know at least the mother of each family with unmarried parents
- The closer the relationship to the Home Person, the more "urgent" the information gap is.
- The closer the common ancestor is from the main person, the more "urgent" the information is (e.g. nephews are considered more "urgent" than uncles, even though both have a distance of 3 generations, because for nephews the common ancestor is father/mother, while for uncles, the common ancestor is grandfather/grandmother)
- Marriage data and personal data of the spouse is slightly less "urgent" than personal data of the directly related person
- Half-siblings are less "urgent" than siblings

You may copy the text from inside of this Gramplet by selecting it and pasting into an empty document. {{-}} ![[_media/WhatsNext-Gramplet-Configuration-tab-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} What&#39;s Next? Gramplet - Configuration tab shown]]

The Gramplet can ignore previously verified events by making use of some custom Tags. The tags are selected in the Gramplets configuration. For example you can tag the following to be ignored:

- that a person is complete
- that a family is complete
- that a person or family should be ignored for shortening lists

{{-}}

[Category:He:תיעוד](wiki:Category:He:תיעוד)
