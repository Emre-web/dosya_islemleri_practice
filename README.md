Öğrenci Notları İşleme Programı
Bu Python programı, öğrenci notları içeren bir dosyayı okuyarak, her öğrencinin başarı durumu (geçme ve kalma) ile ilgili dosyalar oluşturur. Öğrencilerin bilgilerini ve notlarını doğru şekilde hizalayarak, başarı durumlarına göre "Geçenler" ve "Kalanlar" adında iki ayrı dosya oluşturur.

Özellikler
Notların Hesaplanması: Öğrencilerin final notları, vize notları ve ortalamaları hesaplanır. Vize 1 ve Vize 2'nin her biri %30, final notu ise %40 oranında hesaba katılır.
Başarı Durumu: Öğrenciler, ortalamalarına göre 70 ve üzeri not almışlarsa "Geçenler" dosyasına, aksi takdirde "Kalanlar" dosyasına yazdırılır.
Dosya Formatı: Program, öğrenci bilgilerini ve başarı durumlarını düzenli bir şekilde dosyaya yazdırır. Her öğrencinin adı, soyadı, bölümü ve ortalaması 20 karakterlik boşluklarla hizalanır.
Gerekli Kütüphaneler
Python 3.x
Kullanım
1. Notlar Dosyasını Hazırlayın
Program, öğrenci bilgilerini içeren bir dosyayı okumaktadır. Bu dosya, her satırda bir öğrenci bilgisi bulunacak şekilde düzenlenmelidir. Satırda, öğrencinin adı, soyadı, bölümü ve notları (Vize1/Vize2/Final formatında) bulunmalıdır. Örnek bir satır şu şekilde olabilir:

perl
Kopyala
Düzenle
Kara Çalışma Ekonomisi 74/80/90
2. Programı Çalıştırın
Programı çalıştırarak, "not_listesi.txt" dosyasını okuyabilir ve not hesaplamaları ile birlikte geçme ve kalma durumlarına göre iki farklı dosya oluşturabilirsiniz.

bash
Kopyala
Düzenle
python ogrenci_notlari_isleme.py
3. Sonuç Dosyaları
Çalıştırdıktan sonra program, iki dosya oluşturacaktır:

gecenler.txt: Geçen öğrencilerin bilgileri buraya yazılacaktır.
kalanlar.txt: Kalan öğrencilerin bilgileri buraya yazılacaktır.
Her iki dosyada da öğrencilerin bilgileri düzenli bir şekilde hizalanarak sunulacaktır.

Örnek Çıktı
Geçenler (gecenler.txt)
markdown
Kopyala
Düzenle
Adı                     Soyadı                  Bölümü                        Ortalama
--------------------------------------------------------------
Kara                    Çalışma Ekonomisi       74.6
Yasemin                 Karabağ                 Biyoteknoloji                  88.1
Emine                   Özdemir                 Fizik Mühendisliği             80.2
...
Kalanlar (kalanlar.txt)
markdown
Kopyala
Düzenle
Adı                     Soyadı                  Bölümü                        Ortalama
--------------------------------------------------------------
Ali                     Tuncer                  Elektrik ve Elektronik         71.8
Hikmet                  Tekin                   İleri Kimya                    78.1
...
