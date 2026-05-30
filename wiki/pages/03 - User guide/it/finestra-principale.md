---
title: It:Manuale Wiki per Gramps 6.0 - Finestra Principale
categories:
- It:Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 119905
wiki_fetched_at: '2026-05-30T19:29:35Z'
lang: it
---

{{#vardefine:chapter\|3}} {{#vardefine:figure\|0}}

Elementi di Gramps finestra principale.

## Finestra Principale

Quando si apre una banca dati (sia esistente che nuova), si apre la schermata principale: (Fig. {{#var:chapter}}.{{#expr:{{#var:figure}}+1}}): {{-}} ![[_media/MainWindow-PeopleCategory-PeopleTreeView-annotated-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Gramps Main Window]] {{-}}

La finestra principale di Gramps contiene i seguenti elementi: {{-}}

### Barra del Titolo

- La barra del titolo mostra il nome dell’albero genealogico selezionato, il nome della applicazione e i pulsanti per minimizzare, massimizzare e chiudere l’applicazione Gramps. La finestra può anche essere trascinata dalla barra del titolo.

### Barra dei Menu

- Barra dei Menu: la barra dei menu ([Menu principale](wiki:Gramps_6.0_Wiki_Manual_-_Navigation#Main_Menus)) si trova nella parte superiore della finestra (a destra sotto il titolo della finestra) e fornisce l'accesso a tutte le funzionalità di Gramps.

### Barra degli Strumenti

- Barra degli Strumenti: La barra degli strumenti si trova proprio sotto la barra dei menu. Esso consente di accedere alle funzioni più frequentemente utilizzate di Gramps.

La barra degli strumenti può essere nascosta o rivelata dal opzione nel menu .

### Navigatore

- Navigatore: Il navigatore si trova nella parte sinistra della finestra e consente di selezionare le diverse categorie. Vedere [Categorie del Navigatore](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Categories_of_the_Navigator)

Il Navigatore può essere nascosto o visualizzato dalle opzioni nel menu oppure con la [scorciatoia](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#7) .

### Area di Visualizzazione

- Area di visualizzazione: L'area al centro della finestra di Gramps è l'area di visualizzazione. Che cosa viene visualizzato dipende dalla vista attualmente selezionata. Discuteremo Vista in dettaglio più avanti.

### Barra di Stato e Barra di Avanzamento

- Barra di stato e barra di avanzamento: sono situati nella parte inferiore della finestra di Gramps.
  - La barra di avanzamento si trova nell'angolo in basso a sinistra della finestra Gramps. Mostra lo stato di avanzamento del tempo consumato dalle operazioni, quali l'apertura e il salvataggio di grandi database di alberi genealogici, l’importazione e l’esportazione in altri formati, la generazione di siti web, ecc. Quando non stai facendo questo tipo di operazioni, la barra di avanzamento non viene mostrata.
  - La barra di stato si trova a destra della barra di avanzamento. Visualizza informazioni sulle attività correnti di Gramps e informazioni contestuali sugli elementi selezionati.

### Barra in basso e laterale

- Barra in basso: si trova sotto l'area di visualizzazione.

<!-- -->

- Barra laterale: si trova alla destra dell'area di visualizzazione.

La Barra in basso e la Barra laterale permettono [Gramplets](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets) e [filtri](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Filters) di essere mostrati insieme ad una visualizzazione.

La Barra in basso e la Barra laterale possono essere individualmente nascosti o visualizzati utilizzando le opzioni nel menu o la relativa [scorciatoia](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#17). {{-}}

Se non viene visualizzata la barra laterale, al suo posto viene visualizzata la .

![[_media/MainWindow-SearchBar-sidebar-hidden-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} People Category View - showing Search Bar after Sidebar has been hidden]]

{{-}}

#### Barra Menu Gramplet

#### Finestra di dialogo Ripristinare ai valori predefiniti?

#### Barra ricerca

## Cambiare le modalità dal Navigatore

![[_media/Navigator-mode-selection-dropdownlist-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Navigator mode selection drop down list]]

È possibile scegliere la modalità del Navigazione dalla barra laterale attraverso la selezione di un’opzione dalla lista a cascata :

- **"Categoria"**(Default)
- Expander
- Drop-Down

{{-}}

Modalità **Categoria** del Navigatore (default)  

![[_media/Navigator-mode-selection-category-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Category (default) Navigator mode]]

Barra laterale delle Categorie - Una barra laterale permette di selezionare le categorie da visualizzare. {{-}}

Modalità **Drop-Down** del Navigatore  

![[_media/Navigator-mode-selection-drop-down-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Drop-Down navigator mode]]

Barra laterale Drop-down - E' possibile selezionare le cagorie e le visualizzazioni da liste a cascata. {{-}}

Modalità **Expander** del Navigatore  

![[_media/Navigator-mode-selection-expander-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Expander navigator mode]]

Barra laterale Expander - La selezione delle visualizzazioni avviene attraverso liste che, espandendosi, mostrano le scelte possibili a partire dalle categorie. {{-}} {{-}}

## Cambiare Categoria

Gramps è provvisto di un certo numero di categorie predefinite. Le categorie predefinite sono descritte in [categorie](wiki:Gramps_6.0_Wiki_Manual_-_Categories#Categories_of_the_Navigator). E’ possibile [scaricare addon](wiki:6.0_Addons) 'Gramps View's attraverso il menu preferenze. Se la vista è una nuova vista o è un aggiornamento per una categoria esistente, la vista si aggiunge a quella categoria. Tuttavia, se la vista è una vista per una *nuova* categoria, allora la nuova categoria viene aggiunta al navigatore.

Il modo in cui si modifica la categoria attualmente visualizzata dipende dalla modalità del Navigatore. Normalmente (per la maggior parte delle modalità Navigatore) è possibile selezionare la categoria che si desidera cliccando su una delle icone del Navigatore.

In alternativa è possibile utilizzare la [scorciatoia da tastiera](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#4) e per spostarsi alla categoria successiva e precedente rispettivamente o usare la [scorciatoia da tastiera](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#45) (Only available for the first 10 categories eg Repositories/Media/Notes miss out.). Se hai nascosto il [Navigatore](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Navigator) questo sarà l'unico modo per cambiare le categorie (a meno che non si accende il navigatore di nuovo).

{{-}}

## Cambiare Visualizzazione

Una categoria può contenere diversi modi di presentare i dati, chiamata Vista. Se ci sono diverse viste, è possibile passare da una visualizzazione all'altra. Il modo in cui si cambia vista dipende dalla modalità di visualizzazione. In alcuni tipi di visualizzazione, vi è un pulsante con l'icona sulla barra degli strumenti per passare a una visione diversa. È anche possibile passare attraverso il menu , oppure la [scorciatoia](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#6) premendo , dove <numbero> è la vista desiderata in quella categoria. {{-}}

## Filtri

![[_media/PeopleCategory-sidebar-filter-enabled-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Filter Controls Displayed]]

I database di genealogia possono contenere informazioni su tante Persone, Famiglie, Luoghi e Oggetti. E' quindi possibile che una visualizzazione possa contenere un lungo elenco di dati, tale da rendere difficile da lavorare. Gramps offre la possibilità di ovviare a questa condizione, consentendo di filtrare un elenco riducendola ad una dimensione più gestibile, con due modalità.

Questi metodi sono **Cerca** e **filtraggio**.

Una ricerca cercherà il testo visualizzato nella lista, mentre il filtro seleziona le persone i cui dati corrispondono ai criteri del filtro.

La ricerca è un metodo semplice ma veloce di cercare le colonne visualizzate sullo schermo. Quando ‘’’non’’’ è visualizzata la [Barra laterale](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar), è visualizzatala . Digitando il testo nella e cliccando il bottone verranno visualizzate solo le linee che corrispondono a quel testo.

In alternativa, è possibile attivare un filtro sia nella [Barra inferiore che nella Barra laterale](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Bottombar_and_Sidebar). Quando viene visualizzato il filtro nella barra laterale, la non è visualizzata. Il Filtro consente di costruire in modo interattivo una serie di regole di filtraggio che possono essere applicate alla visualizzazione. Il filtro si applica in base alle regole e ai dati, non alla visualizzazione. I filtri della categoria visualizzata possono anche essere costruiti cliccando sulla voce contrassegnata con 'Editor filtri' nel menu.

Ulteriori dettagli sulle funzionalità dei filtri sono riportati nel [Capitolo sui Filtri](wiki:Gramps_6.0_Wiki_Manual_-_Filters)

{{-}}

All’apertura di un Albero genealogico con Gramps, nessun Filtro sarà attivo. Ad esempio, nella visualizzazione Persone, come impostazione predefinita, verranno elencate tutte le Persone dell’Albero genealogico. {{-}}

[Category:it:Documentation](wiki:Category:it:Documentation)
