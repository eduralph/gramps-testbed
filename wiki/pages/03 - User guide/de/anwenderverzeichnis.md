---
title: De:Gramps 6.0 Wiki Handbuch - Anwenderverzeichnis
categories:
- De:Dokumentation
managed: false
source: wiki-scrape
wiki_revid: 127054
wiki_fetched_at: '2026-05-30T16:15:37Z'
lang: de
---

{{#vardefine:chapter\|D}} {{#vardefine:figure\|0}} Dieser Anhang dokumentiert den Speicherort des Gramps- [Anwenderverzeichnises](wiki:De:Gramps_Glossar#user_directory). Dieses Verzeichnis bzw. dieser Ordner ist an verschiedenen Orten gespeichert, da

- Unterschiede in den Betriebssystemen
- Dein Benutzername, d.h. das Konto, mit dem du dich bei deinem Computer angemeldet hast. An den Stellen, an denen *<Benutzername>* angezeigt wird, ist dieser durch deinen Benutzernamen zu ersetzen.
- Benutzerkonfiguration

\_\_TOC\_\_

## Neue und alte Standardspeicherorte und Rückfallverhalten

In Gramps 6.0 hat sich auf allen Betriebssystemen der Standardspeicherort des Benutzerverzeichnisses geändert. Die neuen und alten Standardspeicherorte des Benutzerverzeichnisses für jedes Betriebssystem sind unten angegeben. Wenn Gramps 6.0 und später ein Benutzerverzeichnis am alten Standardspeicherort erkennt, wird dieses Verzeichnis verwendet und nicht am neuen Standardspeicherort angelegt. Andernfalls wird ein Benutzerverzeichnis am neuen Standardspeicherort erstellt.

## Systeme nach [POSIX](wiki:De:Gramps_Glossar#POSIX) - Stil

Der Standartort für das Anwenderverzeichnis von Gramps in einer [POSIX](http://de.wikipedia.org/wiki/Portable_Operating_System_Interface) [Umgebung](http://de.wikipedia.org/wiki/Filesystem_Hierarchy_Standard) wurde in Gramps 5.2 geändert

`/home/`*`<Benutzername>`*`/.local/share/gramps`  

In Gramps 5.1 und früher war das Anwenderverzeichnis in einer POSIX-ähnlichen Umgebung

`/home/`*`<Benutzername>`*`/.gramps`

Dies trifft zu auf [BSD](http://de.wikipedia.org/wiki/Berkeley_Software_Distribution), [Linux](https://de.wikipedia.org/wiki/Linux), [Solaris](https://de.wikipedia.org/wiki/Solaris_%28Betriebssystem%29) und [Unix](https://de.wikipedia.org/wiki/Unix).

Der Einfachheit halber kannst du die Tilde-Schreibweise verwenden. Der obige Pfad kann vereinfacht werden zu

`~`*`<Benutzername>`*`/.local/share/gramps`

oder um zu vermeiden, dass auf den Benutzername verwiesen wird,

` ~/.local/share/gramps`

Du kannst auch die [**\$HOME** Umgebungsvariable](http://www.linfo.org/home_directory.html) verwenden. Obwohl Gramps intern keine Umgebungsvariablen in Pfaden erkennt, kannst du sie in einem Terminal oder in Skripten verwenden. Mit **\$HOME** kann der obige Pfad vereinfacht werden zu

` $HOME/.local/share/gramps`

### Flatpak

Wenn du Gramps über die Flatpak-Route installiert hast, wird ein zusätzliches Benutzerverzeichnis an einem anderen Ort erstellt:

`$HOME/.var/app/org.gramps_project.Gramps/data/gramps`

Wenn es jedoch auch ein Benutzerverzeichnis von früheren Versionen gibt, die direkt (nicht über Flatpak) installiert wurden, wird Gramps dieses Verzeichnis für einige Zwecke weiterhin verwenden.

Wenn du also versuchst, Benutzerdateien in einer Installation zu finden, in der Flatpak eine andere Art der Installation ersetzt hat (z.B. aus einem Linux-Repository), ist es wichtig, beide Orte zu berücksichtigen.

## macOS

![[_media/macos_200x200.png]] Das Standard- Anwenderverzeichnis für Gramps unter macOS, sowohl für das Mac OS X: Anwendungspaket als auch für das aus dem Quellcode erstellte, ist (ähnlich wie bei anderen POSIX-Systemen) (geändert in 5.2)

`/Users/`*`<Benutzername>`*`/.local/share/gramps`

In Gramps 5.1 und früher war das Anwenderverzeichnis für das Gramps Mac OS X:Programmpaket

`/Users/`*`<Benutzername>`*`/Library/Application Support/gramps`

aber das Anwenderverzeichnis für Gramps [aus dem Quellcode unter macOS](wiki:Build_from_source#Mac_OS_X) war (ähnlich wie bei anderen POSIX-Systemen)

`/Users/`*`<Benutzername>`*`/.gramps`

### Zugriff auf versteckte Verzeichnisse unter macOS

macOS-Dateinamen, einschließlich Verzeichnisse, die mit "." (Punkt) beginnen, werden im Finder nicht angezeigt. Greif auf das Gramps-Benutzerverzeichnis auf eine der folgenden Arten zu:

- Navigiere im Finder zu dem Verzeichnis, das die versteckte Datei oder das Verzeichnis enthält, das du sehen willst, und tippe Befehl-Umschalt-. (Punkt) ein. Alle versteckten Dateien und Verzeichnisse in diesem Verzeichnis werden dann angezeigt.

<!-- -->

- Klicke im Finder auf \[<https://osxdaily.com/2011/08/31/go-to-folder-useful-mac-os-x-keyboard-shortcut/> und tippe

`~/.gramps`

  
in das daraufhin erscheinende macOS-Dialogfeld ein.

- Öffne ein Terminalfenster mit der Anwendung Terminal und gib ein

` ln -s ~/.gramps ~/Documents/Gramps`

Dies führt dazu, dass Finder das Verzeichnis als einen Ordner in deinem Dokumente-Ordner namens „Gramps“ anzeigt. (Du kannst "Gramps" durch jeden beliebigen Namen ersetzen, aber benutze ein \\ vor jedem Leerzeichen.)

## MS Windows

![[_media/windows_180x160.png]] Das Standard-**Anwenderverzeichnis** für alle Gramps-Benutzerdaten auf einem Windows 7 (und neuer) System ist wurde in 5.2 geändert

`C:\Users\`*`%Benutzername%`*`\AppData\Local\gramps`

In Gramps 5.1 und früher war das Benutzerverzeichnis für Windows 7 (und neuer)

`C:\Users\`*`%Benutzername%`*`\AppData\Roaming\gramps`

Alternativ kannst du die [Umgebungsvariable](https://wikipedia.org/wiki/Environment_variable#APPDATA) **%LocalAppData%** verwenden, um den Verweis auf den Benutzernamen zu vermeiden. (Wir haben uns dafür entschieden, in der Dokumentation für Windows die Umgebungsvariable Benutzername zu verwenden und nicht <Benutzername>, die für die Dokumentation anderer Betriebssysteme verwendet wird). Obwohl Gramps intern keine Umgebungsvariablen für Pfade erkennt, kannst du sie in Windows verwenden, um Gramps-Benutzerdateien zu finden. Der obige Pfad kann vereinfacht werden zu:

%LocalAppData%\gramps

### Zugriff auf versteckte Verzeichnisse in MS Windows

Unter Microsoft Windows sind die Dateinamen und Ordner für Programme und Benutzerdaten im Datei-Explorer [versteckt](https://de.wikipedia.org/wiki/Versteckte_Datei). Um den Zugriff auf das Gramps-Benutzerverzeichnis zu erleichtern, befolge die folgenden Ratschläge von Microsoft:

- [Anzeigen versteckter Dateien - Windows Hilfe](https://support.microsoft.com/de-de/windows/anzeigen-versteckter-dateien-0320fe58-0117-fd59-6851-9b7f9840fdb2)

Wie das "Anwenderverzeichnis" ist auch der Speicherort für Programme/Anwendungen für das Durchstöbern mit dem Windows Explorer nicht sichtbar.

Der Standartort für eine Gramps Installation unter Windows 10 und höher ist:

`C:\Program Files\GrampsAIOXX64-6.X.X`

{{-}}

## Siehe auch

- Option für die [Befehlszeilen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kommandozeilen_Referenz)-Konfiguration mit [Umgebungsvariablen](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Kommandozeilen_Referenz#Umgebungsvariablen)
- [Switching from Breadcrumbs to a location text box](https://winaero.com/how-to-enter-file-location-manually-in-gtk-3-opensave-dialog/) using in GTK file dialogs
- Diskursforenthreads :
  - [how to use Environment Variables in Gramps](https://gramps.discourse.group/t/how-to-set-the-base-path-from-media-relative-to-grampshome/481/2)
  - [Using Python Eval gramplet to list the Plugins folder path](https://gramps.discourse.group/t/manually-installing-addons/5696/5)
  - [Fehlersuche bei Gramps Pfaden und Umgebungsvariablen](https://gramps.discourse.group/t/troubleshooting-gramps-paths-and-environmental-variables/5692) mit dem [Python-Auswertung](wiki:De:Gramps_6.0_Wiki_Handbuch_-_Gramplets#Python-Auswertung) Gramplet

[A](wiki:Category:De:Dokumentation)
