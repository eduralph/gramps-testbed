---
title: Sq:Gramps 6.0 Wiki Manual - Command Line
categories:
- Sq:Documentation
managed: false
source: wiki-scrape
wiki_revid: 111420
wiki_fetched_at: '2026-05-30T20:42:55Z'
lang: sq
---

Kjo pjesë e shtuar siguron referencën e aftësive të linjës komanduese e cila është në dispozicion kur Gramps lëshohet nga fundi.

## Opsione të mundshme

Ky seksion siguron listën e referencës të të gjitha opsioneve të linjës së komandës që janë në dispozicion në Gramps. Nëse doni të dini më shumë se vetëm një listë opsionesh, shih seksionin tjetër: [Operacione](wiki:Gramps-command_line#Operation) dhe [Shembuj](wiki:Gramps-command_line#Examples).

### Opsione të formatit

Formati i cilitdo skedar i përcaktuar për t'u hapur, importuar apo eksportuar, mund të caktohet me opsionin

    -f format

. Vlerat e pranueshme *`format`* janë të vëna në listë më poshtë.

- Baza e të dhënave grdb e Gramps: Ky format është i mundshëm për hapje, importim dhe ekspotim. Ku nuk është i përcaktuar, mund të supozohet nëse emri i skedarit mbaron me .grdb
- Baza e të dhënave gramps-xml e Gramps XML: Ky format është i mundshëm për hapje, importim dhe eksportim. Kur nuk është i përcaktuar, mund të supozohet nëse emri i skedarit mbaron me .gramps
- Skedari gedcom i GEDCOM: Ky format është i mundshëm për hapje, importim dhe eksportim. Kur nuk është i përcaktuar, mund të supozohet nëse emri i skedarit mbaron me .ged
- Paketa gramps-pkg e Gramps: Ky format është i mundshëm për importim dhe eksportim. Kur nuk është i përcaktuar, mund të supozohet nëse emri i skedarit mbaron me .gpkg
- Skedari geneweb i GeneWeb: Ky format është i mundshëm për importim dhe eksportim. Kur nuk është i përcaktuar, mund të supozohet nëse emri i skedarit mbaron me .gw
- wft Veb Pemë familjarë: Ky format është i mundshëm vetëm për eksportim. Kur nuk është i përcaktuar, mund të supozohet nëse emri i skedarit mbaron me .wft
- Imazhi iso i CD: Ky format është i mundshëm vetëm për eksport. Gjithmonë duhet të përcaktohet saktë.

### Opsione për hapje

Ka dy mënyra për t'i dhënë Gramps emrin e skedarit që duhet të hapet:

- plotëso emër të thjeshtë të skedarit
- përdor këtë osion :
      -O filename

  or

      --open=filename

-O, Hap një pemë familjare. Kjo gjithashtu mund të bëhet vetëm duke shtypur emrin (emri ose direktoriumi i bazës së të dhënave)

Shembuj:

`python gramps.py 'Family Tree 1'`  
`python gramps.py /home/cristina/.gramps/grampsdb/47320f3d`  
`python gramps.py -O 'Family Tree 1'`  
`python gramps.py -O /home/cristina/.gramps/grampsdb/47320f3d`

Nëse është i dhënë emri i skedarit pa ndonjë flamur të opsionit, do të bëhet përpjekje për të hapur skedarin, dhe pastaj do të lëshohet sesioni ndërveprues i Gramps.

Formati mund të përcaktohet me opsionin

    -f format

apo

    --format=format

, menjëherë pas *emrit të skedarit* . Nëse nuk përcaktohet, do të bëhet përpjekje për supozimin bazuar në *emrin e skedarit*. Format i mundshëm: 'gedcom','gramps-xml','gramps-pkg', 'grdb','geneweb'.

### Opsione për importim

Skedarët e përcaktuar për importim, mund të përcaktohen me opsionin

    -i filename

ose

    --import=filename

. Formati mund të përvaktohet me opsionin

    -f format

ose

    --format=format

, menjëherë pas *emrit të skedarit* . Nëse nuk përcaktohet, supozimi do të bëjë përpjekje bazuar në *emrin e skedarit*.

Shembull:

`  python gramps.py -i 'Family Tree 1' -i 'Family Tree 2'`  
`  python gramps.py -i test.grdb -i data.gramps`

Ku jipen më shumë se një skedarë, secili duhet të ndiqet me flamurin

    -i

. Skedarët importohen me një rend të caktuar, i.e.

     -i file1 -i file2 

dhe

     -i file2 -i file1 

mund të japin Gramps ID të ndryshme në bazën e të dhënave që vjen si rezultat.

### Opsione të eksportit

Skedarët e përcaktuar për ekspotim, mund të përcaktohen me ospionin

    -e filename

apo

    --export=filename

. Formati mund të përcaktohet me opsionin

    -f

menjëherë pas *emrit të skedarit* . Nëse nuk është i përcaktuar, përpjekje për supozime do të bëhen bazuar në *emrin e skedarit* . Për iso formatin, *emri i skedarit* është aktualisht emri i direktoriumit ku do të shënohen bazat e të dhënave të Gramps. Për grdb, gramps-xml, gedcom, wft, geneweb, dhe gramps-pkg, *emri i skedarit* është emri i skedarit që del si rezultat.

-e, nxjerr një pemë familjare në formatin që kërkohe. Nuk është e mundshme të eksportohen në një pemë familjare.

Shembull:

` python gramps.py -i 'Family Tree 1' -i test.grdb -f grdb -e mergdeDB.gramps`

Vini re, kjo më lartë nuk ndryshon 'Family Tree 1' pasi që çdo gje ndodh përmes një baze të përkohshme të të dhënave, ndërsa:

` python gramps.py -O 'Family Tree 1' -i test.grdb -f grdb -e mergdeDB.gramps`

do të importojë import test.grdb në Family Tree 1, dhe pastaj e eksporton në skdear !

Kur jipen më shumë se një skedr i nxjerrë, secili prej tyre duhet të ndiqet nga flamuri

    -o

. Skedarët shkruhen një nga një, në rend të caktuar.

### Opsione të veprimit

Veprimi që kryhet për importimin e të dhënave mund të caktohet me opsonin

    -a action

apo

    --action=action

. Kjo bëhet pasi të plotësohen të gjitha importet me sukses.

Veprimet të cilat janë të mundshme për momentim:

- *përmbledhje*: Ky veprim është i njejtë me **Raporte -\>Pamje -\>Përmbledhje**

<!-- -->

- *kontrrollo*: Ky veprim është i njejtë me **Vegla -\>përpunimi i të dhënave -\>Kontrrollo dhe riparo** .

<!-- -->

- *vegla*: Ky veprim mundëson akzekutimin e një vegle nga linja e komandës.

<!-- -->

- *raporte*: Ky veprim mundëson dhënien e raporteve nga linja e komandës. Pasi që raportet në përgjithësi kanë disa opsione të veta, ky veprim duhet të ndiqet me vargu i opsionit për raporte. Vargu jipet duke përdorur opsionin
      -p option_string

  apo

      --option=option_string

  .

Shumica e opsioneve të raporteve janë të veçanta për çdo raport. Por, ka edhe disa opsione të përbashkëta.

- emri=emri_i raportit: Ky opsion i detyrueshëm përcakton se cili raport do të nxirret. Nëse emri_i raportit i shtuar nuk përshtatet me ndonjë raport që është në dispozicion, do të printohet mesazhi për gabimin i ndjekur nga një listë e raporteve të mundshme.

<!-- -->

- shfaqet=të gjitha: Ky do të japë listën e emrave për të gjitha opsionet e munshme për një raport të dhënë.

<!-- -->

- shfaq=emrin_e opsionit: Kjo do të printojë përshkrimin e funksionimit e plotësuar me emrin_e opsionit, si dhe llojet dhe vlerat e pranueshme për këtë opsion.

Përdor opsionet e mësipërme për të kuptuar gjithçka rreth një raporti të dhënë.

Kur jipen më shumë se një veprim të daljes, secili duhet të ndiqet nga flamuri

    -a

. Veprimet kryhen një nga një, në një rend të përcaktuar.

### Opsioni për listën

-l, prinoton një listë të pemëve të njohura familjare

## Operacioni

Nëse agumenti i parë në linjën e komandës nuk fillon me vizë (dmth. pa flamur), Gramps do të provojë të hapë skedarin me emrin e dhënë nga argumenti i parë dhe të fillojë sesionin ndërveprues, duke injoruar pkjesën tjetër të argumenteve të linjës së komandës.

Nëse jipet flamuri

    -O

, atëherë Gramps do të provojë të hapë emrin e skedarit të plotësuar dhe pastaj të punojë me atë të dhënë, siç është prezentuar nga parametrat vijuese të linjës së komandës.

Me apo pa flamur

    -O

, mund të ketë importime, eksportime dhe veprime të shumëfishta, më tej të përcaktuara në linjën e komandës duke përdorur flamujt

    -i

,

    -e

, dhe

    -a

.

Rendi i opsioneve

    -i

,

    -e

, apo

    -a

nuk është aq i rendësishëm. Rendi aktual i ekzekutimit është gjithmonë: të gjitha importimet (nëse ka ndonjë) -\> të gjitha eksportimet (nëse ka ndonjë) -\> të gjitha veprimet (nëse ka ndonjë).

'

Nëse nuk jipen opsione

    -O

apo

    -i

, Gramps do të lëshojë dritaren e tij dhe do të nisë sesionin e zakonshëm ndërveprues me bazën e zbrazët të të dhënave, meqë nuk ka të dhëna për t'u përpunuar.

Nëse nuk jipen opsione

    -e

apo

    -a

, Gramps do të lëshojë dritaren e tij kryesore dhe të nisë sesionin e zakonshëm ndërveprues me bazën e të dhënave që del si rezultat nga hapja dhe të gjitha importimet (nëse ka ndonjë). Kjo bazë e të dhënave gjendet në skedarin *import_db.grdb* nën direktoriumin *~/.gramps/import/* .

Cilido gabim që ndeshemni gjatë importimit, eksportimit apo veprimit, do të hidhet në stdout (nëse këto janë përjashtime që manovrohen nga Gramps) apo në stderr (nëse këto nuk manovrohen nga Gramps). Përdor ridrejtimet e guaskës së stdout dhe stderr për të ruajtur mesazhe dhe gabime në skedarë.

## Shembuj

- Për të importuar katër baza të të dhënave (formatet e të cilave mund të përcaktohen nga emrat e tyre) dhe për të kontrrolluar bazën e të dhënave që vjen si rezultat nëse ka gabime, mund të shtypni:

  
    gramps -i file1.ged -i file2.gpkg -i ~/db3.gramps -i file4.wft -a check

- Për të përcaktuar me saktësi formatet në shembullin e mësipërm, shto emra të skedarëve me opsionet e përshtatshme -f:

  
    gramps -i file1.ged -f gedcom -i file2.gpkg -f gramps-pkg -i ~/db3.gramps -f gramps-xml -i file4.wft -f wft -a check

- Për të regjistruar bazën e të dhënave që rezulton nga të gjitha importimet, plotëso me flamur -e (përdor -f nëse emri i skedarit nuk mundëson që Gramps të supozojë formatin):

  
    gramps -i file1.ged -i file2.gpkg -e ~/new-package -f gramps-pkg

- Për të ruajtur ndonjë mesazh për gabimet e shembujve të mësipërm në skedarët outfile dhe errfile, ekzekuto:

  
    gramps -i file1.ged -i file2.dpkg -e ~/new-package -f gramps-pkg >outfile 2>errfile 

- Për të importuar tri baza të të dhënave dhe për të nisur sesionin ndërveprues të Gramps me rezultatin:

  
    gramps -i file1.ged -i file2.gpkg -i ~/db3.gramps 

- Për të hapur një bazë të të dhënave dhe bazuar në atë të dhënë, nxjerr raporte kronologjike në format PDF duke vendosur përfundimin në skedarin my_timeline.pdf:

  
    gramps -O file.grdb -a report -p name=timeline,off=pdf,of=my_timeline.pdf 

- Për të kthyer grdb në një skedar .gramps xml:

  
    gramps -O myoriginal.grdb -e output.gramps -f gramps-xml

- Më në fund, për të nisur sesionin e zakonshëm ndërveprues, shtyp:

  
    gramps 

## Ndryshoret e mjedisit

Gramps mund të shfrytëzojë këto ndryshore të ambientit (por mos i ndryshoni ato përderisa nuk e dini se çka jeni duke bërë):

- **GRAMPSHOME** - nëse është e vendosur, parandaloni paraqitjen e shtegut të parazgjedhur duke i mundësuar përdoruesit të përdorë psh. njësinë e rrjetit për të ruajtur në kujtesë të dhëna dhe të gjitha parametrat.
- **LANG** - përdoret nga Gramps për të përcaktuar se cili skedar për gjuhën duhet të lëshohet.

[Category:Sq:Documentation](wiki:Category:Sq:Documentation)
