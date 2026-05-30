---
title: Gramps 6.0 Wiki Manual - Error and Warning Reference/sk
categories:
- Pages with broken file links
- Sk:Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 119271
wiki_fetched_at: '2026-05-30T20:04:53Z'
lang: sk
---

{{#vardefine:chapter\|E}} {{#vardefine:figure\|0}} V tejto časti sa vysvetľuje, čo robiť, keď sa stane niečo neočakávané.

# Keď sa niečo pokazí

Niekedy sa niečo pokazí, buď preto, že ste požiadali o niečo, čo Gramps nevie urobiť, alebo preto, že sa stalo niečo, čo vývojári Gramps nepredpokladali, alebo preto, že v kódovaní Gramps došlo k chybe.

# Upozornenia

Upozornenie je dialógové okno, ktoré sa zobrazí, keď vám Gramps potrebuje poskytnúť dôležitú správu o chybovom stave alebo vás upozorniť na potenciálne nebezpečné situácie alebo následky.

Väčšina upozornení je samozrejmá a ide o rovnaký typ upozornení, aké môžete dostať v akomkoľvek programe. Tu sa nimi nebudeme ďalej zaoberať.

Niektoré výstrahy však vyžadujú zložitejšie akcie, preto sú opísané nižšie. {{-}} == Ste si istí, že chcete aktualizovať tento rodinný strom?

![[_media/AreYouSureYouWantToUpgradeThisFamilyTree-dialog-DbUpgradeRequiredError-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialógové okno "Are you sure you want to upgrade this Family Tree?" - Db Upgrade Required - example]]

![[_media/AreYouSureYouWantToUpgradeThisFamilyTree-dialog-BsddbUpgradeRequiredError-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialógové okno "Are you sure you want to upgrade this Family Tree?" (Určite chcete aktualizovať tento rodinný strom?) - Bsddb Upgrade Required Error (Chyba požadovanej aktualizácie Bsddb) - príklad]]

![[_media/AreYouSureYouWantToDowngradeThisFamilyTree-dialog-BsddbDowngradeRequiredError-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialógové okno "Are you sure you want to downgrade this Family Tree?" - Bsddb Downgrade Required Error - príklad]]

![[_media/AreYouSureYouWantToUpgradeThisFamilyTree-dialog-PythonUpgradeRequiredError-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialógové okno "Určite chcete aktualizovať tento rodinný strom?" - Chyba vyžadovaná aktualizáciou Pythonu - príklad]]

Tieto dialógové okná sa zobrazujú z uvedených dôvodov:

- "Db Upgrade Required" (Vyžaduje sa aktualizácia Db) - Ak sa pokúšate otvoriť Db(Sqlite3) Rodokmeň vytvorený pomocou predchádzajúcej staršej verzie programu Gramps s novšou verziou programu Gramps.
- "Bsddb Upgrade Required Error" (Vyžaduje sa aktualizácia Bsddb) - ak sa pokúsite otvoriť rodinný strom Bsddb vytvorený pomocou predchádzajúcej staršej verzie programu Gramps s novšou verziou programu Gramps.
- "Bsddb Downgrade Required Error" (Chyba vyžadovaná pri aktualizácii Bsddb) - ak sa pokúsite otvoriť rodinný strom Bsddb vytvorený pomocou predchádzajúcej staršej verzie Bsddb s novšou verziou Bsddb.
- "Python Upgrade Required Error (Vyžaduje sa aktualizácia Pythonu)" - ak sa pokúsite otvoriť rodinný strom Bsddb vytvorený pomocou predchádzajúcej staršej verzie programu Gramps, ktorá používa Python 2, s novšou verziou programu Gramps, ktorá používa Python 3.

Z každého z týchto dôvodov môžete postupovať podľa rovnakej všeobecnej rady; ak máte stále k dispozícii staršiu verziu programu Gramps, mali by ste:

- Zrušiť tento dialóg a ukončiť program Gramps
- Otvoriť rodinný strom s predchádzajúcou verziou programu Gramps (Preinštalovať starú verziu programu Gramps),
- Exportujte svoj rodinný strom do [Gramps XML (export rodinného stromu)](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/sk#Gramps_XML_.28family_tree.29_export) alebo [Gramps XML Package (family tree and media)](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/sk#Gramps_XML_Package_.28family_tree_and_media.29_export),
- Ukončite starú verziu programu Gramps a spustite novú verziu programu Gramps,
- Otvorte rodinný strom v novej verzii programu Gramps a v tomto dialógu kliknite na .

{{-}}

## Nemožno otvoriť databázu

![[_media/Cannot_open_database.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialóg zobrazujúci chybu prostredia DB]]

![[_media/DbVersionError.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialóg zobrazujúci chybu verzie DB]]

Ako je vysvetlené v dialógu, rodinný strom bol pravdepodobne vytvorený pomocou starej verzie databázového programu Berkeley. To nie je celkom to isté ako stará verzia programu Gramps, pretože verzia programu Gramps a verzia databázy Berkeley sú nezávislé. Účinok je však do istej miery rovnaký. Ako sa navrhuje v dialógu, ak máte starú verziu programu Gramps a jeho podporného softvéru, mali by ste:

- zrušiť tento dialóg,
- otvoriť rodinný strom pomocou predchádzajúcej verzie programu Gramps,
- exportovať rodinný strom do formátu XML databázy Gramps alebo do formátu balíka Gramps (pozri [Export do formátov Gramps](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/sk#Export_do_formátov_Gramps)),
- spustite novú verziu programu Gramps,
- otvorte dialóg "Správa rodinných stromov",
- kliknite na a vytvorte nový rodinný strom,
- načítajte nový rodinný strom
- importujte balík Gramps XML alebo Gramps.

Prípadne je možné použiť nástroje na obnovu. Pozrite si časť "získanie nástrojov na obnovu bsddb" v časti [Obnova poškodeného rodinného stromu](wiki:Obnova_poškodeného_rodinného_stromu). {{-}}

## Zistené poškodenie databázy na nízkej úrovni

![[_media/LowLevelDatabaseCorruptionDetected-dialog-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialógové okno "Zistené poškodenie databázy na nízkej úrovni" - príklad]]

Tento dialóg sa zobrazí, keď sa zistí problém so základnou databázou, ktorá podporuje Rodinné stromy.

- zatvorte dialóg,
- kliknite na Správca rodinných stromov,
- vyberte Rodinný strom, ktorý ste sa pokúšali otvoriť,
- malo by byť k dispozícii tlačidlo ; kliknite naň,
- po oprave rodinného stromu by malo byť možné otvoriť ho bežným spôsobom.

Ak to nefunguje, skúste "získať nástroje na obnovu bsddb" v časti [Obnova poškodeného rodinného stromu](wiki:Obnova_poškodeného_rodinného_stromu). {{-}}

## V databáze bola zistená chyba

![[_media/RunDatabaseRepair.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialóg zobrazujúci spustenie opravy databázy]]

Vykonajte navrhovanú akciu. {{-}}

# Varovania

Ak Gramps zistí menšiu chybu alebo vás chce upozorniť na nejakú udalosť v programe, potom môže Gramps na stavovom riadku zobraziť tlačidlo , ako je znázornené nižšie. Toto tlačidlo sa zobrazuje len 180 sekúnd, takže ak ho uvidíte, mali by ste naň okamžite kliknúť, ak chcete vidieť správy.

![[_media/Status-bar-warning-button-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Hlavné okno programu Gramps zobrazujúce tlačidlo Varovanie na stavovom riadku]]

{{-}}

Ak kliknete na tlačidlo , zobrazí sa dialógové okno zobrazujúce posledných 20 prijatých správ. [Viac informácií](wiki:Logovanie_systému) ![[_media/Gramps-warnings-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Hlavné okno programu Gramps zobrazujúce varovné hlásenia]] {{-}}

Niektoré z varovaní, ktoré sa môžu objaviť, sú opísané nižšie:

## Upozornenia týkajúce sa lokálneho jazyka

Niekedy sa vyskytne problém s jazykom, ktorý ste si vybrali.

Ak ste nainštalovali program Gramps pomocou štandardnej inštalačnej metódy vašej platformy (Správca balíkov/AIO inštalátor/Balík aplikácií) a používate zabudovaný mechanizmus vašej platformy (Systémové nastavenia/Ovládací panel/Systémové nastavenia) na výber jazyka/poradia/formátov, v ktorých pracujete, potom by sa tieto chyby nemali vyskytovať a môžu znamenať, že v programe Gramps je problém.

Ak ste však nastavili jazyk/poradie triedenia/formáty ručne nastavením "prostredia", pozri [jazyky](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Jazyk), najmä ak spúšťate program Gramps z príkazového riadku, potom môže byť problém v tom, čo ste zadali. Správa (ktorej časť je zobrazená len nižšie) by vám mala pomôcť pochopiť, kde je chyba.

- "Parser dátumu pre '%s' nie je k dispozícii, použite predvolené nastavenie"
- "Zobrazovač dátumu pre '%s' nie je k dispozícii, používa sa predvolené nastavenie"
- "Prekladač rodinných vzťahov nie je k dispozícii pre jazyk '%s'. Namiesto toho použite 'english'."
- "Nie je možné určiť váš Locale, používate angličtinu
- "Lokalizačná knižnica libintl nie je na %PATH%, lokalizácia bude neúplná"
- "Neboli nájdené žiadne preklady pre %s, nastavenie lokalizácie na americkú angličtinu"
- "Nepodarilo sa vytvoriť kolokátor: %s"
- "Nebol poskytnutý žiadny jazyk, používame americkú angličtinu"
- "V zozname neboli nájdené žiadne použiteľné jazyky, používame americkú angličtinu"
- "Žiadny z požadovaných jazykov (%s) nebol k dispozícii, namiesto toho použite %s"

## Upozornenia na nenačítaný modul

Aplikácia Gramps obsahuje mnoho rôznych "modulov". Niektoré z týchto modulov sú potrebné na to, aby aplikácia Gramps vôbec fungovala; niektoré sú "dôrazne odporúčané" a niektoré sú voliteľné.

Ak ste program Gramps nainštalovali pomocou štandardnej inštalačnej metódy vašej platformy (Správca balíkov/AIO inštalátor/Balík aplikácií), potom tvorca tohto balíka rozhodol, ktoré moduly sú prítomné. Musí zahrnúť všetky požadované moduly, pretože inak Gramps nebude fungovať, ale môže si vybrať, ktoré z odporúčaných a voliteľných balíkov zahrnie. Pozrite si dokumentáciu k svojmu balíku, aby ste zistili, ktoré moduly sú zahrnuté.

Ak sa pokúsite vykonať niečo, čo vyžaduje modul, ktorý nie je zahrnutý, zobrazí sa varovanie, ako je uvedené nižšie (zahrnutá je len prvá časť správy). Čo s tým môžete urobiť, závisí od vašej platformy:

**Linux** Mali by ste byť schopní nainštalovať balík pomocou štandardného správcu balíkov vašej distribúcie alebo pomocou grafického rozhrania správcu balíkov. V niektorých prípadoch však budete musieť modul zostaviť zo zdrojových kódov.

**MS Windows a Mac OS X** Inštalačný program MS Windows AIO a balík aplikácií Max OS X sa dodávajú so zabudovanými určitými modulmi. Bežný používateľ nemá možnosť pridávať ďalšie moduly. Preto, ak nájdete modul, ktorý by podľa vás mal byť obzvlášť zahrnutý, mali by ste to napísať do zoznamu Gramps [mailing list](wiki:Contact#Mailing_lists). (pravdepodobne zoznam vývojárov) s vysvetlením, prečo si myslíte, že jeho vynechanie je chybou.

- "WARNING: PIL module not loaded. "
- "ICU nie je načítaný, pretože %s. Lokalizácia bude narušená. "
- "Modul OsmGpsMap nie je načítaný. "
- "Modul GExiv2 nie je načítaný. "
- "Webkit module not loaded. "
- "PIL (Python Imaging Library) nie je načítaný. "
- "GtkSpell nie je načítaný. "

### Zobraziť dialógové okno stavu zásuvného modulu pri chybe načítania zásuvného modulu.

Možno vypnúť pomocou možnosti v dialógovom okne [Predvoľby &gt; Warnings](wiki:Gramps_6.0_Wiki_Manual_-_Settings/sk#Varovania).

## Výstrahy konfigurácie

Niekedy sa oplatí staré konfiguračné súbory jednoducho vymazať.

- "Importovanie starého súboru s kľúčmi 'keys.ini'..."
- "Hotovo importovanie starého súboru s kľúčmi 'keys.ini'"
- "V definovaných vlastných filtroch nemožno nájsť filter %s"
- "Počet argumentov sa nezhoduje s počtom " +
- "Hodnota '%(val)s' nebola nájdená pre možnosť '%(opt)s'"
- "Nie je možné otvoriť nedávny súbor %s, pretože %s",
- "WARNING: ignoruje starý kľúč '%s'"
- "VAROVANIE: ignorovanie kľúča s nesprávnym typom "
- "Nepodarilo sa analyzovať možnosti dokumentu"
- "Preskočený riadok vo výpise doplnkov: "
- "Nepodarilo sa načítať gramplety z %s, pretože %s"

## Ďalšie upozornenia

{{-}}

### Nemôže sa uložiť osoba

![[_media/CannotSavePerson-dialog-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nemožno uložiť osobu (okno s upozornením)]] Pri pokuse o uloženie osoby bez akýchkoľvek údajov z editora osôb sa zobrazí toto výstražné okno. Potrebujete aspoň jedno písmeno pre krstné meno.

**Nemožno uložiť osobu**  
Pre túto osobu neexistujú žiadne údaje. Zadajte prosím údaje alebo zrušte úpravu.  
Zatvoriť {{-}}

### Duplicitné dialógové okno s upozornením na rodinu

}

![[_media/DuplicateFamily-warning-dialog-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Duplicitná rodina - varovný dialóg]]

{{-}}

### Potlačiť varovanie pri pridávaní rodičov k dieťaťu

Možno zapnúť pomocou } možnosti v dialógovom okne [Preferences &gt; Warnings](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Varnings).

{{-}}

#### Dialógové okno Pridanie rodičov k osobe

![[_media/AddingParetsToA-Person-warning-dialog-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialógové okno s upozornením "Pridanie rodičov k osobe"]]

{{-}}

### Potlačiť varovanie pri zrušení so zmenenými údajmi

Možno vypnúť pomocou } možnosti v dialógovom okne [Preferences &gt; Warnings](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Varnings).

Používa sa v dialógovom okne [Úprava osoby](wiki:Gramps_6.0_Wiki_Manuál_-_Vstupovanie_a_editácia_údajov:_detail_-_časť_1#Úprava_osoby).

#### Dialóg Uložiť zmeny?

![[_media/SaveChanges-alert-dialog-60.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Uložiť zmeny?" - dialógové okno s upozornením]]

{{-}}

### Potlačiť upozornenie o chýbajúcom výskumníkovi pri exporte do GEDCOM

![[_media/xxx.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} xxx]]

Možno vypnúť z možnosti } v dialógovom okne [Preferences &gt; Warnings](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Varnings).

{{-}}

### Upozornenie na zrušenie histórie

![[_media/UndoHistoryWarning-Tool-dialog-52.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialógové okno nástroja "Upozornenie na zrušenie histórie" - predvolené]]

Zobrazí sa dialógové okno a môžete buď alebo . Odporúča sa zastaviť a zálohovať databázu; aby ste v prípade potreby mohli vrátiť proces spustenia nástroja (alebo importu). {{-}} ![[_media/UndoHistoryWarning-Import-dialog-52.png|Obrázok {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialógové okno Import &quot;Upozornenie na zrušenie histórie&quot; - predvolené]] {{-}}

# Chyby

Vážnejšie problémy spôsobia zobrazenie dialógového okna , v ktorom sú popísané kroky, ktoré by ste mali vykonať.

{{-}}

## Hlásenie o chybe

![[_media/ErrorReport-dialog-collapsed-ErrorDetail-default-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pomocník pri hlásení chýb - dialógové okno - zbalené "Detail chyby" - predvolené]]

Dialógové okno sa zobrazí vždy, keď sa v programe Gramps stane niečo, čo programátori neočakávali.

Prečítajte si článok [Ako vytvoriť dobré hlásenie chyby](wiki:Ako_vytvoriť_dobré_hlásenie_chyby). Ak sa domnievate, že viete, ako by mohli vývojári programu Gramps chybu reprodukovať alebo nie, potom vyberte tlačidlo , čím spustíte dialóg a potom môžete postupovať podľa pokynov. {{-}} ![[_media/ErrorReport-dialog-expanded-ErrorDetail-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Pomocník pri hlásení chýb - dialógové okno - rozšírené &quot;Detail chyby&quot; - predvolené]] {{-}}

## Dialógové okno Pomocník pre nahlasovanie chýb

Umožňuje vám zostaviť hlásenie o chybe a potom ho ručne odoslať do systému hlásenia chýb Gramps (vyžaduje si to registrované konto v systéme hlásenia chýb Gramps)

- [Používanie nástroja na sledovanie chýb](wiki:Používanie_nástroja_na_sledovanie_chýb)

Asistent pre nahlasovanie chýb je známy aj ako Asistent pre nahlasovanie chýb. {{-}}

### Stránka Nahlásenie chyby

![[_media/ErrorReportingAssistant-ReportABug-page-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Nahlásiť chybu (stránka) - Asistent pre nahlasovanie chýb]]

Toto je asistent pre nahlasovanie chýb. Pomôže vám vytvoriť hlásenie chyby vývojárom programu Gramps, ktoré bude čo najpodrobnejšie.

Asistent položí niekoľko otázok a zozbiera niekoľko informácií o chybe, ktorá sa práve vyskytla, a o operačnom prostredí.

Na konci procesu asistenta budete vyzvaní, aby ste podali hlásenie o chybe prostredníctvom systému [Gramps bug tracking](https://gramps-project.org/bugs/my_view_page.php).

Asistent skopíruje hlásenie o chybe do schránky operačného systému. To vám umožní vložiť ho do formulára v systéme [Gramps bug tracking](https://gramps-project.org/bugs/my_view_page.php) a skontrolovať, aké informácie presne chcete zahrnúť. {{-}}

### Stránka s podrobnosťami o chybe

![[_media/ErrorReportingAssistant-ErrorDetails-page-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Podrobnosti o chybe (stránka) - Asistent pre nahlasovanie chýb (Zobrazenie príkladu chyby)]]

Ak vidíte, že sú v chybe zahrnuté nejaké osobné údaje, odstráňte ich.

Toto sú podrobné informácie o chybe Gramps, nebojte sa, ak im nerozumiete. Na nasledujúcich stránkach asistenta budete mať možnosť pridať ďalšie podrobnosti o chybe. {{-}}

### Stránka so systémovými informáciami

![[_media/ErrorReportingAssistant-SystemInformation-page-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Systémové informácie (stránka) - Pomocník pri hlásení chýb]]

Toto sú informácie o vašom systéme, ktoré pomôžu vývojárom opraviť chybu. {{-}}

### Stránka s ďalšími informáciami

![[_media/ErrorReportingAssistant-FurtherInformation-page-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Ďalšie informácie (stránka) - Asistent pre nahlasovanie chýb]]

Uveďte čo najviac informácií o tom, čo ste robili, keď sa chyba vyskytla.

Toto je vaša príležitosť opísať, čo ste robili, keď sa chyba vyskytla. {{-}}

### Súhrnná stránka hlásenia chyby

![[_media/ErrorReportingAssistant-BugReportSummary-page-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Súhrn hlásení o chybách (stránka) - Asistent pre hlásenie chýb]]

Toto je dokončené hlásenie o chybe. Ďalšia stránka asistenta vám pomôže vyplniť chybu na webovej stránke systému sledovania chýb Gramps. {{-}}

### Odoslanie stránky s hlásením chyby

![[_media/ErrorReportingAssistant-SendBugReport-page-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Odoslať hlásenie o chybe (stránka) - Asistent pre hlásenie chýb]]

Pomocou dvoch nižšie uvedených tlačidiel najprv skopírujte hlásenie o chybe do schránky a potom otvorte webový prehliadač na odoslanie hlásenia o chybe na adrese <https://gramps-project.org/bugs/login_select_proj_page.php?ref=bug_report_page.php>

- \- Toto je posledný krok. Pomocou tlačidiel na tejto stránke spustite webový prehliadač a podajte hlásenie o chybe v systéme sledovania chýb Gramps (Predpokladá sa, že už máte používateľské konto v systéme sledovania chýb, ak nie, najskôr sa zaregistrujte.)

  - \- Toto tlačidlo použite na spustenie webového prehliadača a podanie hlásenia o chybe v systéme sledovania chýb Gramps.

  - \- Toto tlačidlo použite na skopírovanie hlásenia o chybe do schránky. Potom prejdite na webovú stránku sledovania chýb pomocou nižšie uvedeného tlačidla, vložte hlásenie a kliknite na tlačidlo Odoslať hlásenie

{{-}}

### Kompletná stránka

![[_media/ErrorReportingAssistant-Complete-page-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kompletná (stránka) - Asistent pre nahlasovanie chýb]]

Gramps je projekt s otvoreným zdrojovým kódom. Jeho úspech závisí od jeho používateľov. Spätná väzba od používateľov je dôležitá. Ďakujeme, že ste si našli čas na odoslanie hlásenia o chybe. {{-}}

## Ďalšie chyby

### Správu sa nepodarilo vytvoriť

![[_media/xxxx.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialógové okno Správa nemohla byť vytvorená]]

Dialógové okno sa môže vyskytnúť z rôznych dôvodov, napr. jedným z dôvodov je, že vlastný formát papiera, ktorý ste zvolili pre správu, je príliš veľký pre použitý formát PDF.

# Zobrazenie všetkých chybových správ

Niekedy sa na obrazovke nezobrazia všetky informácie potrebné na pochopenie toho, čo sa pokazilo. Napríklad, ak spustíte program Gramps s nesprávnym nastavením jazyka (a niektorými chýbajúcimi komponentmi), potom sa v dialógovom okne zobrazí táto správa:

![[_media/Warning_message_GExiv2.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dialóg zobrazujúci obmedzené varovania]] {{-}} Úplný súbor varovných hlásení je však:

` (process:10929): Gtk-WARNING **: Locale not supported by C library.`  
`   `  
`   Použitie záložného 'C' locale.`  
` 2013-03-13 18:49:04.376: WARNING: __init__.py: line 69: Parser dátumu pre 'xx_XX.UTF-8' nie je k dispozícii, používa sa predvolený`  
` 2013-03-13 18:49:04.547: WARNING: __init__.py: line 85: Zobrazovač dátumu pre 'xx_XX.UTF-8' nie je k dispozícii, používa predvolené nastavenie`  
` 2013-03-13 18:49:05.949: WARNING: spell.py: line 74: Kontrola pravopisu nie je nainštalovaná`  
` 2013-03-13 18:49:16.023: WARNING: gramplet.gpr.py: line 400: WARNING: GExiv2 module not loaded.  Funkcionalita metadát obrázkov nebude k dispozícii.`

Niekedy sa Gramps jednoducho nespustí a na obrazovke sa nič nezobrazí, alebo sa Gramps náhle ukončí, takže na obrazovke nič nevidíte. Vo všetkých týchto prípadoch možno budete musieť urobiť niečo špeciálne, aby ste videli všetky chyby.

### Linux

Program Gramps môžete spustiť z príkazového riadku, ako je popísané v poznámke [tu](wiki:Gramps_6.0_Wiki_Manual_-_Getting_started#Linux). V termináli sa potom zobrazia všetky diagnostické informácie.

### MS Windows

Program Gramps môžete spustiť z príkazového riadku, ako je popísané v poznámke [tu](wiki:Gramps_6.0_Wiki_Manual_-_Getting_started/sk#MS_Windows). Potom sa vám na termináli zobrazia všetky diagnostické informácie.

### Mac OS X

Spustenie programu Gramps prostredníctvom CLI v systéme Mac OS X je popísané [tu](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/sk#Mac_OS_X).

#### Konzolová aplikácia

Správy denníka z programu Gramps si môžete pozrieť aj pomocou aplikácie Apples . Aplikácia Console sa nachádza v priečinku Utilities vášho Macu, ktorý sa nachádza v priečinku Applications (Aplikácie). (Skratkou v posledných verziách Mac OS X je stlačenie klávesu Command a medzerníka na spustenie vyhľadávania Spotlight. Vo výslednom okne zadajte niekoľko prvých znakov slova "Console" a potom vyberte aplikáciu Console).

Napríklad jedna z prvých alfa verzií programu Gramps sa jednoducho nespustila a na obrazovke sa nič nezobrazilo. Otvorením aplikácie Console a zadaním Gramps do filtra v pravom hornom rohu sa však objavili niektoré diagnostické informácie. (V skutočnosti sme napísali "gramps\[", pretože tam boli aj iné správy, ktoré neboli relevantné, ale nevadilo by, keby boli zahrnuté aj tie). ![[_media/Console_output.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Výstup z konzoly]] {{-}} Kliknutím na shift na označenie všetkých relevantných správ a ich skopírovaním dostaneme:

` 01/03/2013 00:08:02 [0x0-0x88088].org.gramps-project.gramps[1867] 2939: Chyba: importer.py: riadok 51: Nepodarilo sa nájsť žiadny typelib pre Gtk `  
` 01/03/2013 00:08:05 [0x0-0x88088].org.gramps-project.gramps[1867] Gtk typelib nie je nainštalovaný. Nainštalujte Gnome Introspection a pygobject vo verzii 3.3.2 alebo novšej. `  
` 01/03/2013 00:08:05 [0x0-0x88088].org.gramps-project.gramps[1867] Gramps sa teraz ukončí. `

V tomto konkrétnom prípade to stačilo na to, aby vývojár objavil problém.

{{-}}

[Category:Sk:Documentation](wiki:Category:Sk:Documentation)
