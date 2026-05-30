---
title: Sq:Gramps 6.0 Wiki Manual - Manage Family Trees
categories:
- Sq:Documentation
managed: false
source: wiki-scrape
wiki_revid: 120305
wiki_fetched_at: '2026-05-30T20:50:48Z'
lang: sq
---

Tani të kthehemi te një eksplorim më i detajuar të përdorimit të zakonshëm të Gramps. Në këtë kapitull japim një përmbledhje të detajuar të asaj se si mund të menaxhoni pemët tuaja familjare, si dhe të ndani të dhënat tuaja me gjenealogji të tjera.

## Nis një Pemë të re familjare

![[_media/Dbmanager01_sq.png|Fig. 6.0. Nisja e pemës familjare]]

Për të nisur një Pemë të re familjare, zgjidh **Pemë familjare -\>Menaxho Pemët familjare** ose përzgjedh butonin nga shiriti i veglave. Kjo do të hapë menaxhuesin e Pemës familjare.

Përzgjedh butonin dhe Gramps do të shtojë një qasje të re të Pemës familjare në listën e Pemëve familjare. Për të ndryshuar emrin e tij nga parazgjedhja *Pema familjare 1*, kliko mbi emrin dhe shtyp një emër të ri.

Tani përzgjedh për të hapur një Pemë familjare të re dhe të zbrazët.

## Hap një Pemë familjare

Për të hapur një pemë familjare, zgjedh **Pemë familjare -\>menaxho pemët familjare** ose kliko butonin në shiritin e veglave. do të shfaqet dhe ju do të shihni një listë të të gjitha Pemëve familjare të njohura për Gramps. Një ikonë do të afishojënë shtyllën e pranë ndonjë Peme familjare e cila aktualisht është e hapur. Përzgjedh pemën që doni ta hapni, dhe hapeni atë duke përzgjedhur butonin . Si alternative, mund të klikoni dy herë mbi Pemën e dëshiruar.

Për të hapur një Pemë familjare të kapur kohën e fundit, zgjedh **Pemë familjare -\>Hap të fundit** ose rreshtin e poshtëm pranë butonit dhe përzgjedh Pemën familjare nga lista.

Nëse nuk keni të "drejtën e shkrimit" për Pemën familjare të përzgjedhur, do të hapet vetëm në gjendjen Vetëm Lexim. Në këtë gjendje, të dhënat mund të shifen por nuk dot të bëhen ndryshime në Pemë. Për ta dëshmuar këtët gjendje, titulli i dritares kryesore do të hapet me tekst**(Vetëm Lexim)** .

## Hapja e të dhënave GEDCOM ose XML

Gramps ju mundëson të hapni baza të dhënave të caktuara të cilat nuk kanë qenë të ruajtura në formatin e vet Gramps-it nga vija e komandës. **PËR TË BËRË lidhet me faqen për të sqaruar si.** Këto përfshijnë baza të të dhënave XML dhe GEDCOM. Por duhet të keni kujdes se nëse baza e të dhënave XML apo GEDCOM është relativisht e madhe, do të hasni në probleme me performancën, dhe në ngjarje kur të bëhet një përplasje, të dhënat tuaja mund të prishen. Prandaj, nomralisht është më mirë të krijoni një pemë të re familjare (bazë të të dhënave) Gramps dhe të importoni të dhënat tuaja XML/GEDCOm në të.

## Heqja e Pemës familjare

Përzgjidh pemën familjare që doni ta largoni, dhe kliko butonin .

Kjo do të largojë **plotësisht** pemën me pamundësi për të rinxjerrur të dhënat. Merrni në konsideratë të merrni një rezervë nga të dhënat tuaja duke eksportuar në formatin XML të Gramps, dhe të klasifikoni skedarin.

## Riemërimi i një Peme familjare

Mund të riemëroni një Pemë familjare (ose një arkive nga ajo) duke pëzgjedhur pemën që doni ta riemëroni dhe duke klikuar . Gjithashtu mund të klikoni mbi emrin në listën e pemëve.

Në secilin rast, vetëm shtypni emrin e ri për të pasur efekt.

## Krijimi i kopjes rezervë të Pemës familjare

- Mënyra më e sigurtë për të krijuar një kopje rezervë të Pemës tuaj familjare Gramps është të eksportoni në formatin **Gramps XML** (ose **Paketën Gramps** për të përfshirë artikuj nga galeria juaj) dhe të kopjoni skedarin që del si rezultat në një vend të sigurtë, and copy the resultant file to a safe place, preferohet në një konstruksion të ndryshëm.

### Backup dialog

Simply select "Make Backup..." from the "Family Trees" menu item.

![[_media/MakeBackup-GrampsXML-Backup-example-60.png]]

You can either choose to include the media or not.

Note that this is just a regular XML export, except that no data is filtered out. You can import these as usual with any exported file.

You can also define the pattern for the backup filename by setting the *paths.quick-backup-filename* in the ~/.gramps/gramps34/gramps.ini key file like the following:

`[paths]`  
`quick-backup-filename='%(filename)s_%(year)d-%(month)02d-%(day)02d.%(extension)s'`

You can use any of the following keywords in the pattern: year, month, day, hour, minutes, seconds, filename, extension.

  

- Mund të përdorni tiparin Arkivë për të ruajtur pamjet e çastit të pemës tuaj. Këto pamje të çastit mund të përdoren si kopje rezerve të thjeshta, dhe shumë të dobishme nëse doni të provoni diçka që më vonë do të doni ta zhbëni. Megjithatë kjo metodë nuk duhet të përdoret për kopje rezervë standarde, meqë nuk do të përballojë një thyerje të diskut të ngurtë ose shumicës së fatkeqësive të tjera që mund t'i ndodhin kompjuterit.

<!-- -->

- *Për përdorues të avancuar:* çdo bazë e të dhënave ruhet në nëndirektoriumin e vet nën ~/.gramps. Një kopje rezervë e udhëzimit mund të bëhet duke krijuar kopje rezervë të këtij direktoriumi.

## Arkivimi i Pemës familjare

Lehtë mund të arkivoni dhe të shënoni sipas kohës pemë familjare me një përdorim të ndërtuar në Gramps të [GNU Sistemit të ripunuar kontrrollues](http://www.gnu.org/software/rcs/)ose *RCS*. Që kjo të jetë e mundshme, kjo gjë e dobishme duhet të instalohet në kompjuterin tuaj.

Për të bërë një arkivë, së pari sigurohu që pema që dëshironi ta arkivoni të jetë e hapur. Pastaj përzgjedh hap pemën familjare dhe kliko butonin . Arkiva do të vendoset në listë nën pemën prej së cilës u krijua. Arkivat mund të hiqen dhe të riemërohen.

## Restaurimi i një arkive të Pemës familjare

![[_media/ManageFamilyTrees-Archive-Selected-to-Extract-example-60.png|Fig. 6.0 Përzgjedhja e një verzioni për ta restauruar]] Thjesht thekso arkivën që doni ta restauroni, dhe përzgjedh butonin . ![[_media/ManageFamilyTrees-Archive-Extracted-version-selected-example-60.png|Fig. 6.0 Verzioni i restauruar]]

Gramps do të transferojë arkivën në një Pemë të re familjare. Emri i Pemës familjare bazohet në emrin origjinal dhe në emrin e arkivës.

## Zhbllokimi e një Peme familjare

Kur Gramps hap një pemë, ajo e bllokon pemën, duke ju parandaluar juve apo dikë tjetër që ta hapni atë në të njejtën kohë. Një kopje e dytë e Gramps do të ketë mundësi të hapë një tjetër pemë familjare, por pema tashmë e hapur do të shfaqet me ikonën e bllokimit, që ju regon se nuk mund ta hapni atë. Duke mbyllur pemën në kopjen e parë të Gramps do të bëjë të mundshme të hapet në kopjen e dytë.

Nëse do të kishit mundur të hapni Pemën e njejtë familjare në dy Gramps përnjeherë, ëshët e mundshme që të dhënat tuaja të humbin.

Në një ngjarje të pashpresë të një dështimi të Gramps, pema familjare do të mbetet në gjendje të bllokuar. Për ta hapur pemën, përzgjedh pemën familjare të bllokuar, dhe kliko butonin i cili do të jetë i mundshëm. Veproni kështu vetëm nëse jeni të sigurtë se asnjë kopje tjetër e Gramps nuk është duke e përdorur këtë pemë familjare.

## Riparimi i një Peme familjare të dëmtuar

![[_media/FamilyTreesManager-Dialog-ShowingRedErrorStatusIcon-Sample-50.png|Fig. 6.0 Riparimi i një Peme familjare]]

Nëse Pema juaj familjare do të dëmtohet ose do të prishet në njëfarë mënyre, menaxhuesi e Pemës familjare të Gramps do të afishojë një ikonë të kuqe për Gabime në shtyllën e .

Për t'i thënë Gramps të përpiqet të riparojë dëmin, përzgjedh Pemën dhe pastaj kliko butonin .

Kjo do të përpiqet të rindërtojë pemën tuaj nga skedarët rezervë që krijohen automatikisht në dalje.

## Ruajtja e ndryshimeve në Pemën tuaj familjare

Gramps ruan ndryshimet sapo t'i aplikoni ato. Kjo do të thotë, për shembull, që çdoherë që klikoni kur përdorni Gramps, ndryshimet tuaja menjëherë regjistrohen dhe ruhen. Nuk ka komandë të veçantë "ruaj".

Mund të zhbëni ndryshimet që keni bërë duke përzgjedhur **Redakto -\>Zhbëj**. Nëse vazhdimisht e përzgjedhni këtë komandë, ndryshimet tuaja të fundit do të zhbëhen një nga një. Për të filluar përsëri komanda të shumëfishta përnjëherësh, mund të bëni atë duke përdorur dialogun i cili është i mundshëm nga menyja .

Nëse doni ta ktheni Pemën tuaj familjare në atë gjendje që ka qenë kur e keni hapur, përzgjedh, **Skedar -\>Heq dorë nga ndryshimet dhe braktis** . (Kjo është sikur kur e braktisni pa ruajtur në programe tjera.)

Nës do të donit të ruani një kopje të Pemës tuaj familjare me një emër tjetër, do të duhet të eksportoni atë dhe pastaj të importoni në një Pemë të familjare të re. Formati i *bazës së të dhënave XML të Gramps* rekomandohet për këtë qëllim.

## Importimi i të dhënave

Importimi ju mundëson të sjellni të dhëna nga programe tjera gjenealogjike në një bazë të të dhënave Gramps. Aktualisht, Gramps mund të importojë nga formatet në vazhdim:

Baza e të dhënave GRAMPS V2.x (.grdb prapashtesë e skedarit)

GEDCOM (.ged prapashtesë e skedarit)

Gramps XML (.gramps prapashtesë e skedarit)

Paketa Gramps (.gpkg prapashtesë e skedarit)

GeneWeb (.gw prapashtesë e skedarit)

Fletëllogaritëse Gramps CSV - vlera të ndara me presje (.csv prapashtesë e skedarit)

Pro-Gen (.def prapashtesë e skedarit)

Për të importuar të dhëna, përzgjedhni **Skedar -\>Importo** . Dialogu **Importo baza të të dhënave** do të hapet, duke kërkuar që të përcaktoni skedarin që dëshironi ta importoni. Kujdes, mund të importoni të dhëna vetëm në një bazë të të dhënave që ekziston, pra nëse transferoni të gjitha të dhënat tuaja nga një program tjetër ose nga ndonjë verzion më i vjetër i Gramps, atëherë së pari krijo një bazë të zbrazët të të dhënave dhe pastaj importo të dhënat në të.

Baza e të dhënave GRAMPS V2.x, Gramps XML, dhe paketa Gramps, të gjitha janë formate amëtare të Gramps. Nuk ka rrezik për humbjen e informacioneve kur bëhet importimi nga këto formate ose eksportimi në to.

- Baza e të dhënave GRAMPS V2.x (grdb): Para Verzionit 6.0, ky format i bazës së të dhënave amë të Gramps ishte një formë e veçantë e bazës së të ghënave Berkeley (BSDDB) me një strukturë të veçantë të tabelave të të dhënave. Ky format ishte i varur nga arkitektura binare. Ishte shumë i shpejtë dhe me efekt, por në përgjithësi jo i kalueshëm nëpër kompjuterë me arkitekturë të ndryhme binare.(sh. i386 vs. alfa).

<!-- -->

- Gramps XML: Skedari Gramps XML ishte formati i përzgjedhur për verzionet më të vjetra (para 2.x) të Gramps. Ndryshe nga formati grdb, është i varur nga ndërtimi dhe e lexueshme. Baza e të dhënave gjithashtu mund të ketë referenca në media objekte jo vendore(të jashtme), prandaj nuk garanton se mund të jetë plotësisht e depërtueshme. Baza e të dhënave Gramps XML formohet me eksportimin ( **Pemë familjare -\>Eksporto...** ) në atë format.

<!-- -->

- Paketa Gramps: Paketa Gramps është arkivë e ngjshur që përmban skedar Gramps XML dhe të gjitha media objektet (imazhe, skedarë zëri, etj.) ku përcillet baza e të dhënave. Për shkak se përmban të gjitha media objektet, ky format është plotësisht i depërtueshëm. Paketa Gramps krijohet me eksportimin ( **Pemë familjare -\>Eksporto...** ) e të dhënave në atë format.

Nëse importoni informacione nga një tjetër bazë e të dhënave Gramps apo Gramps XML, do të shihni ecurinë e operacionit në shiritin e ecurisë të dirtares kryesore të Gramps.

Formati i fletëllogaritëses Gramps CSV ju mundëson importimin dhe eksportimin të një nëngrupi të të dhënave tuaja Gramps Gramps në një format të thjeshtë të fletëllogaritëses. Shih [Importi dhe Eksporti i CSV](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees:_CSV_Import_and_Export) për më shumë informacione.

## Eksportimi i të dhënave

![[_media/ExportAssistant-ChooseTheOutputFormat-wizard-60.png|Fig.6.0 Ndihmësi për eksportim: Përzgjedhja e formateve]]

Eksportimi ju mundëson të ndani ndonjë pjesë të bazës së të dhënave tuaja të Gramps me hulumtime tjera database si dhe për t'ju mundësuar që të transferoni të dhënat tuaja në tjetër kompjuter. Aktualish, Gramps mund të eksportojë të dhëna në formatet në vazhdim: Gramps XML, GEDCOM, paketa Gramps, Web Pema familjare, GeneWeb, dhe formatet Fletëllogaritëse Gramps CSV.

Për të eksportuar të dhëna, zgjedh **Skedar -\>Eksporto** . Kjo do të sjellë ndihmësin **Eksporto** . Faqet e tija do t'ju udhëheqin përmes përzgjedhjes së formateve (shih *eksporto-druid-fig* ), seksione të skedarëve, dhe ospione të veçanta eksportimi (shih *gedcom-eksporto-fig* ). Pas faqes së fundit të konfirmimit, eksportimi do të kryhet sipas zgjedhjeve që keni bërë. Në çdo kohë, mund të klikoni në butonin dhe përsërit përzgjedhjen, pastaj vazhdo më tej për të ribërë eksportin.

### Filters and Privacy

Gramps ju mundëson të eksportoni një bazë të të dhënave në formatin e zakonshëm. Ajo siguron opsione që ju mundësojnë t'i akordoni mirë eksportin tuaj.

- Filtër: Filtri ju mundëson të eksportoni një sasi të kufizuar të të dhënave, bazuar në kriteret që përzgjedhni.

<!-- -->

- Mos përfshij regjistrime të shënuara si private: Kontrrollo këtë kuti për të parandaluar regjistrimet private të përfshihen në skedarin e eksportuar.

<!-- -->

- Kufizo të dhëna për njerëzit që jetojnë: Kontrrollo këtë kuti për të kufizuar informacionin e eksportuar për njerëzit që jetojnë. Kjo dë të thotë që të gjitha informacionet sa i përket lindjes së tyre, vdekjes, adresat, ngjarjeve të rendësishme, etj., do të hiqen në skedarin e eksportuar të GEDCOM. Nëse zgjedhni këtë opsion, do t'ju jipet opsione shtesë për të kufizuar më tej të dhënat për njerëzit që jetojnë. Për shembull, mund të zgjedhni ta zëvendësoni fjalën "Që jetojnë" për emrin e parë; mund të përjashtoni shënime; dhe mund të përjashtoni burime për njerëzit që jetojnë.

Ndonjëherë, nuk është gjithmonë e qartë nga të dhënat nëse dikush është vërtet gjallë. Gramps përdor një algoritëm të avancuar për të provuar të përcaktojë nëse një njeri mund të jetë ende gjallë. Mbaj mend, Gramps po bën gjetjen më të mirë të tij, dhe mund të mos ketë mundësi që gjithmonë të gjejë me saktësi. Ju lutem kontrrolloni dy herë të dhënat tuaja. [Probably alive](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive)

### Eksporto në formate Gramps

- Eksporti i bazës së të dhënave Gramps XML: Eksportimi në formatin Gramps XML do të krijojë një bazë të të dhënave të pajtueshëm më versionin e mëparshëm të Gramps. Përderisa XML është një format i bazuar në tekst dhei lexueshëm, gjithashtu mund ta përdorni për të shikuar të dhënat tuaja.

<!-- -->

- Eksporti i paketës Gramps: Eksportimi në formatin e paketës Gramps do të formojë një skedar të ngjedhur që përmban bazë të të dhënave dhe kopje të të gjitha media skedarëve të bashkuar. Kjo është e dobishme nës doni të zhvendosni bazën e të dhënave tuaja në kompjuter tjetër apo ta ndani atë me dikë.

<!-- -->

- Eksporto në CD: Eksportimi në CD do të prgatitë bazën e të dhënave tuaja dhe kopjet e të gjitha skedarëve të media objekteve për t'i regjistuar në një CD. Për ta djegur CD, duhet të shkoni në vendndodhjen e GNOME **digje:///** , e cila mund të hyjë duke naviguar nëpër Nautilus: Pas eksportimit në CD, përzgjedh **Shko -\>Krijues i CD** në menynë e Nautilus-it. Do të shfaqet direktoriumi i bazës së të dhënave tuaja. Për ta djegur atë në CD, kliko në ikonën e CD shiritin e veglave të Nautilus, ose përzgjedh **Skedar -\>Shkruaj në CD** në manynë Nautilus.

Nëse një media skedar nuk gjindet gjatë eksportimit, do të shihni dialogun**Media e humbur**.

### Eksportim në formatin GEDCOM

![[_media/ExportAssistantGEDCOM-ExportOptions-40.png|Fig.3.5.Ndinmës i eksportit: opsionet e GEDCOM]]

Gramps ju mundëson të eksportoni një bazë të të dhënave në formatin e zakonshëm të GEDCOM. Ajo siguron opsione që ju mundësojnë t'i akordoni mirë eksportin tuaj (shih \[imazh:Gedcom-eksport.png\]gedcom-eksport-fig'' ).

- Filtër: Filtri ju mundëson të eksportoni një sasi të kufizuar të të dhënave, bazuar në kriteret që përzgjedhni.

<!-- -->

- Mos përfshij regjistrime të shënuara si private: Kontrrollo këtë kuti për të parandaluar regjistrimet private të përfshihen në skedarin e eksportuar.

<!-- -->

- Kufizo të dhëna për njerëzit që jetojnë: Kontrrollo këtë kuti për të kufizuar informacionin e eksportuar për njerëzit që jetojnë. Kjo dë të thotë që të gjitha informacionet sa i përket lindjes së tyre, vdekjes, adresat, ngjarjeve të rendësishme, etj., do të hiqen në skedarin e eksportuar të GEDCOM. Nëse zgjedhni këtë opsion, do t'ju jipet opsione shtesë për të kufizuar më tej të dhënat për njerëzit që jetojnë. Për shembull, mund të zgjedhni ta zëvendësoni fjalën "Që jetojnë" për emrin e parë; mund të përjashtoni shënime; dhe mund të përjashtoni burime për njerëzit që jetojnë.

Ndonjëherë, nuk është gjithmonë e qartë nga të dhënat nëse dikush është vërtet gjallë. Gramps përdor një algoritëm të avancuar për të provuar të përcaktojë nëse një njeri mund të jetë ende gjallë. Mbaj mend, Gramps po bën gjetjen më të mirë të tij, dhe mund të mos ketë mundësi që gjithmonë të gjejë me saktësi. Ju lutem kontrrolloni dy herë të dhënat tuaja. [Probably alive](wiki:Gramps_6.0_Wiki_Manual_-_Probably_Alive)

### Eksporto në formate tjera

- Ueb Pema familjare: Eksportimi në Ueb Pemën familjare do të formojë një skedar teksti i cili mund të përdoret nga programi Ueb Pema familjare. Opsionet e eksportit përfshijnë përzgjedhjen e filtrit dhe aftësinë për të kufizuar të dhëna për njerëzit që jetojnë në atë të lidhjeve të tyre familjare.

<!-- -->

- GeneWeb: Eksportimi në GeneWeb do të ruajë një kopje të të dhënave tuaja në një ueb format të kërkuar gjenealogjik. Për të mësuar më shumë rreth dhe formatin e tij, viyitoni <http://cristal.inria.fr/~ddr/GeneWeb/en/>.

<!-- -->

- vKalendar dhe vKartela: Eksportimi në vKalendar apo vKartelë do të ruajë informacione në një format që përdoret në shumë aplikacione kalendarike dhe libër shënimesh, ndonjëherë të quajtura PIM për Menaxhues për Informacione Personale.

<!-- -->

- Formati i Fletëllogaritëses Gramps CSV: Mundëson eksportimin (dhe importimin) e nëngrupeve të të dhënave tuaja Gramps në një format të thjeshtë të fletëllogaritëses. Shih [CSV Importimi dhe Eksportimi](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees:_CSV_Import_and_Export) për më shumë informacione. Gjithashtu shih [Afishim i eksportit](wiki:Gramps_6.0_Wiki_Manual_-_Settings#Export_the_screen) .

## Zhvendosja e bazave të të dhënave 2.2 në Gramps 3

Ka dy mënyra për të zhvendosur të dhënat tuaja Gramps nga verzioni 2.2 në verzionin 3; por edhe duke importuar në mënyrë direkte verzionin tuaj 2.2 të skedarit grdb apo duke eksportuar së pari në format XML. Për shkak të ndërlikimit në mënyrën se si verzioni 2.2 grumbullon të dhëna, eksportimi në XML është zakonisht mënyra më e përshtatshme dhe pa problem e zhvendosjes së të dhënave tuaja në verzionin 3.

- Importo skedarë 2.2 grdb: Në një bazë të të dhënave Gramps 2.2, të dhënat tuaja grumbullohen në një skedarë grdb së bashku me një ose dy skedarë të ditarëve që mbahen në direktoriume të gjetura në .gramps/env direktorium. Për të importuar të dhënat tuaja 2.2 direkt në Gramps 3, krijo një bazë të re të të dhënave dhe përzgjedh opsionin për të importuar një bazë të të dhënave Gramps 2.2. Duhet të jeni të sigurtë që jeni duke ekzekutuar Gramps 3 nga përdoruesi i njejtë që jeni mësuar të ekzekutoni Gramps 2.2 dhe që ka pasur qasje në të njetën .gramps/env direktorium që përmban skedarë të ditarëve që plotësojnë të dhënat tuaja. Nëse merrni një thënie gabim "/tmp/tmpDkI5pO nuk mund të hapet" ose diçka të ngjajshme kur provoni të importoni bazën e të dhënave tuaja, atëherë dë të thotë që Gramps 3 i shef të gjithë skedarët që formojnë bazën e të dhënave tuaja.

<!-- -->

- Gramps XML: Me këtë qasje së pari nis Gramps 2.2 dhe esporto bazën e të dhënave tuaja në formatin Gramps XML. Skedari XML në të vërtetë është i ngjeshur dhe i përfshirë në një skedar.gramps. Ky skedar është i transferueshëm, nuk ka tjetër skedar të varur dhe mund të zhvendoset gjithkund ku keni të instaluar Gramps 3. Pastaj, nis Gramps 3 dhe krijo një bazë të zbrazët të të dhënave duke përdorur Menaxhuesin e Pemës familjare dhe importo skedarin .gramps.

[Category:Sq:Documentation](wiki:Category:Sq:Documentation)
