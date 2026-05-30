---
title: Sq:Gramps 6.0 Wiki Manual - Reports
categories:
- Sq:Documentation
managed: false
source: wiki-scrape
wiki_revid: 118940
wiki_fetched_at: '2026-05-30T20:51:11Z'
lang: sq
---

Ky seksion përshkruan raporte të ndryshme të mundshme në Gramps.

## Nxjerrja e raporteve

Raportet janë forma më e zakonshme e daljes e krijuar nga hulumtimi gjenealogjik. Pjesa më e madhe e softuerit gjenealogjik vë theksin në zhvillimin e raporteve që kanë pamje të mirë. Gramps pa përjashtim sa i përket kësaj, ofron një zgjidhje të një shumëllojshmërie të raporteve. Gramps mund të nxjerrë raporte në një grup të formateve të hapura, të bazuar në tekste dhe grafike. Gramps gjithashtu mund të krijojë raporte të bazuara në ekran, të cilat janë të pështatshme për të shikuar përmbledhjen e bazës së të dhënave tuaja. Pëfundimisht, Gramps mund të nxjerrë një veb sajt të përshtatshëm për ta vendosur menjëherë në Internet. Të gjitha këto janë pothuajse pafund fleksibile. Nëse dëshironi të modifikoni apo të zgjeroni formatin e parazgjedhur të raportit të Gramps, mund të krijoni dhe të zgjedhni stilin për çdo raport tuajin.

Të gjitha raportet mund të hyjnë përmes menysë duke zgjedhur **Raporte -\>Tipi i raporteve -\>Raport i veçantë** . Si alterntivë, mund ta shfletoni gjithë përzgjedhjen e raporteve që janë në dispozicion së bashku me përshkrimin e tyre të shkurtë në një dialog që thirret duke klikuar ikonën në shiritin e veglave.

## Vlerat zëvendësuese

Shumë raporte grafike ju mundësojnë të ndryshoni informacionin në afishim. Zëvendësimet e ndryshoreve përdoren për të zëvendësuar datën për një simbol të caktuar. Ka dy stile të ndryshoreve. Dallimi është në manovrimin e të dhënave të zbrazëta.

Stili i parë i ndryshoreve ndiqet nga një '\$'. Nëse ndryshorja vlerësohet në një varg të zbrazët, ndryshorja zëvendësohet me vargun e zbrazët. Stili i dytë i ndryshoreve ndiqet nga një '%'. Nëse ndryshorja vlerësohet në një varg të zbrazët, vija që përmban ndryshoren largohet nga përfundimi.

- \$n/%n

Afishon emrin e personit në formën Emri Mbiemri

- \$N/%N

Afishon emrin e personit në formën Mbiemri, Emri

- \$i/%i

Afishon ID e Gramps të shoqëruar me personin.

- \$b/%b

Afishon datën e lindjes së personit

- \$B/%B

Afishon vendin e lindjes së personit

- \$d/%d

Afishon datën e vdekjes së personit

- \$D/%D

Afishon vendin e vdekjes së personit

- \$s/%s

Afishon emrin bashkëshortit të preferuar të personit në formën Emri Mbiemri

- \$S/%S

Afishon emrin e bashkëshortit të preferuar të personit në formën Mbiemri, Emri.

- \$m/%m

Afishon datën e martesës së personit dhe bashkëshortin e preferuar.

- \$M/%M

Afishon vendin të shoqëruar me martesën e personit dhe bashkëshortin e preferuar.

Vlerat zëvendësuese mund të kombinohen :sh. \$n \$i \$b \$B \$d \$D

kjo do të japë shumë informacione në kutitë e afishuara.

## Librat

Aktualisht, raporti i vetëm që është në dispozicion nën këtë kategori, është Raporti i librave.

Raporti i librave krijon një dokument të vetëm (dmth. një Libër) që pëmban një përmbledhje të raporteve grafike dhe tekstuale. Si rrjedhim, kjo merr parasysh një grup shumë të pasur të dokumenteve që Gramps mund t'i paraqesë.

Kur përzgjedhet **Raporte--\>Libra--\>Raport i librave...** , paraqitet dialogu në vijim :

![[_media/ManageBooks-dialog-default-60.png|200x|Fig. a.1 Raporti i librave]]

Fusha ku hyn teksti përdoret për të ruajtur librin (një grup i përzgjedhjeve të konfiguruara) për përdorim të mëtutjeshëm. Pjesa e sipërme vë në listë artikujt që janë në dispozicion për t'i përfshirë në libër. Paneli i poshtëm vë në listë artikujt e përzgjedhur aktualisht në renditjen në të cilën do të paraqiten në libër.

Grupa horizontale e butonave pranë fushës vepron në gjithë librin. Kliko butonin (pastro librin) për të pastruar gjithë artikujt nga libri i fundit. Kliko butonin për të ruajtur librin aktual (nën titullin e shtypur në fushën ku hyn teskti ) për përdorim të mëtutjeshëm. Kjo ruan grupën aktuale të përzgjedhjeve të konfiguruara.

Kliko butonin për të ngarkuar librin (Hap librin e krijuar më parë) nga lista e librave të ruajtura më parë.

Më në fund, kliko butonin për të thirrur listën redaktuese të librave që janë në dispozicion (Rregullo librat e krijuar më parë).

Grupi vertikal i butonave në të djathtë të pjesës së poshtme, vepron në artikullin e përzgjedhur të librave. Kliko butonin për të shtuar artikull të përzgjedhur nga lista që është në dispozicion në librin aktual. Kliko butonin për të larguar një artikull nga libri aktual. Pëdor dhe për të ndryshuar radhitjen e artikujve në librin aktual. Kliko butonin për të konfiguruar opsionet e artikullit të përzgjedhur të librit aktual.

Dialogjet e konfigurimit të thirrura nga janë me artikuj të veçantë. Nëse zgjedhni të mos konfiguroni artikullin, parazgjedhje të njejta do të përdoren për të gjitha opsionet e duhura. Opsioni i zakonshëm pothuajse për të gjithë artikujt e librit është personi qëndrorë: personi mbi të cilin përqëndrohet artikulli. Falë këtij opsioni, ju mund të krijoni një libër me artikuj të përqëndruar në njerëz të ndryshëm (sh. paraardhësit a babait dhe nënës tuaj si kapituj të ndarë). Me parazgjedhje, personi qëndrorë vendoset në Personin aktiv.

Nëse bëhen të gjitha përzgjedhjet e raporteve që do të përfshihen, kliko butonin . Kjo do të thërret dritaren . Ka një skedë me që janë në dispozicion, ku mund të ndryshoni Madhësinë dhe Orientimin për Formatin e letrës dhe të gjitha margjinave. Kutija për klikim është në dispozicion të ndryshohet në vlera metrike.

Në pjesën e poshtme të dritares mund të ndryshoni disa :

- Formatin përfundimtar: menyja me lëshim poshtë ju lejon të zgjedhni mes: **Hap tekst të dokumentit**, **PDF dokument** apo **Printo...**. Kutija për klikim është në dispozicion për t'u hapur në Përpunuesin e fjalëve OpenOffice.org
- Emrin e skedarit: vlera e parazgjedhur është /yourhomedir/book.odt. Kliko butonin dhe mund të ndryshoni parametrat e emrit të skedarit në mënyrë të zakonshme.

Pothuajse gjithë artikujt e mundshëm për përfshirje në libër, janë raporte tekstuale apo grafike, prandaj janë të mundshme në formën e raporteve të pavarura. Përjashtohen artikujt në vijim, të cilët janë të mundshme vetëm si artikuj të librave:

- Faqja me titull

Nëse keni përzgjedhur artikullin dhe keni klikuar butonin për të vendosur këtë artikull në librin tuaj dhe klikoni butonin (Konfiguro artikullin e përzgjedhur aktualisht) do të merri një dritare . Janë të mundshme ty skeda: **Teksti** dhe **Imazhi**. Në skedën keni në dispozicion tri fusha ku hyn teksti ku mund të ndryshoni **Titullin**, **nëntitullin** dhe një **Fund të faqes** (E drejta e autorit e parazgjedhur 2008).

Pjesa e poshtme e dritares shfaq disa **Opsione të dokumentit**: Këtu mund të zgjedhni **Stilin**. Mund të zgjedhni stilin e parazgjedhur apo të klikoni në butonin . Kjo paraqet një dritare ku mund të shtoni dhe të largoni Stile.

Lidhja PËR TË BËRË në dritaren Redaktues i stilit

Në skedaën , një imazh mund të vendoset sipas dëshirës mes nëntitullit dhe fundit të faqes. Ka mundësi për dhe me butonin mund të përzgjedhni imazhin që doni nga dialogu . Gjithashtu mund të ndryshoni edhe

Për shkaka se mund të konfiguroni elementet e ndryshme, ky artikull mund të përdoret për krijimin e faqe me tituj për tërë librin, kapitujt e tij apo edhe një artikull të vetëm.

- Tekst i përshtatur

Ky artikull krijon një faqe me tre paragrafe, secili përmban tekst të përshtatur: Tekst Fillestarë, Tekst i Mesëm dhe Tekst Përfundimtar. Fushat ku hyn teksti mund të shtohen, kështu që mund ta vendosni aty gjithë tekstin që doni ju. Pamja e tekstit mund të përshtatet duke përdorur stilet për përshtatje (shih opsione të dokumentit të Faqes titull). Ky artikull u mendua të përdoret për epigrafe, përkushtime, sqarime, shënime dhe kështu me rradhë.

## Raporte grafike

Raportet grafike paraqesin informacione në formë të tabelave dhe grafeve. Shumica e opsioneve janë të zakonshme midis raporteve grafike, për këtë arësye ato do të përshkruhen vetëm një herë, në fund të këtij seksioni. Opsionet e pakta të cilat të veçanta për një raport të dhënë, do të përshkruhen direkt në të hyrën e atij raporti.

Raportet vijuese grafike janë aktualisht të mundshme në Gramps:

### Pema e paraardhësve

![[_media/voorouderpdf.png|200x\|Fig. a.2 Pema e paraardhësve e dalë në PDF]] Ky raport nxjerr tabelën e njerëzve të cilët janë paraardhës të Personit aktiv.

- Opsionet e letrës: Me mund të ndryshoni formatin e letrës (Madhësinë dhe orientimin) dhe margjinat (Majtas, Djathtas, në Krye dhe në Fund) dhe të përdorni apo të mos përdorni vlera metrike.
- Opsione të dokumentit: zgjedh formatin përfundimtar: Hap tekst të dokumentit, PDF dokument, Poshtëshënim, Printo..., apo SVG (Grafiqë me Vektor shkallëzues). Një është e mundshme aty ku mund të shënoni prë të shënuar dokumentin e bërë me Përpunuesin e Fjalëve OpenOffice.org apo një Shikues i dokumentit (skedarë PDF).
- Opsione për raporte: Së pari afishohet personi qëndrorë. Duke përdorur butonin mund të përzgjedhni një person tjetër. Me fushën ku hyn teksti mund ta ndryshoni numrin e gjeneratave të cilat merren në konsideratë. fusha hyrëse ju jep mundësinë për të ndryshuar para,etrat e parazgjedhura për të hyrat e afishuara (shiko [Vlerat zëvendësuese](#Substitution_Values)).

Në fund, tri kuti kontrrolluese janë në dispozicion: shkallëzo për t'u përshtatur në një faqe të vetme, përfshij faqe të zbrazëta dhe ngjesh grafik.

### Kalendar

![[_media/Calendarreport1.png|Fig. a.1 Opsione të kalendarit në letër]]

Ky raport paraqet një kalendar me ditëlindje dhe përvjetore në një faqe sipas muajit.

-   
  Me opsionet e letrës mund të ndryshoni

  - Formatin e letrës (madhësinë dhe orientimin)
  - Margjinat (Majtas, Djathtas, në Krye dhe në Fund)

dhe nëse do të përdorni vlera metrike apo jo.

------------------------------------------------------------------------

![[_media/calendarreport4.png|Fig. a.1 Opsione të dokumentit kalendarik]]

-   

  - Format përfundimtar: zgjedh formatin përfundimtarë:
    - Hap tekst të dokumentit
    - Dokument PDF
    - Poshtëshënim
    - Printo...
    - SVG (Grafiqë të vektorëve shkallëzues). Një është e mundshme aty ku mund të shënoni të hapni dokumentin e bërë me Përpunesin e Fjalëve OpenOffice.org apo një Shikues Dokumenti (skedar PDF).
  - Emri i skedarit: vlera e parazgjedhur është */home/<username>/calendar.pdf*.
  - Stili: i parazgjedhur *stil i parazgjedhur* . Me mund të shtoni Stile të dokumentit.

------------------------------------------------------------------------

![[_media/calendarreport2.png|Fig. a.1 Opsione të raporteve kalendarike]]

-   

  - Viti i kalendarit: Për cilin vit doni të bëhet kalendari.
  - Filtri: përzgjedh filtër për të kufizuar njerëz që paraqiten në kalendar
    - E gjithë baza e të dhënave: nuk rekomandohet!
    - Pasardhësit e ...
    - Familjet e pasardhësve të ...
    - Paraardhësit e ...
    - Njerëz me paraardhës të përbashkët me ...
    - cilido filtër i zakonshëm që u krijua
  - Personi Qëndrorë: personi qëndrorë për raportin
  - Formati i emrit: Përzgjedh formatin për të afishuar emra: zgjedh mes:
    - Mbiemri, Patronim i dhënë
    - Mbiemri i dhënënGiven Surname
    - Patronim, i dhënë
    - I dhënë
  - Vend për festa: Përzgjedh vendin për të parë festat e shoqëruara, zgjedh mes:
    - Mos përfshij festa: vlerë e parazgjedhur
    - kanada / Kina / Gjermania / Finlanda / Franca / Sverige - röda dagar / Shtetet e Bashkuara / Republika Çeke
  - Dita e parë e javës:
  - Mbiemër për ditëlindje:
  - Kutitë kontrrolluese:
    - Përfshij vetëm njerëzit që jetojnë: përfshij vetëm njerëzit që jetojnë në kalendar
    - Përfshij ditëlindjet: përfshij ditëlindjet në kalendar
    - Përfshij përvjetore: përfshij përvjetore në kalendar

------------------------------------------------------------------------

![[_media/calendarreport3.png|Fig. a.1 Opsione të tekstit kalendarik]]

-   
  këtu mund të mbushni tri vija tekst të cilat do të vendosen në fund të faqes.

  - Zona 1 e tekstit: Vija e parë e tekstit në fund të vlerës kalendarike të parazgjedhur: *Kalendari im*
  - Zona 2 e tekstit: Vija e dytë e tekstit në fund të vlerës kalendarike të parazgjedhur: *E sjellur nga Gramps*
  - Zona 3 e tekstit: Vija e tretë e tekstit në fund të vlerës kalendarike të parazgjedhur: *<http://gramps-project.org/>*

------------------------------------------------------------------------

![[_media/calendarreport5.png|Fig. a.1 Rezultati i kalendarit]]

  

Rezultati përfundimtarë mund të shifet në anën e djathtë.

[Veglat për festat në kalendar](wiki:Calendar_tools_holidays) sqarojnë se si të shtoni festa që paraqiten në dalje të prizës së kalendarit.

### Pema e pasardhësve

Ky raport nxjerr një graf të njerëzve të cilët janë pasardhës të Personit aktiv. Opsione të veçanta përfshijnë formatin e të hyrave të afishuara.

Ky raport krijon një kalendar me ditëlindje dhe përvjetore në një faqe muaj për muaj.

-   
  Me opsionet e letrës mund të ndryshoni

  - Formatin e letërs (madhësinë dhe orientimin)
  - Margjinat (Majtas, Djathtas, në Krye dhe në Fund)

dhe nëse do të përdorni vlera metrike apo jo.

------------------------------------------------------------------------

-   

  - Formati dalës: zgjedh formatin përfundimtar:
    - Hap tekst të dokumentit
    - Dokument PDF
    - Poshtëshënim
    - Printo...
    - SVG (Grafiqe të vektorëve shkallëzues). Një është e mundshme aty ku mund të shënoni për të hapur dokumentin e bërë me Përpunuesin e Fjalëve OpenOffice.org apo me një SHikues të Dokumentit (skedarë PDF).
  - Emri i skedarit: vlera e parazgjedhur është */home/<username>/descend_chart.pdf*.
  - Stili: *stil i parazgjedhur* i parazgjedhur . me mund të shtoni Stile të Dokumentit.

------------------------------------------------------------------------

![[_media/descendant_tree1.png|Fig. a.1 Opsionet e pemës]]

-   

  - Personi qëndrorë: personi qëndrorë për pemën.
  - Gjeneratat: Numri i gjeneratave që duhet të përfshihen në pemën. E parazgjehdur : 10 gjenerata
  - Formati i parazgjedhur: Formati i parazgjedhur për kutinë dalëse. E parazgjedhur është

`$n`  
`b. $b`  
`d. $d`

- - Kutia zgjedhëse: Shkallëzo për të përshtatur në një faqe të vetme.
  - Kutia zgjedhëse: Përfshij faqe të zbrazëta.
  - Kutia zgjedhëse: Ngjesh pemën: të ngjeshni apo jo pemën.

------------------------------------------------------------------------

![[_media/descendant_tree2.png|Fig. a.1 Rezultati i pemës së pasardhësve]]

  

Rezultati përfundimtarë mund të shihet në anën e djathtë.

### Tabela ventilator

![[_media/fanchartoptions.png|Fig. a.3 Opsione të tabelës ventilator]] Ky raport jep një tabelë që i ngjan një ventilatori, me Personin aktiv në qendër, prindërit në gjysëm rreth pranë tij, stërgjyshët në gjysëm rrethin tjetër dhe kështu me rradhë, për plot pesë gjenerata. ![[_media/fanchartpdf.png|Fig. a.4 Tabela ventilator]]

- Opsionet e letrës: Me mund ta ndryshoni formatin e letrës (madhësinë dhe orientimin) dhe margjinat (Majtas, Djathtas, në Krye dhe në Fund) dhe të përdorni apo jo vlerat metrike.
- Opsione të dokumentit: zgjedh një format përfundimtarë: Hap tekst të dokumentit, dokument PDF , Poshtëshënim, Printo..., apo SVG (Grafiqe të vektorëve shkallëzues). një është i mundshëm aty ku mund të shënoni për të hapur dokumentin e bërë me OpenOffice.org Përpunuesin e Fjalëve apo një Shikues të Dokumentit (skedar PDF ).
- Opsione të raporteve: Së pari afishohet Personi qëndrorë. Duke përdorur butonin mund të përzgjedhni një person tjetër. Me fushën tjetër për dalje mund të ndryshoni numrin e gjeneratave të atyre gjeneratave që merren në konsideratë.

Fusha tjetër për dalje : zgjedh përmes menysë zvarrit dhe lësho: rreth i plotë, gjysëm rreth apo çerek rreth. Fusha tjetër për dalje : zgjedh të bardhën ose varësisht nga gjenerata. Fusha tjetër për dalje : zgjedh pingul apo të tërthortë

### Tabela e statistikës

![[_media/statistic.png|Fig. a.5 Tabela e statistikës]] Ky raport mund të mbledhë dhe të afishojë të dhëna të pasura statistikore për bazën tuaj të të dhënave. Opsionet e veçanta për përfshirje në statistikë përfshijnë filtrin, mënyrat për renditje dhe kufi shtesë të bazuar në lindjet dhe gjinitë. Gjithashtu mund të vendosni numrin minimal të artikujve për kufizim të tabelës së shiritit, ashtu që tabelat me më pak artikuj do të nxjerrin një tabelë tortë në vend të tabelës së shiritit. Skeda **Përzgjedhje e grafikut** ju mundëson të zgjedhni grafikun që doni të përfshini në raportin tuaj.

- Opsionet e letrës: Me mund të ndryshoni formatin e letrës (Madhësinë dhe orientimin) dhe margjinat (Majtas, Dtathtas, në Krye dhe në Fund) dhe të përdorni apo jo vlerat metrike.
- Opsionet e dokumentit: zgjedh formatin dalës: Hap tekst të dokumentit, dokument në PDF, Poshtëshënim, Printo..., apo SVG (Grafiqe të vektorëve shkallëzues). Një është e mundshme aty ku mund të shënoni për të hapur dokumentin e bërë me Përpunuesin e Fjalës OpenOffice.org apo me një Shikues të Dokumentit (skedar PDF).
- Opsionet e raportit:
  - Filtri: përcakton se çfarë njerëz janë përfshirë në raport. Mund të zgjedhni gjith Bazën e të dhënave, apo pasardhësit e një personi të caktuar, njerëz me paraardhës të përbashkët si... apo një filtër të bërë të parazgjedhur/të zakontë.
  - Personi i filtrit: Personi qëndrorë për filtrin: e mundshme vetëm nëse nëse përzgjedhet si filtër e jo si bazë e tërë e të dhënave. Butoni ju lejon të zgjedhni një tjetër paron të filtrit.
  - Rendit artikujt e grafikut sipas: Përzgjedh si janë rradhitur të dhënat statistikore: Zgjedh numrin e Artikujve apo emrin e artikullit nga lista me lëshim poshtë.
  - kutia e zgjedhjes: rendit në rradhitje të kundërt
  - Njerëz të lindur pas: Viti i lindjes nga prej ku përfshihen njerëzit: plotëso vitin për të filluar nga
  - Njerëz të lindur përpara: Viti i lindjes deri te i cili do të përfshihen njerëz: plotëso vitin
  - Kutia zgjedhëse: Të përfshihen njerëz me vite të panjohura të lindjes apo jo
  - Gjendja e përfshirë: Përzgjedh cilat gjini janë përfshirë në statistikë. Zgjedh të dyja, meshkujt apo femrat.
  - Artikuj maksimal për një tortë: Në vend të grafikur të shiritit do të përdoret grafiku tortë dhe legjendë me më pak artikuj. Zgjedh një numër nga lista me lëshim poshtë.

![[_media/statistic1.png|Fig. a.6 Opsione të tabelës së statistikës]]

- Grafiqet 1: 9 kutitë e zgjedhjes janë të mundshme për të përfshirë grafiqe me data që treguese:

![[_media/statgraftaart.png|Fig. a.6 Rezultate]] ![[_media/statistic2.png|Fig. a7 Rezultate]]

- - Mosha
  - Vendi i vdekjes
  - Muaji i vdekjes
  - Mosha kur u lind fëmija i parë
  - Titulli
  - Mosha kur u lind fëmija i fundit
  - Muaji i limdjes
  - Mosha në martesë
  - Mosha në vdekje
- Grafiqet 2: 10 kuti të zgjedhjes janë të mundshme për të përfshirë grafiqe me data të shënuara:
  - Tipi i ngjarjes
  - Numri i fëmijëve
  - Vendi i martesës
  - Numri i marrëdhënieve
  - Mbiemri
  - Viti i vdekjes
  - Gjinia
  - Emri
  - Viti i lindjes
  - Vendi i lindjes

Nëse plotësohen të gjitha informacionet e nevojshme, kliko për tu nisur mbledhja e të dhënave. Do të shfaqet një shirit përparimi: Mbledhja e të dhënave... -\>Renditja e të dhënave...-\>Ruajtja e grafiqeve...

Imazhi shfaq rezultatin e **Moshës kur lindi fëmija i parë** për të gjitha femrat e lindura mes viteve 1500 dhe 2008. Për më shumë (576) persoa, mungojnë informacionet personale, për disa mungojnë informacionet e lindjes, por për 33 gra fëmija i tyre i parë ka lindur në moshën 20 vjeçare. Mund të bëhen analiza të mëtutjeshme, me informacion të hollësishëm: llogarit mesataren, std. dev. etj.

### Grafiku kronologjik

Ky raport nxjerr listën e njerëzve me jetën e tyre të paraqitur nga intervale në një shkallë të zakonshme kronologjike. Opsionet specifike përfshijnë filtrin, metodën e renditjes dhe titullin e raportit.

------------------------------------------------------------------------

## Grafiqe

### Grafiku i Brezit familjar

![[_media/Familylines.gif|Shembull i një grafiku i nxjerrë duke përdorur FamilyLines.py, pa imazhe imazhe të vogla.]] ![[_media/Familylines_with_thumbnails.gif|Shembull i një grafiku të nxjerrur duke përdorur FamilyLines.py, pa imazhe të vogla.]] Priza FamilyLines.py u krijua për të nxjerrur grafiqe që janë të lehta për t'u ndjekur. Vini re, Brezi famljar nuk afishon të gjithë njerëzit në bazën e të dhënave -- në vend të saj, kjo prizë nxjerr pemë më të vogla familjare, me disa opsione për të provuar dhe për të kufizuar numrin e njerëzve që janë të përfshirë.

Një përdorim i zakonshëm për këtë prizë është nxjerrja e grafeve të thjeshtëzuara të printuara në vizatues të mëdhenj.

------------------------------------------------------------------------

![[_media/Familylines_graphviz.png|Fig. xx]]

- **Opsionet e GraphViz**:Kjo prizë përdor [GraphViz](http://www.graphviz.org/). GraphViz merr .dot skedarët dhe krijon skedarë përfundimtarë, si .gif, .png, .pdf, .ps, etj.

Skeda e parë mundëson të vendosen disa GraphViz opcione:

- - *Gjerësia*: gjerësia, në inç, e imazhit përfundimtar. Vendoseni në një numër të madh mës nxjerr .png apo .gif skedarë.
  - *Lartësia*: lartësia, në inç, e imazhit përfundimtar. Vendoseni në një numër të madh nëse nxjerr .png apo .gif skedarë.
  - *DPI*: pika në një inç. Zakonisht mes 75 dhe 120 nëse nxjerr .png apo .gif skedarë, por 300 apo 600 nëse nxjerr skedarë që duhet të printohen.
  - *Ndarja e rreshtave me hapësira*: hapësira e bardhë që duhet të lihet, në inç, mes rreshtave.
  - *Ndarja e shtyllave me hapësira*: Hapësira e bardhë që duhet të lihet, në inç, mes shtyllave
  - *Drejtimi i grafit*: nëse pema rritet nga e majta-djathtas, apo nga e djathta-majtas.
  - *Përpjestimi*: GraphViz përdor këtë për të caktuar pozicionimin e artikujve. Vetëm rovat dhe gabimet do t'ju ndihmojnë të caktoni që ta përdorni opsionin më të mirë. (Kur jeni në hamendje, **ngjesh** përpiqet të punojë mirë.)

  

------------------------------------------------------------------------

![[_media/Familylines_people.png|Fig. xx Njerëzit që na duhen]]

- **Njerëzit që na interesojnë**: Priza FamilyLines.py funksionon duke nisur me një listë të "njerëzve që na interesojnë". Kjo listë fillestare e njerëzve më vonnë përdoret për të gjetur paraardhësit dhe pasardhësit.
  - *Njerëzit që na duhen*: kliko "+" dhe "-" për të shtuar/larguar njerëzit që na interesojnë. Kur jeni në hamendje, provoni të shtoni stërgjyshërit tuaj si një vend nisës.
  - *Ndiq prindërit për të caktuar brezin familjarë*: kur përzgjedhet, kjo bën që FamilyLines.py të ndjekë prindërit për të caktuar tërë listën e njerëzve që na interesojnë. Me siguri dëshironi që të përzgjedhni këtë.
  - *Ndiq fëmijë për të caktuar brezin familjarë*: kur përzgjedhet, kjo bën që FamilyLines.py të ndjekë fëmijët e njerëzve që na interesojnë.
  - *Provoni të largoni njerëz dhe familje të tepërta*: kur përzgjedhet, ky opsion bën që FamilyLines.py të tentojë në mënyrë të rreptë paraardhësti dhe familjet e tepërta nga pema familjare.

  

------------------------------------------------------------------------

- **Ngjyrat familjare**

![[_media/Familylines_family.png|Fig. xx Ngjyrat familjare]] Përzgjedh ngjyrën për ta përdorur për njerëz me mbiemër të veçantë. Kliko "+" apo "-" që të shtoni një mbiemër. Kliko dy herë mbi mbiemrin që të redaktoni mbiemrin.  

------------------------------------------------------------------------

- **Individ**

![[_media/Familylines_individuals.png|Fig. Individ]]

- - *Meshkuj*, *Femra*, *Të panjohur*: ngjyra që përdoret për njerëz mbiemri i të cilëve nuk përputhet me asnjërin emër në skedën "Ngjyrat e familjes" .
  - *Familjet*: ngjyra që përdoret për familje (martesa).
  - *Limit the number of parents*: if selected, then the number of ancestors will be limited by the amount shown. This can only be selected if "Follow parents" has also been selected on the "People of Interest" tab.
  - *Kufizo numrin e fëmijëve*: nëse përzgjedhen, atëherë numri i fëmijëve do të kufizohet nga vlera e shfaqur. Kjo mund të përzgjedhet vetëm nëse "Ndiq fëmijët" gjithashtu është përzgjedhur në skedën "Njerëzit që na interesojnë".

  

------------------------------------------------------------------------

- **Opcione**

![[_media/Familylines_options.png|Fig. xx Opcione]]

- - *Përfshij data*: kur të përzgjedhet kjo, në grafik do të përfshihet data e lindjes, data e vdekjes, dhe datat e martesave.
  - *përfshij vende*: kur të përzgjedhet kjo, do të përfshihet vendi i lindjes, vendi i vdekjes, dhe vendi i martesës.
  - *Përfshij numrin e fëmijëve*: kur të përzgjedhet kjo, teksti i martesës do të përfshijë numrin e përgjithshëm të fëmijëve.
  - *Përfshij datën dhe hulumtuesin*: kur të përzgjedhet kjo, do të vendoset një emërtim në fund të grafikut.
  - *Përfshij regjistrime personale*: kur të përzgjedhet kjo, do të përfshihen në grafik njerëz dhe ngjarje të shënuara si personale.

  

------------------------------------------------------------------------

- **Nxjerrja e grafiqeve**

Nëse FamilyLines.py një herë krijon .dot skedarë dalës (parazgjedh në *./familylines.dot*), paketa GraphViz do të jetë e nevojshme për të krijuar skedarin përfundimtarë dalës. Nëse GraphViz nuk është i instaluar, mund ta shkarkoni atë nga [<http://www.graphviz.org/>](http://www.graphviz.org/).

Disa shembuj të zakonshëm të komandave që përdoren për të nxjerrur grafiqe nga skedari familylines.dot, janë:

`dot -v -Tgif -ofamilylines.gif familylines.dot`  
`dot -v -Tpng -ofamilylines.png familylines.dot`  
`dot -v -Tpcl -ofamilylines.pcl familylines.dot`  
`dot -v -Tps -ofamilylines.ps familylines.dot`

![[_media/Hourglass_report.png|Hourglass: Smith John Hjalmar si person qëndrorë]]

### Grafiku orë me rërë

### Grafiku i marrëdhënieve

Grafiku i marrëdhënieve krijon një graf të ndërlikuar të marrëdhënieve në formatin GraphViz dhe pastaj e konverton në dalje grafike duke e ekzekutuar atë përmes veglës së GraphViz *dot* prapa skene. Opsionet e veçanta për këtë raport përfshijnë filtrin, opsione për datat dhe vendet për ngjarjet, dhe nëse duhet të përfshijnë URL dhe ID për individ dhe familje. Ka gjithashtu disa opsione tç veçanta GraphViz lidhur me ndarjen në faqe, ngjyrën dhe detalet e grafikut. Kjo prizë përdor [GraphViz](http://www.graphviz.org/). GraphViz merr .dot skedarët dhe krijon skedarët përfundimtarë, si .gif, .png, .pdf, .ps, etj.

#### Opsione të grafikut

Përmes menysë: . Do t'ju paraqitet një dritare ku mund të ndryshoni të gjitha parametrat. Dritarja është e ndarë në dy pjesë. Njëra pjesë siguron për gjithë skedat e ndryshme të cilat janë në dispozicion, pjesa tjetër ka . ![[_media/Relgraf1.png|Fig. xx Opsionet e letrës]]

- **Opsionet e letrës**

Skeda e parë si zakonisht në raporte rregullon Formatin e letrës dhe Margjinat.

Një kuti e zgjedhjes kontrrollon nëse keni madhësi metrike apo jo.

Grafiqet i marrëdhënieve shumë shpejt mund të bëhen **shumë të mëdhenj**.

Parametrizimi i formatit të letrës është e rëndësishme për të pasur sukses.

------------------------------------------------------------------------

![[_media/Relationship-graph-graphs-report-options-tab-42.png|Fig. xx Opsione të raportit]]

- **Opsione të raportit**: Disa opsione të rëndësishme këtu:
  - *Filtër*: Këtu, opsionet standarde janë: e gjithë baza e të dhënave (**nuk ju sugjerojmë!**), Pasardhësit e, Familjet pasardhëse të, Paraardhësit e, Njerët me paraardhës të përbashkët me, apo një filtër i bërë në mënyrë të zakonshme.
  - *Personi për filtër*: Nëse përdorni një filtër të zakonshëm, asnjë person nuk do të mund të zgjedhet. Përndryshe, zgjedh personin e saktë këtu. Ka disa kuti shkallëzimi këtu:
    - Përfshij datat e Lindjes, Martesës dhe të Vdekjes
    - Kufizo datat vetëm në vite
    - Përdor vendin kur nuk ka data
    - Përfshij URL
    - Përfshij ID
    - Përfshij imazhe të vogla të njerëzve: zgjedhja e kësaj kutie ju jep një fushë tjetër të daljes
  - *Vendndodhje e vogël*: vetëm aktive kur u zgjedh kutia e fundit e zgjedhjes: mundësitë janë sipër apo pranë emrit

------------------------------------------------------------------------

![[_media/Relationship-graph-graphs-graph-style-tab-42.png|Fig. xx Stili i Grafikut]]

- **Stili i grafikut**
  - *Ngjyrosja e grafikut*: Meshkujt do të paraqiten me të kaltër, femrat me të kuqe. Nëse nuk dihet gjinia e një individi, do të paraqitet me të hirtë. Opsionet janë:
    - Plan i ngjyrosur
    - Plani B&W
    - Mbushje e ngjyrës
  - *Drejtim kah koka e shigjetës*: Zgjedh drejtimin që tregon shigjeta: Pasardhës \<- Paraardhës, Pasardhës -\> Paraardhës, Pasardhës \<-\> Paraardhës, Pasardhës - Paraardhës
    - Përdor kende të rrumbullakta: Përdor kënde të rrumbullatkta për të bërë dallimin mes grave dhe burrave
    - Trego marrëdhënie jo farefisnore me vija me pika: Marrëdhënie jofarefisnore do të shfaqen në grafik si vija me pika.
    - Shfaq nyje familjare: Familjet do të shfaqen si elipse, të lidhura me prindërit dhe fëmijët.

------------------------------------------------------------------------

![[_media/Relgraf4.png|Fig. xx Struktura GraphViz]]

- **Struktura GraphViz**
  - *Fonti i familjes*: Zgjedh fontin për familjen. Nëse nuk shfaqen karakteret ndërkomëtare, përdor fontin **FreeSans**. FreeSans është i mundshëm nga [org NonGNU](http://www.nongnu.org/freefont/).
    - E parazgjedhur
    - Poshtëshënim/ Helvetika
    - Tip i vërtetë/ FreeSans
  - *Madhësia e fontit*: Madhësia e fontit në pika
  - *Drejtimi i grafikut*: Nëse grafiku shkon nga lart poshtë, apo nga e majta djathtas
    - Vertikalisht (prej lart poshtë)
    - Vertikalisht (prej poshtë lart)
    - Horizontalisht (nga e majta në të djathtë)
    - Horizontalisht (nga e djathta në të majtë)
  - *Numri i faqeve horizontale*: GraphViz mund të krijojë grafiqe shumë të mëdhaja duke shpërndarë grafikun nëpër një fushë drejtëkëndëshe të faqeve. Kjo kontrrollon numrin e faqeve në fushë, hirizontalisht. **Vlen vetëm për dot, poshtëshënim dhe pdf përmes Ghostscript**.
  - *Numri i faqeve vertikale*: GraphViz mund të krijojë grafiqe shumë të mëdhenj duke shpërndarë grafikun nëpër një fushe derjtëkëndëshe të faqeve. Kjo kontrrollon numrin e faqeve në fushë, vertikalisht. Vlen vetëm për dot, poshtëshënim dhe pdf përmes Ghostscript.
  - *Drejtimi i faqeve*: Rendi në të cilin dalin faqet grafike. Ky opsion zbatohet vetëm nëse faqet horizontale apo ato vertikale janë më shumë se 1.

------------------------------------------------------------------------

![[_media/Relgraf5.png|Fig. xx Opsionet e GraphViz]]

- **Opsionet eGraphViz**
  - *Përpjestimi i aspektit*: **Ka ndikim të madh** në atë se si grafiku është vendosur në faqe.
    - Madhësia minimale
    - Plotëso zonën e dhënë
    - Përdor numrin optimal të faqeve
  - *DPI*: pika në një inç. Zakonisht mes 75 dhe 120 nëse nxjerrin .png apo .gif skedarë, por 300 apo 600 nëse nxjerrin skedarë që duhet të prinothen. Kur krijon ikazhe si .gif apo .png skedarë për ueb-in, provo numrat si 100 apo 300 DPI. Kur krijon Poshtëshënim apo PDF, përdor 72 DPI.
  - *Ndarje e nyjes me hapësira*: Vlera minimale e hapësirës së lirë, në inç, mes nyjeve të vetme. Për grafie vertikale, kjo i përgjigjet ndarjes me hapësira mes shtyllave. Për grafiqet horizontale, kji i përgjigjet ndarjes me hapësira mes rreshtave. E parazgjedhur është 0.20''.
  - *Ndarje e rradhëve me hapësira*: Vlera minimale e hapësirës së lirë, në inç, mes rradhëve. Për grafiqet vertikale, kjo i përgjigjet ndarjes me hapësira mes rreshtave. Për grafiqet horizontale, kjo i përgjigjet ndarjes me hapësira mes shtyllave. E parazgjedhur është 0.20''.

------------------------------------------------------------------------

![[_media/Relgraf6.png|Fig. xx Shënim]]

- **Shënim**:
  - SHënim për t'u shtuar në grafik: Ky tekst do të shtohet në grafik
  - Vendndodhja e shënimit : Nëse shënimi do të shfaqet në krye apo në fund të faqes
  - Madhësia e shënimit: Madhësia e shënimit si tekst, në pika

  

#### Opsione të dokumentit

- *Formati dalës*: formatet të cilat janë në dispozicion: PDF (Ghostscript dhe GraphViz), PostScript, SVG, SVGz, JPEG, GIF, PNG dhe Skedari GraphViz Dot
- *Emri i skedarit*: zgjedh se ku do të ruhet skedari dhe me cilin emër të skedarit

#### *.Dot* skedarët

Nëse përdorni skedarë duhet të kuptoni se ato skedarë janë planifikuar që të përpunohen nga programe tjera. Vetë skedarët nuk do të sigurojnë informacione me kuptim; Skedarët së pari duhet të përpunohen nga program tjetër.

Vegla **'dot**' e GraphViz mund ta transformojë grafikun në postscript, jpeg, png, vrml, svg, dhe formate tjera. Veglat GraphViz janë të mundshme nga \[sajti i GraphViz <http://www.graphviz.org/>\].

Prandaj sigurohu nëse keni instaluar **Graphviz**. Përdor rregulluesin tuaj të paketës në Linux.

Në Ubuntu Hardy verzioni aktual është **2.16.3ubuntu2**. Skedari është vetëm 1.2 MB dhe siguron disa komanda si: *dot*, *gvcolor*, *dijkstra* ....

Përdoruesit Ubuntu Gutsy marrin paketën deb përmes Synaptic apo linjës së komandës (versioni i tanishëm GraphViz 2.12)

You can find a detailled explanation in a tutorial [How to make a relationship chart](http://www.gramps-project.org/wiki/index.php?title=Howto:_Make_a_relationship_chart)

#### Shembull

![[_media/Relgrafexample.png|Fig. xx Shembull i Familjeve të pasardhësve të ...]]

Të japim një shembull të thjeshtë. Duam grafik të një marrëdhënie me Familje të pasardhësve të një personi të caktuar.

1.  Së pari kontrrollo nëse ky është *person aktiv*. (Më vonë mund ta ndryshoni por kjo është më e lehtë)
2.  Shko përmes menysë
3.  Madhësia e letrës : A4 peisazh metrik: e dimë që nuk do të ketë shumë njerëz në grafik, pra kjo është në rregull
4.  Opsione të raportit: filtër: Familjet e pasardhësve të... zgjedh data të përfshira, të kufizuara me vite dhe duam edhe ID
5.  Stili i grafikut : Mbush ngjyrën, kënde të rrumbullakëta dhe shfaq Nyje të familjeve
6.  Peisazh i GraphViz: Madhësia e fontit: 15 pts Drejtimi FreeSans: nga lart poshtë
7.  Opsione të GraphViz: Mbush zonën e dhënë dpi 133
8.  Shënim : SHtojmë titullin në krye madhësia: 18 pts
9.  Fromat i përfundimtarë: duam një skedarë JPEG dhe pasi të bëhet grafiku, të hapim një Shikues Imazhi.

Rezultatin mund ta shihni në imazhin nga ana e djathtë..

## Raporte tekstuale

Raportet tekstuale paraqesin informacionin e dëshirueshëm si tekst i formatuar. Shumica e opsioneve janë të zakonshme mes raporteve tekstuale, prandaj ato do të përshkruhen vetëm një herë, në fund të këtij seksioni. Opsionet të cilat janë të veçanta për një raport të dhënë, do të përshkruhen direkt në të hyrën e raportit.

Raportet vijuese tekstuale janë momentalisht të mundshme në Gramps:

### Raporti Ahnentafel

![[_media/Ancestor_report1.png|Fig. a.1 Opsine të raportit]]

Ky raport vë në listë Personin aktiv dhe paraardhësit e tij apo të saj së bashku me të dhënat e tyre të domosdoshme.

Njeërzit numërohen sipas një mënyre të veçantë e cila është një standard i quajtur Ahnentafel.

Personit aktiv i jipet numri 1. Babai dhe nëna e tij apo e saj kanë numrat 2 dhe 3.

Ky rregull vazhdon për çdo person përderisa shkoni mbrapa në gjenerata: prindërit e babait janë me numër 4 dhe 5, ndërsa prinëdrit e nënës janë me numrër 6 dhe 7, baballarët gjithmonë numërohen me numra çift ndërsa nënat me numra tek.

Si rrjedhim, secili person që ka numrin N në këtë pemë, numrat e babait dhe nënës janë 2N dhe 2N+1.

`   personi = n`  
`   Babai   = 2n`  
`   Nëna    = 2n+1`

Çdo e hyrë do të përmbajë një paragraf të vetëm, dhe duhet të përmbajë përmajtjet në vijim:

- Numrin e personit.
- Emrin e personit.
- Informacione të lindjes, nëse janë të mundshme.
- Informacione mbi vdekjen, nëse janë të mundshme.
- Informacione mbi varromin, nësa janë të mundshme

<!-- -->

-   
  Me opsionet e letrës mund të ndryshoni

  - Formatin e letrës (madhësinë dhe orientimin)
  - Margjinat (Majtas, Djathtas, në Krye dhe në Fund)

dhe nëse duhet të përdorni vlera metrike apo jo.

------------------------------------------------------------------------

-   

  - Format përfundimtarë: zgjedh formatin përfundimtarë:
    - Dokument HTML
    - LaTex
    - Tekst i hapur i dokumentit
    - Dokument PDF
    - Printo...
    - Dokument RTF
    - dokument me tekst të thjeshtë

Me mund të shënoni për të hapur dokumentin e bërë me Përpunuesin e Fjalës OpenOffice.org apo një Shikues Dokumenti (skedarë PDF).

- - Emri i skedarit: vlera e parazgjedhur është */home/<username>/ancestor_report.pdf*.
  - Stili: *stili i parazgjedhur* i parazgjedhur . Me mund të shtoni Stilet e dokumentit.

------------------------------------------------------------------------

-   

  - Personi qëndrorë: personi qëndrorë për raportin.
  - Gjeneratat: Numri i gjeneratave për t'u përfshirë në raport. E parazgjedhur : 10 gjenerata
  - Kutia e zgjedhjes: Ndërprerje e faqes mes gjeneratave: A të nisni një faqe të re pas çdo gjenerate.
  - Kutia e zgjedhjes: Shto një ndrëprerës të vijës pas çdo emri: Tregon nëse një ndërprerje e vijës dohet të ndjekë emrin.
  - Kutia e zgjedhjes: Ngjesh pemën: të ngjeshni pemën apo jo.

------------------------------------------------------------------------

![[_media/Ancestor_report2.png|Fig. a.1 Rezultatet e raportit Ahnentafel]]

  

------------------------------------------------------------------------

### Raporte të ditëlindjeve dhe përvjetoreve

![[_media/Birthday_report1.png|Fig. a.1 Opsione të raporteve]]

ky raport jep informacione të njejta si një raport kalendarik por në format tekstual.

-   
  Me Opsionet e letrës mund të ndryshoni

  - Formatin e letrës (madhësia dhe orientimi)
  - Margjinat (Majtas, Djathtas, në Krye dhe në Fund)

dhe nëse duhet të përdorni vlera metrike apo jo.

------------------------------------------------------------------------

-   

  - Formati përfundimtarë: zgjedh formatin përfundimtarë:
    - Dokument HTML
    - LaTex
    - Tekst i hapur i dokumentit
    - Dokument PDF
    - Printo...
    - Dokument RTF
    - dokument me tekst të thjeshtë

Me mund të shënoni për të hapur dokumentin e bërë me Përpunuesin e Fjalëve OpenOffice.org apo një Shikues Dokumenti (skedarë PDF).

- - Emri i skedarit: vlera e parazgjedhur është */home/<username>/birtday_report.pdf*.
  - Stili: *stil i parazgjedhur* i parazgjedhur. Me mund të shtoni Stile të dokumentit.

------------------------------------------------------------------------

-   

shihni opsione të raportit kalendarik

------------------------------------------------------------------------

![[_media/Birthday_report2.png|Fig. a.1 Rezultat i raportit të ditëlindjeve]]

  

------------------------------------------------------------------------

### Raport i plotë personal

Ky raport siguron përmbledhje personale të ngjajshme me atë të raportit të përmbledhjes personale (gramps 2.0.x). Përparësia e këtij raporti është opsione i filtrit të veçantë. Varësisht nga zgjedhja e filtrit (vetëm Personi aktiv, pasardhësti e tij apo të saj, paraardhësit e ti apo të saj, apo e gjithë baza e të dhënave), raporti mund të përmbajë prej një në disa përmbledhje personale. Një opsion tjetër për këtë raport është përfshirja e informacioneve burimore kur i vendosni ngjarjet në listë.

### Raport për pasardhësit

Ky raport jep një përshkrim të shkurtër të pasardhësve të Personit aktiv. Opsione të veçanta: numri i gjeneratave të mëtutjeshme që duhet të merret në konsideratë.

### Raport i hollësishëm për paraardhësit

Ky raport mbulon në hollësi paraardhësit e personit aktiv. Përfshin të dhëna të rëndësishme (të lindjes dhe të vdekjes) si dhe martesa. Opsione të veçanta: numri i gjeneratave nga prapa që duhet të merret në konsideratë, si dhe një opsione të ndryshme për sa i përket përmbajtjeve të sakta që duhet të përfshihen.

### Raport i hollësishëm për pasardhësit

Ky raport përfshin në detale pasardhësit e personit aktiv. Përfshin informacione të rëndësishme (të lindjes dhe të vdekjes) si dhe martesa. Opsione të veçanta: numri i gjeneratave të mëtutjeshme që duhet të merren në konsideratë.

### Raport për mbarimin e brezit

Ky siguron një listë të paraardhësve të fundit me prejardhje të njohur për personin, të rradhitur sipas gjeneratave.

### Raport për grupën famljare

Kjo krijon një raport për grupën familjare, duke shfaqur informacione mbi një palë prindër dhe fëmijët e tyre. Opsione të veçanta: bashkëshorti/ja (është i mundshëm vetëm nëse Personi aktiv ka më shumë se një bashkëshort).

### Raporte për farefisninë

Kjo siguron farefisninë e personit të përzgjedhur sipas hulumtimit të niveleve (lartë, poshtë sipas gjeneratave) të vendosur nga përdoruesit.

### Raport i shënuesit

Kjo vë në listë objektet parësore (personin, familjen, shënime) të cilat përputhen me shënuesin e përzgjedhur.

------------------------------------------------------------------------

### E zvogëluar

- Përmbledhje e raportit të paraardhësve: Ky raport krijon një përshkrim të përmbledhur të paraardhësve të Personit aktiv. Ngjarjet e këtij raporti përfshijnë peisazh të përpunuar, imazhe të fëmijëve, bashkëshortët e tanishëm dhe të mëparshëm dhe citate të burimeve. Opsione të veçanta: numri i gjeneratave nga mbrapa që duhet të mirret në konsideratë, nëse duhet të citohen burime dhe nëse duhet të ndërprehen faqe mes gjeneratave.
- FTM stili i raportit të paraardhësve: Ky raport krijon një raport për paraardhësit të ngjajshëm me atë që është dhënë nga programi i SHënuesit të pemës familjare (tm). Përfshin në detale Personin aktiv dhe paraardhësit e tij/saj. Përfshin informacione të rëndësishme si dhe martesa, fëmijë dhe shënime. Opsione të veçanta: numri i gjeneratave nga mbrapa që duhet të merret në konsideratë.
- FTM Stili i raportit për pasardhësit: Ky raport krijon një raport për pasardhësit të ngjajshëm me atë të dhënë nga programi i Shënuesit të pemës familjare (tm). Përfshin në detale Personin aktiv dhe pasardhësit e tij/saj. Përfshin informacione të rëndësishme si dhe martesa, fëmijë dhe shënime. Opsione të veçanta: numri i gjeneratave të mëtutjeshme që duhet të merret në konsideratë.
- Përmbledhje e një individi: Ky raport jep një përmbledhje të hollësishme për personin aktiv. Raporti përfshin të gjitha faktet në bazën e të dhënave rreth atij personi.

------------------------------------------------------------------------

### Opsionet e përbashkëta

Opsionet e përbashkëta për raportet e tekstit janë: emri i skedarit i përfundimit, formati i përfundimit, stili i përzgjedhur, madhësia dhe orientimi i faqes. Pëe raporte HTML, nuk ka informacione të faqes. Në vend të saj, opsionet HTML përfshijnë zgjedhjen e shabllonit HTML, është i mundshëm në Gramps ose në një shabllon të përbashkët të përcaktuar nga ju. raportet mund të hapen menjëherë me aplikimin e parazgjedhur.

## Pamja

Raportet e pamjes paraqesin përmbledhje të tërësishme të informacioneve të të dhënave të cilat janë të mundshme përnjeherësh për shikim në ekran. Raportet vijuese të pamjes aktualisht janë të mundshme në Gramps:

### Nuk janë në lidhje

![[_media/NotRelated-NotRelatedToWindow-40.png|Fig. a.a Nuk janë në lidhje]] Ky raport do të gjejë njerëz të cilët nuk janë të lidhur me personin e përzgjdhur. Mund të ekzekutoni këtë pamje përmes menysë **Raporte--\>Pamje--\>Nuk janë në lidhje...**.

Do të merrni një dritare e cila shfaq një listë të të gjith personave të cilët NUK janë në lidhje me personin e përzgjedhur.

Kjo listë ju jep:

- Emrin
- ID
- Prindërit
- Shënuesin

Me butonin dhe butonin mund ta mbyllni apo ta zgjeroni listën. Klikimi i dyfishtë mbi një person, do të sjellë dritaren për redaktim të hollësishëm të personit apo dritarja për redaktimin e familjes.

Nëse përzgjedhni një person, mund ta përdorni fushën për e tekstit: janë të mundshme 3 zgjedhje: e zbrazët (mund ta plotësoni me çfarëdo që ju përshtatet juve), PËR TË BËRË, dhe Nuk janë të lidhur. Me butonin mund ta aplikoni shënuesin e përzgjedhur tek personi. Ky shënues pastaj do të shfaqet në anën e djathtë të shtyllës.

### Numri i paraardhësve

![[_media/numberanc.png|Fig. a.a Numri i paraardhësve]]

Ky raport afishon numrin e paraardhësve të personit aktiv.

Vetëm zgjedh një person dhe kliko në menynë **Raport--\>Pamje--\>Numri i paraardhësve...**.

Dritarja do të shfaqet me bërjen e listës së detaleve:

gjenerata e 1 ka 1 individ : 100% : ky është personi me të cilin keni filluar gjenerata e 2 ka 2 individ : 100% : të dy prondërit njihen

Gjenerata e 8 ka 35 individ : 27.34 % : kjo do të thotë që nga (2\*\*7) 128 paraardhës të mundshëm në gjeneratën 8, njihen 27%.

Paraardhësit total në gjeneratën e 2 në .. është gjithashtu e dhënë në numra dhe përqindej.

Me butonin mund të mbyllni dritaren dhe këtë raport.

### Përmbledhje nga baza e të dhënave

![[_media/sumdata.png|Fig. a.b Përmbledhje]]

Ky raport afishon statistikat e tërësishme për sa i përket numrit të individëve të secilës gjini, statistika të ndryshme të të hyrave jo të plota, si dhe familje dhe media statistikë.

Mund ta akzekutoni këtë raport përmes menysë **Raport--\>Pamje--\>Përmbledhje nga baza e të dhënave...**.

- Individë: shfaqen numrat në kategori të ndryshme
  - Numri i individëve:
  - Meshkuj:
  - Femra:
  - Individ me gjini të panjohur:
  - Individ me emra jo të plotë:
  - Individ që ju mungojnë datat e lindjes:
  - Individ me lidhje të ndërprera:

<!-- -->

- Informacione për familjen:
  - Numri i familjeve:
  - Emra të veçantë:

<!-- -->

- Media Objekte:
  - Individ me media objekte:
  - Numri i përgjithshëm i referencave të media objekteve:
  - Numri i media objekteve të vetme:
  - Madhësia totale e media objekteve: në bajt

<!-- -->

- Media objekte që mungojnë: kjo do të shfaqë shteg të plotë dhe emra të skedarëve të secilit media objetk që mungon.

Informacioni i dhënë në këtë raport është i njejtë me si me atë në [Statistics_Gramplet](http://www.gramps-project.org/wiki/index.php?title=Gramps_6.0_Wiki_Manual_-_Gramplets#Statistics_Gramplet)

## Ueb faqe

### Veb sajt i rrëfyer

![[_media/NWeb-Man-Mainz.jpg|fig. c.1 Faqe e listës individuale në stilin Mainc]] Njëri nga raportet në këtë kategori është raporti i veb sajtit të rrëfyer. Ai nxjerr një veb sajt (që është, një grup i veb faqeve të lidhura), për një grup të individëve të përzgjedhur.

#### Hyrje

Gramps 2.0.6 e vë në zbatim gjeneratorin Narrative Web. Raporti i veb sajtit të rrëfyer të Gramps 6.0 siguron funksionim të përmirësuar, mbështet standarded e veb-it dhe tiparet plotësuese. Raporti i ri krijon faqe të cilat me kujdes ndjekin Rekomandimin World Wide Web Consortium’s për XHTML 1.0 Strict dhe CSS 1. Këto rekomandime përfshijnë një ndarje të përmbajtjes nga paraqitja. Sa i përket kësaj, stili dhe pamja e veb faqes së re, mund plotësisht të kontrrollohet nga një CSS fletë e stilizuar pa ndryshuar faqet e vetme.

Më shumë informacione tani afishohen për secilin person, së bashku me informacione për burime, vende, dhe media objekte. Faqet hyrëse mund të shtohen për të sigurar informacione shtesë, si historinë e një familjeje.

Regjistrimet gjenealogjike mund të nxjerrin shumë skedarë. Shumë veb server kanë vështirësi me një numër të madh skedarësh në një direktorium të vetëm. Raporti i veb sajtit të rrëfyer përpiqet të mbajë numrin e skedarëve në direktorium në një nivel që është i lehtë për përdorim. Për të vepruar kështu, krijohet një hierarki e direktoriumeve. Emrat e skedarëve të nxjerrur nuk janë intuitive, por janë të veçanta për çdo person. Ekzekutimet në vijim do të nxjerrin emra identik të skedaërve, duke e bërë më të lehtë përditësimin e skedarëve të veçantë.

Nëse keni probleme kur transferoni skedarë në një veb pritës të jashtëm, mund të krijoni një skedar të vetëm gzip'd tar për të ngarkuear më lehtë të dhënat. (Ju lutem përdoreni këtë metodë nëse dëshironi të përdroni veb sajtin pritës të Gramps.)

Për të përzgjedhur skedarin gzip'd, përzgjedh Ruaj veb faqet në opsionin e arkivës .tar.gz .

#### Përdorimi i raportit

Raporti i veb sajtit të rrëfyer furnizon përdoruesin me opsione që lejojnë një përfshirje të gjërë të përshtatjes. Mun ta ekzekutoni këtë raport përmes menysë **Raporte--\>Veb Faqe--\>Veb sajt i rrëfyer...**.

Dritarja e dialogut i raportit të veb sajtit të rrëfyer, ka katër skeda: **Opsionet e raportit**, **Gjenerata e faqes**, **Fshehtësi** dhe **E përparuar**. Secila prej atyre skedave do të rishikohet më poshtë.

#### Opsionet e raportit

![[_media/NWeb-Man-Nebr.jpg|fig. c.2 Faqe Individuale e hollësishme në stilin Nebraska]]

Rauj veb faqe në arkivën .tar.gz  
Numri i madh i skedarëve dhe direktoriumeve në këtë veb dalje mund ta bëjë të vështirë transferimin e skedarëve në një veb pritje të jashtme. Gramps ka aftësinë e ruajtjes së gjitha skedarëve të Narrative Web në një arkivë të ngjeshur duke përdorur formatet gzip dhe tar (rastësisht e njëhur si një ‘tarball’). Ky skedar i vetëm me shpejtësi mund të transferohet në server-in tuaj. Për fat të keq jo të gjithë veb serverat mbështesin ruajtjen e veb skedarëve në këtë mënyrë, prandaj kontaktoni furnizuesin tuaj për më shumë informacione.

<!-- -->

  
Sajti i lirë pritës gjenealogjik i siguruar nga organizata e Gramps do të pranojë skedarët tuaj vetëm në një arkivë të ngjeshur. Për sajtin e lirë pritës gjeneaëogjik mëso këtu: <http://library.gramps-project.org>

Drejtimi  
Dalja e raportit të të Veb-it të rrëfyer është suajtur këtu sipas parazgjedhjes . Ky opsion ju mundëson të ruani daljen e raportit tuaj në një drejtim që zgjedhni ju.

Filtri  
Sikur gjeneratori i mëparshëm i veb faqes dhe raporteve tjera të Gramps, mund të kontrrolloni se pka është përfshirë në dalje duke zgjedhur një filtër. Disa filtra të parazgjedhur sigurohen për ju, por mund të bëni filtër tuaj personal për nevojat tuaja. Këtu mund të mësoni më shumë për filtrat tuaj personal : [Filter](wiki:Filter).

Secili person që pëputhet me këtë filtër i cili nuk përjashtohet për shkak të rregullave për fshehtësi, do të përfshihet në daljen. Filtri i parazgjedhur përfshin të gjithë njerëzit në bazën e të dhënave.

Person për filtrin  
Ky opsion është joaktiv nëse opsioni parësor i filtrit vendoset në ‘Gjith bazën e të dhënave’. Filtrat në përgjithësi janë subjekt i asja se si një person i veçantë lidhet me individ tjerë. Ky opsion ju mundëson të përcaktoni individin parësorë. Përdor butonin për të përzgjedhur ndonjë individ në bazën tuaj të të dhënave.

Titulli i veb sajtit  
Vlera e titullit të parazgjedhur është **Pema ime familjare**. Mund të futni një titull të përshtatur sajti në këtë opsion.

Zgjerimi i skedarit  
Zgjerimi i skedarit që do të përdoret për veb skedarët. Zgjedh mes vlerës së parazgjedhur , .htm, .shtml, .php, .php3, apo .cgi.

E drejta e autorit  
Kur krijoni një veb sajt publik, është me rëndësi të përcaktoni kushtet e të drejtës së autorit, sipas të cilave i publikoni të dhënat tuaja. Ligji ndërkombëtar për të drejtat e autorit ruan të gjitha të drejtat e të dhënave tuaja në diskrecionin tuaj. Ju i zotëroni të dhënat dhe individët duhet të kenë leje nga ju nëse dëshirojnë t'i përdorin përsëri të dhënat. Gjatë hulumtimit gjenealogjik, ndarja e të dhënave me hulumtuesit tjerë është e zakonshme. Sipas parazgjedhjes raport i i Vbe-it të rrëfyer përdor të drejtën e autorit **Të gjitha të drejtat janë të ruajtura**. Opsionet tjera përfshijnë licencat Creative Commons, duke ofruar zgjedhje të kufizimeve për përdorim apo asnjërën prej tyre. Më shuë për Creative Commons mësoni në <http://creativecommons.org/>

Enkodimi i grupës së karaktereve  
Gramps është një aplikacion ndërkombëtarë i zhvilluar me shumë gjuhë dhe përkthime në kujtesë. Për shkak të kësaj, grupa e parazgjedhur e karaktereve për faqet HTML është , e cila mbështet një një zgjedhje të gjerë të kaaktereve dhe simboleve ndërkombëtare. Nga menyja me lëshim poshtë, mund të përzgjedhni nga grupe të ndryshme të enkodimit apo dhe një grupe enkodimi . Në të vërtetë, kaa mbështetje për të gjitha enkodimet e njohura të grupeve të karaktereve. Nëse keni probleme me paraqitjen e karaktereve në veb faqet tuaja, mund të jetë për shkak se duhet të përzgjedhni enkodim të grupës së karaktereve të përshtatshëm për mjedisin e veb serverit tuaj.

![[_media/NWeb-Man-BasicSet.jpg|fig. c.3 Stili themelorë - 5 zgjedhje të ngjyrave]]

Fletë e stilit  
Gramps siguron shtatë fletë të stilin të vendosura për ju prej të cilave do të zgjedhni për të përcaktuar pamjen apo veb faqet tuaja. Në Gramps 6.0 mund të zgjedhni mes stileve **Themelorë** (skema e ngjrave: hiri, qiparis, vjollcë, pjeshkë apo e gjelbërt), **Mainc**, apo **Nebraska**. Gjithashtu ka opsion edhe për mospërfshirjen e një flete të stilit (**Pa fletë të stilit**). Pa marrë parasysh se çfarë stili zgjedhni, emri i skedarit të fletës së stilit është *narrative.css*. Mund të redaktoni këtë skedar për të përshtatur më tutje pamjen e veb faqeve tuaja.

Nëse bëni modifikime në fletën tuaj të stilit, të jeni të vetëdijshëm se rinxjerrja e faqeve tuaja me drejtimin e nejtë të daljes do të mbishkruajë fletën tuaj të përshtatur të stilit. Për ta mbrojtur fletën tuaj të përshtatur të stilit përmes përditësimeve të veb faqeve tuaja që vijnë në vazhdim, përzgjedh .

*figurat c.1, c.2 dhe c.3 janë shembuj të stileve të përfshira kohën e fundit me Gramps 6.0*

Përfshij grafë të paraardhësve  
Zgjedhja e kësaj kutie përfshin një grafë të paraardhësve në faqen e detaleve të secilit individ’s nëse ato kanë përcaktuar paraardhës në bazën tuaj të të dhënave.

Gjenerata në graf  
Ky opsion është joaktiv nëse nuk zgjedhet opsioni "Përfshij graf të paraardhësve". Numri i parazgjedhur i gjeneratave të shfaqura në grafin e paraardhësve është me ospione 2, 3, 4 apo 5.

<!-- -->

  
Individët e paraqitur në grafin e paraardhësve, janë individët e njejtë informacionet e të cilëve sigurohen gjithkund në veb faqet tuaja.

#### Nxjerrja e faqeve

Raporti i veb sajtit të rrëfyer mund të vendoset për të nxjerrur tri faqe plotësuese: **Fillestare**, **Hyrje** **Kontaktet e publikuesit**. Nga kjo skedë mund të aktivizoni faqet dhe të caktoni media artikuj apo artikuj të shënimeve në secilën faqe. Sipas paraazgjedhjes asnjë përmabjtje (media apo tekst) nuk është caktuar në këto faqe. Përmbajtja për këto faqe duhet të dalin si media artikuj apo artikuj të shënimeve. Nëse tashmë artikujt që keni dëshiruar janë shtuar në bazën tuaj të të dhënave, do të keni mundësi t'i zgjedhni ato nga një listë e shënimeve apo media objekteve.

Faqja fillestare, Hyrje dhe Kontaktet e publikuesit  
Këto faqe do të afishojnë një media objekt të vetëm dhe/apo një shënim sipas zgjedhjes tuaj. Për të aktivizuar cilëndo nga këto fae, zgjedh një gjatë përzgjedhjes së butonit në të djathtë të vënies në listë të faqes përkatëse.

<!-- -->

  
Ju lutem përdorni me kujdes faqen kontaktuese të publikuesit nëse jeni duke publikuar veb faqet tuaja në një veb server me qasje publike.

HTML koka e faqe së përdoruesit dhe HTML fundi i faqes  
Këto lemente do të afishojnë një shënim të vetëm sipas zgjedhjes suaj. Teskti i kokës së faqes së përdoruesit të HTML do të shfaqet poshtë titullit të sajtit në çdo faqe. Fundi i faqes së përdoruesit HTML do të shfaqet brenda fundit të faqes, sipër njoftimit për të drejtën e autorit nç çdo veb faqe. (Ky tipar momentalisht po zhvillohet me shpejtësi dhe mund të bëhet subjekt i ndryshimeve dramatike në publikimet në vazhdim të Gramps.)

Përfshij imazhe dhe media objekte  
Ky opsion përcakton nëse duhet të përfshihet/përjashtohet një galeri e media objekteve në veb sajtin tuaj.

Përfshij faqe për shkarkim  
Ky opsion përcakton nëse duhet të përfshini një faqe të quajtur "Shkarkime". Kjo faqe do të jetë e zbrazët dhe sigurohet në rast se do të donit të ofroni shkarkime të bazës suaj të të dhënave, media objekteve apo referencave, për visitorët tuaj.

Ndalo Gramps ID  
Ky opsion përcakton nëse duhet të përfshihet Gramps ID e objekteve në daljen e veb faqes tuaj.

#### Privatësi

Privatësia e informacioneve personale është një çështje e rëndësishme. Gramps siguron vegla dhe parametra që ju japin mundësi të kontrrolloni privatësinë e të dhënave tuaja.

Përfshij regjistrime që janë shënuar si personale  
Nëse keni për qëllim të siguroni një regjistrim të plotë nga hulumtimi juaj, zgjedhja e kësaj kutie do të përfshijë të gjitha të hyrat e shënuara **personale** së bashku me bazën tjetër të të dhënave tuaja.

Njerëzit që jetojnë  
Mund të kontrrolloni afishimin e informacioneve të ndieshme të bazuar në atë së a është momentalisht gjallë një individ apo jo. Sidoqoftë, që kur Gramps është vegël kërkimi, mund të ketë individ me datë të panjohur të vdekjes në bazën tuaj të të dhënave. Për të konkluduar nëse një individ *mund të jetë akoma i gjallë* Gramps përdor një algoritëm që krahason datat e vdekjes, datat e lindjes, data të pagëzimit, datat e vdekjes dhe të lindjes të paraardhësve. Algoritmi supozon se çdo individ *mund të jetë akoma i gjallë* veç nëse datat me referencë të kryqëzuar bëjnë që *mundësia për të qenë i gjallë* i një individi të jetë e pamundshme.

- **Përfshij** – Përfshij të gjitha informaconet e të gjithë individëve edhe pse ato *mund të jenë të gjallë*
- **Përjashto** – Përjashto të gjitha informacionet e të gjithë individëve të cilët *mund të jenë të gjallë*
- **Kufizo** – Përjashto të gjitha informacionet e të gjithë individëve të cilët *mund të jenë të gjallë*, por afisho marrëdhënien e tyre me individ të tjerë përderisa zëvendësoni emrin e tyre me fjalën “Jeton”

Vitet nga vdekja për të konsideruar se jetojnë  
Ky opsion është joaktiv nëse opsion "Njerëz që jetojnë" vendoset në **Përfshij**. Disa shtete kanë ligje që përcaktojnë një numër të caktuar të viteve pas vdekjes para se të publikohen informacionet për individin. Këtu mund të përcaktoni numrin e viteve pas vdekjes të cilat duhet të përputhen me ligjet e këtilla. Vlera e parazgjedhr është 30 vite.

![[_media/NWeb-Man-Print.jpg|fig. c.4 Pamja e parazgjedhur e faqeve të printuara nga vebd faqja e Veb sajtit të rrëfyer]]

  
Ju lutem vini re hulumtuesi ka përgjegjësi tÇi nënshtrohet ligjeve për privatësi dhe privatësinë e individëve. Gramps nuk mund të mbajë përgjegjësi për nënshtrimin e ligjeve për privatësi apo për çështje tjera private.

#### E avancuar

Parametrat aktual të përparuar së pari i drejtohen sasisë së informacionit të afishuar në veb faqet për hollësitë e Mbiemrit dhe treguesit individual. Ato janë opsione të thjeshta kyç-apo-çkyç të cilat mund të kuptohen me disa sqarime.

- përfshij një lidhje në personin amë në çdo faqe
- përfshij një shtyllë për datat e lindjes në faqet treguese
- përfshij një shtyllë për datat e vdekjes në faqet treguese
- përfshij një shtyllë për partnerë në faqet treguese
- përfshij një shtyllë për prindër në faqet treguese
- përfshij një shtyllë për motrat/vëllezërit nga njerka në faqet treguese

### Veb kalendar

## Raporte të shpejta

[Raporte të shpejta](wiki:Quick_Reports) janë raporte të cilat janë të mundshme në menynë e përmbajtjes së personit, familjes , ... Përdoruesit lehtë mund t'i bëjnë ato, edhe me njohuri me kodim të kufizuare.

![[_media/Gramps_quick_report_view.png|menyja e përmbajtjes të raporteve të shpejta në Pamjen e personit]] Shumica e përdoruesëve duan të krijojnë me shpejtësi një raport për nevojat e tyre të veçanta, por pengohen për shkak se nuk duan ta mësojnë plotësisht python, dhe as ndërlikimet e një programi të ndërlikuar si Gramps.

Për ata, është krijuar një vegël e re: raportet e shpejta. Këto janë raporte të shkurtëra tekstuale të clat përdoruesi mund të regjistrojë me Gramps, pra ato automatikisht shfaqen në menynë e përmbajtjes. Duke shoqëruar këtë, krijohet një [qasje e thjeshtë në bazën e të dhënave](wiki:Simple_Access_API) dhe një ndërfaqe e thjeshtë e dokumentit, për të fshehur sa më shumë ndërlikime.

[Category:Sq:Documentation](wiki:Category:Sq:Documentation)
