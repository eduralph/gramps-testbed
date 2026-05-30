---
title: Ru:Gramps 6.0 Вики Руководство - Папка Gramps
categories:
- Ru:Documentation
managed: false
source: wiki-scrape
wiki_revid: 111143
wiki_fetched_at: '2026-05-30T20:00:41Z'
lang: ru
---

{{#vardefine:chapter\|D}} {{#vardefine:figure\|0}} В этом разделе описано, где Gramps создает каталог с Вашими данными в различных операционных системах.

\_\_TOC\_\_

## [POSIX](wiki:Gramps_Glossary#posix) - системы

По умолчанию путь к пользовательскому каталогу Gramps в [POSIX](http://ru.wikipedia.org/wiki/POSIX) [окружении](http://ru.wikipedia.org/wiki/FHS):

`/home/<~username>/.gramps`

Такое расположение справедливо для [BSD](http://ru.wikipedia.org/wiki/BSD), [Linux](http://ru.wikipedia.org/wiki/Linux), [Solaris](http://ru.wikipedia.org/wiki/Solaris), [Unix](http://ru.wikipedia.org/wiki/UNIX) и [OS-X](http://ru.wikipedia.org/wiki/Mac_OS_X), если [собирать из исходных кодов](wiki:Installation#Mac_OS_X:Build_from_source).

### Mac OS X

![[_media/macos_200x200.png]] На платформе Mac файлы, которые начинаются с "." не видны в Finder. Чтобы сделать доступ к каталогу Gramps проще, откройте окно терминала Finder-Applications-Utilities-Terminal и наберите там

`ln -s .gramps gramps_user_directory`

что позволит Finder показать содержимое. Или нажмите Go -\> 'Go to Folder...' в Finder и наберите

`~/.gramps`

в окне диалога Go to Folder.

По умолчанию для [Mac OS X:Application package](wiki:Mac_OS_X:Application_package) пакет расположен в

`/Users/`<username>`/Library/Application Support/gramps`

## MS Windows

![[_media/windows_180x160.png]] По умолчанию каталог с программой и пользовательскими данными не отображаются в *Проводнике*. Для доступа к каталогу пользователя Gramps следуйте совету Microsoft:

- [Показать скрытые файлы - Справка Windows](https://support.microsoft.com/en-ca/help/14201/windows-show-hidden-files)

По умолчанию путь установки Gramps в Windows 7 и выше

`C:\Program Files\GrampsAIO64-5.X.X`

или

`C:\Program Files (x86)\GrampsAIO32-5.X.X`

Расположение пользовательских данных в Windows 7 и выше

`C:\Users\<~username>\AppData\Roaming\gramps`

[Category:Ru:Documentation](wiki:Category:Ru:Documentation)
