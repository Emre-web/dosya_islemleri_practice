with open("not_listesi.txt", encoding="utf-8") as f: 
    with open("gecenler.txt", "w", encoding="utf-8") as g:
        with open("kalanlar.txt", "w", encoding="utf-8") as k:
            # g: geçenler, k: kalanlar
            icerik = f.readlines()
            print(icerik)
            
            # Başlıkları düzgün şekilde yazalım
            g.write("Geçenler:\n")
            k.write("Kalanlar:\n")
            g.write("\n")  # Başlık sonrasında bir boş satır ekleyelim
            k.write("\n")

            # İçeriği işleme
            m = 0
            for satir in icerik:
                if m == 0:
                    m += 1
                    continue
                satir = satir.replace("\n", "")
                bosluk_sayisi = 0
                bosluk_indexleri = []
                index = 0

                for karakter in satir:
                    if karakter == " ":
                        bosluk_sayisi += 1
                        bosluk_indexleri.append(index)
                    index += 1
                
                # Eğer boşluk yoksa bu satırı atla
                if bosluk_sayisi == 0:
                    print(f"Boşluk bulunmayan satır: {satir}")
                    continue

                ad_soyad = satir[:bosluk_indexleri[0]]
                soyad = ad_soyad.split("-")[-1]
                ad = ad_soyad[:ad_soyad.index(soyad) - 1].replace("-", " ")

                # Notlar kısmını alalım
                notlar = satir.split(" ")[-1]
                notlar = notlar.split("/")
                vize1 = int(notlar[0])
                vize2 = int(notlar[1])
                final = int(notlar[2])

                ortalama = vize1 * 0.3 + vize2 * 0.3 + final * 0.4 
                ondaliksiz_ort = round(ortalama, 3)
                print(ondaliksiz_ort)

                # Ders kısmını kapsayan alanı alma
                bolum = satir[bosluk_indexleri[0] + 1:bosluk_indexleri[len(bosluk_indexleri) - 1]]
                print(bolum)

                # Dosyaya yazdırma
                yazdirilacak_satir = f"{ad:<25}{soyad:<25}{bolum:<30}{ondaliksiz_ort:>10}\n"
                
                if ondaliksiz_ort >= 70 and final >= 70:
                    g.write(yazdirilacak_satir)
                else:
                    k.write(yazdirilacak_satir)
