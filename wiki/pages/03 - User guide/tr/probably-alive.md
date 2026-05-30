---
title: Gramps 6.0 Wiki Manual - Probably Alive/tr
categories:
- Tr:Documentation
managed: false
source: wiki-scrape
wiki_revid: 111456
wiki_fetched_at: '2026-05-30T20:56:10Z'
lang: tr
---

{{#vardefine:chapter\|7}} {{#vardefine:figure\|0}}

Bir Gramps veri tabanındaki kişilerin yaşam durumu, verilerinizi başkalarıyla paylaşmanız gerektiğinde, ancak hayatta olanların ayrıntılarını korumak istediğinizde önemlidir. Bazı raporlarda da kullanılır. Bu nedenlerden dolayı Gramps, birinin hayatta olup olmadığını belirlemenize yardımcı olacak bazı araçlara sahiptir.

## Gramps birinin hayatta olup olmadığını nasıl belirler?

![[_media/EditPreferences-Dates-tab-default-51.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Edit&gt;Preferences..." - "Dates" - tab - defaults]]

Birinin hayatta olup olmadığını anlamanın basit bir yolu, bir ölüm etkinliği mi yoksa ölümle ilgili bir etkinlik mi (mezar gibi) olduğunu görmektir. Ancak veri tabanınızdaki bir çok kişinin ölüm ayrıntılarını bilmiyor olabileceğinizden dolayı birçok kişinin bu tür etkinliklere sahip olmadığı muhtemelen doğrudur. Birinin öldüğünü biliyorsanız, bir ölüm etkinliği oluşturmak iyi bir fikir olabilir. Ayrıca, bir kez bilindiğinde geri dönüp yararlı ayrıntılar (ölüm tarihi ve yeri gibi) ekleyebilirsiniz. Kesin ayrıntılar içermeseler bile, öldüğü bilinen kişiler için etkinlikler eklemek biraz yararlıdır. Ancak, Gramps sizin için tahmini tarihleri ​​olan (veya olmayan) etkinlikler de ekleyebilir (aşağıda açıklanmıştır).

Bir kullanıcının bir kişiye elle bir ölüm etkinliği eklemesini istemek (böylece canlı olarak kabul edilmemeleri için) çok can sıkıcı olurdu ---biri birçok kişi hakkında ayrıntı girmek zorunda kalacaktı. Birinin hayatta olduğu düşünülürse, dışa aktarıldığında ayrıntılarının paylaşılmasının engellenmesi gerektiğini hatırlayın. Bu nedenle Gramps, birinin etkinlik tarihlerine veya etkinlik tarihleri ​​olabilecek kişilerle olan ilişkilerine göre muhtemelen hayatta olup olmadığını hesaplayabilen bir işleve sahiptir. Örneğin, bir kişinin herhangi bir ölüm kanıtı yoksa (ölüm veya defin etkinliği gibi), o zaman Gramps bu kişinin ebeveynlerini, çocuklarını, kardeşlerini bir kanıt bulunana kadar sürekli olarak kontrol eder---veya kontrol edilecek bağlantılar bitene kadar. Tipik yaş ve etkinlik süreleri hakkındaki bilgileri kullanarak (kardeşler arasındaki tipik yaş farklılıkları, annelerin doğum anındaki tipik yaşları vb.) Gramps, bir kişinin hayatta mı yoksa ölü mü olduğu konusunda tahminlerde bulunabilir. Tahmin edebileceğiniz gibi bu yürütülmesi zaman alan bir işlev olabilir, ancak oldukça yararlı olabilir. Tipik doğum yaşı, kuşaklar arası vs. için değerler sekmesinden ayarlanabilir.

Muhtemelen yaşıyor işlevi, bir kişinin belirli bir tarihte veya bir zaman aralığında hayatta olup olmadığını kontrol edebilir. Bu, [Tarihteki Yaşı](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Tarihteki_Yaşı) Grampletinde kullanılır. Normalde sistem doğum ve ölüm olaylarını tahmin eder ve bu ikisi arasında bir tarih olup olmadığına bakar.

Ancak, özel bir durum var: Muhtemelen *bugün* yaşayan insanları arıyorsanız ve bir ölüm etkinliği varsa, o zaman ne olursa olsun ölü olarak kabul edilirler (etkinliğin tarihi olmasa bile). Bu nedenle, kimin dün (veya geçen yıl) hayatta olduğunu ve bugün kimin hayatta olduğunu görürseniz farklı sonuçlar alırsınız. Bunun nedeni, eğer bir ölüm etkinliğiniz varsa, geçmişte bir kişinin öldüğünü biliyorsunuz ama ne zaman olduğunu bilmiyorsunuz. Bir kişinin geçmişte (dün ve önceki) hayatta olup olmadığına bakarsanız, ölüm tarihini bilmeden o kişinin ölü olup olmadığını kesin olarak söyleyemezsiniz.

Gramps'ın bir bireyin canlı veya ölü olduğunu neden belirlediğinin ayrıntılarını bilmek istiyorsanız, bir açıklama almak için [Tahmini Tarihleri ​​Hesapla](wiki:Addon:Calculate_Estimated_Dates/tr) Aracı eklentisini kullanabilirsiniz. Bu, tahmini doğum ve ölüm tarihlerini ve bunların dayandığı bir olay tarihi olan biriyle olan ilişkiyi gösterecektir.

## Muhtemelen Yaşayan Proxy

İlk araç "Muhtemelen Yaşayan" proxy'sidir. Bu, verilerinizi canlı insanlarla ilgili ayrıntıları kısıtlama özelliğini destekleyen bir biçime aktardığınızda otomatik olarak kullanılır. Proxy, veritabanını, yaşayan insanların adları ve olayları gibi hassas ayrıntılarına erişimi engelleyen bir katmana sarar.

## Muhtemelen Yaşayan Süzgeci

Bugünün tarihi, tarihi bulunmayan etkinliklerde ve geçmişte canlı durumu kontrol edildiğinde özel olarak ele alınır. Örneğin, bir kişinin tarihi olmayan bir ölüm etkinliği varsa, o kişinin bugün itibariyle ve her zaman gelecekte öldüğünü biliyoruz. Ancak, geçmişte bir tarihte bir kişinin hayatta olup olmadığını kontrol edebileceğiniz bu işlevler için, o tarihte hayatta mı yoksa ölü mü olduğunu söyleyemeyiz. Bu nedenle, tarihi olmayan bir ölüm etkinliğiniz varsa ve daha dün hayatta olup olmadıklarını kontrol ederseniz, Gramps canlı/ölü durumunu belirleyemez.

Bakınız:

- [Muhtemelen yaşayan kişiler süzgeci](wiki:Gramps_6.0_Wiki_Manual_-_Filters/tr#Muhtemelen_yaşayan_kişiler)

## Takvim Gramplet

[Takvim](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets/tr#Takvim) gramplet bakınız.

## Tarihleri ​​Düzenleme

See [Editing dates](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Editing_dates).

[Category:Tr:Documentation](wiki:Category:Tr:Documentation)
