import os

# Klasörün yolu
klasor_yolu = "C:\\Users\\albur\\Desktop\\Datasets\\roundabouts\\original\\annotations_txt"  # Kendi klasör yolunla değiştir

# Klasördeki tüm txt dosyalarını işle
for dosya_adi in os.listdir(klasor_yolu):
    if dosya_adi.endswith(".txt"):
        dosya_yolu = os.path.join(klasor_yolu, dosya_adi)

        # Dosyayı okuyup işleyecek
        with open(dosya_yolu, "r", encoding="utf-8") as dosya:
            satirlar = dosya.readlines()

        # İlk karakteri '4' olan satırları filtrele
        yeni_satirlar = [satir for satir in satirlar if not satir.startswith("4")]

        # Yeni dosya içeriğini yaz
        with open(dosya_yolu, "w", encoding="utf-8") as dosya:
            dosya.writelines(yeni_satirlar)

print("İşlem tamamlandı!")
