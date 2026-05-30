---
title: Da:Gramps 6.0 brugsanvisning - Sandsynligvis i live
categories:
- Documentation
managed: false
source: wiki-scrape
wiki_revid: 128318
wiki_fetched_at: '2026-05-30T17:05:10Z'
lang: da
---

{{#vardefine:chapter\|7}} {{#vardefine:figure\|0}} Levetidsstatus for personerne i en Gramps-database er vigtig, når du har brug for at dele dine data med andre, men ønsker at beskytte oplysningerne om dem, der er i live. Det bruges også i nogle rapporter. Af disse grunde har Gramps nogle værktøjer, der kan hjælpe dig med at bestemme, om nogen er i live.

## Hvordan bestemmer Gramps, om nogen er i live?

![[_media/EditPreferences-Limits-tab-default-60-da.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Rediger &gt; Indstillinger..." - fanen "Grænser" - standardindstillinger]]

En simpel måde at se, om nogen er i live, er at se, om de har en dødsbegivenhed eller en dødsrelateret begivenhed (såsom en begravelse). Det er dog sandsynligvis sandt, at mange personer i din database ikke har sådanne begivenheder, da du muligvis ikke kender nogen detaljer om deres død. Hvis du ved, at nogen er død, kan det være en god idé at oprette en dødsbegivenhed. Du kan også gå tilbage og tilføje nyttige detaljer (såsom dødsdato og -sted), når disse er kendte. Det er noget nyttigt at tilføje begivenheder for personer, der er kendt afdøde, selvom de ikke indeholder nøjagtige detaljer. Gramps kan dog også tilføje begivenheder med estimerede datoer (eller ej) til dig (beskrevet nedenfor).

At kræve, at en bruger manuelt tilføjer en dødsbegivenhed til en person (så de ikke betragtes som levende) ville være meget besværligt --- man ville være nødt til at indtaste oplysninger om mange personer. Husk, at hvis nogen betragtes som levende, bør deres oplysninger forhindres i at blive delt ved eksport. Derfor har Gramps en funktion, der kan beregne, om nogen sandsynligvis er i live baseret på deres begivenhedsdatoer eller deres relationer til personer, der kan have begivenhedsdatoer. For eksempel, hvis en person ikke har nogen beviser for død (såsom en døds- eller begravelsesbegivenhed), vil Gramps kontrollere denne persons forældre, børn, søskende kontinuerligt, indtil der findes beviser --- eller den løber tør for forbindelser at kontrollere. Ved at bruge information om typisk alder og begivenhedsspænd (såsom typiske aldersforskelle mellem søskende, typisk alder på mødre ved fødselstidspunktet osv.) kan Gramps gætte på, om en person er i live eller død. Som du kan forestille dig, kan dette være en tidskrævende funktion at udføre, men den kan være ret nyttig. Værdierne for de typiske aldre ved fødslen, mellem generationer osv. kan indstilles i fanen .

Funktionen "sandsynligvis i live" kan kontrollere, om en person var i live på en bestemt dato eller i et bestemt tidsrum. Dette bruges i [Age on Date](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Age_on_Date) Gramplet. Normalt vil systemet estimere fødsels- og dødsbegivenheder og se, om en dato falder mellem disse to.

Der er dog et særligt tilfælde: Hvis du leder efter personer, der sandsynligvis er i live "i dag", og de har en dødsbegivenhed, betragtes de som døde uanset hvad (selvom begivenheden ikke har en dato). Derfor får du forskellige resultater, hvis du ser, hvem der sandsynligvis var i live i går (eller sidste år) sammenlignet med, hvem der betragtes som i live i dag. Årsagen til dette er, at hvis du har en dødsbegivenhed, ved du, at en person døde i fortiden, men du ved ikke hvornår. Hvis du ser, om en person var i live i fortiden (i går og før), kan du ikke sige med sikkerhed, om de var døde dengang, uden at kende en dødsdato.

Hvis du vil vide detaljerne om, hvorfor Gramps har fastslået, om en person er i live eller død, kan du bruge værktøjsudvidelsen til at få en forklaring. Dette vil vise de estimerede fødsels- og dødsdatoer og relationen til en person, der har en begivenhedsdato, som disse er baseret på. {{-}}

## Sandsynligvis levende proxy

Det første værktøj er "Sandsynligvis levende" proxyen. Denne bruges automatisk, når du eksporterer dine data til et format, der understøtter muligheden for at begrænse oplysninger om levende personer. Proxyen indkapsler databasen i et lag, der forhindrer adgang til følsomme oplysninger om levende personer, såsom deres fornavn og deres begivenheder. {{-}}

## Filter for sandsynligt levende

Dagens dato behandles specielt i tilfælde af begivenheder uden datoer og kontrol af status for levende i fortiden. Hvis en person f.eks. har en dødsbegivenhed uden dato, ved vi, at personen er død i dag og altid i fremtiden. Men for de funktioner, hvor du kan kontrollere, om en person var i live på en dato i fortiden, kan vi ikke sige, om de var i live eller døde på den dato. Så hvis du har en dødsbegivenhed uden dato og kontrollerer, om de var i live i går, vil Gramps ikke være i stand til at bestemme status for levende/død.

Se:

- [Filter for personer sandsynligvis i live](wiki:Da:Gramps_6.0_brugsanvisning_-_Filtre#People_probably_alive)

{{-}}

## Kalender Gramplet

Se [Kalender](wiki:Da:Gramps_6.0_brugsanvisning_-_Gramplets#Kalender) gramplet. {{-}}

## Redigere datoer

Se [Redigere datoer](wiki:Da:Gramps_6.0_brugsanvisning_-_Indtaste_og_redigere_data:_detaljeret_-_del_1#Redigering_af_datoer).

[Category:Documentation](wiki:Category:Documentation)
