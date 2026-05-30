---
title: Sq:Gramps 6.0 Wiki Manual - FAQ
categories:
- Sq:Documentation
- Stub
managed: false
source: wiki-scrape
wiki_revid: 128629
wiki_fetched_at: '2026-05-30T20:49:16Z'
lang: sq
---

Kjo pjesë e shtuar përmban listën e pyetjeve që shpesh dalin në diskutimet dhe forumet e listës postare. Kjo listë, në asnjë mënyrë nuk është e plotë. Nëse do të donit të shtoni pyetje/përgjigje në këtë listë, ju lutem na dërgoni sugjerimet tuaja në gramps-devel@lists.sourceforge.net

Also consider having a look at:

- [Si...](wiki::Category:How_do_I...)
- [Studimet e Gramps](wiki::Category:Tutorials)

## Të përgjithshme

- Ç'është Gramps?

Gramps është Sistem i programit për Hulimtim Gejenalogjik dhe Menaxhim. Me fjalë të tjera, është program personal gjenealogjik i cili ju lejon të ruani në kujtesë, të redaktoni dhe të hulumtoni të dhëna gjenealogjike duke përdorur fuqitë e kompjuterit tuaj, shih [Rreth Gramps](wiki:Gramps:About).

- Ku mund ta gjej dhe sa kushton?

Gramps mund të [instalohet](wiki:Installation) pa pagesë. Gramps është një projekt Burimor i Hapur i mbrojtur nga Licenca e Përgjithshme Publike GNU . Keni qasje të plotë në kodin burimorë dhe ju mundësohet lirshëm të shpërndani programin dhe kodin burimorë.

- A ekziston Gramps në gjuhet tjera?

Po, për momentin Gramps është përkthyer në 23 gjuhë, shih [Përkthimet e Gramps](wiki:Gramps_translations).

- Si të mbaj rezerva?

Përdor verzionin e fundit të Gramps! Nga 2.2.5 e tutje, a një shërbim për bërjen automatike të rezervës.

Është shumë e rendësishme për të mbajtur bërjen e rezervës së të dhënave tuaja, dhe për t'i mbajtur ato në vend të sigurtë. Gramps ka një format të depërtueshëm të skedarit i cili është i vogël, dhe e lexueshme për njerëzit, e paraqitur nga `.gramps`. Nëse ju është mundësuar kjo në preferencat (Në `menyja Redakto->Preferenca->Të përgjithshme`), Gramps do të mbajë në dalje një rezervë të bazës së të dhënave tuaja. Kohë pas kohe mund ta kopjni këtë skedar për bërje të rezervës në një vendodhje për ruajtje. (sh një usb-shkop). \[Shënim: Skedarët e .gramps janë të ngjeshur. Duke klikuar ato do të hapet Gramps. Për të parë XML përzgjedh ato dhe hapi përmes shërbimit për çngjeshje (si ark, gunzip), pas së cilës mund të nxjerrni skedain XML i cili është i lexueshëm për njerëzit, shih [hollësirat](wiki:Generate_XML#How_do_I_uncompress_the_file?).

**Mos mbaj rezerva në GEDCOM**. Jo të gjitha informacionet që i ruan Gramps mund të shkruhen në GEDCOM. Kështu që, një operacion eksporti/importi Gramps --\> GEDCOM --\> Gramps, do të thotë që i **humbni** të dhënat. Përdor formatin e skedarit `.gramps` për bërjen erezervave!

**Mos mbaj rezervat në formatin GRDB**. GRDB është bazë e të dhënave, e cila mund të varet nga kompjuteri (lexo, nuk punon në PC tjetër). Një dëmtim i vogël i skedarit GRDB mund gjithashtu të mos rregullohet. Përdor formatin e skedarit `.gramps` për bërjen e rezervave!

- A mbështet Gramps fonte Unicode? A mbështet veçanërisht fonte Unicode jo-Roman?

Po. Gramps funksionon së brendshmi me Unicode (UTF-8), pra të gjitha aëfabetet mund të përdoren në të gjitha fushat e të hyrave. Të gjitha raportet e mbështesën këtë plotësisht, edhe pse për PDF/PS duhet të punoni me gnome-print apo openoffice.

## Instalimi

- Çka është e nevojshme për të instaluar Gramps në Linux, Solaris, apo FreeBSD?

Gramps është një aplikim [GTK](http://en.wikipedia.org/wiki/Gtk). Gramps duhet të ketë të instaluar në sistem bibliotekat [pygtk](http://en.wikipedia.org/wiki/Pygtk). Përderisa të jenë të instaluara këto biblioteka, Gramps duhet të funksionojë. Do të funksionojë nën tryezën e GNOME, të KDE apo ndonjë tryeze tjetër. Nëse lidhjet e GNOME për Python janë të instalura në sistem, Gramps do të ketë funksionim plotësues. Projekti i Gramps çaraqet versionin 2.8 apo më të lartë nga GTK.

- A funksionon me Windows?

[Linux Genealogy CD](wiki:Linux_Genealogy_CD) mund të funksionojë si lëvizëse CD prej të cilës filoni direkt. Pastaj mund ta ekzekutoni Linux dhe Gramps pa CD, edhe nëse kompjuteri juaj është i gjith me Windows.

Një [Windows installer](wiki:Windows_installer) **eksperimental** është në dispozicion, mirëpo ne nuk kemi gjithë fuqinë për t'i ofruar një mbështetje Windows-it. Mirëpo, një [listë postare e windows-it](wiki:Contact) është e mundshme dhe ne mundohemi që sa më mirë të zgjedhm problemet lidhur me windows-in.

- A funksionon me Mac?

Projekti Fink project ka bartur disa versione të vjetra të Gramps në OS X (tm). Bartja Mac OS X nuk mbështetet direkt nga projekti i Gramps, së pari sepse asnjëri nga zhvilluesit e Gramps nuk kanë qasje në Mac OS X dhe sepse OS X nuk ësht Softuer i Lirë.

Ky version aktual i Gramps (2.2.x) nuk duket se mund të bartet nga projekti Fink. Ju lutem kontaktoni projektin Fink për më shumë informacione. Megjithatë, disa përdorues kanë [pasur sukses](wiki:Mac_OS_X) kur kanë instaluar 2.2.x në Mac OSX ose gjatë ekzekutimit në gjendjen e thjeshtë, ose duke ekzekutuar në X11 duke përdorur disa paketa të fink.

- Cilat janë kushtet specifike minimale për të ekzekutuar Gramps?

Ne do t'ju rekomandojmë së paku një video afishim 800x600. Për Gramps 2.0, janë reduktuar nevojat për memorie, dhe Gramps mund me efekt mund të ekzekutojë në një sistem 256MB, duke mbajtur mjaft njerëz. Një sistem me 512MB duhet të ketë mundësi të mabjë rreth 200,000 njerëz. Kërkesat e haësirës së diskut për bazat e të dhënave janë mjaft të mëshaja, me një bazë të zakonshme të të dhënave me madhësi prej disa mega bajtësh. Për 120.000 njerëz, ju duhet të keni 530Mb për bazën e të dhënave. Pikturat ruhen në kujtesë në disk veçmas, ashtu që është o nevojshëm një disk i ngurtë i madh.

## Preferencat

- A mund të ndryshoj datat në raporte në 'ditë muaj vit'

Po, ndrysho preferncat e datës në Gramps ("Redakto-\>Preferenca") në formatin që ju kërkohet (sh VVVV-MM-DD apo ditë muaj vit), dhe bëj raportin. Do të përdoren preferencat tuaja të përgjithshme për datat.

## Bashkëpunim-Depërtueshmëri

- A përputhet Gramps me softueret tjerë gjenealogjik?

Gramps bën çdo përpjekje për të qenë i përputhshëm me [GEDCOM](wiki:GEDCOM), standard i përgjithshëm i regjistimeve të informacioneve gjenealogjike. Kemi filtra importues dhe eksportues që i mundësojnë Gramps të lexojë dhe të shkruajë skedarë GEDCOM.

Është me rëndësi të kuptohet që standardi i GEDCOM është dobët i krijuar -- në të vërtetë çdo softuer gjenealogjik ka "shpërndarje" në GEDCOM. Siç mësojmë për shpërndarjen e re, filtrat importues/eksportues mund të krijohen shumë shpejtë. Megjisthatër, të kuptojmë për shpërndarje jo të njohura, kërkon [user feedback](wiki:Contact). Ju lutem na informoni lirshëm për ndonjë shpërndarje të GEDCOM që nuk mbështetet nga Gramps, dhe do të bëjmë të pamundurën për t'i dhënë asaj mbështetje!

- A mund Gramps të lexojë skedarë nga programet tjera gjenealogjike?

Shij me lartë.

- A mund Gramps të shkruajë skedarë të lexueshme nga programet tjera gjenealogjike?

Shih më lartë.

- Cilat standarde mbështeten nga Gramps?

Gjëja e mirë për standardet është se asnjëherë nuk janë me sasi të pakta. Gramps testohet për mbështetje shpërndarjet vijuese të GEDCOM: GEDCOM5.5, Brother's Keeper, Family Origins, Family Tree Maker, Ftree, GeneWeb, Legacy, Personal Ancestral File, Pro-Gen, Reunion, dhe Visual Genealogie.

- Si të importoj të dhëna nga një program tjetër gjenealogjik në Gramps?

Mënyra më e mirë është krijimi i një peme të re familjare, dhe të pëzgjedhni ospionin për importim në menynë e skedarit. Këtu përzgjedhni GEDCOM që e keni nxjerrë me program tjetër dhe ta importoni atë.

- A mund ta instaloj Gramps në një Veb shfletues të Linux dhe ta përdor atë përmes një veb shfletuesi? Kjo do të mundësojë një qasje të njerëzve nëpër botë të lidhen me mua dhe përditësimin e të dhënave.

Edhe pse Gramps mund të nxjerrë veb sajte, nuk siguron një ndërfae të veb-it e cila mundëson redaktim. Nëse kjo është e nevojshme, atëherë [GeneWeb](http://geneweb.org) ose [PhpGedView](http://phpgedview.sourceforge.net) janë programe që më shumë i përshtaten nevojave tuaja. Megjithatë, mund t'i bëni këto pyetje vetes tuaj:

1.  A dua në të vërtetë që familjarët e mi apo njerëz të tjerë të redaktojnë direkt të dhënat e mija gjenealogjike?
2.  A i besoj plotësisht, pa vërtetuar, cilësdo të dhënë që njerëzit mund ta fusin?
3.  A e kuptojnë njejtë këta njerë praktikën e mirë gjenealogjike si unë?

Një qasje më e mirë mund të jetë sigurimi i një veb forme të interfaqes që mundëson që të tjerët të fusin të dhëna që mandej ruhen për ekzaminimin tuaj. Pastaj mund të vendosni nëse duhet të futet informacioni në bazën tuaj të të dhënave.

Gjtihashtu mund të merrni parasysh efektete e kohës së mundshme të sajtit tuaj nëse nuk mund t'i siguroni vetes një shërbim të lartë për veb pritje.

## Raporte

- A mundet Gramps të printojë një pemë gjenealogjike për familjen time?

Po. Njerëz të ndryshëm kanë mendime të ndryshme se çka është pema gjenealogjike. Disa mendojnë se ajo është një grafik që fillon nga paraardhësi i largët dhe vë në listë të gjithë pasardhësit e tij/saj dhe familjet e tyre. Të tjerët mendojnë se duhet të jetë një grafik që fillon nga personi në të kaluarën, dhe vë në listë paraardhësit dhe familjet e tyre. Kurse të tjerët mendojnë se është një tabelë, raport teksti, etj.

Gramps mund të krijojë cilindo nga të përmendurat me lartë, dhe shumë grafiqe dhe raporte tjera të ndryshme. Gjithashtu, ndërtimi i prizës bën të mundshme që përdoruesit (ju) të krijojnë prizat e veta të cilat mund të jenë raporte të reja, grafiqe, apo vegla për hulumtim.

- Në çfarë formati mund t'i nxjerrë Gramps raportet e tij?

Raporte tekstuale janë të mundshme në formate HTML, PDF, ODT, LaTeX, dhe RTF. Raporte Grafikore (grafiqe dhe diagrame) janë të mundshme në formate PostScript, PDF, SVG, ODS, dhe GraphViz.

- Si mund ta ndryshoj gjuhën e përzgjedhur në raporte?

Raportet janë në gjuhën në të cilën është instalimi linux. Mund ta ndryshoni të duke instaluar paketa shtesë gjuhësore, shih [Howto:Change the language of reports](wiki:Howto:Change_the_language_of_reports).

- A përputhet Gramps me Internetin?

Gramps mund të ruajë në kujtesë veb adresa dhe të drejtojë shfletuesin tuaj drejt atyre. Mund të importojë të dhëna që keni shkarkuar nga Interneti. Mund të eksportojë të dhëna të cilat keni mundur t'i dërgoni përmes Internetit. Gramps ka njohuri për formatet standarde të skedarëve të përdorura në mënyrë të zgjeruar në Internet (sh. JPEG, PNG, dhe imazhe GIF, MP3, OGG, dhe skedarë zëri WAV, QuickTime, MPEG, dhe AVI skedarë filmash, etj). Përveç kësaj, ka shumë pak gjëra që programi gjenealogjik mund të bëjë me Internetin.

- A mund të krijoj raporte/filtra/çkadoqoftë të përshtatur?

Po. Ka disa nivele të përshtatjes. Njëri është krijimi dhe modifikimi i shablloneve të përdorura për raportet. Kjo ju mundëson të kontrrolloni fontet, ngjyrat dhe disa tabela të raporteve. Gjithashtu mund të përdorni komanda të Gramps në dialogjet e raporteve për të treguar se çfarë përmbajtjesh duhet të përdoren për një raport të caktuar. Si vazhdim i kësaj, keni mundësinë për të krijuar filtrat tuaja -- kjo është e dobishme kur përzgjedhni njerëz bazuar në kriteriume të vendosura nga ju. Mund t'i kombinoni këto filtra për të krijuar filtra të ri, dhe më të ndërlikuar. Përfundimish, keni një opsion për të krijuar prizat tuaja. Lëto mund të jenë raporte të reja, vegla kërkimi, filtra importues/eksportues, etj. Kjo kërkon njohuri për programim tëë Python.

- Pse karakteret jo-Latin afishohen në raporte PDF/PS?

Ky është një kufizim i fonteve të ndërtuara të formateve PS dhe PDF. Për të printuar tekst jo-Latin, përdor Printo... në menynë për përzgjedhje të formatit të dialogut të raportit. Kjo do të përdorë `gnome-print`, i cili mbështet krijimin e PS dhe PDF, si dhe pritnimin direkt. (Shënim: do të duhet të instaloni gnome-print veçmas, pasi që nuk kërkohet për Gramps).

Nëse keni vetëm teskt Latin, opsioni PDF do të formojë një PDF më të vogël, krahasuar me atë që e ka krijuar gnome-print, thjesht sepse nuk do të futet asnjë informacion për fontin.

- Do të doja të kontribuoja në Gramps duke shkruar raportin tim të preferuar. Si ta bëj atë?

Mënyra me e lehtë për të kontribuar në raporte, filtra, vegla, etj. është të kopjoni një raport, filtër apo vegël që ekziston të Gramps. Nëse mund të krijoni atë që doni duke modifikuar gjendjen që ekziston -- shkëlqyeshëm! Nëse mendimi juaj nuk përputhet me logjikën e asnjërës veëgl të Gramps që ekziston, do të duhet që të shkruani prozën tuaj nga fillimi. Ndihma është e mundshme në [Hyrjen e zhvilluesve](wiki:Portal:Developers), apo në [Listën postare të zhvilluesve](wiki:Contact): gramps-devel@lists.sourceforge.net.

Për ta testuar punën tuaj në zhvillim, mund ta ruani rizën tuaj nën direktoriumin HOME/.gramps/plugins dhe duhet të gjendet dhe të importohet në nisje. Priza e shkruar saktë do të regjistrohet vet në Gramps, do të krijojë artikuj të menysë, e kështu me rradhë.

Nëse jeni të kënaqur me prizën tuaj dhe do të donit të kontribuoni me kthimin e kodit në projektin e Gramps, do të jeni të mirëpritur nëse veproni ashtu duke na kontaktuar në gramps-devel@lists.sourceforge.net

## Baza e të dhënave - Formate të skedarit Gramps

- Cila është madhësia maksimale e bazës së të dhënave (bajt) të cilën Gramps mund ta mbajë?

Gramps nuk ka kufi të caktuar për madhësinë e një baze të të dhënave që mund ta mbajë. Me fillimin e botimit 2.0.0, Gramps nuk ngarkon më të dhëna në mermori, e cila mundëson që ajo të funksionojë me një bazë të të dhënave më të madhe se më parë. Në të vërtetë, ka kufi të vërtetë. Faktortë kryesorë për kufizime janë memoria e mundshme në sistem dhe madhësia e vendit të fshehtë që përdoret qasjen e bazës së të dhënave BSDDB. Me madhësitë e zakonshme të memorieve të kohëve të fundit, Gramps nuk duhet të ketë probleme për përdorimin e bazës së të dhënave me [dhjetë mijë njerëz](wiki:Gramps_Performance).

- Sa njerëz mund të mbajë baza e të dhënave e Gramps?

Shih më lartë. Përsëri, kjo varet nga ajo se sa memorie keni, shih [Gramps Performance](wiki:Gramps_Performance).

- Baza e të dhënave të mija është vërtetë e madhe. A ka ndonjë mënyrë për ngarkimin e të gjitha të dhënave në memorie?

Me fillimin e botimit 2.0.0, Gramps nuk ngarkon më të gjitha të dhënat në memorie, e cila mundëson që ajo të funksionojë me një bazë të të dhënave më të madhe ng a ajo më parë. Formati i skedarit që u përdor është `.grdb` që do të thotë baza e të dhënave gramps.

- A mund ta ekzekutoj Gramps nga baza e të dhënave në një ndarje NFS?

Po mundeni.

- Pse formati i bazës së të dhënave nuk është i depërtueshëm?

Çështja më e madhe me depërtueshmërinë e Gramps i përket 'transakcioneve'. Me Gramps 2.2, kemi shtuar mbështetjen për transakcionet atomike për të mbrojtur të dhënat. Me transkacionet atomike, ndryshime të shumta bëhen si një njësi e vetme . Ose do t'ia dalin të gjitha ndryshimet, ose nuk do t'ia dalë asnjë ndryshim. Asnjëherë nuk keni mbetur në një situatë me një grupë të pjesërishme të ndryshimeve. Një dobi dytësore e përdorimit të transakcioneve është që qasjet e bazës së të dhënave (lexon dhe shkruan) janë më të shpejta.

Problemi me transakcionet (së paku përdorimi i BSDDB) është që nuk lejon të gjitha bazat e të dhënave të ruhen në kujtesë në një skedar të vetëm. Shënimi në ditarë i skedarëve duhet të ndjekë gjërat. Këto skedarë të shënuar në ditar mbahën në direktoriumin DB të Ambientit. Na duhet një diretorium i veçantë për secilin skedar, përndryshe skedarët e ditarëve mund ta pengojnë njëri tjetrin.

Në 2.2, ne mbajmë skedarët e ditarëve nën direktoriumin ~/.gramps/<path> , duke krijuar një direktorium të veçantë për çdo bazë të të dhënave. Problemi është se skedarit tuaj GRDB i duhen skedarët e ditarit, të cilët janë në direktorium tjetër. Kopjimi i skedarit GRDB është vetëm kopjim i një pjese të bazës së të dhënave.

## Viruse dhe kërkesa

- Gjeta një virus dhe dua të më rregullohet tani! Çka të bëj?

Gjëja më e mirë që mund të bëni është të rregulloni virusin dhe ta dërgoni korigjuesin në gramps-devel@lists.sourceforge.net :-)

Nëse kjo nuk është e mundshme, duhet të [paraqit një raport për viruse](wiki:Using_the_bug_tracker)

Një raport i mirë do të përfshinte:

1.  Versionin e gramps që keni qenë duke e përdorur kur jeni ndeshur me virusin (e mundshme përmes artikullit ty menysë Ndihmë → Rreth).
2.  Gjuhën nën të cilën u ekzekutua grampsn (e mundshme me zbatimin e `echo $LANG` në fund).
3.  Simptomet që tregojnë se ky në të vërtetë është virus.
4.  Cilindo mesazh për Gjurmim, mesazhe për gabime, paralajmërime, etj, që u shfaqën në fund apo në një dritare të veçantë për gjurmim.

Shumica e problemeve mund të rregullohen shpejtë, nëse sigurohen mjaft informacione. Për t'u siguruar, ju lutem ndiqni raportet tuaja për viruse. Atëherë do të kemi mundësi t'ju kontaktojmë nëse do të na duhen më shumë informacione.

- Gramps duhet të jetë një .... lloj aplikacioni

Është e qartë Gramps plotësisht duhet të bëhet një aplikacion (client-server/web-based/PHP/weblog/Javascript/C++/distributed/KDE/Motif/Tcl/Win32/C#/You-name-it). Kur do të ndodhë kjo?

Mënyra më e sigurtë për të parë se çka po ndodh, është ta atë bëni vet. Që kur Gramps është burim i lirë/i hapur, askush s'ju mbron nga marrja e gjith kodit dhe vazhdimin e zhvillimit të tij në cilindo drejtim që të shihni se ju përshtatet. Për të vepruar kështu, mund të duhet të merrni parasysh që projektit tuaj të ri t'i jipni një tjetër emër për t'iu larguar ngaterrimeve me vazhdimin e zhvillimit të Gramps. Nëse do të donit që projekti i Gramps të sigurojë këshillë, mendim profesional, filtra, etj., me kënaqësi do të bashkëpunojmë me projektin tuaj të ri, për tç siguruar ospione për përputhje apo të importit/eksportit në fomratin e ri të projekti.

Nëse, do të donit që projekti Gramps të pranojë strategjinë tuaj, do t'ju duhet të bindni zhvilluesit e Gramps që strategjia juaj është në të mirën e Gramps dhe e mrrekulueshme për strategjinë aktuale për zhvillim.

[Category:Sq:Documentation](wiki:Category:Sq:Documentation)
