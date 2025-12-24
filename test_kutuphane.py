from Kutuphane import Kitap, Kutuphane, harfkontrol
import os
TEST_DOSYA = "kitap_test.txt"
class TestKutuphane(Kutuphane):
    def kitap_dosyasi(self):
        self.kitaplar = []
        if os.path.exists(TEST_DOSYA):
            with open(TEST_DOSYA, "r", encoding="utf-8") as dosya:
                for satir in dosya:
                    isim, yazar, yil = satir.strip().split(" | ")
                    self.kitaplar.append(Kitap(isim, yazar, int(yil)))

    def kitap_ekle(self, kitap):
        for k in self.kitaplar:
            if (harfkontrol(k.isim) == harfkontrol(kitap.isim) and
                harfkontrol(k.yazar) == harfkontrol(kitap.yazar) and
                k.yil == kitap.yil):
                return
        self.kitaplar.append(kitap)
        with open(TEST_DOSYA, "a", encoding="utf-8") as dosya:
            dosya.write(f"{kitap.isim} | {kitap.yazar} | {kitap.yil}\n")
def test_harfkontrol():
    print("harfkontrol testi")
    assert harfkontrol("İSTANBUL") == harfkontrol("istanbul")
    assert harfkontrol("IĞDIR") == harfkontrol("ığdır")
    print("harfkontrol testi başarılı\n")
def test_kitap_ekleme():
    print("kitap ekleme testi")
    k = TestKutuphane()
    k.kitap_ekle(Kitap("Test Kitabı", "Deneme Yazar", 2024))
    assert len(k.kitaplar) >= 1
    print("kitap ekleme testi başarılı\n")


def test_ayni_kitap_ekleme():
    print("aynı kitap ekleme testi")
    k = TestKutuphane()
    kitap = Kitap("Tekrar", "Aynı", 2023)
    once = len(k.kitaplar)
    k.kitap_ekle(kitap)
    k.kitap_ekle(kitap)
    sonra = len(k.kitaplar)
    assert sonra == once + 1
    print("aynı kitabı eklemenin engellendiği test başarılı\n")


def test_isme_gore_arama():
    print("isme göre arama testi")
    k = TestKutuphane()
    k.kitap_ekle(Kitap("Python", "Guido", 1991))
    sonuc = [b for b in k.kitaplar if harfkontrol(b.isim) == harfkontrol("python")]
    assert len(sonuc) >= 1
    print("isme göre arama testi başarılı\n")


def test_yazara_gore_arama():
    print("yazara göre arama testi")
    k = TestKutuphane()
    k.kitap_ekle(Kitap("Dil", "Yazar", 2020))
    sonuc = [b for b in k.kitaplar if harfkontrol(b.yazar) == harfkontrol("yazar")]
    assert len(sonuc) >= 1
    print("yazara göre arama testi başarılı\n")


def tum_testleri_calistir():
    print("\ntestler başlıyor\n")
    test_harfkontrol()
    test_kitap_ekleme()
    test_ayni_kitap_ekleme()
    test_isme_gore_arama()
    test_yazara_gore_arama()
    print('\033[92m'"tüm testler geçildi\n")


if __name__ == "__main__":
    tum_testleri_calistir()
