---
title: It:Manuale Wiki per Gramps 6.0 - Gestire gli Alberi genealogici
categories:
- It:Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 120301
wiki_fetched_at: '2026-05-30T19:29:48Z'
lang: it
---

{{#vardefine:chapter\|5}} {{#vardefine:figure\|0}} Un'esplorazione dettagliata dell'uso quotidiano di Gramps. In questo capitolo forniamo una panoramica dettagliata di come è possibile gestire i propri alberi genealogici e condividere i dati con altri genealogisti.

## Iniziare un nuovo albero genealogico

Per iniziare un nuovo albero genealogico, scegli il menu oppure seleziona dalla barra degli strumenti il pulsante oppure usare [scorciatoie da tastiera](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings/It) . Ciò aprirà la finestra di gestione .

Seleziona il pulsante e aggiungi un nuovo Albero Genealogico alla lista degli Alberi Genealogici. Cambiare il suo nome preimpostato *`Albero Genealogico 1`*, seleziona il nome e premi il pulsante poi digita un nuovo nome.

Per caricare l'Albero Genealogico puoi fare doppio click su esso o selezionarlo e premere li pulsante . {{-}}

### Finestra di gestione degli Alberi Genealogici

![[_media/FamilyTreesManager-window-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Iniziare Alberi genealogici]] {{-}}

## Aprire un Albero Genealogico

Per aprire un Albero Genealogico, scegli il menu o clicca il pulsante dalla barra degli strumenti. La finestra di apparirà e vedrai una lista di tutti gli Alberi di Famiglia conosciuti da Gramps. Nella colonna una icona (sembra una cartella aperta) sarà mostrata a fianco di ogni Albero Genealogico che è attualmente aperto. Seleziona l'albero che vuoi aprire, e aprilo selezionando il pulsante . Altrimenti potrai fare doppio click sull'Albero desiderato.

Per aprire un Albero Genealogico aperto recentemente, scegli dal menu oppure premi la freccia in basso vicino al pulsante nella barra degli strumenti e seleziona l'Albero Genealogico dalla lista.

## Aprire una base dati GEDCOM o XML

Gramps ti permette di aprire alcune base dati che non sono stati salvati da Gramps con i propri formati dalla riga di comando, vedi [Riferimenti della riga di comando](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line#Opening_options). Tra questi formati vi sono le basi dati XML e GEDCOM. Tuttavia, dovresti sapere che se la base dati XML o GEDCOM è relativamente grande, si verificheranno problemi di prestazioni e, in caso di arresto anomalo, i dati potrebbero essere danneggiati. Quindi, normalmente è meglio creare un nuovo albero genealogico (database) Gramps e importare i dati XML / GEDCOM in esso.

## Cancellare un Albero Genealogico

Seleziona l'albero genealogico che vuoi cancellare, e premi sul pulsante .

Ciò rimuoverà **completamente** l'albero, senza nessuna possibilità di recuperare i dati. Considera la possibilità di fare una copia di sicurezza dei tuoi dati esportandoli nel formato GRAMPS XML, e conservando il file

## Rinominare un Albero Genealogico

Puoi rinominare un Albero Genealogico ( o un suo archivio) selezionando l'albero desiderato e cliccando . Puoi anche cliccare sul nome dalla lista degli alberi.

In entrambi i casi, dovrai solo digitare il nuovo nome affinche abbia effetto.

## Fare una copia di sicurezza di un Albero Genealogico

Il modo più sicuro per fare una copia di sicurezza di un Albero Genealogico è quello di esportare, senza opzioni di privacy e fitri attivi, verso un formato **Gramps XML** (o **pacchetto Gramps XML** per includere gli oggetti della Galleria) e salvare il file risultante in un posto sicuro, preferibilmente in una differente costruzione.

### Finestra di dialogo Copia di Sicurezza

![[_media/MakeBackup-GrampsXML-Backup-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Eseguire una copia di sicurezza]]

Dal menu lelezionare semplicemente .

La finestra apparirà.

Puoi inserire un percorso, dove la copia di sicurezza sarà salvata, manualmente oppure utilizzando il pulsante del slettore di percorso.

Puoi inserire manualmente un nome di file o usare il nome generato in modo automatico.

Puoi scegliere di **Includere** (scelta predefinita) oppure *Escludere* la .

{{-}}

### Impostazioni avanzate

E' possibile anche definire la traccia/modalità con cui sarà autogenerato il nome proposto per le copie di sicurezza impostando *paths.quick-backup-filename* nel file chiave ~/.gramps/gramps42/gramps.ini come esposto di seguito: {{-}}

`[paths]`  
`quick-backup-filename='%(filename)s_%(year)d-%(month)02d-%(day)02d.%(extension)s'`

Nella traccia puoi usare qualsiasi parola chiave tra le seguenti:

- filename
- year
- month
- day
- hour
- minutes
- seconds
- extension :
  - **.gpkg**(default) se comprende multimedia.
  - *.gramps* se esclude multimedia.

Utilizza l'appropriato file chiave ~/.gramps/gramps{XX}/gramps.ini

- Gramps versione 6.0 :

`~/.gramps/gramps42/gramps.ini`

- Puoi usare le funzioni di Archivio (vedi la sezione seguente) per immagazzinare istantanee del tuo Albero genealogico. Queste istantanee possono essere usate come semplici copi di sicurezza, molto fruibili se desideri provare qualcosa che potresti in seguito voler disfare. Tuttavia questo metodo non dovrebbe essere usato per le copie di sicurezza abituali, in quanto non sopravviverà a un arresto anomalo del disco rigido o alla maggior parte degli altri disastri che possono verificarsi su un computer.

<!-- -->

- *Per utenti avanzati:* ogni base dati è salvata in una propria sottocartella sotto ~/.gramps. Una copia di sicurezza manuale può essere fatta facendo una copia di sicurezza di questa cartella.

## Archiviare un Albero genealogico

<center>

</center>

Puoi facilmente archiviare e applicare una marca temporale all'Albero genealogico conGramps usando [GNU Revision Control System](http://www.gnu.org/software/rcs/) o *RCS* se installato. Affinchè ciò sia possibile questa utilità deve essere istallata nel tuo computer.

Per fare un archivio :

![[_media/ManageFamilyTrees-Archive-RevisionComment-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Esempio di archivio di Albero genealogico]]

1.  carica il tuo Albero genealogico.
2.  clicca sul pulsante della barra degli strumenti (mostra quando passi il mouse su di esso).
3.  clicca sull'albero genealogico che hai appena caricato: il pulsante dovrebbe apparire.
4.  clicca e ti verrà chiesto di inserire un "Commente di revisione - Descrizione della versione" per il tuo archivio.

Dopo aver archiviato, la lista degli alberi di famiglia mostrerà l'albero di famiglia originale con un tringolo nella sua sinistra.

- Clicca sul triangolo per mostrare il nome dell'archivio.(Clicca ancora per chiudere la lista degli archivi).

Gli archivi possono essere cancellati, rinominati ed estratti.

{{-}}

## Estrarre un Archivio di un Albero genealogico

![[_media/ManageFamilyTrees-Archive-Selected-to-Extract-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Selezionare la versione da estrarre]]

Se clicchi su un archivio, il pulsante diventa visibile. Clicca su di esso per ottenere un archivio estratto. Se apparirà nella lista degli Alberi genealogici come *\<nome dell'albero originale\>:\<nome dell'archivio\>* e è ora un Albero genealogico indipendente. Questo può essere un modo utile per preservare un archivio, perchè gli archivi sparicono se gli alberi originali vengono cancellati; e non vengono incorporati nei Pacchetti Gramps XML di esportazione dell'albero genealogico.

Semplicemente evidenziando l'archivio che vuoi ripristinare, e seleziona il pulsante .

![[_media/ManageFamilyTrees-Archive-Extracted-version-selected-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Mostra una versione estratta]]

Gramps trasferirà l'archivio nel nuovo Albero genealogico. Il nome dell'Albero genealogico è basato sul nome originale e sul nome dell'archivio (vedi anche [Archiviare un Albero genealogico](#Archiviare_un_Albero_genealogico)).

{{-}}

## Sbloccare un Albero genealogico

![[_media/FamilyTreesManager-Dialog-ShowingLocked-Sample-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Albero genealogico bloccato - Esempio di finestra di dialogo]]

Quando Gramps apre un albero, blocca l'albero, prevenendo che tu o qualcun altro lo aprano allo stesso tempo. Una seconda copia di Gramps sarà abilitata ad aprire un altro albero genealogico, ma l'albero già aperto apparirà con l'icona del lucchetto, indicando che non può essere aperto. Chiudendo l'albero nella prima copia di Gramps sarà reso disponibile per essere aperto nella seconda copia.

Se ti riuscisse di aprire lo stesso Albero genealogico in due Gramps allo stesso momento, è probabile che i tuoi dati vengano danneggiati. {{-}} Nell'improbabile caso di un arresto inaspettato di Gramps, l'albero genealogico verrà lasciato in uno stato bloccato. Per sbloccare l'albero: {{-}} ![[_media/ErrorParsingArguments-dialog-DatabaseIsLocked-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} La base di dati è bloccato]]

- Se Gramps è stato impostato per aprire automaticamente all'avvio, quando vedrai la finestra di dialogo 'La Base di dati è bloccata'. Clicca sul pulsante e la apparirà. Scelgli l'Albero genealogico e poi clicca il pulsante . La finestra di dialogo 'Rompi il blocco' apparirà.

{{-}} ![[_media/Break-the-lock-on-the-database-Dialog-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Rompi il blocco sul database &quot;Albero genealogico esempio&quot;? - Dialog]]

- Clicca il pulsante che sarà disponibile. Fai questo solo se sei sicuro che nessun'altra copia di Gramp stia usando questo Albero genealogico.

{{-}}

## Riparare un Albero genealogico danneggiato

![[_media/FamilyTreesManager-Dialog-ShowingRedErrorStatusIcon-Sample-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Riparare un Albero genealogico danneggiato]]

I tuo Albero genealogico potrebbe danneggiarsi in qualche modo, il gestore degli alberi di Gramps mostrerà un'icona nella colonna .

Per far si che Gramps tenti di riparare il danno, seleziona l'Albero genealogico e poi clicca il pulsante .

Così cercherà di ricostruire il tuo Albero genealogico a partire dai file della Copia di sicurezza che automaticamente ha creato all'uscita.

{{-}}

## Salvare le modifiche al tuo Albero genealogico

Gramps salva le modifiche man mano che le realizzi. Questo significa, che ogni volta che tu clicchi mentre usi Gramps, i tuoi cambiamenti sono immediatamente registrati e salvati. Non è previsto un comando "salva" separato.

Puoi disfare le modifiche apportate selezionando dal menù . Se selezioni questo comando ripetutamente, le tue modifiche più recenti saranno annullate una alla volta. Per ripristinare più comandi alla volta, puoi utilizzare l'apposita finestra di dialogo accessibile dal menu .

Se vuoi far tornare il tuo Albero genealogico allo stato in cui era quando lo hai aperto, seleziona dal menu . (Ciò equivale ad uscire senza salvare in altri programmi.)

Se volessi salvare una copia del tuo Albero genealogico con un nome diverso, devi esportarlo e poi importarlo in un nuovo Albero genealogico. Per questo scopo è raccomandata il formato base di dati *Gramps XML*.

## Importare dati

L'importazone ti permette di trasferire dati da altri programmi di genealogia in Alberi genealogici di Gramps. Gramps puo importare dati dai seguenti formati:

- [Gramps XML](#Gramps_XML_and_XML_Package_import) (`.gramps` estensione del file)
- [Pacchetto Gramps XML](#Gramps_XML_and_XML_Package_import) (`.gpkg` estensione del file)
- [Fogli di calcolo Comma Separeted Values CSV](#Gramps_CSV_import) - comma separated values (`.csv` estensione del file)
- [base di dati GRAMPS V2.x](#GRAMPS_V2.x_database_import) (`.grdb` estensione del file)
- [GEDCOM](#GEDCOM_import) (`.ged` estensione del file)
- GeneWeb (`.gw` estensione del file)
- Pro-Gen (`.def` estensione del file)

### Finestra di dialogo Importa albero genealogico

Per prima cosa crea un [nuovo albero genealogico vuoto](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees#Starting_a_new_Family_Tree). In seguito seleziona dal menu o la [scorciatoia da tastiera](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#2) per importare o ripristinare una copia di Albero genealogico salvato in precedenza (da una versione precedente di GRamps o dalla versione attuale) la finestra di dialogo **** verrà aperta, chiedendoti di specificare il file che vuoi importare.

Se cerci di importare in un Albero genealogico già esistente, la finestra di dialogo verrà aperta dandoti l'opportunità di interrompere l'importazione e creare un nuovo Albero genealogico, oppure di tentare deliberatamente di fondere i dati.

### GRAMPS V2.x database import

GRAMPS V2.x database (.grdb): Prima di Gramps versione 6.0 questo formato di database nativo di Gramps era una forma particolare del database Berkeley (BSDDB) con una struttura speciale di tabelle di dati. Questo formato era binario e dipendente dall'architettura. Era molto veloce ed efficiente, ma non generalmente portadile su computer con architettura binaria diversa (per esempio da i386 a alpha).

L'importazione dal formato di database GRAMPS V2.x è supportata solo dalla versione 3.0.x di Gramps. L'importazione di V2.x in Gramps V3.0.x non perderà alcun dato.

### Gramps XML and XML Package import

I database di Gramps [XML](wiki:XML) e Gramps [XML](wiki:XML) sono i formati nativi di Gramps. Non vi è alcun rischio di perdita di informazioni durante l'importazione (ripristino) o l'esportazione in questi formati.

- Gramps [XML](wiki:XML) (.gramps): Il file [XML](wiki:XML) di Gramps è il formato standard di scambio di dati e copia di sicurezza di Gramps, ed era anche il formato predefinito della base di dati di lavoro per le versioni precedenti (pre 2.x) di Gramps. A differenza del formato GRAMPS V2.x grdb, è indipendente dall'architettura e leggibile dall'uomo. La base di dati potrebbe anche avere riferimenti a oggetti multimediali non locali (esterni), pertanto non è garantito che sia completamente portabile (per la portabilità completa, compresi gli oggetti multimediali, dovrebbe essere usato il formato pacchetto Gramps [XML](wiki:XML) (.gpkg)). La base dati [XML](wiki:XML) di Gramps viene creato selezionando (Menu ) esportando verso questo formato.

<!-- -->

- Gramps [XML](wiki:XML) package (.gpkg): Il pacchetto Gramps [XML](wiki:XML) è un archivio **compresso** contenenteil file Gramps [XML](wiki:XML) e tutti gli oggetti multimedia (immagini, file audio, ecc.) ai quali la base di dati si riferisce. Siccome contiene tutti gli oggetti multimedia, questo formato è completamente portabile. Il pacchetto Gramps [XML](wiki:XML) è stato creato per esportare ( Menu ) dati in questo formato.

Se importi informazioni da una altra base di dati Gramps o database Gramps [XML](wiki:XML), vedrai il progresso delle operazioni avanzare nella barra dei progressi della finestra principale di Gramps. Quando l'importazione termina, una finestra di risposta mostrerà il numero di oggetti importati. Se i dati importati provengono dalla stessa famiglia a cui si riferisce l'albero genealogico in cui si importano i dati, la finestra di risposta di importazione fornisce suggerimenti su cosa potrebbe essere unito; l'unione **non** è fatta automaticamente. Se si desidera unire automaticamente i dati genealogici di base, prendere in considerazione l'esportazione/importazione di fogli di calcolo CSV.

### Importare Gramps CSV

- Il formato CSV Spreadsheet consente di importare ed esportare un sottoinsieme dei dati di Gramp in un semplice formato di foglio di calcolo. Vedi [Importa ed Esporta in CSV](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees:_CSV_Import_and_Export) per maggiori informazioni.

### Importare GEDCOM

Quando importi informazioni da GEDCOM, la finestra principale di Gramps ti mostrerà una [barra di progresso](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Status_Bar_and_Progress_Bar). Quando l'importazione GEDCOM sarà terminata, la finestra delle e la finestra **** mostrerà ogni dato che non è stato importato. I dettagli del **** dettaglia descrive la maggior parte delle linee GEDCOM che sono state ignorate o che non possono essere capite (molto probabilmente perché non fanno parte dello standard GEDCOM 5.6.0. Vedi [Estensioni GEDCOM](wiki:Estensioni_GEDCOM)). Vengono mostrati anche i contenuti della linea GEDCOM (o linee dove sono presenti linee di continuazione). In alcuni casi, le righe potrebbero non essere esattamente ciò che è contenuto nel file GEDCOM di input, poiché la linea viene ricostruita dopo l'elaborazione.

Gramps utilizza un diverso 'modello di dati' da GEDCOM e quindi alcuni dati in GEDCOM non possono essere importati in Gramps (Vedi [Gramps e GEDCOM](wiki:Gramps_e_GEDCOM)).

Le principali eccezioni sono:

- Alcune strutture di attributi GEDCOM sono trattati come di Gramps e quindi molti degli elementi primitivi di GEDCOM non possono essere memorizzati.
- Gli elementi DATA di un SOURCE_RECORD (indicanti gli eventi registrati e l'agenzia responsabile) sono ignorati.
- Tutte le citazioni delle fonti sulle note vengono ignorate.
- Molti elementi primitivi di GEDCOM non hanno esattamente gli elementi di dati corrispondenti in Gramps, e sono quindi memorizzati come oppure con nomi appropiati, solitamente le etichette GEDCOM. Ciò si applica in particolare ai record GEDCOM di intestazione, submitter e submission e campi particolari come REFN, RFN, RIN e AFN.

![[_media/Source-Note-GEDCOMImportNote-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Import report:Example of a note indicating omitted data]] Quando i dati vengono dichiarati 'ignorati', la loro omissione viene riportata nel feedback alla fine dell'importazione ed è inclusa in una nota allegata a un oggetto pertinente.

Quando si dice che i dati sono 'silenziosamente ignorati', è (al momento - questo può essere considerato come una mancanza), non riportato e non incluso in una nota.

{{-}}

#### Finestra di dialogo statistiche di importazione

{{-}}

#### Finestra di dialogo rapporto di importazione GEDCOM

![[_media/GEDCOM-import-report-result-example-50.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} GEDCOM rapporto di importazione - esempio.]]

{{-}}

#### Limitazioni nell'importazione di GEDCOM

Questa sezione descrive qualsiasi dato GEDCOM che non può essere rappresentato direttamente in Gramps e come viene gestito. Per ulteriori informazioni sui limiti delle importazioni (ed esportazioni) di GEDCOM, leggi la sezione su [Gramps and GEDCOM](wiki:Gramps_and_GEDCOM).

##### HEADer, SUBMitter e SUBmissioN

Gramps non ha una rappresentazione diretta di questi dati e quindi tutte le informazioni devono essere memorizzate in altri oggetti. A seconda delle impostazioni delle [Preferenze generali](wiki:Gramps_6.0_Wiki_Manual_-_Settings#General), un oggetto 'Fonte predefinita' può essere creata. Se questa è creata, la maggior parte dei dati verranno immagazinati in tale , o nel collegato a tale fonte.

`   HEADER:=`  
`        n HEAD                                          {1:1}`  
`          +1 SOUR `<APPROVED_SYSTEM_ID>`                  {1:1}  (Elemento dati della 'fonte predefinita')`  
`            +2 VERS `<VERSION_NUMBER>`                    {0:1}  (Elemento dati della 'fonte predefinita')`  
`            +2 NAME `<NAME_OF_PRODUCT>`                   {0:1}  (Elemento dati della 'fonte predefinita')`  
`            +2 CORP `<NAME_OF_BUSINESS>`                  {0:1}  (Deposito della 'fonte predefinita')`  
`              +3 <`<ADDRESS_STRUCTURE>`>                  {0:1}  (Deposito della 'fonte predefinita')`  
`            +2 DATA `<NAME_OF_SOURCE_DATA>`               {0:1}  (Elemento dati della 'fonte predefinita')`  
`              +3 DATE `<PUBLICATION_DATE>`                {0:1}  (Elemento dati della 'fonte predefinita')`  
`              +3 COPR `<COPYRIGHT_SOURCE_DATA>`           {0:1}  (Elemento dati della 'fonte predefinita')`  
`          +1 DEST `<RECEIVING_SYSTEM_NAME>`               {0:1*} (Elemento dati della 'fonte predefinita')`  
`          +1 DATE `<TRANSMISSION_DATE>`                   {0:1}  (Elemento dati della 'fonte predefinita')`  
`            +2 TIME `<TIME_VALUE>`                        {0:1}  (Elemento dati della 'fonte predefinita')`  
`          +1 SUBM @`<XREF:SUBM>`@                         {1:1}  (Elemento dati della 'fonte predefinita')`  
`                                                               (Utilizzato anche per determinare SUBMITTER_RECORD)`  
`                                                               (che dovrebbe essere memorizzato come proprietario del database)`  
`          +1 SUBN @`<XREF:SUBN>`@                         {0:1}  (ignorato)`  
`          +1 FILE `<FILE_NAME>`                           {0:1}  (Elemento dati della 'fonte predefinita')`  
`          +1 COPR `<COPYRIGHT_GEDCOM_FILE>`               {0:1}  (memorizzato come informazione di pubblicazione della 'fonte predefinita')`  
`          +1 GEDC                                       {1:1}`  
`            +2 VERS `<VERSION_NUMBER>`                    {1:1}  (Elemento dati della 'fonte predefinita')`  
`            +2 FORM `<GEDCOM_FORM>`                       {1:1}  (Elemento dati della 'fonte predefinita')`  
`          +1 CHAR `<CHARACTER_SET>`                       {1:1}  (Elemento dati della 'fonte predefinita')`  
`            +2 VERS `<VERSION_NUMBER>`                    {0:1}  (Elemento dati della 'fonte predefinita')`  
`          +1 LANG `<LANGUAGE_OF_TEXT>`                    {0:1}  (Elemento dati della 'fonte predefinita')`  
`          +1 PLAC                                       {0:1}`  
`            +2 FORM `<PLACE_HIERARCHY>`                   {1:1}  (vedi sotto)`  
`          +1 NOTE `<GEDCOM_CONTENT_DESCRIPTION>`          {0:1}  (nota collegat alla 'fonte predefinita')`  
`            +2 [CONT|CONC] `<GEDCOM_CONTENT_DESCRIPTION>` {0:M}`  
`            `  
`   * NOTE: Gli inserimenti al Family History Department for Ancestral`  
`     File submission oppure per cancellare ordinanze del tempio devono usare un`  
`     DESTination of ANSTFILE o TempleReady.`

Il PLAC FORM è memorizzato internamente e utilizzato per governare l'interpretazione dei luoghi (in conformità con le specifiche GEDCOM).

Il SUBMISSION_RECORD (dovrebbe essere solo uno, ma questo non è controllato) è memorizzato come un elemento della 'fonte predefinita'

`    SUBMISSION_RECORD:=`  
`        n @`<XREF:SUBN>`@ SUBN                            {1:1]`  
`          +1 SUBM @`<XREF:SUBM>`@                         {0:1}`  
`          +1 FAMF `<NAME_OF_FAMILY_FILE>`                 {0:1}`  
`          +1 TEMP `<TEMPLE_CODE>`                         {0:1}`  
`          +1 ANCE `<GENERATIONS_OF_ANCESTORS>`            {0:1}`  
`          +1 DESC `<GENERATIONS_OF_DESCENDANTS>`          {0:1}`  
`          +1 ORDI `<ORDINANCE_PROCESS_FLAG>`              {0:1}`  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`

SUBMITTER_RECORDs (ce ne possono essere più di uno) sono memorizzati come registrazioni del collegato alla 'fonte predefinita ad eccezione di quanto indicato in grassetto di seguito. Il SUBMITTER_RECORD che corrisponde con la registrazione SUBM nell'HEADER è usato per impostare il [proprietario della base dati](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Edit_Database_Owner_Information...) q.v.

`   SUBMITTER_RECORD:=`  
`        n @`<XREF:SUBM>`@   SUBM                          {1:1}`  
`          +1 NAME `<SUBMITTER_NAME>`                      {1:1}`  
`          +1 <`<ADDRESS_STRUCTURE>`>                      {0:1}`  
`          `**`+1 <`<MULTIMEDIA_LINK>`> {0:M}`**  
`          `**`+1 LANG `<LANGUAGE_PREFERENCE>` {0:3}`**  
`          `**`+1 RFN `<SUBMITTER_REGISTERED_RFN>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- I collegamenti Mutimedia sono ignorati
- LANG è ignorato
- RFN e RIN sono ignorati

##### INDIvidual

Il INDIVIDUAL_RECORD è memorizzato come un record Gramps , ad eccezione di quanto indicato di seguito in grassetto.

`   INDIVIDUAL_RECORD: =`  
`        n @`<XREF:INDI>`@  INDI                           {1:1}`  
`          +1 RESN `<RESTRICTION_NOTICE>`                  {0:1}`  
`          +1 <`<PERSONAL_NAME_STRUCTURE>`>                {0:M}`  
`          +1 SEX `<SEX_VALUE>`                            {0:1}`  
`          +1 <`<INDIVIDUAL_EVENT_STRUCTURE>`>             {0:M}`  
`          `**`+1 <`<INDIVIDUAL_ATTRIBUTE_STRUCTURE>`> {0:M}`**  
`          +1 <`<LDS_INDIVIDUAL_ORDINANCE>`>               {0:M}`  
`          +1 <`<CHILD_TO_FAMILY_LINK>`>                   {0:M}`  
`          +1 <`<SPOUSE_TO_FAMILY_LINK>`>                  {0:M}`  
`          `**`+1 SUBM @`<XREF:SUBM>`@ {0:M}`**  
`          +1 <`<ASSOCIATION_STRUCTURE>`>                  {0:M}`  
`          +1 ALIA @`<XREF:INDI>`@                         {0:M}`  
`          `**`+1 ANCI @`<XREF:SUBM>`@ {0:M}`**  
`          `**`+1 DESI @`<XREF:SUBM>`@ {0:M}`**  
`          +1 <`<SOURCE_CITATION>`>                        {0:M}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 RFN `<PERMANENT_RECORD_FILE_NUMBER>`         {0:1}`  
`          +1 AFN `<ANCESTRAL_FILE_NUMBER>`                {0:1}`  
`          +1 REFN `<USER_REFERENCE_NUMBER>`               {0:M}`  
`            `**`+2 TYPE `<USER_REFERENCE_TYPE>` {0:1}`**  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`  
`   `

- Il collegamento al mittente, agli interessi degli antenati e agli indicatori di interesse discendente viene silenziosamente ignorato.
- L'indicatore alias ("Un indicatore per collegare descrizioni di registrazioni diverse di una persona che potrebbe essere la stessa persona") è registrato come una chiamata 'Alias'.
- Il REFN e REFN:TYPE sono immaganizzati come della , ma se c'è più di un REFN, potrebbe non essere chiaro quale TYPE è associato a quale REFN.

La gestione di INDIVIDUAL_ATTRIBUTE_STRUCTURE è piuttosto complicata. I seguenti tag:

- EDUC (Risultato scolastico),
- NMR (Conto dei matrimoni),
- OCCU (Occupazione),
- PROP (Patrimonio),
- RELI (Affiliazione religiosa),
- RESI and
- TITL (Titolo di nobiltà)

sono trattati tutti come di Gramps e le informazioni associate sono immagazinate nella struttura degli eventi. I dettagli che seguono il tag principale (mostrato tra parentesi nella lista sopra) sono memorizzati come dell'. Il <EVENT_DESCRIPTOR> che segue l'etichetta TYPE sarà sovrascritto nella se il <EVENT_DESCRIPTOR> non è il nome dell'attributo.

Le seguenti etichette:

- CAST (Nome della casta),
- DSCR (Descrizione fisica),
- INDO (Numero di ID nazionale),
- NATI (Origine nazionale o tribale),
- NCHI (Tribunale dei bambini) e
- SSN (Social Security Number)

sono tutti trattati come Gramp e la maggior parte dei campi tranne i dettagli che seguono il tag principale (mostrati tra parentesi nella lista sopra), la citazione della fonte e la struttura della nota sono ignorati, come indicato in grassetto sotto.

`   INDIVIDUAL_ATTRIBUTE_STRUCTURE: =`  
`        n  CAST `<CASTE_NAME>`                            {1:1}`  
`          +1 <`<EVENT_DETAIL>`>                           {0:1}`  
`             etc.`  
`   `  
`   EVENT_DETAIL: =`  
`        `**`n TYPE `<EVENT_DESCRIPTOR>` {0:1}`**  
`        `**`n DATE `<DATE_VALUE>` {0:1}`**  
`        `**`n <`<PLACE_STRUCTURE>`> {0:1}`**  
`        `**`n <`<ADDRESS_STRUCTURE>`> {0:1}`**  
`        `**`n AGE `<AGE_AT_EVENT>` {0:1}`**  
`        `**`n AGNC `<RESPONSIBLE_AGENCY>` {0:1}`**  
`        `**`n CAUS `<CAUSE_OF_EVENT>` {0:1}`**  
`        n  <`<SOURCE_CITATION>`>                          {0:M}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`        `**`n <`<MULTIMEDIA_LINK>`> {0:M}`**  
`        n  <`<NOTE_STRUCTURE>`>                           {0:M}`  
`        `  
`        `

- La singola struttura di attributi, il tipo, la data, la struttura del luogo, la struttura dell'indirizzo, l'età, l'agenzia, la causa e il collegamento multimediale sono tutti ignorati.

##### FAM_RECORD

Il FAM_RECORD è immagazzinato come una registrazione di Gramps.

`   FAM_RECORD:=`  
`        n @`<XREF:FAM>`@   FAM                            {1:1}`  
`          +1 <`<FAMILY_EVENT_STRUCTURE>`>                 {0:M}`  
`          +1 HUSB @`<XREF:INDI>`@                         {0:1}`  
`          +1 WIFE @`<XREF:INDI>`@                         {0:1}`  
`          +1 CHIL @`<XREF:INDI>`@                         {0:M}`  
`          +1 NCHI `<COUNT_OF_CHILDREN>`                   {0:1}`  
`          +1 SUBM @`<XREF:SUBM>`@                         {0:M}`  
`          +1 <`<LDS_SPOUSE_SEALING>`>                     {0:M}`  
`          +1 <`<SOURCE_CITATION>`>                        {0:M}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 REFN `<USER_REFERENCE_NUMBER>`               {0:M}`  
`            +2 TYPE `<USER_REFERENCE_TYPE>`               {0:1}`  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- Il collegamento al mittente è tacitamente ignorato.
- Il REFN e il REFN: TYPE sono memorizzati come di , ma se c'è più di un REFN, potrebbe non essere chiaro quale TYPE è associato a quale REFN.

##### SOURCE_RECORD

SOURCE_RECORD è memorizzato come record di Gramps , ad eccezione di quanto indicato in grassetto sotto.

`   SOURCE_RECORD:=`  
`        n @`<XREF:SOUR>`@ SOUR                            {1:1}`  
`          `**`+1 DATA {0:1}`**  
`            `**`+2 EVEN `<EVENTS_RECORDED>` {0:M}`**  
`              `**`+3 DATE `<DATE_PERIOD>` {0:1}`**  
`              `**`+3 PLAC `<SOURCE_JURISDICTION_PLACE>` {0:1}`**  
`            `**`+2 AGNC `<RESPONSIBLE_AGENCY>` {0:1}`**  
`            `**`+2 <`<NOTE_STRUCTURE>`> {0:M}`**  
`          +1 AUTH `<SOURCE_ORIGINATOR>`                   {0:1}`  
`            +2 [CONT|CONC] `<SOURCE_ORIGINATOR>`          {0:M}`  
`          +1 TITL `<SOURCE_DESCRIPTIVE_TITLE>`            {0:1}`  
`            +2 [CONT|CONC] `<SOURCE_DESCRIPTIVE_TITLE>`   {0:M}`  
`          +1 ABBR `<SOURCE_FILED_BY_ENTRY>`               {0:1}`  
`          +1 PUBL `<SOURCE_PUBLICATION_FACTS>`            {0:1}`  
`            +2 [CONT|CONC] `<SOURCE_PUBLICATION_FACTS>`   {0:M}`  
`          +1 TEXT `<TEXT_FROM_SOURCE>`                    {0:1}`  
`            +2 [CONT|CONC] `<TEXT_FROM_SOURCE>`           {0:M}`  
`          +1 <`<SOURCE_REPOSITORY_CITATION>`>             {0:1}`  
`          +1 <`<MULTIMEDIA_LINK>`>                        {0:M}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 REFN `<USER_REFERENCE_NUMBER>`               {0:M}`  
`            +2 TYPE `<USER_REFERENCE_TYPE>`               {0:1}`  
`          +1 RIN `<AUTOMATED_RECORD_ID>`                  {0:1}`  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- DATA e i relativi record sussidiari vengono ignorati

##### REPOSITORY_RECORD

REPOSITORY_RECORD è memorizzato come un record di di Gramps, ad eccezione di quanto indicato in grassetto di seguito.

`   REPOSITORY_RECORD: =`  
`        n @`<XREF:REPO>`@ REPO                            {1:1}`  
`          +1 NAME `<NAME_OF_REPOSITORY>`                  {0:1}`  
`          +1 <`<ADDRESS_STRUCTURE>`>                      {0:1}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          `**`+1 REFN `<USER_REFERENCE_NUMBER>` {0:M}`**  
`            `**`+2 TYPE `<USER_REFERENCE_TYPE>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- REFN, REFN:TYPE e RIN sono ignorati

##### MULTIMEDIA_RECORD

Il MULTIMEDIA_RECORD è memorizzato come record di Gramps , ad eccezione di quanto indicato in grassetto sotto.

`   MULTIMEDIA_RECORD:=`  
`        n @`<XREF:OBJE>`@ OBJE                            {1:1}`  
`          +1 FORM `<MULTIMEDIA_FORMAT>`                   {1:1}`  
`          +1 TITL `<DESCRIPTIVE_TITLE>`                   {0:1}`  
`          +1 <`<NOTE_STRUCTURE>`>                         {0:M}`  
`          +1 <`<SOURCE_CITATION>`>                        {0:M}`  
`          `**`+1 BLOB {1:1}`**  
`            `**`+2 CONT `<ENCODED_MULTIMEDIA_LINE>` {1:M}`**  
`          +1 OBJE @`<XREF:OBJE>`@     /* chain to continued object */  {0:1}`  
`          `**`+1 REFN `<USER_REFERENCE_NUMBER>` {0:M}`**  
`            `**`+2 TYPE `<USER_REFERENCE_TYPE>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**

- Si prevede che ci sarà una etichetta "FILE" per indicare il file contenente l'oggetto multimediale. Questo utilizzo è preso da GEDCOM 5.6.0, ma la capacità in GEDCOM 5.6.0 di avere più di un <MUTIMEDIA_FILE_REFN> e di avere l'integrazione di FORM, TYPE e TITL nel file FILE gedcom_line non è supportata (un FILE successivo potrebbe sovrascriverne uno precedente - non c'è controllo degli errori).
- BLOB è ignorato
- REFN, REFN:TYPE e RIN sono ignorati

##### NOTE_RECORD

NOTE_RECORD è memorizzato come record di Gramps , ad eccezione di quanto indicato in grassetto sotto.

`   NOTE_RECORD:=`  
`        n @`<XREF:NOTE>`@ NOTE `<SUBMITTER_TEXT>`           {1:1}`  
`          +1 [ CONC | CONT] `<SUBMITTER_TEXT>`            {0:M}`  
`          `**`+1 <`<SOURCE_CITATION>`> {0:M}`**  
`          `**`+1 REFN `<USER_REFERENCE_NUMBER>` {0:M}`**  
`            `**`+2 TYPE `<USER_REFERENCE_TYPE>` {0:1}`**  
`          `**`+1 RIN `<AUTOMATED_RECORD_ID>` {0:1}`**  
`          +1 <`<CHANGE_DATE>`>                            {0:1}`

- citazione fonte ignorata
- REFN, REFN:TYPE e RIN sono ignorati

## Esportare dati

L'esportazione consente di condividere qualsiasi parte del database di Gramps con altri ricercatori e di trasferire i dati su un altro computer. Gramps può esportare i dati nei seguenti formati: Gramps [XML](wiki:XML), GEDCOM, pacchetti Gramps [XML](wiki:XML), Web Family Tree, GeneWeb e foglio di calcolo CSV.

Per esportare i dati, selezionare Menu opure usa la [scorrciatoia da tastiera](wiki:Gramps_6.0_Wiki_Manual_-_Keybindings#) . Verrà visualizzata la finestra di dialogo .

### Finestra di dialogo Salvataggio dei dati

![[_media/ExportAssistant-SavingYourData-wizard-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} finestra di dialogo Salvataggio dei dati: schermata iniziale]]

Le pagine della ti guideranno attraverso la selezione del formato (vedi Fig 6.04), la selezione dei file e la formattazione delle specifiche opzioni di esportazione. Dopo una pagina di conferma finale, l'esportazione verrà eseguita in base alle scelte effettuate. In qualsiasi momento, puoi cliccare sul pulsante e modificare qualsiasi selezione, quindi andare avanti per ripetere l'esportazione.

{{-}} ![[_media/ExportAssistant-ChooseTheOutputFormat-wizard-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Finestra di dialogo Salvataggio dei dati: Schemata per la scelta del formato di salvataggio]]

{{-}}

### Filtri e riservatezza

![[_media/ExportAssistantGEDCOM-ExportOptions-40.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Finestra di dialogo Salvataggio dei dati: Opzioni di filtro e riservatezza dell'esportazione]]

Gramps ti permette di esportare un database in formati di file comuni.

Fornisce opzioni che consentono di ottimizzare l'esportazione.

- Filtri su Persone e Note: i filtri consentono di esportare una quantità limitata di dati, in base ai criteri selezionati.

<!-- -->

- Non includere record contrassegnati come privati: selezionare questa casella per impedire che i record privati ​​vengano inclusi nel file esportato.

<!-- -->

- Limitare i dati sulle persone viventi: selezionare questa casella per limitare le informazioni esportate per le persone viventi. Ciò significa che tutte le informazioni riguardanti la loro nascita, morte, indirizzi, eventi significativi, ecc. saranno omesse nel file esportato. Se scegli questa opzione, ti verranno fornite ulteriori opzioni per limitare ulteriormente i dati sulle persone viventi. Ad esempio, puoi scegliere di sostituire la parola **Vivente** al posto del nome proprio (vedi le tue [impostazioni](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Text)); puoi escludere le note; ed è possibile escludere le fonti per le [persone viventi](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive).

<!-- -->

- Non includere record non correlati: selezionare questa casella per impedire che i record non correlati vengano inclusi nel file esportato.

A volte, non è sempre ovvio dai dati se qualcuno è effettivamente vivo. Gramps usa un algoritmo avanzato per provare a determinare [se una persona potrebbe essere ancora viva](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive). Ricorda, Gramps sta facendo la sua ipotesi migliore, e potrebbe non essere sempre in grado di indovinare tutte le volte. Si prega di ricontrollare i dati. {{-}}

### Esportare nei formati di Gramps

- La base di dati Gramps [XML](wiki:XML) per l'esportazione (.gramps): Questo formato è il formato standard per lo scambio di dati e i backup (consultare il relativo formato .gpkg di seguito per una portabilità completa, compresi gli oggetti multimediali). L'esportazione nel formato [XML](wiki:XML) di Gramp produrrà un database portabile. Poiché XML è un formato leggibile dal testo basato su testo, puoi anche usarlo per dare un'occhiata ai tuoi dati. Gramps ti garantisce di poter aprire l'output XML di versioni precedenti di Gramps nella nuova versione di Gramps (non il contrario comunque!).

<!-- -->

- Esportazione del pacchetto Gramps (.gpkg): l'esportazione nel formato del pacchetto Gramps creerà un file compresso contenente il database XML di Gramps e copie di tutti i file multimediali associati. Questo è utile se vuoi spostare il tuo database su un altro computer o condividerlo con qualcuno.

<!-- -->

- Esporta su CD: l'esportazione su CD preparerà il tuo database e le copie di tutti i file oggetto multimediali per la registrazione su un CD. Per masterizzare effettivamente il CD, è necessario accedere alla posizione di GNOME **burn: ///**, alla quale è possibile accedere navigando attraverso Nautilus: Dopo aver esportato su CD, selezionare **Vai -\> CD Creator**nel menu Nautilus. La tua directory di database apparirà. Per masterizzarlo sul CD, fare clic sull'icona del CD sulla barra degli strumenti Nautilus o selezionare **File -\> Scrivi su CD** nel menu Nautilus.

Se durante l'esportazione non viene trovato un file multimediale, verrà visualizzata la stessa finestra di dialogo che si incontra con l'esportazione GEDCOM. {{-}}

### Esportare nel formato GEDCOM

![[_media/ExportAssistantGEDCOM-ExportOptions-40.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Export assistant: GEDCOM Export options]]

Gramps ti permette di esportare una base di dati nel formato GEDCOM comune. Vedi [Gramps and GEDCOM](wiki:Gramps_and_GEDCOM) per una specifica di dati che non viene esportata durante l'esportazione in GEDCOM (usa Gramps XML per un'esportazione completa). Gramps offre opzioni che ti permettono di mettere a punto l'esportazione.

- Filtri su persone e note: i filtri consentono di esportare una quantità limitata di dati, in base ai criteri selezionati.

<!-- -->

- Non includere record contrassegnati come privati: selezionare questa casella per impedire che i record privati ​​vengano inclusi nel file esportato.

<!-- -->

- Limitare i dati sulle persone viventi: selezionare questa casella per limitare le informazioni esportate per le persone viventi. Ciò significa che tutte le informazioni riguardanti la loro nascita, morte, indirizzi, eventi significativi, ecc. saranno omesse nel file esportato. Se scegli questa opzione, ti verranno fornite ulteriori opzioni per limitare ulteriormente i dati sulle persone viventi. Ad esempio, puoi scegliere di sostituire la parola **Vivente** al posto del nome proprio (vedi le tue [impostazioni](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Text)); puoi escludere le note; ed è possibile escludere fonti per [persone viventi](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive).

<!-- -->

- Non includere record non correlati: selezionare questa casella per impedire che i record non correlati vengano inclusi nel file esportato.

{{-}}

### Esportare in altri formati

#### GeneWeb

- GeneWeb: l'esportazione in GeneWeb salverà una copia dei tuoi dati in un popolare formato di genealogia web. Per saperne di più su GeneWeb e il suo formato, visita <http://www.geneweb.org>

#### Foglio di calcolo Gramps CSV

- Foglio di calcolo Gramps CSV: consente di esportare (e importare) un sottoinsieme dei dati di Gramp in un semplice formato di foglio di calcolo. Vedi [CSV importazione ed esportazione](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees:_CSV_Import_and_Export) per maggiori informazioni. Inoltre, vedi [Esporta vista](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Export_View) .

#### Web Family Tree

- Web Family Tree: Esportando in Web Family Tree verrà creato un file di testo che può essere utilizzato dal programma Web Family Tree. Le opzioni di esportazione includono la selezione dei filtri e la possibilità di limitare i dati sulle persone viventi a quelle dei loro legami familiari. Per saperne di più su Web Family Tree e relativo formato, visita <http://www.simonward.com/cgi-bin/page.pl?family/tree>

#### vCard

- vCard: L'esportazione su vCard salverà le informazioni in un formato utilizzato in molte applicazioni di rubrica, a volte chiamato PIM (acronimo di Personal Information Manager, ossia gestore delle informazioni personali). Per maggiori informazioni sul formato vedi: <https://it.wikipedia.org/wiki/VCard>

#### vCalendar

- vCalendar: L'esportazione in vCalendar salverà le informazioni in un formato utilizzato in molte applicazioni di calendario, a volte chiamato PIM (acronimo di Personal Information Manager, ossia gestore delle informazioni personali). Per maggiori informazioni sul formato vedi: <https://it.wikipedia.org/wiki/ICalendar>

{{-}}

## Spostamento di un database di Gramps 2.2 su Gramps 3.x

Per spostare i dati di Gramps dalla versione 2.x alla versione 6.0.x devi importare il database v2.x in un programma precedente di Gramps v3.0.x e quindi salvare il database e importarlo in Gramps 6.0.x, o esportarlo il database in formato [XML](wiki:XML) dalla precedente versione di Gramps e importarlo in Gramps 6.0.x.

Fare riferimento al [Manuale dell'utente](wiki:User_manual) per le versioni precedenti di Gramps per le istruzioni sull'importazione dei database v2.x in Gramps v3.x.

[Category:It:Documentation](wiki:Category:It:Documentation)
