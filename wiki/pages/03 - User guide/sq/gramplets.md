---
title: Sq:Gramps 6.0 Wiki Manual - Gramplets
categories:
- Sq:Documentation
managed: false
source: wiki-scrape
wiki_revid: 126014
wiki_fetched_at: '2026-05-30T20:49:37Z'
lang: sq
---

# Gramplete

![[_media/DashboardCategory-DashboardView-default-gramplets-60.png|Fig. 6.0 Pamja e Grampleteve]]

Një Gramplet Gramps është pamje e të dhënave të cilat ose ndryshojnë në mënyrë dinamike gjatë ekzekutimit të Gramps, ose sigurojnë bashkëveprimtari në të dhënat tuaja gjenealogjike. Cili është dallimi midis grampleteve, raporteve, pamjeve të shpejta dhe veglave?

- Raportet sigurojnë një format statik të përfundimeve të të dhënave tuaja, në mënyrë tipike për printim
- Pamja e shpejtë siguron një listë tipike të shkurtër, bashkëvepruese e nxjerrë nga të dhënat tuaja
- Veglat sigurojnë një metodë të përpunimit të të dhënave tuaja
- Grampletet sigurojnë një pamje dhe ndërfaqe dinamike të të dhënave tuaja

Grampletet janë vixhete të cilat janë pjesë e Gramps dhe mund të shihen në [Pamjen Gramplet](wiki:Gramps_6.0_Wiki_Manual_-_Main_Window#Gramplets_View). Vixhet sigurojnë të gjitha llojet e funksioneve që mund të jenë të dobishme për hulumtuesin.

Kur të nisni Pamjen për të parën herë, do të shihni **Gramplet-in e Mesazhit Mirëseardhës** dhe **Gramplet-i i Mbiemrave më të përdorur**.

![[_media/DashboardCategory-gramplet-detached-and-docked-example-60.png|Fig. 6.0 Pamje e Veçuar e Grampleteve]]

Mund të zvarritni butonin e Vetive (lart majtas) të secilit gramplet për të lëvizur atë nëpër ekran. Duke klikuar Vetitë do të ndahet grampleti nga Pamja e Gramplet-it dhe do të vendosë atë në dritaren e vet. Dritarja do të mbetet hapur pavarësisht faqes (marrëdhënia, prejardhja, etj). Mbyllja e pamjes së veçuar do të vendosë në pamjen e Grampleteve. Nëse braktisni Gramps me një gramplet të hapur, kur të nisni gramps përsëri, do të hapet automatikisht.

Kur një apo më shumë Gramplete shkëputen nga Pamja e Grampleteve, mund të ndryshoni në një pamje tjetër (si Pamja e njerëzve apo e prejardhjes). Në këtë mënyrë, mund të përdorni këto gramplete për të plotësuar një pamje të veçantë me detale shtsë dhe një funksionalitet të siguruar nga grampleti.

Mund të shtoni gramplete të reja duke klikuar mbi një hapësirë të çelët në Gramplete. Gjithashtu mund të ndryshoni numrin e shtyllave duke klikuar me të djathtën një zonë të hapur në faqen e Grampleteve.

Këto gramplete janë aktualisht në dispozicion:

- Gramplet për Mirëseardhje
- Gramplet i Mbiemrave më të përdorur
- Grampleti i Mbiemrave të grumbulluar
- Grampleti PËR TË BËRË
- Grampleti i statistikës
- Grampleti i prejardhjes
- Grampleti Python
- Grampleti i të rejave
- Grampleti i ditarit të sesioneve
- Grampleti i kalendarit
- Grampleti i farefisit
- Grampleti i viteve me datë

Nëse një lidhje në një Gramplet është për një person të veçantë, atëherë duke klikuar lidhjen do të ndryshohet Personi aktiv. Duke klikuar dy herë ndonjë lidhje të tillë një artikulli të veçantë të Gramps (si personi apo familja) do të paraqesë Redaktuesin për atë artikull. Për të redaktuar një person të lidhur, pa ndryshuar Personin aktiv, kliko me të djathtën mbi lidhjen e personit. Varësisht nga lloji i hyrjes, klikimi dy herë i një rreshti në një tabelë të Pamjes së shpejtë, ose do të përzgjedhë më shumë të dhëna të veçanta ( double-clicking any row in a Quick View table will either select more specific data (ushtro tani) ose do të paraqesë redaktuesin.

Ky seksion do të përshkruajë secilin gramplet dhe funksionimin themelor të tuj.

## Grampleti për Mirëseardhje

![[_media/Welcome-ToGramps-detached-gramplet-40.png|Fig. 4.3 Grampleti për morëseardhje]]

Grampleti për mirëseardhje ju jep një mesazh hyrës përdoruesve të ri, dhe disa udhëzime bazë.

Mesazhi për mirëseardhje përshkruan se çka është Gramps, që programi është OSS dhe se si filloni një [Pemë familjare](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees).

Ky informacion mund të gjendet në [faqen fillestare të Gramps](wiki:Main_Page)

## Grampleti i mbiemrave më të përdorur

![[_media/TopSurnames-detached-gramplet-40.png|Fig. 4.4 10 mbiemrat më të përdorur]]

Grampleti i mbiemrave më të përdorur shfaq 10 mbiemrat e përdorur (me parazgjedhje).

Më të përdorurit paraqiten si vijon:

- Mbiemri
- përqindja
- ndodhitë

Lista ju jep gjithashtu mbiemrat Total unik në bazën e të dhënave si dhe numrin total të njerëzve në bazën tuaj të të dhënave.

Kliko dy herë një mbiemër për të ekzekutuar . Kjo hap dritaren , e cila ju jep njerëzit me mbiemrin që keni klikuar dy herë.

Paraqitet një tabelë e cila shfaq të gjithë njerëzit me mera që përputhen apo mera alternativ. Jipet emri i personit, data e lindjes dhe lloji i emrit.

Ndrysho numrin e emrave të afishuar duke redaktuar këtë sesion në ~/.gramps/gramplets.ini

## Gramplet i mbiemrave të grumbulluar

![[_media/SurnameCloud-detached-gramplet-40.png|Fig. 4.5 Mbiemrat e grumbulluar]]

Grampleti i mbiemrave të grumbulluar shfaq 100 mbiemrat më të përdorur (me paraqzgjedhje). Madhësia e fontit të emrit është proporcionale me grumbullin e nejrëzve me emra të njejtë.

Kliko dy herë një mbiemër për të ekzekutuar . Kjo do të hapë dritaren ku mund të gjeni të gjithë njerëzit me mera që përputhen apo alternativ. Jipen, personi, data e lindjes dhe lloji i emrit.

Nëse shkoni mbi emrin me miun, do ë shihni përqindjen e ndodhisë dhe pikët totale.

Ndrysho numrine e emrave të afishur duke redaktuar këtë në ~/.gramps/gramplets.ini

## Grampleti PËR TË BËRË

![[_media/TODOList-detached-gramplet-40.png|Fig. 4.6 Grampleti PËR TË BËRË]]

Grampleti PËR TË BËRË është larguar nga zona e tekstit. Mund ta përdorni këtë zonë për të vendosur disa shënime, vërejtje, gjerat që ju duhen për të vazhduar hulumtimin tuaj. Ka eedhe disa programe tjera PËR TË BËRË (sh. Tomboy e.a.) por ky Gramplet është i dobishëm përderisa informacioni qëndron brenda Gramps. Në versionet e ardhshme, do të keni mundësinë të ruani lidhje në artikujt e Gramps (si njerëz, ngjarje dhe familje). Kjo do t'ju mundësojë të mbani një grupë lidhjesh që vazhdoni të punoni së bashku.

Teksit është i qëndrueshëm në mes sesioneve. Të dhënat ruhen në disk, kur të dilni nga Gramps.

Mund të hapni më shumë lista PËR TË BËRË për të ruajtur lloje të ndryshme të temave apo të sistemoni informacionet tuaja.

Ndrysho titullin e gramplet-it duke redaktuar emrin e seksionit në ~/.gramps/gramps33/gramplets.ini

## Grampleti i statistikës

![[_media/Statistics-detached-gramplet-40.png|Fig. 4.7 Grampleti i statistikës]]

Grampleti i statistikës ekzekuton një raport statistikor. Kliko dy herë shprehjet për të paraqitur artikujt që përputhen.

Informacioni në vijim sigurohet për ju në këtë Gramplet:

- Individët
  - Numri i individëve
  - Meshkuj
  - Femra
  - Individ me gjini të panjohur
  - Individ me emra jo të plotë
  - Individ që ju mungojnë datat e lindjes
  - Individ që kanë ndërprerë lidhjet
- Informacione për familjen
  - Numri i familjeve
  - Emra unik
- Media objekte
  - Individ me media objekte
  - Numri total i referencave të media objekteve
  - Numri i media objekteve unike
  - Madhësia totale e media objekteve
  - Media objekte që mungojnë

Si me të gjithë Grampletet, nëse klikoni në butonin e anës së majtë e ndani dritaren, dhe nëse shtoni persona në pemën tuaj familjare, do të shihni grumbullin e individëve duke ndryshuar në mënyrë dinamike.

## Grampleti i prejardhjes

![[_media/Pedigree-detached-gramplet-40.png|Figure: Grampleti i prejardhjes]]

Grapleti i prejardhjes shfaq një pamje të ngjedhur të paraardhësve të personit aktiv. Ai parazgjedh për t'u kthyer 100 gjenerata mbrapa. Emrat mund të klikohen për të ndryshuar personin aktiv, të klikohen dy herë (apo të klikohen me të djahttën) për të redaktuar personin. Ky Gramplet, në fund të grampletit, gjithashtu shfaq numrin e njerëzve në një gjeneratë. Kliko dy herë numrin e Gjeneratës për të parë individët që përputhen.

Në versionin e rradhës së Gramps, mund të shihni datat e lindjes dhe të vdekjes.

## Gramplet Python

Grampleti Python paraqet një Guackë Python për të spjeguar shprehje python.

Mund të shtypni shumë shprehje Python (në vijë të vetme).

Veç kësaj, ambienti u popullua me disa ndryshore të dobishme, përfshirë **vetëveten** (këtë gramplet Python), **Datën**, **uigjendjen** dhe **dbgjendjen**.

Vini re, emri **Datë** do të përkthehet në gjuhën tuaj, nëse ka përkthim.

E hyra **Datë** është një ndërtues i objektit të datës, dhe mund të përdoret për aritmetikë të datës. Për shembull, mund t'ju interesojë një pyetje si kjo:

Cila datë ishte para 56 viteve nga kjo datë:

`> Data(2007, 12, 31) - 56`  
`1951-12-31`

Sa vjeç ishte dikush më 3 Shtator 1955, i cili kishte lindur më 7 Qershor, 1922:

`> Data(1955, 9, 3) - Data(1922, 5, 7)`  
`(33, 3, 27)`

(Rreth 33 vitsh, 3 muaj, dhe 27 ditë). Kur janë bërë 21 vjeçarë?

`> Data(1922, 5, 7) + 21`  
`1943-05-07`

Gjithashtu mund të shtoni vite, muaj dhe ditë:

`> Data(1980) + (0, 0, 25)`  
`1980-01-26`

Gjithashtu mund të përdorni formatet e njejta siç i përdorni në të hyrat e të dhënave:

`> Data("15 Jan, 1962")`  
`1962-15-01`  
`> Data("15 Jan, 1962")`  
`1962-15-01`  
`> Data("1962-15-01")`  
`1962-15-01`

Ka dy mënyra për të përdorur kalendare të ndryshëm:

`> Data("15 Jan, 1532 (Julian)")`  
`1532-15-01 (Julian)`  
`> Data(1671, 12, 31, kalendar="julian")`  
`1671-12-31`

dhe një metodë për të kthyer një datë në një kalendar tjetër, i cili kthen një objekt të ri të datës:

`> Data(1703, 6, 1).në_kalendar("hebrej")`  
`5463-10-17 (Hebrej)`

## Grampleti i risive

![[_media/Newsgadget.png|Fig. 4.9 Grampleti i risive]]

Grampleti i të rejave lexon faqen wiki [të risive](wiki:Main_Page).

Për shkak se grampleti i risive merr informacionin e tij nga Gramps wiki (at <http://gramps-project.org>) ju duhet të keni lidhje interneti për këtë punim. Nëse nuk keni një lidhje interneti, atëherë grampleti i Risive nuk do të tregojë ndonjë risi.

Kur keni lidhje interneti, grampleti Risi do t'ju shfaq të rejat e fundit rreth Gramps.

## Grampleti i ditarit sesioneve

![[_media/SessionLog-detached-gramplet-40.png|Fig. 6.00 Grampleti i ditarit sesioneve]]

Ditari i sesionit ndiek aktivitetet në këtë sesion.

Sipas parazgjedhje, shfaq secilën të hyrë vetëm një herë. Nëse ndryshoni disa informacione mbi personin **a** dhe personin **b** , të dyja përzgjedhjet do të vendosen në listë në Ditar.

Do të merrni këtë lloj liste:

- E përzgjedhur:personi a
- E përzgjedhur:personi b

Kliko një emër pët të ndryshuar personin aktiv. Kjo është shumë praktik sepse shum shpejtë mund të ndryshoni personin aktiv nga lista.

Duke klikuar dy herë mbi një emër do të paraqeitet faqja për atë person. Veç kësaj, nëse doni të redaktoni një person, por nuk doni të ndryshoni personin aktiv, mund të klikoni mbi emrin e personit.

Ndrysho këtë mënyrë duke redaktuar këtë sesion në ~/.gramps/gramplets.ini.

## Gramplet Kalendar

![[_media/Calendar-detached-gramplet-40.png|Fig 6.01 Kalendar]]

Grampleti kalendar shfaq një kalendar mujor, më ngjarje aktuale të shënuara të personit aktiv. (me numra të zeza).

Data e sotme theksohet.

Me butonat dhe në skajin e sipërm majtas (muaji), mund të ndryshoni në muajin e mëparshëm dhe atë të ardhshëm.

Me butonat dhe në skajin e sipërm djathtas (viti), mund të ndryshoni në vitin e mëparshëm dhe të ardhshëm.

Kliko një ditë për të ekzekutuar Raportin e shpejtë .

Dritarja ju shfaq **Ngjarjet e** ditës së përzgjedhur: Ngjarjet në po këtë datë dhe ngjarjet Tjera në këtë Muaj/ditë në history, si dhe ngjarje Tjera në atë vit.

Informacioni paraqitet në një tabelë që shfaq:

- Datën
- Tipin
- Vendin
- Referencën

Gjithashtu mund të zvarritni një datë në fushën e datave të [Grampletit Mosha në Data](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Age_on_Date_Gramplet) për të futur atë datëe.

## Grampleti Mosha me Datë

Ky Gramplet ju jep mundësinë e futjes së një të dhëne në një fushë hyrje. Nëse klikoni Grampleti do të llogaritë moshat për secilin në Pemën tuaj familjare për atë Datë. Data duhet të futet në një format që është i pranueshëm për Gramps.

Pastaj mund të klasifikoni sipas shtyllës së moshës, dhe të klikoni dy herë rreshtin për të shikuar apo për të redaktuar.

## Grampleti i familjarëve

![[_media/Relatives-detached-gramplet-40.png|Fig 6.02 Grampleti i familjarëve]]

Ky Gramplet shfaq të gjithë familjarët e personit aktiv. Përdorimi i caktuar i tij është si një ndihmë për navigim, një mënyrë alternative për të lëvizur përmes të dhënave tuaja Gramps. Nëse largoni grampletin, dhe e vendosni atë pranë Gramps, do t'ju mundësojë ta përdorni atë për të ndryshuar lehtë përmbajtjen aktuale të "pamjes së personit" .

Nëse vazhdoni të punoni në pamjen e prejardhjes, personi aktiv është personi i parë nga e majta. Duke klikuar një emër në grampletin e familjarëve, lehtë mund të ndryshoni personin aktiv, dhe gjithë pamja e personit do të përditësohet në dritaren tjetër. Meqënëse grampleti i failjarëve shfaq të gjithë bashkëshortët, të gjithë fëmijët dhe të gjithë prindërit, kjo ofron një mënyrë alternative të navigimit të të dhënave tuaja.

Merat në këtë gramplet gjithashtu ju mundësojnë të thirrni menjëherë redaktuesin e personit, duke klikuar me të djethtën mbi ndonjërin nga emrat.

[Category:Sq:Documentation](wiki:Category:Sq:Documentation)
