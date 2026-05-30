---
title: Da:Gramps 6.0 brugsanvisning - Navigation
categories:
- Documentation
- Pages using invalid self-closed HTML tags
- Stub
managed: false
source: wiki-scrape
wiki_revid: 128884
wiki_fetched_at: '2026-05-30T17:03:59Z'
lang: da
---

{{#vardefine:chapter\|10}} {{#vardefine:figure\|0}} Så længe en [slægtsbog](wiki:Genealogy_Glossary/da#family_tree) er åben, fokuserer Gramps på en enkelt person, der normalt kaldes den [aktive person](wiki:Gramps_Glossary/da#active_person). Dette giver dig mulighed for at se eller ændre data vedrørende denne person, hans eller hendes nærmeste familie osv. [Navigation i Slægtsbog](wiki:Da:Gramps_6.0_brugsanvisning_-_Navigation#Indstilling_af_den_aktive_person) (dvs. at flytte fra person til person) er faktisk ikke andet end at ændre den aktive person.

Dette afsnit beskriver mange alternative måder at navigere gennem slægtsbogen på ved hjælp af både de komplekse og de praktiske grænseflader, som Gramps tilbyder. Alle disse måder giver grundlæggende det samme resultat, men nogle navigationsmetoder vil være mere praktiske end andre... afhængigt af, hvad du laver i Gramps i øjeblikket.

\_\_TOC\_\_

## Brug af kategorien Personer

Den mest intuitive måde at vælge en aktiv person på er at bruge kategorien ![[_media/gramps-person.png]] [Personer](wiki:Da:Gramps_6.0_brugsanvisning_-_Kategorier#Personer). Når du er i kategorien Personer, skal du blot vælge navnet på den ønskede person fra listen ved at klikke på den pågældende listepost. Den person, du har valgt, bliver aktiv. Statuslinjen opdateres for at afspejle ændringen af den aktive person.

Se også

- [Redigering af oplysninger om personer](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Editing_information_about_people)

## Brug af kategorien Slægtsforhold

Når du er i kategorien ![[_media/gramps-relation.png]] [Slægtsforhold](wiki:Da:Gramps_6.0_brugsanvisning_-_Kategorier#Slægtsforhold), kan du nemt navigere mellem medlemmerne af den viste familie på følgende måde:

Klik på det understregede navn på den person, du vil gå til, og denne person bliver den nye aktive person i kategorien Slægtsforhold.

Navnet på den aktuelt aktive person er ikke understreget.

Derudover giver Gramps et omfattende sæt tastaturgenvejsmuligheder. Den detaljerede reference til tastaturgenveje findes i [Appendiks B: Reference til tastaturgenveje](wiki:Da:Gramps_6.0_brugsanvisning_-_Tastaturgenveje).

## Brug af kategorien Familier

Når du er i kategorien ![[_media/gramps-family.png]] [Familier](wiki:Da:Gramps_6.0_brugsanvisning_-_Kategorier#Familier), kan du nemt navigere mellem de viste familier.

Familier kan bruges til visuelt at sammenligne en række familier for mulige dubletter og manglende data. Ved at sortere på de forskellige kolonner kan man placere partnere med lignende navne tæt på hinanden, så man kan sammenligne ægtefæller. Du kan matche efter fornavn eller kælenavn ved midlertidigt at ændre indstillingen i afsnittet i dialogboksen under fanen . Et eksempel: Et navneformat på ›‹'Fornavn Efternavn Suffiks'›‹ vil få kolonnen til at sortere efter kælenavnet.

Sammenlægning af to familier vil ikke kun kombinere familiens sekundære objekter, men også samtidig sammenlægge de to fædre og de to mødre.

Filter-grampletten i familievisningen gør det muligt at søge efter personer i forskellige familieroller. Så du kan f.eks. søge efter familier med en far ved navn "John", en mor ved navn "Mary" og et barn ved navn "Thomas".

{{-}}

## Brug af Tavler kategorien

![[_media/TimelinePedigreeView-Addon-Existing-Person-ContextMenu-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Timeline Pedigree View - Third Party Addon for Charts Category - context menu example]]

Gramps er stærkt afhængig af formbaserede layouts af sammenkædede listeelementer. Disse antyder relationer mellem poster i din slægtsbog. Kategorien ![[_media/22x22-gramps-pedigree.png]] **Tavler** giver en alternativ, mere visuel måde at repræsentere disse relationer på. Positioner, former og farver på containere sammen med deres forbindelseslinjer og pile kan vise en ekstra dybde i sammenhængen med forskellige faktorer. Containere kan være enkle farvefyldte kasser, buer, bånd eller mange andre former.

Men kategorien [Tavler](wiki:Da:Gramps_6.0_brugsanvisning_-_Kategorier#Tavler) giver også en alternativ måde at navigere gennem slægtsbogen på. Fordelen ved denne metode er, at du kan se mere end én generation af slægtsbogen. Så du kan springe direkte fra et oldebarn til en oldefar uden at gå gennem de mellemliggende generationer.

Bemærk, at efter ændring af [Aktiv person](wiki:Gramps_Glossary/da#active_person) i kategorien Tavler, justeres diagramvisningen til den nyvalgte aktive person. I kategorien Tavler kan du nemt navigere mellem medlemmerne af det viste stamtræ på følgende måde:

For at gøre en vist person til den aktive person skal du venstreklikke på den tilhørende container. Højreklik på containeren for at åbne en kontekstmenu med indholdsspecifikke indstillinger.

Kontekstmenuen for en personcontainer kan indeholde ▶undermenuer med en liste over alle ægtefæller, søskende, børn og forældre til den pågældende person. Den første post i kontekstmenuen vil normalt være navnet på personen i den pågældende container. (Det kan også være en redigeringsmulighed.) Hvis du vælger personens navn, flyttes fokus på samme måde som ved at venstreklikke på containeren. Du kan også ændre fokus for den aktive person til en af ægtefællerne, søskende, børn eller forældre til en hvilken som helst af de viste personer.

Nogle diagramvisninger har en tydelig navigationssammenhæng. At bevæge sig gennem generationer svarer intuitivt til at bevæge sig til venstre, højre, opad eller nedad i diagrammet. Disse kan have brugerdefinerede retningsnavigationsknapper, der gør det muligt at navigere ved at klikke i stedet for at trække.

For eksempel kan du ændre fokus i [Anetavlen](wiki:Da:Gramps_6.0_brugsanvisning_-_Kategorier#Anetavle) til et barn (hvis der er et) af den aktuelle aktive person ved at klikke på (*Venstre pil*) til venstre for den aktive persons diagramfelt. Hvis der kun er ét barn, ændres fokus straks. Hvis den aktive person har mere end ét barn, udvides knappen (*Venstre pil*) med en pop op-menu med en liste over børnene, hvorfra der kan vælges. (For denne særlige (*Venstre pil*)-knap er pop op-menuen med børn sorteret efter forældrenes ægteskabsrækkefølge og undersorteret efter fødselsrækkefølge. Disse [rækkefølger kan ændres](wiki:Gramps_6.0_Wiki_Manual_-_FAQ#How_do_I_change_the_order_of_children.3F) globalt i kategorien Relationer.)

Ligesom containere kan knapper have alternative funktioner, som man får adgang til ved at højreklikke og vælge fra en kontekstuel pop op-menu.

Andre knapper er mindre åbenlyse hjælpemidler til at navigere til ikke personer, men funktioner i Gramps. Hvis vi igen bruger eksemplet [Anetavle](wiki:Da:Gramps_6.0_brugsanvisning_-_Kategorier#Anetavle) , vises der et tip med alle kendte grundlæggende detaljer om forholdet, når man ruller over linjerne mellem felterne, og ved at dobbeltklikke på disse linjer åbnes redigeringsprogrammet for den pågældende familie. Og hvis du dobbeltklikker på boksen Aktiv person, åbnes redigeringsprogrammet for den pågældende person. Det er værd at læse den detaljerede dokumentation om hver diagramvisning for at opdage disse skjulte genveje til favoritfunktioner.

De indbyggede visninger i [kategorien Tavler](wiki:Da:Gramps_6.0_brugsanvisning_-_Kategorier#Tavler) introduceres i referencen [Kategorier](wiki:Da:Gramps_6.0_brugsanvisning_-_Kategorier). Nogle er beskrevet mere detaljeret i artiklerne nederst i introduktionsafsnittet til visningen.

Samlingen af oversigter i kategorien Tavler kan udvides med tredjepartsudvidelser ved hjælp af Gramps' [Plugin Manager](wiki:Gramps_6.0_Wiki_Manual_-_Plugin_Manager)-funktion. De tilgængelige tredjeparts-tilføjelsesplugins kan findes under kolonnen **Visning** i tabellen [liste over tilføjelser](wiki:6.0_Addons#Addon_List). Vedligeholdelsen af nogle få tredjeparts-tilføjelsesvisninger er gennem årene blevet overtaget af Gramps' frivillige team. Disse blev 'indbygget' efter at være blevet godkendt og derefter inkluderet i de vigtigste Gramps-distributioner. Artikler om brugen af hver Addon View er linket til kolonnen **Plugin/Documentation**. Kvaliteten af dokumentationen varierer meget for disse artikler.

{{-}}

## Brug af Gramplets <span id="Using Gramplets"/>

![[_media/DashboardCategory-DashboardView-default-gramplets-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kontrolpanel kategorivisning - med standard Gramplets vist]]

I [sidepanelet og bundpanelet](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#The_split-screen_Sidebar_.26_Bottombar) kan du tilføje Gramplets for at udvide dine navigationsmuligheder ud over en enkelt generations afstand. Her er nogle eksempler:

- [Slægtninge](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Relatives)
- [Efterkommere](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Descendants)
- [Stamtavle](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Pedigree)
- [Fan Chart](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Fan_Chart)

Disse eksempler giver mulighed for at navigere i fokus på den aktive person ved hjælp af perspektivet på familieforhold... til nære slægtninge, efterkommere eller forfædre. Fremtidige Gramplets vil muligvis give mulighed for at navigere efter geografisk nærhed, [DNA-matchning](wiki:Addon:DNASegmentMapGramplet) eller andre forbindelser, som vi endnu ikke har overvejet.

De tekstbaserede Gramplets har ofte navne, der er [hotlinket til navigation](#Hotlink_Navigation), mens de grafiske Gramplets kan bruge [kontekstuelle menuer](#Contextual_Menu_Navigation).

{{-}}

## Indstilling af proband

En (og kun én) person i slægtsbogen kan udpeges som [proband](wiki:Gramps_Glossary/da#home_person) ad gangen. Når probanden er udpeget, kan fokus for [aktiv person](wiki:Gramps_Glossary/da#active_person) flyttes tilbage til denne person med et enkelt klik, uanset hvilken kategori der bruges i øjeblikket.

For at indstille probanden skal du først [navigere](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Setting_the_Active_Person) til den pågældende person ved hjælp af en hvilken som helst metode, du foretrækker. Vælg derefter kategorien Personer og vælg menuen . Når dette er gjort, kan du flytte til probanden fra hvor som helst i slægtsbogen ved blot at klikke på værktøjslinjens ![[_media/Gramps_Go-Home48x48_win.png]] ikon. Du kan også vælge menuen eller vælge fra en hvilken som helst kontekstmenu, der er tilgængelig ved højreklik, eller bruge tastaturgenvejen .

- [Indstilling af proband](wiki:Da:Gramps_6.0_brugsanvisning_-_Indstillinger#Indstilling_af_proband)
- I dialogboksen [Rediger person](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Edit_Person_dialog) kan du vælge fra kontekstmenuen.

## Indstilling af den aktive person

Den [aktive person](wiki:Gramps_Glossary/da#active_person) forventes at være det kontekstuelle fokus for handlinger, rapporter og redigeringer. Det er det valgte element i personvisningen eller øverst i relationsvisningen.

Fokus på den aktive person kan vælges direkte eller "navigeres" til indirekte. Metoder omfatter:

- at klikke på en person i person oversigten
- at vælge personen fra menuen [Bogmærker](#Bookmark_Navigation)
- [Brug af historikbaseret navigation](#Using_history-based_Navigation) ( og værktøjslinjeknapper og menuen )
- [hotlink-navigation](#Hotlink_Navigation)
- [Kontekstmenuer](#Contextual_Menu_Navigation)
- [Noter som navigationsgenveje](#Notes_as_Navigational_Shortcuts)

Der er en markering som visuel angivelse af den aktive person i Person-visningen. I Relationsvisningen vises den aktive person i et separat afsnit øverst. Alle andre personer, der vises nedenfor, har et direkte forhold (forælder, søskende, ægtefælle, barn) til den aktive person. Valgfrit kan [statuslinjen indstilles](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display) til at vise det fokuserede objekt for visningskategorien. (Den aktive person er i fokus for flere visningskategorier.)

### Hotlink navigation

Normalt vil et enkelt klik på navnet på en person med et hotlink vælge denne person og flytte det aktive persons kontekstuelle fokus.

![[_media/Relationships-category-view-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Visning af kategorien Relationer]]Hver persons navn i visningerne Person og Relation er et hotlink. Ændring af fokus for den aktive person i personvisningen ser ud til blot at ændre, hvilken post der er fremhævet. Men dette medfører også, at Gramplets-indholdet opdateres, og at visningerne for relationer, diagrammer og geografi fokuseres på den nye aktive person.

Hvis du vælger et andet hotlinket navn i kategorivisningen Relationer, medfører det en mindre subtil ændring. Perspektivet på, hvordan familiedataene vises, ændres i retning af det fokus. Deres detaljer flyttes til den øverste sektion, og deres nærmeste familie omarrangeres nedenfor.

{{-}}

### Kontekstmenu navigation

Hotlinkede navne i fanen Referencer og Noter (og i nogle Gramplets) åbner dog blot vinduet Personredigeringsprogrammet *uden* at flytte fokus fra den aktive person til den pågældende person. (Disse links fungerer, som om du havde klikket på knappen i stedet for et hotlinket navn.) Dette gør det nemmere at redigere personer omkring den aktive person uden at miste orienteringen ved at flytte fokus.

![[_media/QuickViewReport-EditPerson-context-menu-popup-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kontekstmenu i Person Editor]] Fokus på den aktive person kan indstilles i ved hjælp af kontekstmenuen (højreklik) i det tomme område i headerområdet. Indstillingen i den kontekstmenu ændrer fokus for aktiv person til den person, der redigeres.

{{-}}

### Historik-baseret navigation

![[_media/History-based-navigation-tools-Go-menu-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Eksempel på de historikbaserede navigationsværktøjer (»Gå«-menuen)]]

Gramps har også et kraftfuldt sæt historikbaserede navigationsværktøjer. Disse værktøjer ligner dem, der almindeligvis bruges i webbrowsere.

De omfatter og -elementer, der er tilgængelige fra -menuen, kontekstmenuer og tastaturgenveje (tilgængelige i kategorierne Personer, Familie og Slægtsbøger), samt og værktøjslinjeknapper. De indeholder også listen over de seneste valg, der er tilgængelige under -menuen, som giver dig mulighed for at springe direkte til et af de seneste valg. Endelig kan du ved at klikke på og værktøjslinjeknapperne går til det forrige eller næste objekt i historikken. {{-}}

### Bogmærke navigation

![[_media/Gramps_Go-Home48x48_win.png]] på værktøjslinjen er et specielt bogmærke. Den flytter fokus fra den aktive person til den person, der i øjeblikket er angivet som [Proband](wiki:Gramps_Glossary/da#home_person). Dette er så ofte nyttigt, at denne funktion har [tastaturgenvejen](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings) . {{-}} På samme måde som ved indstilling af Proband kan du bogmærke andre personer fra databasen for at forenkle yderligere navigation. For at bogmærke en person skal du først navigere til den pågældende person og derefter vælge menuen eller bruge [tastaturgenvejen](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings) . Hvis der ikke er valgt nogen person, får du advarslen . For at flytte til den pågældende person et andet sted i databasen skal du vælge menuen fra listen over bogmærkede navne. De andre kategorier har deres egen liste over bogmærker.

#### Organiser bogmærker

![[_media/OrganizeBookmarks-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Organiser bogmærker" dialog - eksempel]]

Du kan administrere dine bogmærker ved at vælge menuen eller [tastaturgenvej](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings) . Dette åbner dialogboksen med listen over bogmærker og kontrolelementerne til at ændre denne liste.

Brug knapperne og til at ændre rækkefølgen på listen. Brug knappen til at fjerne et bogmærke. Knappen bringer dig til denne side, og du lukker vinduet med knappen .

Listen over bogmærkede personer kan vælges via kategorien Personer, som forklaret ovenfor, men deles også med kategorierne Relationer og Tavler.

På samme måde opretholdes separate lister over bogmærker i hver af følgende kategorier: Familier, Begivenheder, Steder, Kilder, Kildehenvisninger, Arkiver, Medier og Noter.

{{-}}

### Noter som navigationsgenveje

![[_media/Note-showing-tooltip-for-link-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Noteredigeringsprogram - Linkning af tekst]] Der er separate bogmærkelister i flere kategorier. Men de er stadig bare simple lister. Lange lister med bogmærker bliver hurtigt uhåndterlige.

Vedvarende links kan oprettes i [Noter](wiki:Gramps_Glossary/da#note). Brug [Link Editor](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_2#Link_Editor) i Noter til at organisere navigationslinks til forskellige typer Gramps-poster efter dine egne organisationsmetoder. Når en note har linket tekst, kan den linkede post bruges som et bogmærke. I Note Gramplets, hvor redigering ikke er aktiv, åbner et klik på linket Objekteditoren for det pågældende link. (Det kræver en ekstra modifikator i Noted Editor: naviger til den pågældende post ved at holde -tasten nede og klikke på den linkede tekst.) En note kan bruges som et linket indeks til andre noter med forskellige sæt links.

Et eksempel på en sammenkædet note kan være en nekrolog, hvor alle personer, steder og endda begivenheder er sammenkædet. Dette gør det lettere at navigere til de indirekte relaterede (eller endda ikke-relaterede) kistebærere, begravelsesforrettere [officiators](wiki:Gramps_Glossary/da#officiator) eller deltagere.

En anden note kan være den transskriberede bibliografi for en anden genealogs offentliggjorte originale forskning. Når du samler digitale kopier af de oprindeligt citerede referencer, kan den sammenkædede bibliografi bruges som en tjekliste for kildeanskaffelse. Når den er fuldstændig sammenkædet, kan bibliografien bruges til at navigere gennem kilder for hver henvisning, mens du søger efter uunderstøttede konklusioner, unøjagtigheder eller udeladelser. {{-}}

## Find poster

### Browse til en post

For at finde en post i en af kategorilistevisningerne skal du først skifte til den relevante kategori, der indeholder listen over de ønskede poster: Personer, Kilder, Steder eller Medier. Rul derefter til den ønskede post. Fokus for den aktive post for kategorien ændres ved at vælge en post. Det er ikke nok at rulle gennem visningen for at ændre fokus for den aktive post.

Som standard sorteres listen efter den første kolonne i tabelopstillingen. For grupperede poster (Personer) eller hierarkiske træstrukturer (Steder) skal den første kolonne være kolonnen »Navn«. I Personer er grupperingen baseret på det foretrukne efternavn. I Steder er grupperingen baseret på rækkefølgen af omgivende steder.

Rækkefølgen og visningen (eller skjult) af kolonner kan konfigureres. En dialogboks vises, når du vælger menupunktet ; eller ved at klikke på knappen Konfigurer på værktøjslinjen; eller ved at bruge den aktive visning [konfigurer almindelige tastaturgenveje](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings).

Listen over poster i visningen kan reduceres ved at filtrere med [Søgefeltet](wiki:Da:Gramps_6.0_brugsanvisning_-_Hovedvindue#Søgelinje) eller [filter-grampletten](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Filter).

{{-}}

### Find en post

![[_media/Find-type-ahead-search-PeopleTreeView-list-example-detail-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Interaktivt søgefelt nederst i listevisningen – eksempel]]

![[_media/Find-type-ahead-search-PeopleTreeView-list-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Find type-ahead søgning på listen "Personer træstruktur" eksempel]]

Også kendt som en "interaktiv type-ahead søgning".

Vælg en linje i listen for at få fokus, og begynd derefter at indtaste oplysninger (indeholdt i dataene i den aktuelle sorteringskolonne) om en person eller titlen på en kilde, et sted eller et medieobjekt, som du forsøger at finde. Fokus flyttes til den første post, der matcher teksten i tekstfeltet i søgefunktionen.

Alternativt kan du, efter at have klikket et vilkårligt sted i det primære visningsområde for at få fokus, trykke på ( på macOS) [tastaturgenvej](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#All_List_Views_bindings) for at aktivere søgefeltet. Denne tastaturgenvej overses ofte, da det også er nok at begynde at skrive for både at åbne feltet og begynde at indtaste søgeordet.

Når du skriver, ruller den første matchende post i sorteringskolonnen på listen til midten af listen og vælges. Når du skriver flere tegn, bliver matchet mere præcist. Så længe tekstfeltet til søgefunktionen er synligt, kan du flytte til det næste match ved at trykke på pil ned-tasten , mens du kan flytte til det forrige match ved at trykke på pil op-tasten . Feltet forsvinder, når det har været inaktivt i 5 til 15 sekunder. Når søgefeltet ikke er aktivt, vender piletasterne tilbage til at flytte postudvælgelsen op og ned på listen.

Hvis du ændrer sorteringskolonnen (ved at klikke på overskriften), ændres den kolonne, der matches, også. Søgning i en anden sorteringskolonne fungerer bedst i visningstilstande med flad liste.

Visningstilstande for kategorierne Personer eller Steder med hierarkisk gruppering er lidt mindre responsive end visningen Flad liste, som allerede er sorteret alfabetisk. Den grupperede person er den mest komplekse funktionalitet. Som standard sorteres den efter gruppens navn og derefter efter kolonnen 'Navn' i 'Vis som' [Navneformat](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Display_Name_Editor) fra menuen Data i Indstillinger. Det vil være det foretrukne/primære navn i formatet "Efternavn, fornavn, suffiks", og "Efternavn" inkluderer præfikset og forbindelsesordene. Indstillingerne 'Gruppér som', 'Sorter som' og 'Vis som' kan dog bruges til at tilsidesætte rækkefølgen ved hjælp af '[Navneditoren](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data%3A_detailed_-_part_3#Name_Editor).' {{-}}

### Hop til efter Gramps ID

![[_media/Jump-to-by-Gramps-ID-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Hop til efter Gramps ID" - dialog - eksempel]]

Hvis du kender ID'et for den ønskede post i den aktuelt aktive kategori, kan funktionen **Hop til** være den mest effektive måde at navigere til den ønskede post.

Ved at trykke på eller på macOS [tastkombination](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings) vises dialogboksen , hvor du kan indtaste det specifikke [Gramps ID](wiki:Gramps_6.0_Wiki_Manual_-_Settings#ID_Formats) i den aktuelle visning, som du vil gøre aktiv.

søger kun efter en nøjagtig tekstmatch. Gramps ID kan enten genereres automatisk, når ID-feltet efterlades tomt, når der tilføjes en post, eller [indtastes manuelt](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#ID) som en overskrivning.

Det ligner Find, bortset fra at det ikke er interaktivt og KUN fungerer på Gramps ID-feltet i stedet for den kolonne, der aktuelt er valgt til sortering. Og kan ændre fokus for den aktive post i alle visningskategorier undtagen kategorierne Geografi og Kontrolpanel.

#### Se også

- [Funktionen »Gå til« Gramps ID](https://gramps.discourse.group/t/the-ctrl-j-jump-to-gramps-id-feature/3756) diskussion
- GEPS: [Forslag til design af vælger](wiki:GEPS_041:_New_Selector)

{{-}}

### Navigationshistorik

En historik over de senest aktive poster for den aktive kategori. De sidste ti er tilgængelige via menuen og dens [tastaturgenveje](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings). Du kan også rulle gennem fokushistorikken med venstre og højre piletaster.

{{-}}

## Brug af udklipsholderen

![[_media/Clipboard-dialog-example-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Udklipsholder - dialog - Visning af kontekstmenu (højreklik) eksempel]]

For et program som Gramps er meget vigtig, da den hjælper med at reducere gentagen dataindtastning.

Værktøjet giver en midlertidig notesblok til opbevaring af databaseoptegnelser, så de let kan genbruges under en enkelt Gramps-session, f.eks. indtil du afslutter Gramps. Kort sagt er dette en slags kopier-og-indsæt-funktionalitet, der er udvidet fra tekstobjekter til andre typer optegnelser, der bruges i Gramps. Udklipsholderen gør omfattende brug af [*drag and drop*](http://en.wikipedia.org/wiki/Drag-and-drop)-teknikken

For at åbne skal du enten vælge menuen eller klikke på værktøjslinjen ![[_media/Gramps_Clipboard48x48_win.png]] -knappen eller brug [tastaturgenvejen (genvejstast)](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#8) . {{-}}

understøtter adresser, attributter (både personlige og familiemæssige), begivenheder (både personlige og familiemæssige), navne, medieobjektreferencer, citater, URL'er og selvfølgelig tekstinformation fra noter og kommentarer. For at gemme enhver type af disse poster skal du blot trække den eksisterende post over på vinduet fra den tilsvarende redigeringsdialog. For at genbruge posten skal du trække den fra udklipsholderen til det tilsvarende sted i editoren, f.eks. fanen Adresse, fanen Attribut osv.

### Udklipsholder kontekstmenu

Hvis du vælger en post ved hjælp af kontekstmenuen (højreklik), vises følgende tre muligheder for hver posttype:

- 

- 

- 

{{-}}

Et eksempel  
Du finder en fødselsattest for en person. I denne attest nævnes også vidnerne. Og fødselsattesten bestemmer også en kilde, hvor oplysningerne blev gemt. Den bedste måde er at åbne udklipsholderen og trække den kilde, du vil arbejde med, derhen. Brug derefter træk og slip for at bruge den i nye elementer, du bruger.

Nu kan du færdiggøre oplysningerne på personredigeringsskærmen. Træk også disse oplysninger til udklipsholderen.

Nu tilføjer du to nye personer til vidnerne (forudsat at du ikke allerede har dem i din database). Træk og slip blot fødselsoplysningerne til vidnebegivenhedsskærmen. Du får derefter vist skærmen, hvor du kan ændre vidnets rolle til at vidne for denne fødselsbegivenhed. Du gør det samme med det andet vidne.

Dette sparer dig for en masse skrivefejl og mulige fejl.

## Brug af Tilføjelsesprogram-håndterer

![[_media/AddonManager-addons-listing-60.png|Højre\|thumb\|550px\|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} **Tilføjelseshåndtering** dialogboksen viser fanen]] Du kan få adgang til fra menuen eller vælge ikonet ![[_media/Gramps-addon.png]] på værktøjslinjen for at vise fanebladet i , der viser en liste over tilgængelige tredjeparts-tilføjelses-plugins baseret på de aktuelt valgte projekter på fanen .

Gramps bruger indbyggede moduler og tilføjelsesmoduler (også kendt som "add-on") plugin-moduler (også kendt som "[plug-in](https://wikipedia.org/wiki/Plug-in_(computing))") til at udvide kerneapplikationens funktioner. En af de primære fordele ved et plugin-framework er, at det tillader udvikling af en specifik funktion uden at skulle opdatere hele programmet. Tilføjelser bør ikke forveksles med at være af mindre nytte for basale brugere end kernefunktioner eller indbyggede plugins. "Tredjepart" betyder heller ikke, at et tilføjelsesmodul er af lavere kvalitet. De tilføjelser, der er offentliggjort til Gramps-Project GitHub-arkivet, er dog blevet kontrolleret og vil ikke i det skjulte ændre dine trædata.

[Addon Manager](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Addon_Manager) giver en måde at udforske, hvilke tilføjelser der vil forbedre dine personlige arbejdsgange. Og de indbyggede plugins [Plugin Manager](wiki:Gramps_6.0_Wiki_Manual_-_Plugin_Manager) (eller [Plugin Manager Enhanced](wiki:Addon:Plugin_Manager) tilføjelsesprogrammet) giver mulighed for at tilpasse Gramps for at fjerne rodet af funktioner, du ikke bruger. {{-}}

### Tilføjelseshåndtering

viser følgende tre faner:

- Fanen , der vises som standard, viser listen over tilgængelige tilføjelser.
- Fanen , hvor indstillinger kan ændres.
- Fanen , hvor eksterne eller lokale links til tilføjelseslageret kan tilføjes.

{{-}}

#### Tilføjelser

## Brug af Fortryd historik

{{-}}

## Hoved-menuer

![[_media/Menubar-MainMenuOverview-NoFamilyTree-Loaded-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menulinje - Oversigt over hovedmenuen - Ingen slægtsbog indlæst]]

Menulinjen viser de tilgængelige Gramps-menuindstillinger.

Der vil være meget forkortede menuer tilgængelige, før en slægtsbog er indlæst. De giver mulighed for at administrere slægtsbøger, afslutte Gramps, redigere programindstillinger, aktivere og deaktivere dele af den grafiske brugergrænseflade (GUI) og hjælpemuligheder.

{{-}} ![[_media/Menubar-MainMenuOverview-FamilyTree-Loaded-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menulinje - Oversigt over hovedmenuen - Slægtsbog indlæst]] Når en slægtsbog er indlæst, vil menuerne , , og altid have ensartede indstillinger. Men tilgængeligheden af indstillingerne i de andre menuer afhænger af konteksten. Indstillingerne i menuerne , og ændres afhængigt af den aktive kategori, og nogle menupunkter vises 'nedtonet', når de valgte objekter i visningen ikke tillader handlingen. {{-}} ![[_media/Menubar-MainMenuOverview-FamilyTree-Loaded-Active-Go-Windows-menus-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menulinje - Oversigt over hovedmenuen - Slægtsbog indlæst viser aktive »«, »« og »« menupunkter i brug]]

Menuerne og er specielt opbygget af navigationslinks inden for hver visning.

En -menu vises, når der er vinduer eller dialogbokse, der skal vises. {{-}} Hvis det er muligt, vises [tastaturgenveje](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings) i menulinjens menuer ved siden af funktionens navn.

Du kan også vælge hver af hovedmenuerne ved hjælp af [genvejstasterne](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Access_Key_Shortcuts) på -tasten plus den første til venstre for hver menuindstilling, f.eks. Hvis du trykker på  + -tasterne samtidigt, vises menuen . {{-}}

### Slægtsbøger

### Tilføj

### Redigér

### Vis

### Gå

### Bogmærker

### Rapporter

### Værktøjer

### Vinduer

### Hjælp

{{-}}

## Værktøjslinjen

![[_media/ToolbarIcon-OpenTheToolsDialog-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Tip til knappen Værktøjer i Kontrolpanel-kategoriens værktøjslinje]] [Værktøjslinjen](wiki:Gramps_Glossary/da#toolbar) er et vandret sæt af knapkontroller, der er placeret lige under menulinjen. Det giver dig adgang til de mest brugte funktioner i Gramps.

- Udvalget af knapper i værktøjslinjen er "kontekstuelt" -- de viste ikoner afhænger af, hvilken kategori [view](wiki:Gramps_Glossary/da#view) og [view mode](wiki:Gramps_Glossary/da#view_mode) der er aktiv.
- Tekstetiketter vises under værktøjslinjeknapperne.
- Hvis du holder musen over en værktøjslinjeknap, vises et tip til dens funktion.
- Værktøjslinjen kan skjules eller vises med valgmuligheden i menuen .

{{-}}

### Almindelige knapper i værktøjslinjen

#### ![[_media/Gramps.png]] Slægtsbøger

![[_media/FamilyTrees-ManageDatabases-icon-toolbar-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} Slægtsbøger (Administrer databaser) - ikon og værktøjstip på værktøjslinjen]] Knappen ![[_media/16x16-gramps-pedigree.png]] er den samme som menupunktet . Den resulterende dialogboks giver mulighed for at skifte mellem forskellige slægtsbøger (genealogiske databaser), {{-}}

#### <big>▼ </big>Vælg en nylig anvendt slægtsbog

![Fig. {{#var:chapter}}.{{#vardefineecho:figure\|{{#expr:{{#var:figure}}+1}}}} "Opret forbindelse til en nylig database" værktøjslinjeknap ](ConnectToARecentDatabase-icon-toolbar-60.png "Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Opret forbindelse til en nylig database" værktøjslinjeknap ") Denne <big>▼ </big>-knap åbner rullemenuen fra værktøjslinjen.

Se: [<big>▼ </big> Opret forbindelse til en nylig database](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#.E2.96.BC_Connect_to_a_recent_database) afsnit. {{-}}

#### ![[_media/Gramps_Go-Previous48x48_win.png]] Gå til det forrige objekt i historikken

Værktøjslinjeknappen ![[_media/Gramps_Go-Previous48x48_win.png]] er et alternativ til menupunktet eller til at trykke på *Tilbage* [tastaturtastatur](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings). Den bruger [historikbaseret navigation](#Using_history-based_Navigation) til at flytte fokus for det aktive objekt til det tidligere valgte objekt i denne kategori. {{-}}

#### ![[_media/Go-next48x48_win.png]] Gå til det næste objekt i historikken

Knappen ![[_media/Go-next48x48_win.png]] på værktøjslinjen er et alternativ til menupunktet eller til at trykke på *Frem* [tastaturets tastebinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings). Den bruger [historikbaseret navigation](#Using_history-based_Navigation) til at gendanne det aktive objektfokus, der blev flyttet med funktionen . {{-}}

Denne knap er kun tilgængelig efter brug af funktionen .

#### ![[_media/Gramps_Go-Home48x48_win.png]] Gå til proband

Knappen ![[_media/Gramps_Go-Home48x48_win.png]] i værktøjslinjen er et alternativ til menupunktet eller ved at trykke på *Hjem* [genvejstast](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings). Den flytter fokus på [Aktiv person](wiki:Gramps_Glossary/da#active_person) til at matche [Proband](wiki:Gramps_Glossary/da#home_person). {{-}}

Denne knap fungerer kun, hvis probanden er angivet.

#### ![[_media/Gramps_Add48x48_win.png]] Tilføj en ny...

Knappen på værktøjslinjen er et alternativ til menupunktet eller ved at trykke på *Tilføj* [tastaturtastatur](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings). Den åbner en tom objekteditor, der matcher objektkategorien i den aktuelle visning. {{-}}

#### ![[_media/Stock_edit.png]] Rediger den valgte...

Knappen er et alternativ til menupunktet eller ved at trykke på *Rediger* [tastaturtastatur](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings). Den åbner en objekteditor for hvert valgt objekt i kategorivisningen. {{-}}

#### ![[_media/Gramps_Remove48x48_win.png]] Slet det valgte...

Knappen på værktøjslinjen er et alternativ til menupunktet eller til at trykke på *Slet* [keyboard keybinding](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings). Den åbner en bekræftelsesdialogboks for sletning. {{-}}

Det element, der skal slettes, identificeres. Hvis der er valgt flere elementer, vises en dialogboks for hvert element. En afkrydsningsboks tilbyder muligheden "Brug dette svar til resten af ​​elementerne". {{-}}

#### ![[_media/Gramps_Merge48x48_win.png]] Sammenflet...

Denne værktøjslinjeknap er et alternativ til menupunktet . Den åbner [Sammenflet dialogboksen](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data%3A_detailed_-_part_3#Merging_records) for den pågældende kategori af poster.

Det er kun muligt at bruge knappen Sammenflet, hvis to (og kun 2) poster er valgt i visningen. {{-}}

#### ![[_media/gramps-tag.png]] Mærkat

Denne værktøjslinjeknap er et alternativ til undermenuen .

Knappen ![[_media/16x16-gramps-tag.png]] viser en pop op-menu med følgende [Mærkat](wiki:Gramps_Glossary/da#tag) muligheder:

- [Nyt mærkat...](wiki:Gramps_6.0_Wiki_Manual_-_Filters#New_Tag_dialog)
- [Organiser mærkater...](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Organize_Tags_Window)

Efterfulgt af en liste over aktuelt tilgængelige mærkater, der kan tilføjes eller fjernes på de valgte objekter i visningen.

[Mærkater benyttes til](wiki:Gramps_6.0_Wiki_Manual_-_Filters#Usage_of_tags) farvekodning af rækker i listevisninger, markørfarveprøver på nogle diagrammer og vedvarende markører til filtrering og organisering.

#### ![[_media/Gramps_Clipboard48x48_win.png]] Åbn dialogboksen Udklipsholder

![[_media/Clipboard-dialog-example-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Udklipsholder - dialogboks - viser (højreklik) kontekstmenu]] Denne værktøjslinjeknap er et alternativ til menupunktet eller til at trykke på *Udklipsholder* [genvejstast](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings). Den åbner dialogboksen [Udklipsholder](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Using_the_Clipboard) uden at tilføje det valgte objekt til dets samling. {{-}}

#### ![[_media/Gramps-config.png]] Konfigurer den aktive oversigt

Denne værktøjslinjeknap er et alternativ til at vælge menupunktet eller trykke på *Konfigurer aktiv visning* [genvejstast](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings).

De fleste kategorivisninger har ⚙ Konfigurerbare indstillinger. Ved at klikke på denne knap åbnes dialogboksen med kontroller til justering af disse indstillinger.

Denne indstilling åbner en dialogboks med valgmuligheder for visning af poster i visningen. (Dialogboksen vil også have faner for alle [Gramplets, som har konfigurerbare indstillinger](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#.E2.9A.99_Configurable_Options_2), der er aktive i visningen.) {{-}}

#### ![[_media/Gramps-reports.png]] Åbn rapportdialogen

![[_media/ReportSelection-dialog-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rapportvalg - dialog]] Dette er et permanent alternativ til at bruge undermenuerne .

Ved at præsentere de tilgængelige rapporter i en flydende dialogboks er der plads til at beskrive hver rapport, dens status og bidragende udviklerinformation. Dialogboksen giver også mulighed for at udforske rapporterne mere struktureret. {{-}}

#### ![[_media/Gramps-tools.png]] Åbn Værktøjer

![[_media/ToolSelection-dialog-example-with-debug-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Værktøjsvalg - dialog]] Dette er et permanent alternativ til at bruge undermenuerne .

Ved at præsentere de tilgængelige værktøjer i en flydende dialogboks er der plads til at beskrive hvert værktøj, dets status og bidragende udviklerinformation. Dialogboksen giver også mulighed for at udforske værktøjerne mere struktureret.

{{-}}

#### ![[_media/Gramps-addon.png]] Åbn Tilføjelsesprogrammer

![[_media/AddonManager-addons-listing-60.png|Right|thumb|550px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} <strong>Tilføjelsesprogrammer</strong> dialogeksempel]]

- Menuen  - Tilføjelseshåndteringen giver en måde at udforske, hvilke tilføjelser der vil forbedre dine personlige arbejdsgange.

{{-}}

#### ![[_media/Gramps-preferences.png]] Åbn Indstillinger

![[_media/EditPreferences-Data-tab-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Rediger -&gt; Indstillinger..." eksempel]]

- Menuen (macOS: ) - De fleste af de indstillinger, der påvirker hele Gramps-programmet, konfigureres i dialogboksen Indstillinger.

{{-}}

{{-}}

[Category:Documentation](wiki:Category:Documentation)
