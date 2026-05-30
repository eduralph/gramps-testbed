---
title: Gramps 6.0 Wiki Manual - Getting started/tr
categories:
- Tr:Documentation
managed: false
source: wiki-scrape
wiki_revid: 112650
wiki_fetched_at: '2026-05-30T20:54:58Z'
lang: tr
---

{{#vardefine:chapter\|2}} {{#vardefine:figure\|0}}

Bu bölümde, temel bilgilerle başlayacağız. İlk olarak, Gramps'taki temel kavramları tanımlayacağız. Ardından, Gramps'ı nasıl başlatacağınızı ve ihtiyacınız olduğunda nasıl yardım alacağınızı göstereceğiz. \_\_FORCETOC\_\_

## Gramps'e Genel Bakış

Gramps, esnek ve güçlü bir soy ağacı aracı olarak tasarlanmış ücretsiz, açık kaynaklı bir programdır. Her bir veri parçasının birbiriyle nasıl ilişkili olduğunu not ederek ve bu ilişkileri sunarak soy araştırma verilerini toplamak için bir çerçevedir.

Gramps'ı genellikle herhangi bir şekilde kullanabilirsiniz. Verilerinizle çalışmanın veya verilerinizi kaydetmenin tek ve doğru bir yöntemi yoktur. Ancak, diğer araştırmacılar veya programlarla işbirliği yapmak isterseniz, bazı ortak yönergelere uymanız yardımcı olur. Yaygın soy araştırma uygulamalarına aşina olsanız bile, Gramps'ın nasıl çalıştığını anlamanız gerekir. Ardından, Gramps yazılımının belirli bir soy araştırma stilini tamamlayacak şekilde nasıl kullanılacağına geçebilirsiniz.

Gramps, tüm soy araştırma bilgilerini 9 ana öğe kategorisine ayırır:

- [Kişiler](wiki:Gramps_Glossary/tr#person)

- [Aileler](wiki:Gramps_Glossary/tr#family)

- [Etkinlikler](wiki:Gramps_Glossary/tr#event)

- [Yerler](wiki:Gramps_Glossary/tr#place)

- [Notlar](wiki:Gramps_Glossary/tr#note)

- [Ortam](wiki:Gramps_Glossary/tr#media)

- [Alıntılar](wiki:Gramps_Glossary/tr#citation)

- [Kaynaklar](wiki:Gramps_Glossary/tr#source)

- [Depolar](wiki:Gramps_Glossary/tr#repository)

Bunların her biri bağımsız öğelerden oluşur. Bu, soy ağacınıza her seferinde bir öğe ve istediğiniz sırayla girebileceğiniz anlamına gelir. Öğeleri birbirine bağlayabilir veya bağlantısız (veya dağınık bir şekilde düzensiz) ancak aranabilir halde bırakabilirsiniz. Veya aklınızda bir ağaç tasarımıyla başlayabilir ve ilerledikçe yeni öğeler bağlayarak onu dışa doğru doldurabilirsiniz.

Örneğin, önce her Kişi öğesini girmek ve daha sonra aile öğeleri oluşturarak bunları birbirine bağlamak isteyebilirsiniz. Veya bir aile ile başlayabilir, çocuk veya ebeveyn olarak yeni bir Kişi ekleyerek aileyi sabitleyebilir, ardından aile penceresinin yuvalarına akrabalar, olaylar ve kaynak materyaller ekleyebilirsiniz. Veya Kaynak öğelerle başlayabilir ve yalnızca araştırmanız birinden söz edildiğinde bir kişi öğesi oluşturabilirsiniz. Veya bazı not ve kaynak öğeleri, ardından aile öğeleri ve daha sonra notlar ve kaynaklar'a geri dönerek bu veri girme stillerini karıştırabilirsiniz. Kısacası, soy araştırmanızı istediğiniz gibi yaparsınız.

Başka sorularınız varsa, Gramps'ın bir kullanıcı ve geliştirici topluluğu vardır. Bir [SSS](wiki:Gramps_6.0_Wiki_Manual_-_FAQ/tr) (sık sorulan soru listesi) vardır; [bir posta listesi](wiki:Contact/tr#ePosta_listeleri); [bir hata, özellik isteği ve sorun izleyici](wiki:Using_the_bug_tracker/tr); ve çevrimiçi [sohbet odaları](wiki:Contact/tr#Sohbet_Odası) veya [topluluk forumlarını](wiki:Contact/tr#Forum) kullanarak etkileşim kurabilirsiniz.

### Bağlantılar

Bu 9 birincil öğe çeşitli şekillerde bağlantılıdır. Bu bağlantılardan bazıları örtük olarak korunur. Örneğin, bir aile öğesine ebeveyn veya çocuk olarak bir kişi öğesi eklemek, otomatik olarak **Referans** adı verilen özel bir bağlantı oluşturur. Ana Kişi penceresindeki Referanslar sekmesinde Kişinin bağlı olduğu Aileleri görebilirsiniz. İlişki Görünümü de dahil olmak üzere bu bağlantıların Gramps'ta görselleştirilmesinin başka birçok yolu vardır.

Bilgilerin tekrarlanmasını önlemek için Gramps, öğeleri yeniden kullanmanıza veya paylaşmanıza izin verir. Bunlar ayrıca **ilişim** adı verilen özel bağlantılardır. Örneğin, bir Kişi öğesi herhangi bir sayıda not öğesine bağlanabilir. Bir not iki ayrı kişiden bahsediyorsa, o tek notu her iki kişi öğesiyle paylaşmak mantıklı olabilir.

Bazı bağlantıların kendileri bilgi içerir. Örneğin, bir kişiyi başka bir çiftin evlilik olayına bağlayabilirsiniz, çünkü bu kişi onların düğününde tanıktı. Bununla birlikte, karı koca evlilik olayıyla **birincil** bir rolde bağlantılıyken, bir tanık farklı bir rolü üstlenir, örn. **tanık** olarak. Bu tür bilgiler, bağlantının kendisinde, rol özelliğinde tutulur.

### Gizlilik

Gramps, soy ağacınızdaki hassas verilerin gizliliğini korumak için iki farklı yöntemi destekler. Bu yöntemler, bir raporun oluşturulması, verilerin dışa aktarılması veya bir web sitesinin oluşturulması yoluyla verilerinizi başkalarıyla paylaşırken kullanılır.

![[_media/Include-data-marked-private-checkbox-example-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Raporlar için gizliliği geçersiz kılma]]

İlk yöntem, Gramps'ın yaşadığına inandığı kişiler hakkındaki bilgileri korur. Bir kişinin öldüğünü özellikle belirtmediyseniz (bir Kişi öğesine bir Ölüm Olayı ekleyerek), bu durumda Gramps, birinin hayatta olup olmadığını belirlemek için gelişmiş, otomatik bir işleve sahiptir. Yaşayan insanlar bu yöntemi kullanırken hassas verilerini düzeltirler. Örneğin, "Smith, John" adlı bir kişi "Smith, \[Yaşayan\]" olarak görünebilir.

İkinci gizlilik yöntemi, her öğe için ayarlayabileceğiniz ["özel" işaretidir](wiki:Gramps_Glossary/tr#private_tag). Örneğin, bir notta hassas, kişisel bilgileriniz olabilir. Böyle bir notu özel olarak işaretlerseniz, o not metinsel ve anlatımlı raporlarda veya dışa aktarmalarda gösterilmeyecektir. Ayrıca bazı bağlantıların kendilerinin özel olarak işaretlenebileceğini unutmayın. Bu, örneğin bir kişiden bir olaya olan bağlantıyı özel olarak işaretlemek istediğinizde, ancak yine de kişi ve olay raporda, dışa aktarmada veya web sitesinde mevcut olduğunda kullanışlıdır.

Bu iki gizlilik yöntemini etkinleştirmek için, bazı raporlar oluştururken veya verilerinizi dışa aktarırken bunların kullanımını belirtmeniz gerekir. {{-}}

### GEDCOM

Gramps, öğelerin temel yapısını GEDCOM adlı bir standarttan alır. Ancak Gramps, gerekli gördüğü durumlarda bu standardı genişletir. Aile verilerinizi GEDCOM kullanan başka bir sistemle kullanmayı planlıyorsanız, muhtemelen yalnızca Gramps uzantıları olan özellikleri kullanımınızı kısıtlamayı denemek isteyeceksiniz. Öte yandan, diğer soyağacı yazılımlarıyla sınırlı değilseniz, verilerinizi sizin için anlamlı olan her şekilde girebilirsiniz.

Bu konuyla ilgili daha fazla ayrıntıyı [Gramps ve GEDCOM](wiki:Gramps_and_GEDCOM/tr) ile ilgili bölümde okuyabilirsiniz.

## Gramps'ı Başlat

Gramps öğrenmenin en iyi yolu, verilerinizle çalışmaktır. Başlayalım!

Gramps'ı başlatma şekliniz, kullandığınız işletim sistemine bağlıdır.

Gramps'ı aşağıda açıklandığı gibi normal grafik kullanıcı arabirimini (GUI) kullanarak başlatmanın yanı sıra, bir komut satırı arabirimi (CLI) kullanarak Gramps'ı başlatmak da mümkündür. CLI kullanımı, GUI üzerinden erişilemeyen raporları üretebilir, pencere açmadan raporlar oluşturmak, dönüşümler yapmak vb. için kullanılabilir ve sorun olması durumunda [ekstra bilgi](wiki:Gramps_6.0_Wiki_Manual_-_Error_and_Warning_Reference/tr#Tüm_hata_mesajlarını_görme) sağlayabilir. Daha fazla bilgi için [Komut Satırı ekine](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/tr) bakın.

### Linux

Gramps geliştiricileri bu platformdaki kaynak kodunu kullanıp test ederek yükseltmeler nedeniyle ortaya çıkan sorunları düzelttiği için yalnızca Linux platformu resmi olarak desteklenir.

Linux dağıtımınız için standart Paket Yöneticisini (bir CLI veya GUI aracılığıyla) kullandığınızı varsayarsak, dağıtımınız için Gramps'ı normal şekilde başlatacaksınız. Örneğin Ubuntu 18.04'te başlatıcıya bir simge yerleştirilir veya program Dash'tan başlatılabilir. Diğer dağıtımlar için Uygulama menüsünde (normalde **Ofis** bölümünde) bir giriş oluşturulabilir.

Gramps'ı Linux'ta CLI aracılığıyla başlatmak [buraya](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/tr#Linux) bakınız.

### MS Windows

MS(Microsoft) Windows, [topluluk tarafından desteklenen](wiki:Download/tr#MS_Windows) bir platformdur. [Windows AIO](wiki:All_In_One_Gramps_Software_Bundle_for_Windows/tr) GrampsAIO32 veya GrampsAIO64 yürütülebilir dosyasını yüklerseniz, bu masaüstüne bir simgenin yanı sıra 'Başlat' menüsünde bir menü öğesi yerleştirir ve Gramps'ı başlatmak için buna tıklayabilirsiniz.

Gramps'ı MS Windows'ta CLI aracılığıyla başlatmak [burada](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/tr#MS_Windows) ele alınmıştır.

MS Windows için Gramps'ı kurmanın başka yolları da vardır, ancak bunlar çok daha karmaşıktır ve burada ele alınmamıştır.

### Mac OS X

Apple Mac OS X (MacOS), [topluluk tarafından desteklenen](wiki:Download/tr#macOS) bir platformdur. Mac OS X disk görüntüsünü (.dmg) indirirseniz, uygulamayı uygulama klasörünüze (veya saklamak istediğiniz başka bir yere) sürüklemeniz ve normal şekilde uygulamaya çift tıklayarak Gramps'ı başlatmanız yeterlidir.

Gramps'ı Mac OS X'te CLI aracılığıyla başlatmak [burada](wiki:Gramps_6.0_Wiki_Manual_-_Command_Line/tr#MacOS) ele alınmıştır.

Mac OS X için Gramps'ı kurmanın başka yolları da vardır, ancak bunlar çok daha karmaşıktır ve burada ele alınmamıştır.

## Soyağacı Seçmek

![[_media/Dashboard-category-view-first-open-no-family-tree-loaded-52-tr.png|Fig {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Dashboard Category View - First open of Gramps with no family tree loaded(Gramps 6.0.0; MS-Windows 10)]]

Gramps, bir soyağacı seçilmeden başlatılırsa, ilk ekranın çok az işlevi olacaktır ve çoğu işlem kullanılamayacaktır. Bir soyağacını (*veri tabanı* olarak da adlandırılır) yüklemek için, sekmesine tıklayarak veya araç çubuğundaki simgesine tıklayarak soyağacı yöneticisini açın. Gramps, en son açılan Soyağaçlarınızı takip eder ve bunlar, düğmesinin yanındaki oka tıklayarak ve açılır menüden seçim yaparak seçilebilir.

Soyağacı yöneticisi ve Soyağaçları menüsü hakkında daha ayrıntılı bilgi için, bununla ilgili bölüme bakın: [Soyağaçlarını Yönetmek](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/tr). {{-}}

## Hemen şimdi nasıl başlayacağımı söyle!

Herkese Gramps kullanımı hakkında her şeyi öğrenmek için kılavuzu okumasını tavsiye ederiz. Soy araştırması zaman alır, bu nedenle araçları öğrenmek zaman kaybı değildir.

Ancak, gerçekten asgari bir başlangıç istiyorsanız, şunu okuyun:

- [Gramps 6.0 Wiki Kılavuzu - Veri girme ve düzenleme: özet](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_brief/tr)
- [Gramps kullanarak Soy Araştırmasına nasıl başlarım?](wiki:Start_with_Genealogy/tr).

## Yardım Alma

Gramps, istediğiniz zaman başvurabileceğiniz bir menüsüne sahiptir.

- menüsü bölümüne bakın.

{{-}}

[Category:Tr:Documentation](wiki:Category:Tr:Documentation)
