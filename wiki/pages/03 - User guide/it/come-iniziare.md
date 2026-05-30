---
title: It:Manuale Wiki per Gramps 6.0 - Come iniziare
categories:
- It:Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 119908
wiki_fetched_at: '2026-05-30T19:29:26Z'
lang: it
---

{{#vardefine:chapter\|2}} {{#vardefine:figure\|0}} In questa sezione inizieremo con le basi. In primo luogo, descriveremo i concetti base in Gramps. Successivamente, vi mostreremo come iniziare con Gramps e come ottenere aiuto quando ne avrete bisogno. \_\_FORCETOC\_\_

## Panoramica di Gramps

Gramps è un programma libero, open source, che è stato progettato per essere uno strumento flessibile e potente per la genealogia. Si può utilizzare Gramps comunque lo si desidera. Non c'è un corretto metodo di lavoro o per la registrazione dei dati. Tuttavia, se si desidera interagire con altri ricercatori o con altri programmi, è di aiuto farsi un'idea di come funziona Gramps prima di lanciarsi nell’utilizzo del programma.

Gramps raccoglie tutte le informazioni sulla genealogia in 9 elementi principali:

- Persone
- Famiglie
- Eventi
- Note
- Multimedia
- Citazioni
- Fonti
- Luoghi
- Depositi

Ciascuno di questi è composto da elementi autonomi. Ciò significa che è possibile inserire nel vostro albero genealogico un elemento alla volta, e in qualsiasi ordine lo si desideri. Ad esempio, si potrebbe desiderare di inserire inizialmente tutte le voci Persona, e solo successivamente collegarle insieme con la creazione di oggetti Familia. In alternativa, si potrebbe iniziare con le Fonti, e creare una Persona man mano che la vostra ricerca lo richiede. Diversamente, potreste mescolare questi stili di inserimento con l'aggiunta di alcuni elementi Nota e Fonte, quindi con le Famiglie, per poi tornare alle Note e alle Fonti. In una parola, fate la vostra ricerca genealogica come desiderate.

Se avete altre domande, Gramps ha una comunità di utenti e sviluppatori. C'è un [FAQ](wiki:Gramps_6.0_Wiki_Manual_-_FAQ) (lista delle domande frequenti); una mailing list; [per segnalare bug e richiedere funzioni aggiuntive](Http://www.gramps-project.org/bugs/); e una stanza per le chat on-line.

### Connessioni

Questi 9 elementi primari sono collegati in vari modi. Alcuni di questi collegamenti sono mantenuti in modo implicito. Ad esempio, l'aggiunta di una voce Persona a un elemento della Famiglia come un genitore, o un Figlio, crea automaticamente una connessione speciale, chiamata **Relazione**. È possibile vedere se una persona è collegata ad una famiglia nella scheda Relazioni della Finestra Principale. Ci sono molti altri modi in cui queste connessioni sono visualizzate anche in Gramps, tra cui la vista di relazioni. Per evitare di ripetere l'informazione, Gramps permette di riutilizzare, o condividere, oggetti. Vi sono anche i collegamenti speciali, chiamati **link**. Ad esempio, un elemento persona può essere collegato a qualsiasi numero di elementi nota. Se una nota parla di due persone distinte, allora potrebbe avere senso condividere questa singola nota con entrambi gli elementi Persona. Alcuni link dispongono di informazioni proprie. Ad esempio, è possibile collegare una persona all'evento matrimonio di un'altra coppia, per esempio, perché la persona era un testimone al loro matrimonio. Tuttavia, il marito e la moglie sono legati all'evento matrimonio in un ruolo di **primo piano**, mentre un testimone ricopre un ruolo diverso, per es. com **testimone**. Questo tipo di informazioni è tenuto sul link in sé, nella proprietà di ruolo.

### Privacy

Gramps supporta due metodi diversi per proteggere la privacy dei dati sensibili del vostro albero genealogico. Questi metodi sono utilizzati quando si condividono i dati con gli altri, sia attraverso la creazione di un report, l'esportazione dei dati, o attraverso la creazione di un sito web. Il primo metodo consiste nel proteggere le informazioni sulle persone che Gramps ritiene che siano in vita. Se non è stato espressamente indicato che una persona è morta (con l'aggiunta di un Evento di decesso a un elemento Persona), Gramps ha una sofisticata funzione automatica per determinare se qualcuno è vivo. Le persone viventi hanno i loro dati sensibili redatti quando si utilizza questo metodo. Per esempio, una persona di nome "Rossi, Mario" potrebbe apparire come "Rossi, \[In vita\]".

Il secondo metodo per la privacy consiste nell’utilizzo di un’opzione esplicita "informazione privata/pubblica", che è possibile impostare su ciascuna voce. Ad esempio, si potrebbero avere informazioni personali sensibili in una Nota. Se si contrassegna una tale nota come privata, quella nota non verrà mostrata nei resoconti testuali e narrativi o nelle esportazioni. E’ utile sapere che anche alcuni collegamenti possono essere contrassegnati con tale opzione. Questo risulta utile quando si desidera contrassegnare la connessione tra una persona ad un evento come privata, ma si vuole che la Persona e l'Evento siano disponibili nel resoconto, nell'esportazione, o nel sito web.

Per attivare questi due metodi di privacy, è necessario indicare il loro utilizzo per la creazione di alcuni rapporti o l'esportazione dei dati.

![[_media/Include-data-marked-private-checkbox-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Privacy overrides for Reports]]In order to activate these two methods of privacy, you will need to indicate their use when creating some reports or exporting your data. {{-}}

### GEDCOM

Gramps deriva la sua struttura di base di elementi da uno standard chiamato GEDCOM. Tuttavia, Gramps estende questo standard dove è stato ritenuto necessario. Se si pensa di utilizzare i dati della vostra famiglia con un altro sistema che utilizza GEDCOM, allora probabilmente converrà cercare di limitare l'uso delle caratteristiche di Gramps coerenti con lo standard. D'altra parte, se non si è limitati da altri software genealogici, è possibile inserire i dati in qualsiasi modo abbiano un senso per voi.

Potete leggere maggiori dettagli su questo problema nella sezione su [Gramps and GEDCOM](wiki:Gramps_and_GEDCOM).

## Avviare Gramps

Il modo migliore per imparare Gramps è quello di lavorare con i propri dati. Iniziamo!

Il modo in cui si avvia Gramps dipende dal sistema operativo che si sta utilizzando.

Si può far partire Gramps utilizzando la normale interfaccia utente grafica (GUI), come descritto di seguito, ma è anche possibile iniziare Gramps utilizzando un'interfaccia a riga di comando (CLI). Con l’uso della CLI si è in grado di produrre resoconti che non sono disponibili tramite l'interfaccia grafica, può essere utilizzata per creare resoconti, fare conversioni, ecc senza aprire una finestra, e potete trovare [altre informazioni](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference#Seeing_all_the_error_messages) in caso di problemi. Per ulteriori informazioni, vedere [the Command Line appendix](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line).

### Linux

Solo la piattaforma Linux è ufficialmente supportata, gli sviluppatori Gramps utilizzano e testano il codice sorgente su quella piattaforma, risolvono gli eventuali problemi che sorgono a causa di aggiornamenti.

Supponendo che abbiate utilizzato il gestore dei pacchetti standard (attraverso una CLI o una GUI) per la vostra distribuzione Linux, si avvierà Gramps nel modo normale per la vostra distribuzione. Per esempio in Ubuntu 18.04, un'icona viene inserita nel programma di avvio, o il programma può essere avviato da Dash. Per le altre distribuzioni, potrebbe essere creata una voce nel menu Applicazioni (normalmente nella sezione ‘’’Office’’’).

Come avviare Gramps attraverso CLI in Linux è spiegato [qui (in inglese)](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line#Linux).

### MS Windows

MS Windows è una [piattaforma supportata](wiki:Download#MS_Windows) dalla comunità. Se installate la [Windows AIO](wiki:All_In_One_Gramps_Software_Bundle_for_Windows) GrampsAIO32 oppure GrampsAIO64 nella versione eseguibile, si creerà un’icona nella scrivania e nel menù ‘Avvio’, e cliccherete su questa per avviare Gramps.

Come avviare Gramps attraverso CLI in MS Windows è spiegato [qui (in inglese)](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line#MS_Windows).

Ci sono altri modi per installare Gramps per MS Windows, ma sono molto più complicato e non son illustrati qui.

### Mac OS X

Mac OS X è una [piattaforma supportata](wiki:Download#Mac_OS_X) dalla comunità. Se avete scaricato il disco imagine Mac OS X (.dmg), potete semplicemente trascinare l’applicazione nel vostro foglio delle applicazioni (oppure in qualsiasi posto la volete salvare) e avviare Gramps eseguendo un doppio click sull’applicazione come qualunque altra.

Come avviare Gramps attraverso CLI in Mac OS X è spiegato [qui (in inglese)](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line#Mac_OS_X).

Ci sono altri modi per installare Gramps per Mac OS X, ma sono molto più complicati e non sono illustrati qui.

## Scegliere un Albero Genealogico

![[_media/Dashboard-category-view-first-open-no-family-tree-loaded-52-it.png|Fig {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dashboard Category View - First open of Gramps with no family tree loaded(Gramps 6.0.0; MS-Windows 10)]]

Se Gramps viene avviato senza un albero di famiglia selezionato, la schermata iniziale avrà poche funzionalità. La maggior parte delle operazioni non saranno disponibili. Per caricare un albero genealogico (a cui ci si riferisce anche come ‘’database’’), selezionate nel menu per aprire la lista degli alberi genealogici, oppure cliccare sull'icona nella barra degli strumenti. Gramps tiene traccia degli Alberi genealogici aperti di recente, e questi possono essere selezionati cliccando sulla freccia accanto al pulsante e scegliendo dal menu a tendina.

Per informazioni più dettagliate sul gestore degli Alberi genealogici e sul menu Alberi genealogici, consultate il capitolo dedicato: [Gestire gli Alberi genealogici](wiki:It:Manuale_Wiki_per_Gramps_6.0_-_Gestire_gli_Alberi_genealogici).

{{-}}

## Dimmi come iniziare subito!

Consigliamo a tutti di leggere il manuale per imparare tutto quanto su come utilizzare Gramps. La genealogia richiede tempo, imparare ad utilizzare gli strumenti non è tempo sprecato.

Tuttavia, se si vuole veramente apprendere il minimo indispensabile per iniziare, potete leggere [Iniziare con la Genealogia](wiki:It:Iniziare_con_la_Genealogia) utilizzando Gramps.

## Ottenere aiuto

Gramps ha un menù di che potete consultare in ogni momento.

- Vedi la sezione menù .

[Category:It:Documentation](wiki:Category:It:Documentation)
