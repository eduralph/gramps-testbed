---
title: Sq:Gramps 6.0 Wiki Manual - Tools
categories:
- Sq:Documentation
managed: false
source: wiki-scrape
wiki_revid: 118119
wiki_fetched_at: '2026-05-30T20:52:01Z'
lang: sq
---

Ky kapitull përshkruan veglat e ndryshme të cilat janë të mundshme në Gramps.

Veglat e Gramps ju mundësojnë të kryeni lloje të ndryshme të analizave të të dhënave tuaja gjenealogjike. Zakonisht, veglat nuk japin dalje në formë të printouts apo skedarëve. Në vend të saj, ato japin dalje në ekran i cili është i mundshëm menjëherë për hulumtuesin. Megjithatër, kur është e duhur, mund të ruani rezultatet e ekzekutimit të një vegle në skedar. Veglat paraqesin një ndër fuqitë më të mëdha të Gramps krahasuar me shumicën e softuerave gjenealogjik.

Veglat mund të futen përmes menysë duke zgjedhur **vegla -\>Seksioni i veglave -\>Vegël e posaçme** . Si alternative, mund të shfletoni përzgjedhjen e plotë të veglave të mundshme së bashku me përshkrimin e tyre të shkurtër në një dialog **Përzgjedhje veglash** i thirrur duke klikuar ikonën në shiritin e veglave.

## Analizë dhe eksplorime

Ky seksion përmban vegla të cilat analizojnë dhe eksplorojnë bazën e të dhënave, por nuk e ndryshojnë atë. Veglat në vijim për analiza dhe eksplorim, aktualisht janë të mundshme në Gramps:

### Krahaso ngjarje të veçanta

Kjo vegël krahason ngjarje në grupën e përzgjedhur të njerëzve. Për këtë krahasim, njerëzit janë zgjedhur me përdorimin e filtrave të përshtatur. Filtrat e përshtatur mund të krijohen në Redaktuesin e Filtrit të përshtatur (shih *vegla-util-cfe* ) i cili mund të thirret duke klikuar butonin . Tabela që del si rezultat e dhënë nga kjo vegël, mund të ruhet si një fletëllogaritëse.

### Shfletues ndërveprues i pasardhësve

![[_media/InteractiveDescendantBrowser-40.png|Fig. z.z Shfletues i pasardhësve]]

Së pari duhet të përzgjedhni një person apo të nisni me Personin aktiv aktual.

Kliko në menynë **Vegla--\>Analizë dhe eksplorim--\>shfletues ndërveprues i pasardhësve**.

Kjo vegl ndërton një pemë me Personin aktiv si rrënja e pemës. Fëmijët degëzohen nga prindërit e tyre në mënyrën e zakonshme.

Mund të klikoni butonat apo për të zgjeruar apo për të mbyllur nyjet.

Përdor këtë vegël për një shikim të shpejtë të pasardhësve të personit.

Butoni do t'ju sjellë në këtë faqe dhe me mund të mbyllni dritaren e shfletuesit të pasardhësve.

## Përpunimi i bazës së të dhënave

Ky seksion përmban vegla të cilat mund të modifikojnë bazën tuaj të të dhënave. Veglat nga ky seksion përdoren më së shumti për gjetjen dhe përmirësimin e gabimeve në të dhënat. Veglat në vijim për përpunimin e të dhënave, aktualisht janë të mundshme në Gramps:

### Llogarit datat e vlerësuara

![[_media/calcestdates.png|Fig. z.z Llogarit datat e vlerësuara]] Klikimi i **Veglave--\>Përpunimi i bazës së të dhënave--\>Llogarit datat e vlerësuara...** sjell dritaren :

Pastaj zgjedhni apo .

Do t'ju paraqitet dritarja . Kjo dritare ka tri skeda.

- Opsionet:

<!-- -->

- - Filtri: në menynë me lëshim poshtë mund të përzgjedhni se cila pjesë e bazës së të dhënave do të përpunohet: gjithashtu mund të përzgjedhni **gjithë bazën e të dhënave**, **Pasardhësit** e Personit aktiv, **familjet pasardhëse** të Personit aktiv, **Paraardhësit** e Personit aktiv, **Njerëz me paraardhës të përbashkët** me Personin aktiv, apo ndonjë **filtër të përshtatur** (Shih filtrat e përshatur).

<!-- -->

- - Person në filtër: Personi aktiv vëhet në listë në këtë fushë, por nëse klikoni në do të sjellë një dritare . Kjo dritare shfaq një listë të njerëzve nga e cla mund të zgjedhni. Përdor shigjetën apo për të zgjeruar apo për të mbyllur nyjet. Në tabelë do të shihni për cilat persona nuk ka data të lindjes dhe të vdekjes.

Nga ana e majtë në këndin e mëposhtëm ka një kuti të shënuar . Duke klikuar në këtë buton, do të shfaqen të gjithë njerëzit në bazën e të dhënave.

- - Teksti burimor: në këtë mund të plotësoni tekstin që do të përdoret në referencën burimore. Vlera e parazgjedhur është: *Janë llogaritur vlerësimet e datatve*.

Janë të mundshme katër kuti shënuese:

- - Largo datat e shtuara më parë
  - Shto data të lindjes të vlerësuara
  - Shto data të vdekjes të vleërsuara
  - Afisho rezultate të hollësishme: do të shfaq hollësi për secilën datë që është futur.

<!-- -->

- Konfig:

<!-- -->

- - Mosha maksimale:
  - Dallimi maksimal në vite mes motrave/vëllezërve:
  - Vite minimale mes gjeneratave:
  - Vite mesatare mes gjeneratave:

### Redakto informacione për zotëruesin e bazës së të dhënave

![[_media/DatabaseOwnerEditor-dialog-default-60.png|Fig. z.z Informacione mbi zotëruesin]]

kliko **Vegla--\>Përpunimi i të dhënave--\>Redakto informacione për zotëruesin e bazës së të dhënave**. Kjo sjell një dritare , ku mund të plotësoni informacionet e duhura.

- Emri:
- Adresa:
- Qyteti:
- Shteti/Provinca:
- Vendi:
- ZIP/Kodi postal:
- Telefoni:
- E-posta:

### Infromacion të nxjerrura nga emri

Kjo vegël hulumton gjith bazën e të dhënave dhe tenton të nxjerrë tituj dhe nofka të cilat mund të futen në fushën e të personit. Nëse do të mund të nxirret ndonjë informacion, kandidatët për përshtatje do të paraqiten në tabelë. Pastaj do të mund të vendosni se cilin të përmirësoni siç është sugjeruar, e cilin jo.

### Nxjerr të dhëna për vendin nga titulli i vendit

Kjo vegël tenton të nxjerrë qytetin dhe shtetin/krahinën nga titulli i vendit.

### Nxjerr përshkrime të ngjarjes nga të dhënat për ngjarjen

Nxjerr përshkrime të ngjarjeve nga të dhënat për ngjarjen.

### Gjej njerëz të mundshëm duplikat...

![[_media/Find-possible-duplicate-people-PotentialMerges-results-41.png|Fig. z.z Njerëz duplikat]] Kjo vegël hulumtoh gjith bazën e të dhënave, duke kërkuara të hyra që mund të araqesin personin e njejtë.

Mund t'i qaseni kësaj vegle përmes **Vegla-\>Përpunimi i të dhënave...-\>Gjej njerëz të mundshëm duplikat...**.

Janë të mudshme dy opsione:

- Përshtat pragun: zgjedh mes E lartë, E mesme dhe e Ulët nga menyja me lëshim poshtë.

<!-- -->

- Opsione: një kuti zgjedhëse për të aktivizuar apo çaktivizuar përdorimin e kodeve [soundex](wiki:Gramps_6.0_Wiki_Manual_-_Tools#Use_of_SoundEx_module_in_Gramps).

Janë paraqitur vetëm tre opsione: butoni ju sjell në këtë faqe, për të ndërprerë përpunimin dhe për të nisur përpunimin e të dhënave.

Nëse shtypni butonin , të dhënat do të përpunohen në dy kalime.

Kalimi 1: ndërtimi i listës paraprake Kalimi 2: llogaritja e përputhjeve të mundshme. Një shirit përparimi do të shfaqet dhe kjo mund t'ju marrë kohë varësiht nga shpejtësia e cpu dhe sasisë së njerëzve në bazën e të dhënave.

Më në fund paraqitet një dritare . Kjo dritare shfaq një listë me tri shtylla:

- Vlerësimi: kjo ju jep një mendim për ngjajshmëri mes dy njerëzve. Sa më i lartë të jetë vlerësimi, aq më i lartë do të jetë mundësia që njerëzit të jenë duplikat.
- Personi i parë
- Personi i dytë

Nëse përzgjedhni një rresht, mund të kontrrolloni hollësitë me butonin apo mund të klikoni dy herë në rreshtin e përzgjedhur.

Janë paraqitur tre butona: butoni ju sjell në këtë faqe, për ta mbyllur dritaren dhe i cili ju sjell një dritare e cila u sqarua me hollësi në [Dialogun për përputhjen e njerëzve](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_Editing_Data:_Detailed#Merge_People). Këtu mund të përzgjedhni me radio butonat njërin nga personat dhe përfundimisht të përdorni butonin për të përputhur të dhënat nëse gjeni se të dy personat janë duplikat.

Nëse shtypni butonin , ktheheni prapa në listë.

### Rregullo shkrimin kapital të emrave familjarë...

![[_media/FixCapitalizationofFamilyNames-CapitalizationChanges-dialog-results-example-50.png|Fig. z.z Rregullo shkrimin kapital]] Kjo vegël hulumton ghith bazën e të dhënave dhe përpiqet të rregullojë shkrimin kpital të emrave familjarë. Qëllimi i kësaj është të ketë shkrim kapital konvencional: shkronja e parë e madhe dhe të tjerat të vogla për pjesën tjetër të mbiemrit. Nëse zbulohet mospërfillje e këtij rregulli, kandidatët për rregullim do të paraqiten në tabelë. Pastaj mund të vendosni se cilin emër ta përmirësoni, siç u sugjerua, e cilin jo.

Mund ta përdorni këtë vegël përmes **Vegla--\>Përpunimi i bazës së të dhënave--\>RRegullo shkrimin kapital të emrave familjarë...**.

Mund të zgjedhni apo .

Nëse do të kishte ndryshime në shkrimin kapital të emrave, do tÇju paraqitej dritarja . Dritarja shfaq një listë të emrave familjarë që Gramps mund t'i kthejë në shkrim kapital të saktë. Në listë d të shihni një tre shtylla: kuti të zgjedhjes, Emrin origjinal dhe ndryshime në shkrimin kapital.

Përzgjedh emrat që doni t'i ndryshoni, pastaj shtyp butonin . Ose përdor butonine për të anuluar ndryshimet.

### Riemëro llojet e ngjarjeve

![[_media/Tools-rename-event-types-change-event-types-dialog-42.png|Fig. z.z Ndrysho llojin]] Kjo vegël mundëson që të gjitha ngjarjet e një emri të caktuar të riemërohen në një emër të ri.

Paraqitet dritarja . Kjo vegël do të riemërojë të gjitha ngjarjet e një lloji në një lloj tjetër.

- Lloji origjinal i ngjarjes: plotëso fushën e tekstit apo përdor menynë me lëshim poshtë dhe përzgjedh një lloj origjinal të ngjarjes
- Lloj i ri i ngjarjes: plotëso fushën e tekstit (mund të krijoni një lloj plotësisht të ri këtu) apo të përdorni menynë më lëshim poshtë dhe të përzgjedhni një lloj të ri

SHembulli shfaq një riemërim të ngjarjes së **Lindjes** në një ngjarje **Pagëzimi**.

Më në fund, përdor butonin apo .

### Rirradhit Gramps ID

Kjo vegël do të rirradhit të gjitha elementet në bazën e të dhënave për ta përshtatur me skemën e përcaktuar në id e parashtesës së bazës së të dhënave.

Mund të ndryshoni ato parametra në menynë **Redakto--\>Preferenca...--\>Formatet e ID**.

Mund të përdorni këtë vegël përmes **Vegla--\>Përpunimi i të dhënave--\>Rirradhit Gramps ID**.

Dritarja do të shfaqë një shirit të përparimit.

ID në viji janë rirradhitur me disa hapa: Rirradhitja e ID të njerëzve, Rirradhitja e ID së familjeve, Rirradhitja e ID së ngjarjeve, Rirradhitja e ID së media objekteve, Rirradhitja e ID së burimeve, Rirradhitja e ID së vendeve, Rirradhitja e ID së depove dhe përfundimisht Rirradhitja e ID së shënimeve.

Në hapin tjetër, kërkohen dhe caktohen ID e papërdorura.

## Riparimi i bazës së të dhënave

### Kontrrollo dhe riparo bazën e të dhënave

Kjo vegël kontrrollon bazën e të dhënave nëse ka probleme të tërësishme, duke rregulluar problemet që mundet. Veçanërisht, kjo vegël kontrrollon:

- Lidhjet e prishura familjare. Këto janë rastet kur regjistrimet e një personi i referohen një familjeje përderisa, regjistrimi i familjes nuk i referohet atij personi, dhe anasjelltas.

<!-- -->

- Media objektet që mungojnë. Media objekti që mungon është objekti skedari i të cilit referohet në bazën e të dhënave, por nuk ekziston. Kjo mund të ndodh kur skedari fshihet rastësisht, riemërohet apo lëvizet në vend tjetër.

<!-- -->

- Familjet e zbrazëta. Këto janë të hyra të familjes të cilat nuk ireferohen asnjë personi si anëtarë i tyre.

<!-- -->

- Marrëdhëniet mes prindërve. Kjo kontrrollon të gjitha familjet për t'u siguruar nëse babai dhe nëna nuk janë përzier. Kontrrollimi gjithashtu bëhet që prindërit të kenë gjini të kundërt. Nëse kanë gjini të njejtë, atëherë marrëdhënia e tyre riemërohet në "Shokë".

### Rindërto hartën e referencimit

### Rindërto tregues dytësor

### Largo objekte të papërdorura...

Kjo vegël do ta hulumtojë bazën tuaj të të dhënave për të gjetur pjesë të informaconeve të cilat nuk janë të lidhura me asgjë tjetër, dhe pastaj do t'i largojë ato.

## Heq viruset

### Dritarja e vlerësimit Python...

### Ringarko Prizat

Ashtu siç sugjeron emri, kjo prish ngarkimin dhe ringaron të gjitha prizat. Në sistemin e Gramps të gjitha raportet dhe veglat janë të ngulitura, pra kjo mund të ndihmojë të pastroni parametrat e padashura dhe të ngarkoni prizat e reja të cilat i keni shtuar në sistem që kur ka nisur Gramps.

### Shfaq objekte jo të mbledhura

## Shërbime

Ky seskion përmban vegla që ju mundësojnë të kryeni një operacion të thjeshtë në një pjesë të të dhënave. Rezultatet mund të ruhen në bazën tuaj të të dhënave, por nuk do të modifikojnë të dhënat tuaja që ekzistojnë. Shërbimet në vijim janë aktualisht të mundshme në Gramps:

### Nxjerr kode SoundEx

#### SoundeEx ç'është kjo?

Ky shërbim nxjerr kode SoundEx për emrat e njerëzve në bazën e të dhënave. Ju lutem vizitoni faqen treguese të NARA Soundex për të mësuar më shumë rreth Sistemit Tregues të Soundex.

Soundex është një tregues mbiemri i koduar i cili është i bazuar në ënyrën se si tingëllon mbiemri e jo në atë se si shqiptohet. Mbiemrat që tingëllojnë njejtë, por shqiptohen ndryshe, si SMITH dhe SMYTH, kanë të njejtin kod dhe skedohen bashkë. Sistemi për kodim i soundex u zhvillua që ju të mund të gjeni një mbiemër edhe pse ai mund të jetë egjistruar me shqiptime të ndryshme.

Së pari u përdor në regjistrimet e vitit 1880, Soundex është tregues fonetik, jo një tregues alfabetik. Tipari kryesorë është kodimi i mbiemrave bazuar në mënyrën se si tingëllon një emër e jo ai i mënyrës se si shqiptohet. U përdor për t'iu ndihmuar hulumtuesve të gjejnë një mbiemër me shpejtësi edhe pse mund të ketë pranuar shqiptime të ndryshme.

Ato që bëjnë kërkime për regjistrime, duhet të përdorin metodën e njejtë për të enkoduar mbiemra siç kanë bërë ato që marrin regjistrime kur kanë nxjerrur bazën e të dhënave.

Për të kërkuar një mbiemër të veçantë, së pari duhet ta përpunoni kodin e tij.

- **Rregulli themelorë për kodim i Soundex:**

Çdo kod soundex përmban një shkronjë dhe tre numra, si W-252. Shkronja gjithmonë është shkronja e parë e mbiemrit. Numrat i caktohen shkronjave të mbiemrit që kanë mbetur sipas udhëzuesit soundex i cili shfaqet më poshtë. Zero-t shtohen në fund nëse është e nevojshme për të krijuar një kod me katër karaktere. Shkronjat shtesë nuk merren parasyshë. Shembull: Washington kodohet si W-252 (W, 2 për S, 5 për N, 2 për G, shkronjat që kanë mbetur nuk merren parasyshë). Lee kodohet si L-000 (L, shtohet 000).

Numri Paraqet shkronjat

1 B, F, P, V

2 C, G, J, K, Q, S, X, Z

3 D, T

4 L

5 M, N

6 R

Nuk merrn parasysh shkronjat A, E, I, O, U, H, W, dhe Y.

- **Rregulla plotësuese të kodimit të Soundex:**

<!-- -->

- - Emrat me shkronja dyfishe: Nëse mbiemri ka ndonjë shkronjë dyfishe, ato duhet të merren si një shkronjë. Për shembull:

Gutierrez kodohet si G-362 (G, 3 për T, 6 për R e parë, R e dytë injorohet, 2 për Z).

- - Emra me shkronja njëra pranë tjetrës që kanë numër të njejtë të kodit të Soundex: Nëse mbiemri ka shkronja të ndryshme njëra-pranë-tjetrës që kanë numër të njejtë në udhëzuesin e kodimit soundex, duhet të merren si një shkronjë. Shembull:
    - Pfister kodohet si P-236 (P, F injorohet, 2 për S, 3 për T, 6 për R).
    - Jackson kodohet si J-250 (J, 2 për C, K injorohet, S injorohet, 5 për N, 0 shtohet).
    - Tymczak kodohet si T-522 (T, 5 për M, 2 për C, Z injorohet, 2 për K). përderisa zanorja "A" ndan Z dhe K, K kodohet.

<!-- -->

- - Emra me parashtesa: Nëse një mbiemër ka një parashtesë, si Van, Con, De, Di, La, apo Le, kodo të dyja me dhe pa parashtesë, sepse mbiemri mund të vihet në listë nën cilindo kod. Vini re, Mc dhe Mac nuk merren si parashtesa. Për shembull, VanDeusen mund të kodohet në dy mënyra:V-532 (V, 5 për N, 3 për D, 2 për S) apo D-250 (D, 2 për S, 5 për N, 0 shtohet).

<!-- -->

- - Ndarës të bashkëtingëlloreve: Nëse një zanore (A, E, I, O, U) ndan dy bashkëtingëllore që kanë kod të njejtë soundex, kodohet bashkëtingëllorja nga ana e djathtë e zanores. Shembull:Tymczak kodohet si T-522 (T, 5 për M, 2 për C, Z injorohet (shih rregullin "Njëra-pranë-tjetrës" më lartë), 2 për K). Përderisa zanorja "A" ndan Z dhe K, K kodohet. Nëse "H" apo "W" ndan dy bashkëtingëllore që kanë të njejtin kod soundex, bashkëtingëllorja nga ana e djathtë e zanores nuk kodohet. Shembull: Ashcraft kodohet si A-261 (A, 2 për S, C injorohet, 6 për R, 1 për F). A-226 nuk kodohet.

#### Përdor modulin SoundEx në Gramps

![[_media/SoundEx-gramplet-example-42.png|Fig. x.y Nxjerrës i kodit SoundEx]] Duke klikuar përmes Shiritit të veglave mbi **Veglat--\>Shërbime --\> nxjerrësi Soundex...** paraqitet dritarja . Në fushën e tekstit mund të shtypni emrin apo mund ta përdorni shigjetën ku mund të zgjedhni një emër nga lista me lëshim poshtë.

Emri që do ta vendosni, mund të jetë çfarëdo emër, po edhe një emër i cili nuk është paraqitur në Pemën familjare.

Rezultati shfaqet në mënyrë automatike: R236

Butoni është në dispozicion i cili ju çon në këtë faqe. Me butonin (apo duke shtypur \<alt+c\>) ju mbyllni këtë dritare të nxjerrësit.

### Media Manageri...

![[_media/MediaManager-FinalConfirmationWindow-40.png|Fig. z.z Dritarja për konfirmimin përfundimtarë]] Kjo vegël lejon grumbull operacionesh në media objekte të ruajtura në kujtesën e Gramps. Një dallim i rëndësishëm duhej të jetë bërë mes një media objekti të Gramps dhe skedarit të tij.

Media objekti Gramps është një përmbledhje të dhënash rreth skedarit të media objektit: emrit të skedarit dhe/apo shtegu, përshkrimit të tij, ID së tij, shënimet, referencat e burimeve, etj. Këto të dhëna **nuk përfshijnë vet skedarin**.

Skedarët që përmbajnë imazhe, zë, video, etj. ekzistojnë si të ndara në njësinë e ndurtë. Këto skedarë nuk menaxhohen nga Gramps dhe nuk përfshihen në bazën e të dhënave të Gramps. Baza e të dhënave të Gramps ruan në kujtesë vetëm shtegun dhe emrat e skedarëve.

Kjo vegël ju mundëson të modifikoni vetëm regjistrimet brenda bazës tuaj të të dhënave të Gramps. Nëse doni të lëvizni apo të riemëroni skedarët, atëherë duhet ta bëni atë vet, jashtë Gramps. Pastaj mund të përshtatni shtigjet duke përdorur këtë vegël, kështu që media objektet ruajnë në kujtesë vendodhjen e saktë të skedarit.

Nëse klikoni butonin (apo shtypni \<Alt+F\>) do t'ju paraqitet një dritare me tre radio butona:

- Zëvendëso nënvargjet në shteg: Nëse përzgjedhni këtë radio buton do të sjellë një dritare ku mund të shtypni cilindo varg në fushën e tekstit dhe fushën etekstit . Në çdo kohë mund të klikoni mbi butonin apo butonin . Nëse klikoni butonin do të sjellë dritaren .
- Konverto shtigjet nga relative në absolute
- Konverto shtigjet nga absolute në relative

### Kalkulator i marrëdhënieve

Ky shërbim llogarit dhe afishon marrëdhënien e secilit person me Personin aktiv.

### Verifiko të dhënat...

![[_media/VerifyTheData-DataVerifyTool-dialog-General-tab-defaults-50.png|Fig. z.z Verifiko të dhënat...]] Ky shërbim ju mundëson të verifikoni bazën e të dhënave bazuar në një grupë kriteriumesh të përcaktuara nga ju.

Për shembull, mund të dëshironi të siguroheni që askush në bazën tuaj të të dhënave kishte fëmijë në moshën 98 vjeçare. Duke u bazuar në mendimin praktik, regjistrimi i këtillë do të çojë në gabim. Megjithatër, nuk ka gabim konsekuent në bazën e të dhënave. Veç kësaj, dikush mund të ketë fëmijë në moshën 98 (edhe pse kjo ndodh rrallë). Vegla për verifikim do të afishojë çdogjë që keqpërdorë kriteriumet tuaja, kështu që ju do të mund të kontrrolloni nëse regjistrimi është gabim apo jo. Vendimi i fundt është i juaji.

Duke klikuar në **Vegla--\>Shërbime--\>Verifiko të dhënat...** do t'ju paraqitet një dritare . Dritarja ka katër skeda. Këto skeda shfaqin një listë me kriteriume dhe një fushë të hyrjes ku mund të ndryshoni vlerën e kriteriumit. Në listën më poshtë do të shfaqi disa vlera të *realizueshme*.

- **Të përgjithshme**:
  - mosha maksimale: 95
  - mohsa maksimale për martesë 16
  - mosha maksimale për martesë 60
  - maksimum bashkëshort për një person 4
  - numri maksimal i viteve pandërprerë të të qenurit e ve para martesë së adhshme 30
  - mosha maksimale e një personi të pamartuar 99

Ka një kuti zgjedhëse: *vlerëson datat që mungojnë*.

- **Femrat**:
  - mosha minimale për të lind fëmijë 16
  - mosha maksimale për të lind fëmijë 51
  - numri maksimal i fëmijëve 15

<!-- -->

- **Meshkujt**
  - mosha minimale për t'u bërë baba 18
  - mosha maksimale për t'u bërë baba 65
  - numri maksimal i fëmijëve 15

<!-- -->

- **Familje**
  - dallimi maksimal në vite mes gruas dhe burrit 41
  - numri maksimal i viteve mes fëmijëve 11
  - diferenca maksimale e viteve për të gjithë fëmijët 32

Nëse pajtoheni me kriteriumet kliko butonin (apo shtyp \<Alt+R\> dhe do t'ju paraqitet një dritare .

Varësisht nga kriteriumi juaj dhe të dhënave tuaja, do të shfaqet një listë. Më poshtë janë vënë në listë disa mundësi për gjetje. Po ka edhe të tjera.

- Individ të ndarë : PËR TË BËRË sqaron me tej çka dhe si
- baba i vjetër/i vdekur
- martesë pas vdekjes/para lindjes
- difrencë e madhë e viteve për të gjithë fëmijët
- martesë e hershme/e vonshme
- nën e re/palindur
- burrë dhe grua me mbiemër të njejtë
- martesë të një gjinie/ burrë femër
- ...

Për të treguar se sa e lehtë për përdorim është ky , ja dy shembuj të vërtetë nga të dhëna të vërteta:

Paralajmërimi tregoi 'Burrë femër': duke kontrrolluar të dhënat, gjeta një familje me baba : Anna Roelants. Për fat, në lexova: *Martea mes Adam Roelants dhe Cornelia Crabbe*. Ishte e qartë se ishte gabim në të shtypur: Anna i.s.o. Adam. Pa këtë **Vegël** do të ishte shumë rëndë të gjendet ky gabim.

Paralajmërimi tregoi 'martesë të vonshme': duke kontrrolluar të dhënat: personi mashkull °1738 personi femë °1756 : martesa X 1804 \[French Republican Calender\] : Gjithçka dukej në rregull: prandaj ato u martuan (përsëri) në moshën 66 dhe 48 vjeçare! The warning showed up because the **General criteria** was set to **60**.

Në fund të dritares, katër janë në dispozicion për të bërë më lehtë përzgjedhje. Those are , , , dhe .

Duke klikuar dy herë mbi një rresht, do tju japë mundësinë për të shikuar apo për të redaktuar të dhënat tuaja.

Me butonin (apo nëse shtypni shtypni \<Alt+C\>) e mbyllni dritaren e . Me butonin (apo nëse shtypni \<Alt+H\>) do të arrini te kjo faqe.

Për shembull, mund të dëshironi të siguroheni që askush në bazën tuaj të të dhënave nuk ka pasur fëmijë në moshën 98 vjeçare. Bazuar në mendimin praktik, një regjistrim i tillë do të shënijë një gabim. Megjithatë, nuk është një gabim i qëndrueshëm në baz\[n e të dhënave. Përveç kësaj, dikush mund të ketë fëmijë në moshën 98 vjeçare (edhepse kjo ndodh rrallë). Vegla për Verifikim do të afishojë çdogjë që nuk respekton kriteriumet tuaja, kështu që ju mund të kontrrolloni nëse regjistrimi është gabim apo jo. Vendimi i fundit është i juaji.

### Redaktues i filtrit të përshtatur

![[_media/Define-filter-dialog-custom-filters-example-41.png|Fig.3.x Përcakto filtrin]] Redaktuesi i filtrit të përshtatur ndërton filtra të përshtaur të cilat mund të përdoren për të përzgjedhur për të përzgjedhur njerëz që janë të përfshirë në raporte, eksportime, dhe vegla dhe shërbime tjera. TKjo nët të vërtetë është një vegël e shkëlqyer kur bëhen analiza gjenealogjike.

Kur e futni atë, shfaqet dialogu që vë në listë të gjitha filtrat (nëse ka ndonjë) të përcaktuara më parë nga ju. Kliko butonin për të përcaktuar një filtër të ri. Sapo të keni përpiluar filtrat tuaja, mund t'i redaktoni, t'i testonit dhe t'i fshini filtrat e përzgjedhur duke përdorur butonat , , dhe . Të gjitha filtrat e afishuara në listë, do të ruhen automatikisht së bashku me bazën tuaj të të dhënave dhe do të jenë të mundshme me sesionin e Gramps që vjen më pas.

### Bllok shënimesh me shenjë

Kjo vegël siguron një bllok shënimesh të përhershëm për ruajtjen në kujtesë të regjistrimeve të bazës të të dhënave për t'i ripërdorur më lehtë. Shkurtimisht, ky është një funksionim i kopjo-dhe-ngjit e zgjeruar nga objekte tekstuale në lloje tjera të regjistrimeve të përdorura në Gramps.

Për të thirrur Bllokun e shënimeve me shenjë, ose zgjedh **Vegla -\>Shërbime -\>Bllok shënimesh** ose kliko butonin në shiritin e veglave. Do të paraqitet dritarja në vijim:

![[_media/Clipboard-dialog-example-context-menu-60.png|Fig.3.xx Bllok shënimesh]]

Blloku i shënimeve mbështet adresat, atribute (të dyja, personale dhe familjare), ngjarje (të dyja, personale dhe familjare), emra, referenca të media objekteve, referenca të burimeve, URL, dhe sigurisht informacione tekstuale të shënimeve dhe komenteve. Për të ruajtur në kujtesë cilindo lloj të këtyre regjistrimeve, thjesht zvarrit regjistrimin që ekziston në Blokun e shënimeve me shenjë nga dialogun përkatës të redaktuesit. Për ta përdorur përsëri regjistrimin, zvarrit atë nga Blloku i shënimeve me shenjë në vendin përkatës në redaktuesin, sh. skeda e Adresave, skeda e Atributeve, etj.

Për shembull, skedari i media objektit nuk do të bëhet duplikat. Në vend të saj, referenca do të bëhet në një media objekt ekzistues, e cila do të rezultojë në të hyrën lokale të galerisë.

[Category:Sq:Documentation](wiki:Category:Sq:Documentation)
