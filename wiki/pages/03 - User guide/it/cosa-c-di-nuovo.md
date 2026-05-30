---
title: It:Manuale Wiki per Gramps 6.0 - Cosa c’è di nuovo?
categories:
- It:Documentation
managed: false
source: wiki-scrape
wiki_revid: 111161
wiki_fetched_at: '2026-05-30T19:29:33Z'
lang: it
---

Questa sezione fornisce una panoramica dei cambiamenti di Gramps dalla versione 4.2. Questi cambiamenti sono descritti approfonditamente anche più avanti in questo manuale. Gli utenti di Gramps che vogliono aggiornare il programma da versioni precedenti sono incoraggiati a leggere questa sezione per essere sicuri di trarre vantaggio dalle nuove funzionalità iniziando ad utilizzare la versione 6.0.

# Prima di aggiornare

Prima di eseguire l'aggiornamento, assicurarsi che i dati del vostro albero genealogico siano al sicuro. Il modo migliore per farlo è:

1.  Avviare Gramps 3.4 or Gramps 4.2
2.  Aprire il vostro albero genealogico
3.  Eseguire il backup dell'albero con il formato *Gramps xml* o *Gramps pacchetto XML* ( il *pacchetto di Gramps XML* include le vostre foto e gli altri file multimediali associati con i vostri dati dell'albero genealogico). Eseguire il backup dell'albero tramite il menu .
4.  Chiudi questo albero genealogico e ripeti i passi precedenti per ogni albero genealogico che si voglia preservare
5.  Copia i file prodotti in un luogo sicuro

Per maggiori informazioni, consultare [Fare una copia di sicurezza di un Albero Genealogico](wiki:It:Manuale_Wiki_per_Gramps_6.0_-_Gestire_gli_Alberi_genealogici#Fare_una_copia_di_sicurezza_di_un_Albero_Genealogico)

Dopo aver salvaguardato correttamente i dati, procedere con l'installazione Gramps 6.0. Si consiglia di utilizzare il processo di installazione standard del sistema operativo in modo che la nuova installazione di Gramps 6.0 non vada in conflitto con la versione precedente di Gramps. Tuttavia, può essere più sicuro disinstallare Gramps 3.4 prima di installare Gramps 6.0, o assicurarsi di installare Gramps 6.0 in una posizione diversa. Ciò è sempre necessario se si esegue l'installazione dal codice sorgente. Per ulteriori informazioni sull'installazione Gramps 6.0, consulta [Scarica l'ultima versione di Gramps](wiki:Download/it)

Dopo aver installato Gramps 6.0, è possibile aprire gli alberi genealogici esistenti e continuare a lavorare. In caso di problemi (ad esempio, dopo un aggiornamento del sistema completo), importare il file di backup creato in precedenza per ricreare il tuo albero genealogico.

# Cambiamenti visibili al nucleo

I cambiamenti apprezzabili dopo la migrazione alla nuova versione riguardano: interfaccia e dati.

## Struttura dei Dati

Ci sono variazioni nella struttura dei dati (se presenti):

1.  Nessun cambiamento

<hr>

- Un Albero genealogico **non può essere aperto** in Gramps 3.4/4.0/4.1/4.2 e Gramps 6.0 senza un aggiornamento.

<!-- -->

- Un downgrade può essere eseguito solo esportando XML e importando la versione precedente.

<!-- -->

- Un file XML generato da Gramps 3.4/4.0/4.1 **non è identico** ad uno generato da Gramps 6.0.

<!-- -->

- Gramps 6.0 è ora solo **python3**

Consultare [maggiori dettagli (inglese)](wiki:Database_Formats#Detailed_Changes) per maggiori dettagli sul database.

## Modifiche primarie

- Ora puoi scegliere di utilizzare database alternativi. BSDDB è ancora l'impostazione predefinita, ma Sqlite è ora disponibile. Per utenti esperti, PostgreSql e MongoDB sono disponibili come componenti aggiuntivi sperimentali di terze parti.

Gli sviluppatori ritengono che Sqlite possa avere meno corruzioni che impediscono un facile recupero.

- Opzioni per la copia di sicurezza automatica periodicamente e all'uscita. La copia di sicurezza all'uscita è l'impostazione predefinita.

<!-- -->

- Preferenze: nuova opzione database-copia di sicurezza-utilizzo-compressione.

 

## Interfaccia grafica utente

- I nuovi schemi di colori consentono una scelta chiara e una scura.
- Ulteriori indicazioni di colore nei grafici per la persona Predefinita, Sconosciuto in vita, Famiglia, Famiglia divorziata.
- Aggiunto il filtro "entro <n> km / miglia / gradi".
- Possibilità di poter inserire coppie di latitudine / longitudine separate da virgola.
- La sidebar si ridimensiona meglio, la posizione viene ricordata.
- L'editor del Cognome Persona è più intuitivo da usare.
- L'ordine dei Pulsanti visualizzati non cambia più con avvii diversi.
- Migliore indicazione del progresso per le operazioni di lunga durata.
- Memorizza la dimensione / posizione della finestra.
- Aggiunto FanChart2Way.
- Aggiungi kmls per la vista dei luoghi geografici.

## Luoghi

- Possibilità di cercare nomi di luoghi alternativi quando si seleziona un luogo.

## Resoconti, Strumenti, Gramplets

- Nuovo Resoconto dell'albero genealogico.
- Editor formato luoghi e opzioni per molti report.
- Editor formato data e opzioni per molti report.
- Opzione su come segnalare persone viventi per molti rapporti.
- Lo strumento ReorderIDs è stato aggiornato; ora può lavorare su ID personalizzati (come gli ID GetGov).
- Il sito web narrativo ha opzioni aggiuntive e cambiamenti di aspetto
  - Consente l'output in una lingua diversa
  - Opzione di output data
  - Pagina delle statistiche
  - Aggiungi l'opzione a Includi tutti gli oggetti Multimedia non referenziati
  - Relazione con la persona centrale su singole pagine
- Aggiunta l'opzione dimensione miniatura al grafico delle linee familiari
- Migliorare il rapporto discendente e il rapporto dettagliato discendente
- Aggiunte opzioni al Rapporto Individuale Completo
  - abilita a includere o escludere note personali e familiari
  - aggiungi l'opzione per includere o escludere i dati del censimento
  - opzione per includere la relazione con la persona centrale
  - opzioni per includere GrampsID, Tags, Attributi
- Includere tutti i tipi di luogo nel rapporto sul luogo
- Opzioni su come disegnare le linee in Relazioni, linee familiari, grafici a clessidra.

## Importa/Esporta

- Gedcom supporta più "tag" non standard e tag standard aggiuntivi
- GEDCOM 5.6.0 supporta l'esportazione di eventi personalizzati
- Nuova opzione di compressione nella esportazione XML

## Nuovi Addons

- Vista grafico trapunta: la vista mostra una visualizzazione del grafico a trapunta di un albero genealogico
- Plugin Manager Enhanced: un Addon / Plugin Manager con diverse funzionalità aggiuntive
- Albero Clessidra: albero Clessidra che utilizza il genealogytree LaTeX
- Strumento di importazione e unione: confronta un database XML di Gramp con quello attuale e consente di unire le differenze.
- Controlla i dati delle associazioni: controllerà i dati sull'associazione per le persone.

# Modifiche del motore

Cambiamenti tecnici

- Numerose modifiche relative al supporto per altri database (Sqlite, PostgreSQL, MongoDB ecc.).
- Alcune correzioni del database (gestione agli oggetti inesistenti) precedentemente nascosti ora sono considerati errori. Potrebbe essere necessario eseguire lo strumento Controlla e Ripara il database per correggere le eccezioni con un database danneggiato.
- Correzioni per impedire all'utente di chiudere o modificare il database durante operazioni a lungo termine.

## Dipendenze

- Supporta solo **python3**. ( supporto a python2 dismesso)
- Necessita di GTK+ 3.10 epygobject 3.12 o versioni più recenti.

# Modifiche del motore

Parte tecnica

## Dipendenze

- Supporta solo **python3**. (non supporta più python2)
- Necessita di GTK+ 3.10 e pygobject 3.12 o versioni successive

# Ulteriori informazioni

Maggiori informazioni per sviluppatori in lingua inglese.

## Miscellaneous

- Optimizations around index, Flat and TreeView models
- More data into *example.gramps*: custom parent relationship, notes.
- New test file: *datetest.gramps*
- New module: *[gen.lib.placename](https://github.com/gramps-project/gramps/blob/master/gramps/gen/lib/placename.py)*
- All importers return now an [ImportInfo](https://github.com/gramps-project/gramps/blob/master/gramps/gen/utils/libformatting.py#L201) object that can hold information about the import.
- Experimental gwplus (geneweb) import file format support
- libgedcom changes ???
- Remove fallback to md5 module, all supported versions now include the hashlib module.
- Removed experimental [HTML renderer view](wiki:Addon:HtmlView)
- New test scripts

## Localization

- Limit usage of markup into messages, better separation of content (str) and style (GUI).
- New [Date Handler](wiki:Date_Handler) for [Japanese](https://github.com/gramps-project/gramps/blob/master/gramps/gen/datehandler/_date_ja.py)
- Review on Slovenian and Czech Date Handlers
- New translations and date handlers : implement both "traditional" and "simplified" Chinese
- Serbian review

## Roadmap

- [Roadmap](wiki:Roadmap): [6.0.0](http://www.gramps-project.org/bugs/roadmap_page.php?version_id=53)

## Changelog

- [Changelog 6.0.0](http://www.gramps-project.org/bugs/changelog_page.php?version_id=53)

[Category:It:Documentation](wiki:Category:It:Documentation)
