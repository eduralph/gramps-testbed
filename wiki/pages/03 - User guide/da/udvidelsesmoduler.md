---
title: Da:Gramps 6.0 brugsanvisning - Udvidelsesmoduler
categories:
- Documentation
managed: false
source: wiki-scrape
wiki_revid: 128165
wiki_fetched_at: '2026-05-30T17:05:31Z'
lang: da
---

{{#vardefine:chapter\|11}} {{#vardefine:figure\|0}}

Dialogboksen giver dig mulighed for at styre, hvordan Gramps administrerer plugins og tredjepartsudvidelser. Gramps består af en kerne plus mange plugins. Når Gramps starter, indlæses kernen og kun et begrænset antal plugins. Dette reducerer Gramps' opstartstid og hukommelseskrav. Efterfølgende indlæses mange plugins automatisk af Gramps, når der er behov for dem, så mange brugere ikke behøver at være opmærksomme på plugins' eksistens eller deres forsinkede indlæsning.

Dialogboksen er tilgængelig fra menuen . Mange af funktionerne i Udvidelsesmoduler er beregnet til udviklere, og de dialogbokse, der beskrives nedenfor, er dem, som udviklere ser. Funktionerne for normale brugere er angivet nedenfor, hvor de er forskellige. \_\_FORCETOC\_\_

## Registrering og indlæsning

[Plugins](wiki:Da:Gramps_6.0_brugsanvisning_-_Udvidelsesmoduler#Plugin_types) findes enten lokalt på computeren og er kendt af Gramps, når de siges at være registrerede, eller de findes på en fjerncomputer, og Gramps kender kun deres navn, type og beskrivelse, når de siges at være tilføjelser.

Når Gramps starter, læses oplysninger automatisk om de lokale plugins, så de bliver registrerede. Tilføjelsesadministratoren kan bruges til at downloade fjern-tilføjelser, så de også bliver registrerede.

Registrede (f. eks. local) plugins bliver **indlæst** af Gramps i de følgende situationer:

1.  de indlæses automatisk ved opstart. Nogle plugin-typer indlæses ved opstart (f.eks. ikke-skjulte visninger), nogle plugins kan have en markering, der tvinger indlæsning ved opstart,
2.  de indlæses automatisk, når brugeren klikker på en visning eller anmoder om en rapport,
3.  de indlæses, når brugeren eksplicit anmoder om indlæsning i plugin-administratoren,
4.  tredieparts plugins indlæses samtidig med, at de registreres ved hjælp af [Install Addons](wiki:6.0_Addons#Installing_Addons_in_Gramps) i menuen .

## Udvidelsesmodul vindue

vindue gør det muligt at kontrollere hvordan Gramps håndterer plugins og tredieparts tilføjelser. Udvidelsesmodulet har to faner:

- og

- 

### Registrerede plugins

![[_media/PluginManager-RegisteredPlugins-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} "Registered Plugins" tab (developer mode)]]

Her ser du en liste over alle plugins, som Gramps har fundet. Dette er de plugins, der er en del af Gramps, samt de plugins/tilføjelser, der findes i mappen `gramps60/plugins` i [Gramps-brugermappen](wiki:Da:Gramps_6.0_brugsanvisning_-_Gramps-brugermappen). Plugin-typen vises i den første kolonne.

Du kan vise eller skjule et plugin ved at vælge en række og trykke på knappen Skjul/Vis. Dette er kun nyttigt for brugerplugins.

By selecting a row and double clicking or pressing the button you will be shown the dialog.

Use the button to exit. The button .... does?

In [developer mode](wiki:Gramps_6.0_Wiki_Manual_-_Plugin_Manager#User_mode_or_Developer_mode) two additional buttons are shown they are:

- \- Which will load the selected rows source code file in your associated text editor.

- \- Forces a reload the selected plugin/addon.

{{-}}

### Indlæste plugins

## Handlinger

### Skjul / vis

### Detaljeret Info vindue

## Plugin typer

Der er to hovedkategorier af plugins i Gramps: **[Bruger plugins](wiki:Da:Gramps_6.0_brugsanvisning_-_Udvidelsesmoduler#Bruger_plugins)** og **[System plugins](wiki:Da:Gramps_6.0_brugsanvisning_-_Udvidelsesmoduler#System_plugins)**. **Bruger plugins** er dem du anvender eller benyttes til at opnå forskellig funktionalitet i Gramps. **System plugins** anvendes internt i Gramps.

Der er mange plugins, der følger med Gramps. Men alle kan også skrive en plugin og dele den. Disse tredjeparts-plugins kaldes »addons«. Vi opfordrer brugere og udviklere til at dele deres kreationer med andre Gramps-brugere.

See also:

- [Addon_list_legend#Type](wiki:Addon_list_legend#Type)
- [Addons development](wiki:Addons_development)
  - [Addons_development#What_can_addons_extend.3F](wiki:Addons_development#What_can_addons_extend.3F)

### Bruger plugins

De følgende **Bruger plugins** typer findes i Gramps:

1.    
    Backends for which Gramps can write reports (pdf, odf, ascii text, ...)

2.    
    export formats you can export your data too via menu

3.    
    small programs you can embed in the Dashboard View, or detach and use as a normal window

4.    
    the views visible in the main window of Gramps

5.    
    import formats from which Gramps can import data via menu

6.    
    targets that can be used on the place view to go to an internet map service (*Go* toolbar button)

7.    
    know as *Quick Views* they are small reports that are available in the context menu on the listviews, or via the Quick View gramplet

8.    
    Textual or graphical reports Gramps can produce

9.    
    Tools you can start via the menu

### System plugins

The following types of **System Plugins** are present in Gramps:

1.    
    Backends that allow Gramps to support [alternate database types](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Family_Tree).

2.    
    libraries that are present giving extra functionality.

3.    
    relationship calculators for different languages

4.    
    rules for custom filters

5.    
    Citation formatter

6.    
    thumbnail generation for previews of media

## Bruger tilstand eller udvikler tilstand

{{-}}

[Category:Documentation](wiki:Category:Documentation)
