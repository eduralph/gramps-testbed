---
title: 'Da:Gramps 6.0 brugsanvisning - Indtaste og redigere data: kort'
categories:
- Documentation
managed: false
source: wiki-scrape
wiki_revid: 128161
wiki_fetched_at: '2026-05-30T17:00:41Z'
lang: da
---

{{#vardefine:kapitel\|8}} {{#vardefine:figure\|0}} Dette Kapitel giver den grundlæggende viden, der er nødvendig for at begynde at indtaste dine genealogiske oplysninger i Gramps. Det vil forklare, hvordan du indtaster personer i din slægtsbog (også kaldet en database), og hvordan du specificerer deres familieforhold. (En mere detaljeret forklaring følger i næste kapitel: [Da:Gramps 6.0 brugsanvisning - Indtaste og redigere data: detaljeret](wiki:Da:Gramps_6.0_brugsanvisning_-_Indtaste_og_redigere_data:_detaljeret).)

Lad os først identificere de typer oplysninger, du kan indtaste i din slægtsbog ved hjælp af Gramps. Disse omfatter:

- Personlige oplysninger om en person (navne, adresser, fødsels- og dødsdatoer osv.)
- Oplysninger om en persons forhold (ægteskaber, skilsmisser, registrerede partnerskaber osv.)
- Oplysninger om en persons forældre og børn
- Kilder, der dokumenterer din forskning

Lad os nu undersøge, hvordan du kan indtaste og redigere disse forskellige typer genealogiske oplysninger.

## Sådan tilføjer eller redigerer du en person

Menuen [](wiki:Da:Gramps_6.0_brugsanvisning_-_Navigation#Tilføj) for hver [Kategori](wiki:Gramps_Glossary/da#category) [View](wiki:Gramps_Glossary/da#view) inkluderer muligheden for at tilføje en [Person](wiki:Gramps_Glossary/da#person). En [tastaturgenvej](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#Common_keybindings) til at tilføje en person understøttes også i alle kategorivisninger.

Der er flere måder at tilføje en ny person til din slægtsbog. Mange har en implicit kontekst, der sparer et trin i at indsætte personen i et træ. (f.eks. tilføjelse af en person fra Familie-konteksten i Slægtsforhold- eller Tavlevisningerne indsætter automatisk den nye person i Familien. Du behøver ikke at oprette personen som en separat handling og derefter finde og trække den nye person ind i den pågældende Familie.) Vi vil gennemgå nogle af de forskellige arbejdsgange, efterhånden som vi fortsætter. {{-}}

### Tilføj en ny person

![[_media/PeopleTreeView-GroupedPeople-example-with-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Personkategori - Trævisning - Grupperede personer]]

Den mest oplagte måde at indsætte en person i din slægtsbog på er at tilføje dem fra -visningen. Mens du er i -visningen, skal du klikke på værktøjslinjens -knap.

{{-}} ![[_media/Edit-person-window-new-person-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rediger person - vindue - Ny tom editor]]

Dialogboksen vises, og du kan indtaste alle data, du kender om denne person, og derefter vælge for at gemme den nye person.

{{-}}

### Rediger en eksisterende person

![[_media/Edit-person-window-existing-person-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rediger person - vindue - Eksempel på eksisterende person]]

For at redigere oplysninger om en person, der allerede findes i slægtsbogen, skal du vælge personen fra -visningen og klikke på knappen Rediger...}} i værktøjslinjen.

Personer kan også tilføjes til slægtsbogen i Vis, dialogboksen og andre steder, hvor det giver mening.

{{-}}

## Sådan specificerer du et slægtsforhold

Der er to primære måder at specificere slægtsforhold mellem personer på:

\(1\) Efter familie:

  
<li>

ved hjælp af visningen . Visningen bruges normalt til at opbygge flere forhold omkring en enkelt person.

</li>

<li>

ved hjælp af dialogboksen fra visningen . bruges normalt til at opbygge alle inden for en enkelt familie ad gangen.

</li>

</ol>

\(2\) Ved tilknytning:

  
<li>

ved hjælp af fanen i dialogboksen . Tilføjelse af en person og angivelse af typen af ​​tilknytning (fadder, kollega, kistebærer, barndomsven osv.) identificerer et interpersonelt forhold.

</li>

<li>

ved hjælp af funktionen i dialogboksen . Krydsreferencer til en person via et personlink i en note vil knytte den linkede person til den person, hvor noten er vedhæftet.

</li>

<li>

Personer, der deler en reference (kilder, noter, placeret på samme steder osv.), har en indirekte eller proximal relation.

</li>

</ol>

{{-}}

### Angivelse af en relation ved hjælp af slægtsforholdvisningen

![[_media/Relationships-category-view-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Slægtsforholdvisning]]

For at angive en ny relation til [Aktiv person](wiki:Gramps_Glossary/da#active_person), skal du skifte til -visningen, og du vil se denne person angivet som den "aktive person". Ved siden af ​​etiketten er der en -knap (typisk repræsenteret af et -tegn).

{{-}}

![[_media/FamilyEditor-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Redigering af en familie]]

Hvis du klikker på knappen , vises dialogboksen med den aktive person angivet som enten far eller mor.

{{-}}

![[_media/SelectMother-selector-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vælg Mor - dialog]]

Nu et spørgsmål?  
Findes den person, der skal danne relationen til den Aktive Person, allerede i slægtsbogen? Hvis ja, skal du klikke på knappen for den anden person. Du vil derefter kunne gennemse listen over personer i slægtsbogen for at vælge den, du ønsker. Hvis ikke, skal du klikke på knappen ; dette giver dig mulighed for at tilføje en ny person til stamtræet og angive den relation, denne person har til den Aktive Person.

For at redigere et eksisterende forhold fra visningen skal du klikke på knappen ved siden af ​​den tilsvarende familiepost. Hvis der er mere end ét forhold på listen, kan du vælge den ønskede ægtefælle eller partner ved at klikke på den tilsvarende -knap ud for forholdet.

{{-}}

### Angivelse af et slægtsforhold ved hjælp af listevisningen Familier

For at angive et nyt forhold i visningen skal du klikke på knappen på værktøjslinjen, hvorefter en tom dialogboks åbnes. På dette tidspunkt kan du tilføje personer til familien.

{{-}}

## Sådan angiver du forældre

Du kan angive den aktive persons forældre i visningen (se  - selector). Der kræves lidt forsigtighed for at forhindre oprettelsen af ​​. Hvis du ønsker at tilføje den aktive person til en allerede eksisterende familie, skal du klikke på knappen . Hvis familien inklusive forældrene ikke allerede findes, skal du klikke på knappen .

{{-}} ![[_media/SelectFamily-SelectorDialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Vælg familie - eksempel på vælgerdialog]]

Hvis du klikker på knappen , vises dialogboksen . Dette giver dig mulighed for at vælge den eksisterende familie, og derefter tilføjes den aktive person som et barn til familien.

Hvis du klikker på knappen , vises en ny dialogboks med den aktive person angivet som et barn af den nye familie. Du kan tilføje forældrene til familien enten ved at tilføje nye personer som forældre eller ved at vælge eksisterende personer som forældre.

{{-}}

## Sådan angiver du børn

Tilføjelse af børn til en relation udføres via en lignende procedure. Fra visningen eller visningen skal du vælge den eksisterende familie eller oprette en ny familie. Børn kan tilføjes ved at vælge knappen eller knappen til højre for underordnede listen.

Hvis du klikker på knappen , vises dialogboksen , hvor du kan indtaste en ny person. Hvis du klikker på knappen , kan du vælge en eksisterende person fra en liste. Som standard tilføjes barnet med relationstypen **fødsel** til begge forældre.

{{-}} ![[_media/ChildReferenceEditor-dialog-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} &quot;Referenceeditor for underordnede&quot;]]

Hvis du ønsker at ændre forholdet mellem forælder og underordnede fra standardindstillingen **Fødsel**, skal du i dialogboksen vælge underordnet og klikke på . Dette vil vise dialogboksen .

{{-}} Hvis du ønsker at ændre rækkefølgen af ​​børnene i familien, skal du bruge pilene eller funktionen [*træk og slip*](http://en.wikipedia.org/wiki/Drag_and_drop) på fanen s . {{-}} Du kan også angive forældrene til en person i visningen . Hvis familien allerede findes, skal du klikke på knappen i værktøjslinjen og tilføje personen som et barn, når dialogboksen vises. Hvis familien ikke allerede findes, skal du klikke på knappen for at oprette en ny familie og tilføje de relevante forældre og børn.

{{-}}

## Tilføjelse af fotos og andre medieobjekter

Forskellige typer medieobjekter (herunder fotos, dokumenter, lydfiler og videofiler) kan vedhæftes som [sekundære objekter](wiki:Gramps_Glossary/da#secondary_object). Du kan også tilføje billeder, der muligvis ikke er begrænset til en enkelt person eller begivenhed. (For eksempel gruppefotos fra en familiesammenkomst)

Gramps understøtter forskellige typer medieobjekter, herunder fotos, dokumenter, lydfiler og videofiler. Den mest almindelige metode til at tilføje medier er via fanen i et primært objekts editor (såsom Personer, Begivenheder, Familier, Steder, Citater, Kilder eller Arkiver).

Før du tilføjer ***nye*** medieobjekter, bør du dobbelttjekke i fanen i Indstillinger. Bekræft, mens du tjekker, at du har brugt kontekstmenuen , så der er en knap til den 'Basismediesti' i [Filvælger](wiki:Gramps_6.0_Wiki_Manual_-_Settings#File_Chooser).

Tilføjelse af valgfri information kan hjælpe med at kategorisere dine medier for lettere søgning senere. Datoer, titler og [Tags](wiki:Gramps_Glossary/da#tag) kan tilføjes til et medieobjekt.

1.  Åbn objekteditoren for det primære objekt
2.  Vælg fanen Galleri.
3.  For at tilføje et nyt medieobjekt skal du klikke på knappen .
    - Naviger til filen i Filvælgeren, og vælg, om du vil bruge indstillingen "Konverter til en relativ sti".
    - klik på knappen .
4.  For at [dele](wiki:Gramps_Glossary/da#sharing) et eksisterende medieobjekt skal du klikke på knappen .
    - Vælg et eksisterende medieobjekt fra dialogboksen [Vælg medieobjekt](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Select_Media_Object_selector).
    - dobbeltklik på objektet, eller klik på knappen .
5.  Tilføj valgfrie oplysninger
    - Hvis medieobjektet er et billede, skal du trække et rektangel i forhåndsvisningen for at forfine miniatureindholdet
6.  Udvid afsnittet , og tilføj derefter nyttige detaljer
    - Brugervenlig **Titel**
    - **Dato**: Medieobjektet blev oprettet, eller som medieobjektet repræsenterer
    - Vælg Tags
7.  Klik på knappen .

Når du tilføjer et par medieobjekter, kan det være mere effektivt at bruge kategorien Vis og tilføje dem. Brug derefter knappen til at linke til forskellige primære objekter efter behov.

### Brug af udklipsholderen

![[_media/Clipboard-dialog-example-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Udklipsholder - dialog - Viser kontekstmenu (højreklik) eksempel]] Hvis du tilføjer mere end et par objekter, bør du overveje at bruge funktionen i [<strong>Media Manager</strong>](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Media_Manager) fra menuen . kategorien for at vise Sidst ændret, sorter til de nye elementer og kopier dem til [Udklipsbord](wiki:Gramps_Glossary/da#clipboard).

Udklipsbordet giver mulighed for hurtig træk-og-slip til Objekteditorens gallerier. Når du tilføjer et medieobjekt til flere gallerier, kan det dog være mere effektivt at dele "Mediereference" end at have en separat kopi af medieobjektreferencen. Når du har slettet et medieobjekt i et galleri, skal du kopiere medieobjektet i galleriet tilbage til udklipsbordet. Dette opretter en "Mediereference" for det pågældende objekt. Fjern derefter det originale medieobjekt fra udklipsbordet.

Brug ensartede navngivningskonventioner for dine mediefiler, og tilføj detaljerede beskrivelser for at gøre søgningen nemmere. Husk regelmæssigt at sikkerhedskopiere dine mediefiler sammen med din Gramps-database.

{{-}} ![[_media/PersonView-PeopleListView-example-with-context-menu-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kategori &quot;Personer&quot; - &quot;Personvisning&quot; - &quot;Personer&quot; (Liste) Visning, der viser kontekstmenu]]

Hvis du vil tilføje et billede til en enkelt person, skal du skifte til visningen (se fig. {{#var:chapter}}.{{#expr:{{#var:figure}}}}), vælge en person og derefter klikke på ikonet på værktøjslinjen. {{-}}

![[_media/Edit-person-window-existing-person-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rediger person]]

Dette vil åbne dialogboksen (se fig. {{#var:chapter}}.{{#expr:{{#var:figure}}}}). Vælg derefter fanen , og klik på knappen for at åbne dialogboksen . Skriv et filnavn, eller søg for at finde den ønskede billedfil, og angiv derefter en titel til billedet. Fortsæt med at tilføje billeder, indtil du er færdig.

{{-}} ![[_media/Families-category-list-view-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Visning af kategorien Familier]]

For at tilføje billeder relateret til et forhold (f.eks. et ægteskab), skal du skifte til visningen (se fig. {{#var:chapter}}.{{#expr:{{#var:figure}}}}) og dobbeltklikke på feltet Ægtefælle. Dette åbner dialogboksen . Vælg fanen , og klik på knappen for at tilføje et billede. {{-}}

![[_media/SourcesCategory-Sources-ListView-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Kildevisning]]

For at tilføje billeder relateret til en kilde eller et sted, skal du først skifte til -visningen (se fig. {{#var:chapter}}.{{#expr:{{#var:figure}}}}) eller -visningen (se fig. {{#var:chapter}}.{{#expr:{{#var:figure}}+1}}). Vælg den ønskede kilde eller det ønskede sted, og dobbeltklik derefter på det, eller klik på ikonet på værktøjslinjen. Vælg fanen , og klik på knappen for at tilføje et billede.

![[_media/PlacesCategory-PlaceView-list-example-60.png|højre|450px|Fig. {{#var:kapitel}}.{{#vardefineecho:figur|{{#udtryk:{{#var:figur}}+1}}}} Stedsvisning]]

{{-}}

![[_media/MediaCategory-Media-ListView-example-60.png|højre|450px|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Medievisning]]

Endelig, for at tilføje billeder, som du vil inkludere i slægtsbogen, men som ikke er begrænset til en bestemt person, slægtsforhold, kilde eller sted, skal du skifte til -visningen (se fig. {{#var:chapter}}.{{#expr:{{#var:figure}}}}). Klik derefter på ikonet på værktøjslinjen for at tilføje et billede. Hvis du allerede har tilføjet billeder til individuelle gallerier, finder du dem også angivet i -visningen.

I ethvert galleri kan du også bruge til at redigere billedoplysninger og knappen til at fjerne billedreferencen fra det pågældende galleri.

{{-}}

## Sådan redigerer du begivenheder, kildehenvisninger/kilder, steder og arkiver

For at redigere oplysninger om begivenheder, kilder, steder og arkiver, der allerede findes i slægtsbogen, skal du skifte til den relevante visning, vælge en post, du vil se/ændre, og derefter klikke på ikonet på værktøjslinjen. Alternativt kan du dobbeltklikke på posten for at redigere den.

![[_media/EventsCategory-EventsListView-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Begivenhedsvisning]]

For at tilføje en begivenhed, en kildehenvisning/kilde, et sted eller et arkiv til slægtsbogen, skal du skifte til den relevante -visning (se fig. {{#var:chapter}}.{{#expr:{{#var:figure}}}}), -visning, -visning, -visning eller -visning. Klik derefter på ikonet på værktøjslinjen for at tilføje det tilsvarende objekt. Indtast oplysningerne i den tilsvarende (, , eller ) dialogboks.

[Category:Documentation](wiki:Category:Documentation)
