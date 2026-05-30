---
title: Da:Gramps 6.0 brugsanvisning - Bruger søgesti
categories:
- Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 128169
wiki_fetched_at: '2026-05-30T16:35:46Z'
lang: da
---

{{#vardefine:chapter\|D}} {{#vardefine:figure\|0}}

Appendiks D: Bruger søgesti

Dette appendiks dokumenterer placeringen af ​​**Gramps [Søgesti](wiki:Gramps_Glossary/da#user_directory)**. Denne søgesti eller brugermappe er gemt på forskellige steder på grund af

- forskelle i operativsystemer
- dit brugernavn, dvs. den konto, du har logget ind på din computer med. Hvor *<brugernavn>* vises nedenfor, skal det erstattes af dit brugernavn.
- brugerkonfiguration

\_\_TOC\_\_

## Nye og gamle standardplaceringer og alternativ adfærd

I Gramps 6.0 ændredes standardplaceringen af ​​brugermappen på alle operativsystemer. Nye og gamle standardplaceringer af brugermapper for hvert operativsystem er angivet nedenfor. Hvis Gramps 6.0 og nyere registrerer en brugermappe på den gamle standardplacering, vil den bruge denne mappe og ikke oprette en på den nye standardplacering. Ellers vil den oprette en brugermappe på den nye standardplacering.

## [POSIX](wiki:Gramps_Glossary/da#posix) - stilsystemer

Standardplaceringen af ​​brugermappen for Gramps i et [POSIX](https://wikipedia.org/wiki/Posix)-stil [1](https://wikipedia.org/wiki/Filesystem_Hierarchy_Standard-miljø) blev ændret i Gramps 5.2

`/home/`*<brugernavn>*`/.local/share/gramps`

I Gramps 5.1 og tidligere var brugermappen i et POSIX-stilmiljø

`/home/`*<brugernavn>*`/.gramps`

Dette gælder for [BSD](https://wikipedia.org/wiki/Bsd), [Linux](https://wikipedia.org/wiki/Linux), [Solaris](https://wikipedia.org/wiki/Solaris_(operating_system)) og [Unix](https://wikipedia.org/wiki/Unix).

For kortheds skyld kan du bruge tilde-notation. Stien ovenfor kan forenkles til

`~`*<brugernavn>*`/.local/share/gramps`

eller, for at undgå at henvise til brugernavnet,

`~/.local/share/gramps`

Du kan også bruge miljøvariablen [**\$HOME**](http://www.linfo.org/home_directory.html). Selvom Gramps ikke genkender miljøvariabler i stier internt, kan du bruge dem i en terminal eller i scripts. Ved at bruge **\$HOME** kan stien ovenfor forenkles til

`$HOME/.local/share/gramps`

### Flatpak

Hvis du installerede Gramps via Flatpak-ruten, oprettes en ekstra brugermappe på en anden placering:

`$HOME/.var/app/org.gramps_project.Gramps/data/gramps`

Men hvis der også er en brugermappe fra tidligere versioner, der blev installeret direkte (ikke via Flatpak), vil Gramps fortsætte med at bruge den mappe til visse formål.

Så hvis du prøver at finde brugerfiler i en installation, hvor Flatpak har erstattet en anden type installation (f.eks. fra et Linux-arkiv), er det vigtigt at overveje begge placeringer.

## macOS

![[_media/macos_200x200.png]] Standardplaceringen af ​​brugermappen for Gramps på macOS, både [Mac OS X:Application-pakken](wiki:Mac_OS_X:Application-pakken) og [bygget fra kildekode](wiki:Build_from_source#Mac_OS_X), er (ligesom andre POSIX-systemer) (ændret i 5.2)

`/Brugere/`*<brugernavn>*`/.local/share/gramps`

I Gramps 5.1 og tidligere var brugermappen for Gramps [Mac OS X:Application-pakken](wiki:Mac_OS_X:Application-pakken)

`/Brugere/`*<brugernavn>*`/Library/Application Support/gramps`

men brugermappen for [Gramps bygget fra kildekode på macOS](wiki:Build_from_source#Mac_OS_X) var (ligesom andre POSIX-systemer)

`/Brugere/`*<brugernavn>*`/.gramps`

### Adgang til skjulte mapper i macOS

macOS-filnavne, inklusive mapper, der starter med "." (punktum), vises ikke i Finder. Få adgang til Gramps-brugermappen på en af ​​disse måder:

- I Finder skal du navigere til den mappe, der indeholder den skjulte fil eller mappe, du vil se, og skrive command-shift-. (punktum). Alle de skjulte filer og mapper i den mappe vises.
- Klik på [](https://osxdaily.com/2011/08/31/go-to-folder-useful-mac-os-x-keyboard-shortcut/) i Finder, og skriv

~/.gramps

  
i den resulterende macOS -dialogboks.

- Åbn et terminalvindue ved hjælp af Terminal-applikationen, og skriv ln -s ~/.gramps ~/Documents/Gramps

hvilket får Finder til at vise mappen som en mappe i din Dokumenter-mappe med navnet "Gramps". (Du kan erstatte "Gramps" med et hvilket som helst navn, men brug en \\ før mellemrum.)

## MS Windows

![[_media/windows_180x160.png|højre\|128px\|link=Download#MS_Windows]] Standardplaceringen i **Brugermappe** for alle Gramps-brugerdata på et Windows 7 (og nyere) system blev ændret i 5.2

`C:\Brugere\`*`%brugernavn%`*`\AppData\Local\gramps`

I Gramps 5.1 og tidligere var brugermappen for Windows 7 (og nyere)

`C:\Brugere\`*`%brugernavn%`*`\AppData\Roaming\gramps`

Alternativt kan du bruge **%LocalAppData%** [miljøvariablen](https://wikipedia.org/wiki/Environment_variable#APPDATA) for at undgå at henvise til brugernavnet. (Vi har valgt at bruge miljøvariablen brugernavn i dokumentationen til Windows i stedet for ***<brugernavn>***, der bruges til at dokumentere andre operativsystemer.) Selvom Gramps ikke genkender miljøvariabler til stier internt, kan du bruge dem i Windows til at finde Gramps brugerfiler. Stien ovenfor kan forenkles til:

`%LocalAppData%\gramps`

### Adgang til skjulte mapper i MS Windows

På Microsoft Windows er filnavne og mapper til programmer og brugerdata [hidden](https://wikipedia.org/wiki/Hidden_file_and_hidden_directory) i *Stifinder*. For at gøre adgang til Gramps brugermappe nemt, følg følgende råd fra Microsoft:

- [Vis skjulte filer - Windows Hjælp](https://support.microsoft.com/en-ca/help/14201/windows-show-hidden-files)

Ligesom **Brugermappen** er placeringen af ​​programmer/applikationer også skjult for browsing med Windows Stifinder.

Standardplaceringen for en installation på et Windows 10 (og nyere) system er

`C:\Program Files\GrampsAIO64-6.X.X`

{{-}}

## Se også

- [Kommandolinje](wiki:Da:Gramps_6.0_brugsanvisning_-_Kommandolinje) Konfigurationsmulighed (config) med [Miljøvariabler](wiki:Da:Gramps_6.0_brugsanvisning_-_Kommandolinje#Miljøvariabler)
- [Skift fra Breadcrumbs til en placeringstekstboks](https://winaero.com/how-to-enter-file-location-manually-in-gtk-3-opensave-dialog/) ved hjælp af i GTK-fildialoger
- Diskursforumtråde:
  - [hvordan man bruger miljøvariabler i Gramps](https://gramps.discourse.group/t/how-to-set-the-base-path-from-media-relative-to-grampshome/481/2)
  - [Brug af Python Eval-gramplet til at liste stien til plugins-mappen](https://gramps.discourse.group/t/manually-installing-addons/5696/5)
  - [Fejlfinding af Gramps-stier og miljøvariabler](https://gramps.discourse.group/t/troubleshooting-gramps-paths-and-environmental-variables/5692) med [Python Evaluation](wiki:Da:Gramps_6.0_brugsanvisning_-_Gramplets#Python_Evaluation) gramplet

[U](wiki:Category:Documentation)
