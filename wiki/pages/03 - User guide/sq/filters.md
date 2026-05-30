---
title: Sq:Gramps 6.0 Wiki Manual - Filters
categories:
- Sq:Documentation
managed: false
source: wiki-scrape
wiki_revid: 111488
wiki_fetched_at: '2026-05-30T20:49:20Z'
lang: sq
---

Kjo pjesë e shtuar vë në litë gjithë rregullta e filtrit, aktualisht të përcaktuara në Gramps. Secila prej këtyre rregullave është në dipozicion për përdorim kur krijoni filtra të përshtaur, shih *vegla-util-cfe* . Rregullat rradhiten sipas kategorisë të tyre.

## Redaktues i filtrit të zakonshëm

![[_media/Define-filter-dialog-custom-filters-example-41.png|Fig.3.x Përcakto filtër]] Redaktuesi i filtrit të përshtatur ndërton filtra të përshtatur të cilat mund të përdoren për të përzgjedhur njerëz që janë të përfshirë në raporte, eksportime dhe vegla dhe shërbime tjera. Kjo në të vërtetë është një vegël shumë e fuqishme në analizat gjeneligjike.

Kur e e lëshoni atë, paraqitet dialogu e cila vë në listë të gjitha filtrat (nëse ka ndonjë) e përcaktuara më parë nga ju. Kliko butonin për të përcaktuar një filtër të ri. Sapo të keni projektuar filtrat tuaja, mund t'i redaktoni, të testoni dhe t'i hiqni filtrat e përzgjedhur duke përdorur butonat , , dhe . Të gjitha filtrat e afishuar në listë, do të ruhen automatikisht së bashku me bazën tuaj të të dhënave dhe do të jenë të mundshme me sesionet vijuese të Gramps.

Nëse klikoni butonin do të thirrni dialogun vijues :

Shtyp emrin e filtrit tuaj të ri në fushën e .

Futni ndonjë koment që do t'ju ndihmojë të identifikoni këtë filtër në të ardhmen në fushën e . Shto sa më shumë rregulla në nëse do të doni që filtri juaj të përdorë butonin . Nëse filtri ka më shumë se një rregull, përzgjedh njërin nga . Kjo ju mundëson të zgjedhni nëse duhet të zbatohen të gjitha rregullat, vetëm një rregull apo saktësisht një rregull duhet të zbatohet , që filtri të nxjerrë një përputhje. Nëse filtri juaj ka vetëm një rregull, kjo përzgjedhje nuk ka efekt.

Kontrrollo për të kthyer rregullin e filtrit. Për shembull, kthimi i rregullit "ka një paraardhës të përbashkët me I1" do të përputhet me gjithkë që nuk ka një paraardhës të përbashkët me atë person).

Duke klikuar butonin thirret dialogu vijues :

![[_media/cfe-ar.png|Fig.3.x Shto rregull]]

Pjesa në anën e majtë afishon rregulla të mundshme të filtrit të rregulluara sipas kategorive në një pemë të zgjeruar. Për referencë të hollësishme të rregullave të filtrit, shih *append-filtref* . Kliko mbi rreshtat për të mbështjellur/shpalosur kategorinë e duhur. Përzgjedh rregullin nga pema duke klikuar mbi emrin e saj. Ana e djathtë afishon emrin, përshkrimin dhe vlerat për rregullin aktualisht të përzgjedhur. Meqë jeni të kënaqur me përzgjedhjen e rregullës suaj dhe vlerat e saj, kliko për të shtuar këtë rregull në listën e rregullave të filtrti të redaktuar aktualisht. Duke klikuar do të ndërprehet shtimi i rregullës në filtër.

## Filtra të përgjithshëm

Kjo kategori përfshin rregullat vijuese më të përgjithshme:

- Ka regjistrim të plotë

Ky rregull përputh të gjith njerëzit regjistrimet e të cilëve shënohen si të plota. Aktualisht, tërësia e informacioneve personale shënohet me dorë, në dialogun .

- Njerëz me emra jo të plotë

Ky rregull përputh të gjith njerëzit me emër të dhënë apo me mbiemër që mungon.

- Është person i shënuar

Ky rregull përputh të gjith njerëzit që janë në listën e shënimeve.

- Ka tekst që përputhet me nënvargun e

Ky rregull përputh gjith njerëzit regjistrimet e të cilëve përmbajnë nënvarg të veçantë. Hulumtohen të gjitha regjistrimet tekstuale. Sipas zgjedhjes suaj, hulumtimi mund të bëhet të njohë shkronja të mëdhaja ose të bëjë përputhje të shprehjeve të zakonshme.

- Gjithkush

Kjo rregull përputh cilindo person në bazën e të dhënave. Si i tillë, vet ai nuk është shumë i dobishëm, veç për qëllime testimesh. Sidoqoftë, mundtë jetë e dobishme në kombinime me rregulla tjerait may be useful in combinations with other rules.

- Njerëz që mund të jenë gjallë

Ky rregull përputh të gjith njerëzit regjistrimet e të cilëve nuk tregojnë vdekjen e tyre dhe të cilët nuk janë shumë të vjetër, gjykuar sipas të dhënave të mundshme të lindjes dhe datës së sotme.

- Ka një emër

Ky rregull përputh cilindo person qmri i të cilit përputhet me vlerën e caktuar, plotësisht apo pjesërisht. Për shembull, Marta Ericsdotter do të përputhet sipas rregullit duke përdorur vlerën "eric" për mbiemrin.

Vlera të ndara mund të përdoren për emrin e Dhënë, Mbemrin, Parashtesën dhe Titullin. Rregulli kthen përputhjen nëse, dhe vetëm nëse të gjith vlerat jo të zbrazëta (pjesërisht) përputhen nga emri i personit. Për të përdorur një vlerë, vlerat tjera leni të zbrazëta.

- Ka Id

Ky rregull përputh cilindo person me një Gramps ID të veçantë. Rregulli kthen përputhjen vetëm nëse ID përputhet me saktësi.

Mund të futni ID në fushën ku hyn teksti, ose përzgjedh një person nga lista duke klikuar butonin . Në rastin e mëvonshëm, ID do të shfaqet në fushën e tekstit pasi të bëhet përzgjedhja.

- Është person i parazgjedhur

Ky rregull përputh personin e parazgjedhur (amë).

- Njerëz të shënuar si personal

Ky rreguëë përputh njerëz regjistrimet e të cilëve shënohen si personale.

- Është femër

Ky rregull përputh cilindo person femër.

- Njerëz që kanë imazhe

Ky regull përputh njerëz me imazhe në galeritë e tyre.

- Njerëz pa data të lindjes

Ky rregull përputh njerëz që ju mungojnë datat e lindjes.

- Është mashkull

Ky rregll përputh cilindo person mashkull.

## Filtra të ngjarjeve

Kjo kategori përfshijnë rregullat në vijim që përputhin njerëz bazuar në ngjarjet e tyre të regjistruara:

- Ka lindjen: Ky rregull përputh njerëz ngjarje e lindjevee të të cilëve përputhen me vlera të caktuara për Datën, Vendin dhe Përshkrimin. Rregulli kthen një përputhje edhe nëse ngjarja e lindjes së personit përputhet me vlerën pjesërisht. Rregullat e përputhjes janë të ndjeshme ndaj kapitaleve. Për shembull, ndonjë i lindur në Suedi do të përputhet sipas rregullit duke përdorur "sw" për Vendin.

Rregulli kthen një përputhje nëse dhe veëtm nëse, të gjitha vlerat jo të zbrazëta përputhen (pjesërisht) sipas lindjes së personit. Për të përdorur vetëm një vlerë, vlerat tjera lëri të zbrazëta.

- Ka vdekjen: Ky rregull përputh njerëz ngjarja e vdekjes e të cilëve përputhet me vlerat e caktuara për Datën, Vendin dhe Përshkrimin. Rregulli kthen një përputhje edhe nëse ngjarja e vdekjes së personit pjesërisht përputhet me vlerat. Rregullat e përputhjes janë të ndjeshme ndaj kapitaleve. Për shembull, çdonjëri që ka vdekur në Suedi do të përputhet sipas rregullit duke përdorur vlerën "sw" për Vendin.

Rregulli kthen një përputhje vetëm dhe nëse vetëm të gjitha vlerat jo të zbrazëta përputhen (pjesërisht) sipas vdekejes së personit. Për të përdorur vetëm një vlerë, vlerat tjera lëri të zbrazëta.

- Ka burim të: Ky rregull përputh njerëz regjistrimet e të cilëve i referohen burimit të caktuar.

<!-- -->

- Ka ngjarjen personale: Ky rregull përputh njerëz që kanë një ngjarje personale që përputhet me vlerat e caktuara për llojin e Ngjarjes, Datën, Vendin dhe Përshkrimin. Rregulli kthen një përputhje edhe nëse ngjarja e personit përputhet pjesërisht me vlerat. Rregullat e përputhjes janë të ndjeshme ndaj kapitaleve. Për shembull, cilido që ka diplomuar në Suedi, do të përputhet sipas rregullit duke përdorur ngjarjen e Diplomimit dhe vlerën "sw" për Vendin.

Ngjarjet personale duhet të përzgjedhen nga menyja me tërheqje të poshtë. Rregulli kthen një përputhje nëse dhe vetëm nëse të gjitha vlerat e zbrazëta përputhen (pjesërisht) sipas ngjarjes personale. Për të përdorur vetëm një vlerë, vlerat tjera lëri të zbrazëta.

- Ka ngjarjen e familjes: Ky rregull përputh njerëz që kanë një ngjarje familjare që pëputhet me vlerat e caktuara për llojin e Ngjarjes, Datën, Vendin dhe Përshkrimin. Rregulli kthen një përputhje edhe nëse ngjarja e personit përputhet pjesërisht me vlerën. Rregullat për përputhje janë të ndjeshme ndaj kapitaleve. Për shembull, çdonjëri që është martuar në Suedi. do të përputhet sipas rregulit duke përdorur ngjarjen e Martesës dhe vlerën "sw" për Vendin.

Ngjarjet familjare duhet të përzgjedhen nga një meny me tërheqëje te poshtë. Rregulli kthen një përputhje nëse dhe vetëm nëse të gjitha vlerat jo të zbrazëta përputhen (pjesërisht) sipas ngjarjes personale. Për ta përdorur vetëm një vlerë, vlerat tjera lëri të zbrazëta.

- Dëshmitar: Ky rregull përputh njerëz të cilët janë të pranishëm si dëshmitarë në ngjarje. Nëse përcaktohet lloji i ngjarjes personale apo familjare, do të kërkohen vetëm ngjarjet e këtij tipi.

<!-- -->

- Njerëz me ngjarje jo të plota: Ky rregull përputh datën apo vendin që mungon në ndonjërën ngjarje personale.

<!-- -->

- Familje me ngjarje jo të plota: Ky rregull përputh njerëz që iu mungon data apo vendi në ndonjërën prej ngjarjeve familjare të tyre.

## Filtrat e familjeve

Kjo kategori përfshin rregullat në vijim që përputhin njerëz bazuar në marrëdhëniet e tyre familjare:

- Njerëz me fëmijë

Ky rregull përputh njerëz me fëmijë.

- Njerëz me regjistrime të shumëfishta martese

Ky rregull përputh njerëz me më shumë se një bashkëshort.

- Njerëz pa regjistrim martese

Ky rregull përputh njerëz pa bashkëshort.

- Njerëz që janë të birësuar

Ky rregull përputh njerëz që janë të birësuar.

- Ka marrëdhënie

Ky rregull përputhe njerëz me një marrëdhënie të veçantë. Marrëdhënia duhet të përputhet ,e tipin që përzgjedhet nga menyja. Sipas zgjedhjes suaj, mund të përcaktohet numri i marrëdhënieve dhe numri i fëmijëve.

Rregulli kthen një përputhje nëse dhe vetëm nëse të gjitha vlerat jo të zbrazëta përputhen (pjesërisht) sipas marrëdhënies së personit. Për të përdorur vetëm një vlerë, vlerat tjera lëri të zbrazëta.

- Është bashkëshort nga përputhja që ka bërë filtrit

Ky rregull përputh njerëz të martuar me dikë që përputhet nga filtri i përcatuar. Emri i filtrit të përcaktuar duhet të përzgjedhet nga menyja.

- Është fëmijë nga pëputhja që ka bërë filtri

Ky rregull përputh njerëz nga i cili prind përputhet nga filtri i përcaktuar. Emri i filtrit të përcaktuar duhet të përzgjedhet nga menyja.

- Është prind nga përputhja që ka bërë filtri

Ky rregull përputh njerëz fëmija i të cilit përputhet nga filtri i përcaktuar. Emri i filtrit të përcaktuar duhet të përzgjedhet nga menyja.

- Është motër/vëlla nga përputhja që ka bërë filtri

Ky rregull përputh njerëz, motrat/vëllezërit e të cilëve përputhen nga filtri i përcaktuar. Emri i filtrit të përcaktuar duet të përzgjedhet nga menyja.

## Filtra të paraardhësve

Kjo kategori përfshin rregullat në vijim për përputhjen e njerëzve, bazuar në marrëdhëniet e paraaedhësve me njerëzit e tjerë:

- Është paraardhës i

Ky rregull përputh njerëz wë janë paraardhës të personit të caktuar. Opsioni përfsfhirës përcakton nëse personi i caktuar duhet të merret parasysh si paraardhësi i tij/saj (i dobishëm për krijimin e raporteve).

Mund të futni ID në një fushë ku hyn teksti, ose të përzgjedhni një person nga lista duke klikuar butonin . Në rastin e dytë, ID do të paraqitet në fushën e tekstit pasi të bëhet përzgjedhja.

- Është paraardhës i një personi së paku N gjenerata larg

Ky rregull përputh njerëz të cilët janë paraardhës të personit të caktuar dhe janë së paku N gjenerata larg nga ai person në fisin e tyre. Për shembull, duke përdorur këtë rregull me vlerën 2 si numër i gjeneratave, do të përputhë gjyshër, stërgjyshër, etj., por jo prindërit e personit të caktuar.

- Është paraardhës i personit jo më shumë se N gjenerata larg

Ky rregull përputh njerëz të cilët janë paraadhës të personit të caktuar dhe janë jo më shumë se N gjenerata larg nga ai person në fisin e tyre. Për shembull, duke përdorur këtë rregull me vlerën 2 si numër i gjeneratave, do të përputh prindër dhe gjyshër, por jo stërgjyshër, etj., të personit të caktuar.

- Ka paraardhës të përbashkët me

Ky rregull përputh njerëz të cilët kanë paraardhës të përbashkët me personin e caktuar.

- Ka paraardhës të përbashkët me përputhjen që ka bërë filtri

Ky rregull përputh njerëz të cilët kanë paraardhës të përbashkët me dikë që përputhet nga filtri i caktuar. Emri i filtrit të caktuar duhet të përzgjedhet nga menyja.

- Është paraardhës i përputhjes që ka bërë filtri

Ky rregull përputh njerëz të cilët janë paraardhës të dikuj që përputhet nga filtri i caktuar. Emri i filtrit të caktuar duhet të përzgjedhet nga menyja.

## Filtra të pasardhësve

Kjo kategori përfshin rregullat në vijim për përputhjen e njerëzve, bazuar në marrëdhëniet e pasardhësve me njerëzit e tjerë:

- Është pasardhës i

Ky rregull përputh njerëz që janë pasardhës të personit të caktuar. Opsioni përfsfhirës përcakton nëse personi i caktuar duhet të merret parasysh si pasardhësi i tij/saj (i dobishëm për krijimin e raporteve).

Mund të futni ID në një fushë ku hyn teksti, ose të përzgjedhni një person nga lista duke klikuar butonin . Në rastin e dytë, ID do të paraqitet në fushën e tekstit pasi u bë përzgjedhja.

- Është pasardhës i një personi së paku N gjenerata larg

Ky rregull përputh njerëz të cilët janë pasardhës të personit të caktuar dhe janë së paku N gjenerata larg nga ai person në fisin e tyre. Për shembull, duke përdorur këtë rregull me vlerën 2 si numër i gjeneratave, do të përputhë nipër, stërnipër, etj., por jo por jo fëmijët e personit të caktuar.

- Është pasardhës i personit jo më shumë se N gjenerata larg

Ky rregull përputh njerëz të cilët janë pasardhës të personit të caktuar dhe janë jo më shumë se N gjenerata larg nga ai person në fisin e tyre. Për shembull, duke përdorur këtë rregull me vlerën 2 si numër i gjeneratave, do të përputh fëmijë dhe nipër, por jo stërnipër, etj., të personit të caktuar.

- Është pasardhës i përputhjes që ka bërë filtri

Ky rregull përputh njerëz të cilët janë pasardhës me dikë që përputhet nga filtri i caktuar. Emri i filtrit të caktuar duhet të përzgjedhet nga menyja.

- Është anëtarë pasardhës i familjes së

Ky rregull jo vetëm që përputh njerëz të cilët janë pasardhës të personit të caktuar, por edhe bashkëshortët e atyre pasardhësve.

## Filtra të marrëdhënieve

Kjo kategori përfshin rregullat në vijim që përputhin njerëz bazuar në marrëdhënien e tyre reciproke:

- Shteg i marrëdhënies mes dy njerëzve

Ky rregull përputhe të gjith paraardhësit e të dy njerëzve, prapa nga paraardhësit e tyre të përbashkët (nëse ekzistojnë). Kjo krijon "shtegun e marrëdhënies" mes këtyre dy njerëzve, përmes paraardhësve të tyre të përbashkët.

Mund të shtoni ID e secilit person në fushën përkatëse të tekstit, ose të përzgjedhni njerëz nga lista duke klikuar butonat e tyre . Në rastin e dytë, ID do të paraqitet në fushën e tekstit pasi të bëhet përzgjedhja.

## Filtra të ndryshëm

Kjo kategori përfshin rregullat në vijim të cilët zakonisht nuk përshtaten në asnjërën kategori të mësipërme:

- Ka atribut peronal

Ky rregull përputh njerëz të cilët kanë atribut personal të vlerës së caktuar. Emri i aributit personal të caktuar. Atributi personal i caktuar duhet të përzgjedhet nga menyja. Vlera e caktuar duhet të shtypet në fushën ku hyn teksti.

- Ka atributin familjar

Ky rregull përputh njerëz të cilët kanë atributin familjar të vlerës së caktuar. Atributi i caktuar i familjes duhet të përzgjedhet nga menyja. Vlera e caktuar duhet të shtypet në fushën ku hyn teksti.

- Përputh filtrin e emëruar

Ky rregul përputh njerëz të cilët përputhen nga filtri i caktuar. Emri i filtrit të caktuar duhet të përzgjedhet nga menyja.

[Category:Sq:Documentation](wiki:Category:Sq:Documentation)
