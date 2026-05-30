---
title: Gramps 6.0 Wiki Manual - User Directory/sk
categories:
- Sk:Documentation
managed: false
source: wiki-scrape
wiki_revid: 111436
wiki_fetched_at: '2026-05-30T20:25:37Z'
lang: sk
---

{{#vardefine:chapter\|D}} {{#vardefine:figure\|0}} Táto príloha poskytuje odkaz na vyhľadanie umiestnenia **[používateľského adresára](wiki:Gramps_Glossary#user_directory) Gramps**. Priečinok/adresár je uložený na rôznych miestach z dôvodu požiadaviek rozdelenia Gramps pre rôzne operačné systémy alebo na špeciálne účely.

\_\_TOC\_\_

## [POSIX](wiki:Gramps_Glossary#posix) - štýly systému

Predvolené umiestnenie používateľského adresára pre Gramps v prostredí [POSIX](https://wikipedia.org/wiki/Posix)-style [1](https://wikipedia.org/wiki/Filesystem_Hierarchy_Standard) je:

/HOME/***<užívateľské meno>***/.gramps ktorý môže byť zadaný aj ako

Platí to pre [BSD](https://wikipedia.org/wiki/Bsd), [Linux](https://wikipedia.org/wiki/Linux), [Solaris](https://wikipedia.org/wiki/Solaris_(operating_system)), [Unix](https://wikipedia.org/wiki/Unix) a [Mac OS-X](https://wikipedia.org/wiki/Mac_OS_X) pri použití [Mac OS X Zostavenie zo zdroja](wiki:Build_from_source#Mac_OS_X).

Prípadne môžete využiť **\$HOME** [ekvivalent domovského adresára](http://www.linfo.org/home_directory.html), aby ste sa vyhli komplikáciám s aktívnymi používateľskými menami. Hoci Gramps interne nerozpozná ekvivalenty adresárov pre cesty, môžete ich použiť v rámci Linuxu na nájdenie používateľských súborov Gramps. Vyššie uvedená cesta k **používateľskému adresáru Gramps** sa zjednoduší buď na:

`$HOME/.gramps`

alebo

`~/.gramps`

Alebo ak používate MS Windows, použite nasledujúcu syntax

`$HOME\.gramps`

alebo

`~\.gramps`

### MacOS

![[_media/macos_200x200.png]] Na počítačoch Apple Mac sa názvy súborov začínajúce na "." vo Finderi nezobrazujú. Ak chcete zjednodušiť prístup do používateľského adresára Gramps, otvorte okno terminálu pomocou aplikácie Terminál a zadajte:

`V -s ~/.gramps ~/Documents/Gramps`

čo spôsobí, že Finder zobrazí adresár ako priečinok v priečinku Dokumenty s názvom "Gramps". (Názov "Gramps" môžete nahradiť ľubovoľným názvom, ale pred medzerami použite znak /.) Prípadne môžete jednoducho kliknúť na [](https://osxdaily.com/2011/08/31/go-to-folder-useful-mac-os-x-keyboard-shortcut/) vo Finderi, a napísať

`~/.gramps`

vo výslednom dialógovom okne macOS .

#### Balík aplikácií MacOS

Balík [Mac OS X:Application package](wiki:Mac_OS_X:Application_package) používa iné, štandardnejšie predvolené umiestnenie adresára systému MacOS:

`/Users/`***`<~username>`***`/Library/Application Support/gramps`

## MS Windows

![[_media/windows_180x160.png]]V systéme Microsoft Windows sú názvy súborov a priečinkov pre programy a používateľské údaje [skryté](https://wikipedia.org/wiki/Hidden_file_and_hidden_directory) v *Prieskumníkovi súborov*. Ak chcete uľahčiť prístup k používateľskému adresáru Gramps, postupujte podľa nasledujúcich rád spoločnosti Microsoft:

- [Zobrazenie skrytých súborov - Podpora Windows](https://support.microsoft.com/sk/help/14201/windows-show-hidden-files)

Predvolené umiestnenie **Adresára používateľa** pre všetky údaje používateľa Gramps v systéme Windows 7 (a novších) je

`C:\Users\`***`<~username>`***`\AppData\Roaming\gramps`

***\<~užívateľské meno\>*** vo vyššie uvedenej ceste k súboru je zástupný znak pre konkrétne meno používateľa zvolené pri prihlasovaní do systému Windows.

Alternatívne môžete využiť premennú prostredia **%AppData%** [2](https://wikipedia.org/wiki/Environment_variable#APPDATA), aby ste sa vyhli komplikáciám s aktívnymi používateľskými menami. Hoci Gramps interne nerozpozná premenné prostredia pre cesty, môžete ich použiť v rámci systému Windows na nájdenie používateľských súborov Gramps. Vyššie uvedená cesta k **používateľskému adresáru Gramps** je zjednodušená na:

`%AppData%\gramps`

<hr />

Podobne ako **Adresár používateľa**, aj umiestnenie programov/aplikácií je skryté pred prehliadaním pomocou Prieskumníka Windows.

Predvolené umiestnenie pre inštaláciu v systéme Windows 7 (a novších) je

`C:\Program Files\GrampsAIO64-5.X.X`

alebo

`C:\Program Files (x86)\GrampsAIO32-5.X.X`

{{-}}

## Pozrite tiež

- [Príkazový riadok](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/sk) Možnosť konfigurácie (config) s [premennými prostredia](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/sk#Premenné_prostredia)
- [Switching from Breadcrumbs to a location text box](https://winaero.com/how-to-enter-file-location-manually-in-gtk-3-opensave-dialog/) pomocou v dialógových oknách súborov GTK
- Vlákno diskusného fóra : [ako používať premenné prostredia v programe Gramps](https://gramps.discourse.group/t/how-to-set-the-base-path-from-media-relative-to-grampshome/481/2)

<!-- -->

- 

[U](wiki:Category:Sk:Documentation)
