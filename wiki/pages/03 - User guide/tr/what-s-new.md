---
title: Gramps 6.0 Wiki Manual - What's new?/tr
categories:
- Tr:Documentation
managed: false
source: wiki-scrape
wiki_revid: 111544
wiki_fetched_at: '2026-05-30T20:56:13Z'
lang: tr
---

Bu bölüm, Gramps sürüm 5.0'dan bu yana yapılan değişikliklere genel bir bakış sunar. Bu değişiklikler ayrıca bu kılavuzun ilerleyen kısımlarında ayrıntılı olarak açıklanmaktadır. Eski sürümlerden yükseltme yapan Gramps kullanıcılarının, sürüm 6.0'i kullanmaya başladıklarında bu yeni özelliklerden yararlanacaklarından emin olmak için eski [kullanım kılavuzlarındaki](wiki:Gramps_6.0_Wiki_Manual/tr) bu bölümü gözden geçirmelerini önerilir.

# Yükseltmeden önce

Yükseltmeden ***önce*** soy ağacı verilerinizin güvende olduğundan emin olun. Bunu yapmanın en iyi yolu şudur:

1.  Mevcut Gramps sürümünüzü başlatın (Gramps 3.4, Gramps 4.2 veya Gramps 5.0)
2.  Soy ağacını açın
3.  Soy ağacını *gramps xml* biçimine veya *gramps xml paket* biçimine yedekleyin (*gramps xml paketi*, fotoğraflarınızı ve soy ağacı verilerinizle ilişkili diğer medya dosyalarınızı içerir). Menüden seçenekleriyle soyağacınızın yedeğini alın.
4.  Bu soyağacını kapatın ve sahip olduğunuz diğer soyağaçları için yukarıdaki adımları tekrarlayın.
5.  Ortaya çıkan dosya(lar)ı güvenli bir yerde saklayın

Daha fazla bilgi için, lütfen [Soyağacı Yedekle](wiki:Gramps_6.0_Wiki_Manual_-_Manage_Family_Trees/tr#Soyağacı_Yedekle)'yi inceleyin. [Yedekleme sırasında nelerin dahil edilmeyeceğini](wiki:Template:Backup_Omissions/tr) not edin.

Verilerinizi uygun şekilde koruduktan sonra, işletim sisteminizin normal kurulum sürecini kullanarak Gramps 6.0'i kurmaya devam edin. Çoğu durumda bu, yeni Gramps 6.0 kurulumunun eski Gramps sürümünüzle çakışmamasını sağlayacaktır. Ancak, Gramps 6.0'i yüklemeden önce Gramps 3.4'ü kaldırmak veya Gramps 6.0'i farklı bir konuma yüklediğinizden emin olmak daha güvenli olabilir. Kaynak kodundan yükleme yapıyorsanız, bu her zaman gereklidir. Gramps 6.0'i yükleme hakkında daha fazla bilgi için lütfen [En son sürüm Gramps](wiki:Download/tr)'ı İndirme bölümüne bakın.

Gramps 6.0'i kurduktan sonra mevcut soy ağaçlarınızı açıp çalışmaya devam edebilirsiniz. Sorun olması durumunda (örneğin, tam bir sistem yükseltmesinden sonra), soy ağacınızı/ağaçlarınızı yeniden oluşturmak için yukarıda oluşturulan yedekleme dosyasını/dosyalarını içe aktarın.

# Çekirdekte görünür değişiklikler

Geçişten sonra görünen değişiklikler: arayüz, veri.

## Veri Örneği

[Veri örneğindeki](wiki:Gramps_Data_Model/tr) değişikliklerin ayrıntıları (varsa):

1.  Değişiklik yok

<hr>

- Gramps 3.4/4.0/4.1/4.2 ve Gramps 6.0 sürümlerinde yükseltme yapılmadan Soy Ağacı **açılamaz**.

<!-- -->

- Bir sürüm düşürme, yalnızca XML dışa aktarılarak ve önceki sürüm içe aktarılarak gerçekleştirilebilir.

<!-- -->

- Gramps 3.4/4.0/4.1 tarafından oluşturulan bir Gramps XML dosyası, Gramps 6.0 tarafından oluşturulan ile **aynı değildir**.

<!-- -->

- Gramps 6.0 artık yalnızca **python3** kullanır

Dahili veri tabanı hakkında daha fazla ayrıntı için [ayrıntılı değişikliklere](wiki:Database_Formats/tr#Değişiklik_Tablosu) bakın.

## Birincil değişiklikler

- SQLite artık BSDDB yerine varsayılan veri tabanı arka ucudur. Yine de [alternatif veri tabanı](wiki:Relational_database_comparison/tr) arka uçlarını kullanmayı seçebilirsiniz. BSDDB standart bir alternatif olarak mevcut olmaya devam etmektedir. Uzman kullanıcılar için PostgreSQL ve MongoDB, deneysel üçüncü taraf eklentileri olarak mevcuttur.

Geliştiriciler, SQLite'ın kolay bozulmayı önleyen daha az veri tabanı bozulmasına sahip olabileceğine inanıyor.

- Periyodik olarak ve çıkışta otomatik yedekleme seçenekleri. Çıkışta Yedekleme varsayılandır.
- Yapılandır: yeni veritabanı-yedekleme-kullan-sıkıştır seçeneği

## GUI

- Yeni renk şemaları, açık ve koyu bir seçime izin verir.
- Ana Kişi, Bilinmeyen Canlı, Aile, Boşanmış Aile için grafiklerde ek renk göstergeleri.
- "<n> km/mil/derece içinde" süzgeç ekle
- Virgülle ayrılmış enlem/boylam çiftleri girebilme
- Kenar çubuğu daha iyi yeniden boyutlandırılır, konum hatırlanır
- Kişi Soyadı düzenleyicisinin kullanımı daha sezgiseldir.
- Görünüm Düğmeleri sırası artık yeni başlatmalarda değişmiyor.
- Uzun süren işlemler için daha iyi ilerleme göstergesi
- Windows boyutu/konumu hatırlar
- Alt-Üst Soy Yelpaze eklendi
- Coğrafya yerler görünümü için kml eklendi.

## Yerler

- Yer seçerken alternatif yer adlarını arama yeteneği

## Raporlar, Araçlar, Gramplet'ler

- Yeni soy ağacı raporu
- Birçok rapor için biçim düzenleyici ve seçenek eklendi
- Tarih biçimi Düzenleyici ve birçok rapor için seçenek eklendi
- Birçok rapor için yaşayan insanların nasıl rapor edileceği seçeneği eklendi
- ReorderID'ler aracı yükseltildi; artık özelleştirilmiş kimlikler (GetGov kimlikleri gibi) üzerinde çalışılabilir.
- Anlatı web sitesi ek seçenekleri ve görünüm değişiklikleri eklendi.
  - Farklı dilde çıktı seçeneği
  - Tarih çıktı seçeneği
  - İstatistikler sayfası
  - Tüm/referanssız ortam nesnelerini dahil etme seçeneği
  - Bireysel sayfalarda merkezi kişiyle ilişki
- Add thumbnail size option to family lines graph
- Altsoy Raporu ve Ayrıntılı Altsoy Raporu geliştirmeleri
- Eksiksiz Bireysel Rapor ekleme seçenekleri
  - Kişi ve Aile notlarını dahil etmeyi veya hariç tutmayı etkinleştirin
  - Sayım verilerini dahil etme veya hariç tutma seçeneği
  - Merkez kişiyle olan ilişkiyi dahil etme seçeneği
  - GrampsID, Etiketler, Nitelikleri dahil etme seçenekleri
- Tüm yer türlerini yer raporuna dahil et
- İlişki, Aile Kuşakları, Kum Saati Grafikleri çizgi seçenekleri
- Yeni: [Giriş verilerini temizle](wiki:Gramps_6.0_Wiki_Manual_-_Tools/tr#Giriş_verilerini_temizle) aracı - Baştaki ve sondaki boşlukları kaldırır.

## İçe aktar/Dışa aktar

- Gedcom daha fazla standart dışı 'etiket' ve ek standart etiketleri desteği
- GEDCOM 5.6.0 Dışa aktarmada Özel Etkinlik desteği
- XML dışa aktarmada yeni sıkıştırma seçeneği

## Yeni Eklentiler

- Kırkyama Tablosu görünümü: Görünüm, bir aile ağacının kırkyama modeli şeklinde görselleştirir
- Gelişmiş Eklenti Yöneticisi: Birkaç ek yeteneğe sahip bir Addon/Plugin Yöneticisi
- Kum Saati Ağacı: LaTeX soy ağacı kullanan kum saati ağacı
- İçe Aktar ve Birleştir aracı: Bir Gramps XML veri tabanını mevcut veri tabanıyla karşılaştırır ve farklılıkların birleştirilmesine olanak tanır.
- Bağlantı verilerini kontrol et: Kişiler için bağlantı verilerini kontrol eder.

# Kaputun altında değişenler

Teknik değişiklikler.

- Diğer veri tabanı arka uçlarının desteklenmesiyle ilgili çok sayıda değişiklik (SQLite, PostgreSQL, MongoDB vb.).
- Daha önce kaldırılmış olan belirli veri tabanı bozulmaları (var olmayan nesnelerle ilgili) hakkındaki uyarılar artık hata olarak kabul edilmektedir. Bozuk bir veritabanıyla ilgili istisnaları düzeltmek için Kontrol Et ve Onar aracını çalıştırmak gerekli olabilir.
- Uzun süren işlemler sırasında kullanıcının veri tabanını kapatmasını veya değiştirmesini engelleyen düzeltmeler.

## Bağımlılıklar

- Yalnızca **python3** desteği. (Python2 desteği, Ocak 2020 itibari ile <ABBR title="Kullanım Ömrünün Sonu (durdurma)">EOL</ABBR> geldi)
- GTK+ 3.10 ve PyGObject 3.12 veya daha üst sürümleri gerekir

# Daha fazla bilgi

## Çeşitli

## Yerelleştirme

- Güncellenen çeviriler: ca, cs, da, de, en_GB, eo, fr, fi, hu, is, it, lt, nb, nl, pt_BR, pt_PT, ru, sk, sl, uk, vi

## Yol Haritası

- [Gramps'ın önceki sürümleri](wiki:Previous_releases_of_Gramps/tr) için sürüm notlarını kontrol edin
- Gramps'ın [sonraki sürümüyle](https://gramps-project.org/bugs/roadmap_page.php) ilgili öngörülen öğeleri görün.
- [Gramps Geliştirme Önerileri (GEPS)](wiki::Category:GEPS) - Gramps 6.0'de uygulanan yeni öğeler için **Yayınlanan** sütununa bakın
- [6.0 Roadmap](wiki:6.0_Roadmap) - viki

## Değişiklik Günlüğü

- Gramps sorun izleyicisinde Gramps [6.0](https://gramps-project.org/bugs/changelog_page.php) ile ilgili öğelere bakın.
- Gramps'ın test sürümleri ve ek bilgiler için değişiklik günlüklerine bakın:
  - Gramps [6.0.0](https://github.com/gramps-project/gramps/releases/tag/v6.0.0)
  - Gramps [6.0.1](https://github.com/gramps-project/gramps/releases/tag/v6.0.1)
  - Gramps [6.0.2](https://github.com/gramps-project/gramps/releases/tag/v6.0.2)
  - Gramps [6.0.3](https://github.com/gramps-project/gramps/releases/tag/v6.0.3)

{{-}}

## *Bir zamanlar* yeni olan

[Önceki Sürüm](wiki:Previous_releases_of_Gramps/tr) sayfası, yıllar içinde ana sürümlerdeki ve bakım sürümlerindeki değişikliklerin madde imli listelerine bağlantılar içerir.

Ancak, her ana sürüm için viki kılavuzunun eski sürümündeki **Yeni ne var?** sayfalar daha fazla ayrıntı sağlayabilir:

- [Sürüm 5.0](wiki:Gramps_5.0_Wiki_Manual_-_What%27s_new%3F)
- [Sürüm 4.2](wiki:Gramps_4.2_Wiki_Manual_-_What%27s_new%3F)
- [Sürüm 4.1](wiki:Gramps_4.1_Wiki_Manual_-_What%27s_new%3F)
- [Sürüm 4.0](wiki:Gramps_4.0_Wiki_Manual_-_What%27s_new%3F)
- [Sürüm 3.4](wiki:Gramps_3.4_Wiki_Manual_-_What%27s_new%3F)
- [Sürüm 3.3](wiki:Gramps_3.3_Wiki_Manual_-_What%27s_new%3F)
- [Sürüm 3.2](wiki:Gramps_3.2_Wiki_Manual_-_What%27s_new%3F)

Geliştirmelere yönelik kısa bir genel bakış, kılavuza ilk olarak 2010 yılında eklenmiştir. Viki'nin ilk 3 yılında, kılavuzun tamamının gözden geçirilmesi gerekliydi.

- [Sürüm 3.1 - Tam kılavuz](wiki:Gramps_3.1_Wiki_Manual)
- [Sürüm 3.0 - Tam kılavuz](wiki:Gramps_3.0_Wiki_Manual)

İlk MediaWiki belgeleri 2006'da başlatıldı. Kılavuzun 2.9 sürümünden önce, belgeler Gramps yazılımıyla dağıtıldı. İndirilebilir kılavuz, Gramps 3.0 sürümüyle ortadan kaldırıldı.

- [Gramps 2.2 (kılavuz sürümü 2.9)](https://gramps-project.org/gramps-manual/2.2/en/index.html)

{{-}}

[Category:Tr:Documentation](wiki:Category:Tr:Documentation)
