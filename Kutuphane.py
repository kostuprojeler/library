class Renk:
    kirmizi = '\033[31m'
    yesil = '\033[92m'
    sari = '\033[93m'
    sade = '\033[0m'
    mavi = '\033[96m'
class Kitap:
    def __init__(self, isim, yazar, yil):
        self.isim = isim
        self.yazar = yazar
        self.yil = yil

    def __str__(self):
        return f"{Renk.sari}Kitap Adı:{Renk.sade} {self.isim} | {Renk.sari}Yazar:{Renk.sade} {self.yazar} | {Renk.sari}Yayın Yılı:{Renk.sade} {self.yil}"

def harfkontrol(metin):# harfkontrol fonksiyonu Türkçe karakter uyumu için casefold ile kontrol yapar.
    metin = metin.replace("I", "ı").replace("İ", "i")
    return metin.casefold()
class Kutuphane:
    def __init__(self):
        self.kitaplar = []
        self.kitap_dosyasi()

    def kitap_dosyasi(self):# kitap_dosyasi fonksiyonu kütüphanedeki ekli kitapları txt dosyası ile hafızada tutmamızı sağlıyor.
        try:
            with open("kitaplar.txt", "r", encoding="utf-8") as dosya:
                for satir in dosya:
                    isim, yazar, yil = satir.strip().split(" | ")
                    self.kitaplar.append(Kitap(isim, yazar, int(yil)))
        except FileNotFoundError:
            pass

    def kitap_ekle(self, kitap):# kitap_ekle fonksiyonu alınan isim, yazar ve yıl değerlerini, eğer kütüphanede aynısı yoksa self.kitaplar listesine ekliyor.
        for k in self.kitaplar:
            if (harfkontrol(k.isim) == harfkontrol(kitap.isim) and
                harfkontrol(k.yazar) == harfkontrol(kitap.yazar) and
                k.yil == kitap.yil):
                print(Renk.kirmizi+"Bu kitap zaten kütüphanede mevcut."+Renk.sade)
                return
        self.kitaplar.append(kitap)
        with open("kitaplar.txt", "a", encoding="utf-8") as dosya:
            dosya.write(f"{kitap.isim} | {kitap.yazar} | {kitap.yil}\n")
        print(Renk.yesil+"Kitap başarıyla eklendi."+Renk.sade)

    def isme_gore_kitap(self, isim):#isme_gore_kitap fonksiyonu kullanıcıdan alınan isim ile self.kitaplar içinde bir kitap arıyor.
        bulunan = [
            kitap for kitap in self.kitaplar
            if harfkontrol(kitap.isim) == harfkontrol(isim)
        ]

        if not bulunan:
            print(Renk.kirmizi+"Kitap bulunamadı."+Renk.sade)
            return

        print(Renk.sari+"\n--- Arama Sonuçları ---"+Renk.sade)
        for kitap in bulunan:
            print(kitap)

    def yazara_gore_kitap(self, yazar):#yazara_gore_kitap fonksiyonu kullanıcıdan alınan yazar ile self.kitaplar içinde bir yazar arıyor.
        bulunan = [
            kitap for kitap in self.kitaplar
            if harfkontrol(kitap.yazar) == harfkontrol(yazar)
        ]

        if not bulunan:
            print(Renk.kirmizi+"Kitap bulunamadı."+Renk.sade)
            return

        print(Renk.sari+"\n--- Arama Sonuçları ---"+Renk.sade)
        for kitap in bulunan:
            print(kitap)

    def kitap_sil_isme_gore(self):#kitap_sil_isme_gore fonksiyonu kullanıcıdan isim alarak silmek istediği kitabı siler.
        isim = input(Renk.sari+"Silinecek kitap adı: "+Renk.sade).strip()

        eslesenler = [
            kitap for kitap in self.kitaplar
            if harfkontrol(kitap.isim) == harfkontrol(isim)
        ]

        if not eslesenler:
            print(Renk.kirmizi+"Kitap bulunamadı."+Renk.sade)
            return

        for i, kitap in enumerate(eslesenler, start=1):
            print(f"{i}. {kitap}")

        try:
            secim = int(input(Renk.sari+"Silmek istediğiniz kitabın numarası: "+Renk.sade))
            secilen = eslesenler[secim - 1]
        except (ValueError, IndexError):
            print(Renk.kirmizi+"Geçersiz seçim."+Renk.sade)
            return

        onay = input(Renk.sari+"Emin misiniz? (evet/hayır): "+Renk.sade).lower()
        if onay != "evet":
            print(Renk.kirmizi+"Silme iptal edildi."+Renk.sade)
            return

        self.kitaplar.remove(secilen)
        with open("kitaplar.txt", "w", encoding="utf-8") as dosya:
            for k in self.kitaplar:
                dosya.write(f"{k.isim} | {k.yazar} | {k.yil}\n")

        print(Renk.yesil+"Kitap başarıyla silindi."+Renk.sade)

    def kitap_listele(self):#kitap_listele fonksiyonu kütüphanedeki tüm kitapları kullanıcının istediği şekilde sıralar.
        if not self.kitaplar:
            print(Renk.sari+"Kütüphanede hiç kitap yok."+Renk.sade)
            return

        print(Renk.mavi+"\n--- Tüm Kitapları Listeleme ---"+Renk.sari)
        print("1. Kitap Adına Göre Sırala")
        print("2. Yazar Adına Göre Sırala")
        print("3. Çıkış Yılına Göre Sırala")
        seçim = input("\nSıralama Türünü Seçiniz: (1-3): ")

        if seçim == "1":
            print(Renk.sari+"\n1. Sıralama (A-Z)")
            print("2. Sıralama (Z-A)")
            seçim1 = input("\nSeçim Yapınız (1-2): ")

            if seçim1 == "1":
                sıralama = sorted(self.kitaplar, key= lambda k: k.isim.lower())

            elif seçim1 == "2":
                sıralama = sorted(self.kitaplar, key= lambda k: k.isim.lower(), reverse= True)

            else:
                print(Renk.kirmizi+"Geçersiz Giriş!")
                return

        elif seçim == "2":
            print(Renk.sari+"\n1. Sıralama (A-Z)")
            print("2. Sıralama (Z-A)")
            seçim1 = input("\nSeçim Yapınız (1-2): ")

            if seçim1 == "1":
                sıralama = sorted(self.kitaplar, key= lambda k: k.yazar.lower())

            elif seçim1 == "2":
                sıralama = sorted(self.kitaplar, key= lambda k: k.yazar.lower(), reverse= True)

            else:
                print(Renk.kirmizi+"Geçersiz Giriş!")
                return

        elif seçim == "3":
            print(Renk.sari+"\n1. Sıralama (Eskiden Yeniye)")
            print("2. Sıralama (Yeniden Eskiye)")
            seçim1 = input("\nSeçim Yapınız (1-2): ")

            if seçim1 == "1":
                sıralama = sorted(self.kitaplar, key= lambda k: k.yıl)

            elif seçim1 == "2":
                sıralama = sorted(self.kitaplar, key= lambda k: k.yıl, reverse= True)

            else:
                print(Renk.kirmizi+"Geçersiz Giriş!")
                return

        else:
            print(Renk.kirmizi+"Geçersiz Giriş!")
            return

        print(Renk.sari+"\nTüm Kitaplar Yazdırılıyor..."+Renk.sade)
        for kitap in sıralama:
            print(kitap)

def main():#Ana fonksiyon arayüzü gösterir ve kullanıcıdan (1-6) arası giriş ister. Ona göre de yönlendirme yapar.
    kutuphane = Kutuphane()

    while True:
        print(Renk.mavi+"\n--- KÜTÜPHANE SİSTEMİ ---"+Renk.sade)
        print(Renk.sari+"1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. İsme Göre Ara")
        print("4. Yazara Göre Ara")
        print("5. Kitapları Listele")
        print("6. Çıkış"+Renk.sade)

        secim = input("Seçiminiz (1-6): ").strip()

        if secim == "1":
            isim = input(Renk.sari+"Kitap adı: ")
            yazar = input("Yazar adı: ")
            try:
                yil = int(input(Renk.sari+"Yayın yılı: "))
            except ValueError:
                print(Renk.kirmizi+"Yıl sayı olmalı.")
                continue
            kutuphane.kitap_ekle(Kitap(isim, yazar, yil))

        elif secim == "2":
            kutuphane.kitap_sil_isme_gore()

        elif secim == "3":
            isim = input(Renk.sari+"Kitap adı: ")
            kutuphane.isme_gore_kitap(isim)

        elif secim == "4":
            yazar = input(Renk.sari+"Yazar adı: ")
            kutuphane.yazara_gore_kitap(yazar)

        elif secim == "5":
            kutuphane.kitap_listele()

        elif secim == "6":
            print("Program durduruldu.")
            break

        else:
            print(Renk.kirmizi+"Geçersiz seçim.")
if __name__ == "__main__":
    main()
