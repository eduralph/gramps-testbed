---
title: Gramps 6.0 Wiki Manual - Manage Family Trees/pl
categories:
- Pl:Dokumentacja
- Stub
managed: false
source: wiki-scrape
wiki_revid: 120670
wiki_fetched_at: '2026-05-30T19:37:16Z'
lang: pl
---

W tej sekcji zapoznasz się ze dokładnym wyjaśnieniem codziennego użycia Grampsa. W rodziale tym uzyskasz szczegółowe wyjaśnienie jak możesz zarządzać swoimi drzewami rodzinnymi, jak również współdzielić swoje informacje z innymi genealogami.

## Tworzenie nowego drzewa rodzinnego

![[_media/FamilyTreesManager-window-example-60.png|Rys. 6.0. Tworzenie drzewa genealogicznego]]

W celu utworzenia nowego drzewa rodzinnego, wybierz **Drzewa rodzinne - \>Zarządzaj drzewami rodzinnymi** albo użyj przycisku z paska narzędziowego. Spowoduje to otwarcie okna menadżera Drzew genealogicznych.

Wybierz przycisk i Gramps doda nowe drzewo rodzinne do listy dostępnych drzew. Aby zmienić jego nazwę z domyślnego *Drzewo genealogiczne 1*, kliknij na nazwę i wprowadź nową nazwę zastępując starą.

Teraz użyj przycisku aby otworzyć nowe, puste drzewo rodzinne.

## Otwieranie drzewa rodzinnego

W celu otwarcia drzewa rodzinnego, wybierz **Drzewa rodzinne -\> Zarządzaj drzewami rodzinnymi** albo kliknij na przycisk na pasku narzędzi. pojawi się i zobaczysz listę wszystkich drzew rodzinnych, o których program wie. Ikona wyświetlona w kolumnie obok drzewa rodzinnego oznacza aktualnie otwarte drzew. Wybierz teraz drzewo, które chcesz otworzyć i kliknij na przycisku . Możesz także podwójnie kliknąć na wybranym drzewie, aby je otworzyć.

Aby otworzyć ostatnio otwierane drzewo, wybierz albo **Drzewa rodzinne -\>Otwórz poprzednie** albo przy pomocy strzałki w dół obok przycisku rozwiń listę i z niej wybierz szukane drzewo.

Jeśli nie posiadasz "praw zapisu" do danego drzewa rodzinnego, zostanie ono otwarte w trybie tylko do odczytu. W tym trybie dane mogą być przeglądane, ale żadne zmiany nie zostaną zapisane do drzewa. W tym trybie pasek menu Grampsa będzie zawierał nazwę drzewa wraz ze tekstem **(Read Only)**.

## Otwieranie bazy GEDCOM albo XML

Gramps pozwala Cię na otwarcie kilku typów baz danych z poziomu linii poleceń, a które nie zostały zapisane w natywnym formacie Grampsa. **TODO dodać link do strony wyjaśniającej jak.** Wśród tych formatów są XML oraz GEDCOM. Powinieneś jednak być świadomym, że bazy te są dosyć duże i możesz napotkać problemy wydajnościowe, a w przypadku błędu Twoje dane mogą zostać uszkodzone. Dlatego zalecane jest utworzenie nowej bazy danych Gramps i zaimportowanie do niej danych z pliku GEDCOM/XML.

## Usuwanie drzewa rodzinnego

Wybierz drzewo, które chcesz usunąć i kliknij na przycisk .

Ta operacja **całkowicie** usunie drzewo rodzinne, i nie będzie możliwe odzyskanie danych z niego. Nim to zrobisz, rozważ eksport danych z niego do formatu Gramps XML, i zachowanie ich jako pliku.

## Zmiana nazwy drzewa rodzinnego

Możesz zmienić nazwę drzewa rodzinnego (albo jego archiwum) poprzez wybranie konkretnego drzewa i kliknięcie na przycisk . Możesz także kliknąć na nazwie danego drzewa na liście drzew.

W obu przypadkach, wystarczy wpisać nową nazwę drzewa, aby zmiany odniosły skutek.

## Kopia zapasowa drzewa rodzinnego

- Najbezpieczniejszą metodą stworzenia kopii zapasowej jest wyeksportowanie do formatu **Gramps XML** (albo **Gramps Package** aby dołączyć elementy z galerii) i skopiowanie pliku wynikowego do bezpiecznego miejsca, najlepiej w innym budynku.

### Backup dialog

Simply select "Make Backup..." from the "Family Trees" menu item.

![[_media/MakeBackup-GrampsXML-Backup-example-60.png]]

You can either choose to include the media or not.

Note that this is just a regular XML export, except that no data is filtered out. You can import these as usual with any exported file.

You can also define the pattern for the backup filename by setting the *paths.quick-backup-filename* in the ~/.gramps/gramps34/gramps.ini key file like the following:

`[paths]`  
`quick-backup-filename='%(filename)s_%(year)d-%(month)02d-%(day)02d.%(extension)s'`

You can use any of the following keywords in the pattern: year, month, day, hour, minutes, seconds, filename, extension.

  

- Możesz też użyć opcji Archiwizacji aby zachowywać snapshoty swojego drzewa. Te snapohoty mogą być później użyte jako proste kopie zapasowe, co jest przydatne, jeśli chcesz coś przetestować i móc później wycofać zmiany. Jednakże, ta metoda nie powinna być używana do normalnych kopii zapasowych, jako że nie jest odporna na awarie dysku twardego albo inne awarie, które mogą dotknąć komputer.

<!-- -->

- *Dla zaawansowanych użytkowników:* Każda baza danych jest zapisywana w swoim własnym podkatalogu w katalogu ~/.gramps (Unix/Linux). Ręczna kopia zapasowa może być dokonana przez kopiowanie tego folderu. Zobacz także stronę man programu i szczegóły opcji GRAMPSHOME.

## Archiwizacja drzewa rodzinnego

Możesz w prosty sposób archiwizować i tworzyć znaczniki swojego drzewa rodzinnego za pomocą wbudowanej w Gramps [GNU Revision Control System](http://www.gnu.org/software/rcs/), w skrócie *RCS*. Aby skorzystać z tej możliwości, to narzędzie musi być zainstalowane na Twoim komputerze.

Aby zrobić archiwum, najpierw upewnij się, że drzewo, które chcesz zarchiwizować, jest otwarte. Następnie otwórz listę drzew rodzinnych i kliknij na przycisk . Archiwum będzie wyświetlone poniżej drzewa, dla którego zostało ono utworzone. Archiwa mogą mieć zmieniane nazwy albo być usuwane.

## Przywracanie drzewa rodzinnego

![[_media/ManageFamilyTrees-Archive-Selected-to-Extract-example-60.png|Fig. 6.0 Wybór wersji do przywrócenia]] Wystarczy podświetlić wersję archiwum, którą chcesz przywrócić, i wcisnąć przycisk . ![[_media/ManageFamilyTrees-Archive-Extracted-version-selected-example-60.png|Fig. 6.0 Przywrócona wersja]]

Gramps przetransferuje archiwum do nowego drzewa rodzinnego. Nazwa drzewa bazować będzie na oryginalnej nazwie drzewa i nazwie archiwum.

## Odblokowywanie drzewa rodzinnego

Kiedy Gramps otwiera drzewo rodzinne, to je blokuje zapobiegając w ten sposób przed otwarciem tego drzewa przez Ciebie albo inną osobę w tym samym czasie. Druga kopia Grampsa będzie w stanie otworzyć inne drzewo rodzinne, ale drzewo aktualnie otwarte oznaczone będzie ikoną blokady, wskazując w ten sposób że nie możesz tego drzewa otworzyć. Zamknięcie instancji Grampsa, która pierwsza otwarła to drzewo pozwoli Ci zwolnić to drzewo i otworzyć w innej kopii programu.

Jeśli jednak zechesz otworzyć to samo drzewo w dwóch instancjach programu Gramps, to jest duża szansa, że Twoje dane zostaną uszkodzone.

W przypadku awarii Grampsa, co jest mało prawdopodobne, drzewo rodzinne pozostanie zablokowane. Aby je odblokować. wskaż zablokowane drzewo i następnie kliknij przycisk , który wtedy będzie dostępny. Używaj tej opcji tylko wtedy, gdy jesteś pewien, że żadna inna kopia Grampsa nie używa tego drzewa.

## Naprawianie uszkodzonego drzewa rodzinnego

![[_media/FamilyTreesManager-Dialog-ShowingRedErrorStatusIcon-Sample-50.png|Fig. 6.0 Naprawianie drzewa rodzinnego]]

Jeśli twoje drzewo rodzinne zostanie uszkodzone, to w oknie zarządzania drzewami Gramps wyświetli ikonę błędu w kolumnie przy takim drzewie.

Można nakazać Grampsowi podjąć próbę naprawy takiej bazy poprzez wskazanie danego drzewa i następnie kliknięcie na przycisk .

Spowoduje to podjęcie próby przebudowy drzewa na podstawie plików kopii, które są tworzone automatycznie podczas zamykania programu.

## Zapisywanie zmian do drzewa rodzinnego

Gramps zapisuje zmiany automatycznie, zaraz po tym jak je zatwierdzisz. Oznacza to, że za każdym razem, jak klikniesz przycisk podczas pracy z programem, to twoje zmiany są logowane i zapisywane. Nie ma oddzielnego polecenia "Zapisz".

Możesz wycofać swoje zmiany przez wybranie opcji **Edycja-\>Cofnij**. Jeśli będziesz używał tej opcji parę razy z rzędu, to za każdym razem najbardziej najnowsza zmiana w historii zostanie wycofana. Aby cofnąć wiele poleceń za jednym razem, możesz skorzystać z dialogu dostępnego z menu .

Jeśli chcesz całkowicie porzucić zmiany, które wprowadziłeś od momentu otwarcia programu, wybierz opcję z menu **Drzewa rodzinne -\> Porzuć zmiany i wyjdź** . (To jest tak jak wyjście bez zapisywania zmian w innych programach).

Gdy chcesz zapisać kopię swojego drzewa rodzinnego pod inną nazwą, możesz to zrobić poprzez wyeksportowanie i zaimportowanie danych do nowego drzewa. Do tej akcji format *Gramps XML database* jest tutaj zalecanym.

## Importowanie danych

Importowanie pozwala Ci na przeniesienie danych z innego programu genealogicznego do bazy Grampsa. Aktualnie, Gramps może importować dane z następujących formatów:

GRAMPS V2.x database (rozszerzenie pliku .grdb)

GEDCOM (rozszerzenie pliku .ged)

Gramps XML (rozszerzenie pliku .gramps)

Pakiet Gramps (rozszerzenie pliku .gpkg)

GeneWeb (rozszerzenie pliku .gw)

Arkusz CSV Gramps (rozszerzenie pliku .csv)

Pro-Gen (rozszerzenie pliku .def)

Aby zaimportować dane, wybierz **Drzewa rodzinne -\>Import** . Pojawi się okno dialogowe **Importowanie bazy danych**, prosząc Cię o wskazanie pliku, który ma być importowany. Zauważ, że możesz tylko zaimportować dane do istniejącej bazy, tak że jeśli przenosisz dane z innego programu albo starszej wersji Grampsa to musisz najpierw stworzyć nową pustą bazę, do której będziesz importował dane i ją otworzyć.

Baza Gramps V2.x, Gramps XML, oraz pakiet Gramps są natywnymi formatami Gramps. Dlatego w tych przypadkach nie występuje możliwość utraty informacji podczas importu albo eksportu do tych formatów.

- Baza Gramps V2.x (grdb): Przed wersją 3.0, ten natywny format bazy był oparty na specyficznej formie bazy Berkeley (BSDDB) ze specjalną strukturą tabel. Jest to format binarny i zależny od architektury. Pomimo że był szybki i wydajny, nie był on przenośnym formatem pomiędzy komputerami o różnych architekturach (np. i386 vs. alpha).

<!-- -->

- Gramps XML: Plik Gramps XML jest domyślnym formatem dla starszych wersji (przed 2.x) Gramps. W przeciwieństwie do formatu grdb, jest on niezależny od architektury oraz zrozumiały dla ludzi. Baza może także posiadać odniesienia do obiektów medialnych nie będących lokalnie, dlatego nie jest on całkowicie przenośnym. Baza Gramps XML jest tworzona podczas eksportu ( **Drzewa Rodzinne -\>Eksport...** ) do tego formatu.

<!-- -->

- Pakiet Gramps: Pakiet Gramps jest skompresowanym archiwum zawierającym plik Gramps XML oraz wszystkie obiekty medialne (obrazy, pliki dźwiękowe, itp.) do których baza się odnosi. Ponieważ zawiera ona wszystkie obiekty medialne, ten format jest całkowicie przenośnym. Pakiet Gramps jest tworzony przez eksport danych ( **Drzewa rodzinne -\>Eksport...** ) do tego formatu.

Jeśli importujesz dane z innej bazy Gramps albo pliku Gramps XML, to zobaczysz pasek postępu w głównym oknie Grampsa.

Format skoroszytu Gramps CSV pozwala na import i eksport części danych z Grampsa w prostej arkuszowej formie. Zobacz [Importowanie i eksportowanie CSV](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees:_CSV_Import_and_Export/pl) po więcej informacji.

## Exporting Data

## Konwersja bazy z 2.2 do wersji 3

Są dwa sposoby przeniesienia danych z wersji 2.2 do wersji 3; poprzez bezpośredni import pliku grdb z wersji 2.2 albo poprzez eksport do formatu XML i następnie jego import. Z powodu złożoności, w jaki sposób wersja 2.2 przechowywała dane, eksport do XML jest zazwyczaj najlepszą i najmniej problematyczną drogą na przeniesienie Twoich danych do wersji 3.

- Import pliku grdb 2.2 : W bazie Gramps 2.2, Twoje dane były przechowywane w pliku grdb wraz z jednym lub większą ilością plików logów, które znajdowały się w podkatalogach w katalogu .gramps/env. Aby zaimportować dane bezpośrednio z 2.2 do Gramps 3, powinieneś utworzyć nową bazę danych i wybrać opcję importu bazy Gramps 2.2. Wymaga to upewnienia się, że uruchamiasz Gramps 3 jako ten sam użytkownik co uruchamiałeś Gramps 2.2 aby mieć dostęp do plików logów przechowywanych w katalogu .gramps/env, które są częścią Twej bazy. Jeśli uruchomiłeś Gramps 3 jako inny użytkownik albo na innym komputerze, będziesz musiał zapewnić, że wymagane pliki i katalog .gramps/env zawiera wymagane pliki. Jeśli widzisz błąd mówiący, że "/tmp/tmpDkI5pO could not be opened" albo coś podobnego, to oznacza, że Gramps 3 nie widzi wszystkich plików składających się na twoją bazę danych.

<!-- -->

- Gramps XML: Przy tym podejściu musisz najpierw uruchomić Gramps 2.2 i wyeksportować swoje dane do pliku Gramps XML. Ten plik XML jest skompresowany i posiada rozszerzenie .gramps. Jest on przenośny i nie zależy od innych plików, przez co może być przeniesiony na komputer, gdzie masz zainstalowaną wersję Gramps 3. Następnie musisz uruchomić Gramps 3 i po utworzeniu pustej bazy zaimportować ten plik za pomocą menadżera drzew rodzinnych.

[Category:Pl:Dokumentacja](wiki:Category:Pl:Dokumentacja)
