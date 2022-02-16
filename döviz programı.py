import requests
from bs4 import BeautifulSoup
import time

url = "https://kur.doviz.com/"

response = requests.get(url)

html_icerigi = response.content
soup = BeautifulSoup(html_icerigi, "html.parser")

if (response.status_code) == 200:
    print("Bağlantı başarılı...")
    kurlar = (soup.find_all("tr", {"class": ""}))
    fiyatlar = (soup.find_all("td", {"class": "text-bold"}))
    kurlarkisaltma = []
    kurlaruzun = []
    fiyatlar1 = []
    fiyatlar2 = []
    for i in range(1, len(kurlar)):
        deneme = kurlar[i].text
        deneme = deneme.strip()
        deneme = deneme.replace("\n", "")
        if len(deneme) != 0:
            kurlarkisaltma.append(deneme[0:4])
            deneme = deneme.split(" ")
            kurismiuzun = deneme[2] + " " + deneme[3] + " " + deneme[4] + " " + deneme[5]
            kurlaruzun.append(kurismiuzun)

    for fiyat in fiyatlar:
        fiyat = fiyat.text
        fiyat = (fiyat[0:5])
        fiyatlar1.append(fiyat)

    yerler = (list(range(0, 198, 3)))

    for i in yerler:
        fiyatlar2.append(fiyatlar1[i])

    sonuc = list(zip(kurlarkisaltma, fiyatlar2))

    print("""

    1. Kısaltma ile kur sorgulama
    2. Kısaltmalar listesi
    3. Hepsini göster
    4. TL'den dövize çevirme
    5. Dövizden TL'ye çevirme""")

    while True:
        secim = input("\nİşlem seçiniz: \n")

        if (secim == "1"):
            istek = input("Fiyatını öğrenmek istediğiniz kurun kısaltmasını büyük harfler ile girin: ")
            istek += " "
            print("Veri yükleniyor...")
            time.sleep(1)
            for isim, kur in sonuc:
                if isim == istek:
                    print(isim, ":", kur)

        elif (secim == "2"):
            sonuckurlar = list(zip(kurlarkisaltma, kurlaruzun))
            print("Veri yükleniyor...")
            time.sleep(1)
            for kisa, uzun in sonuckurlar:
                print(kisa, ":", uzun)

        elif (secim == "3"):
            print("Veri yükleniyor...")
            time.sleep(1)
            for isim, kur in sonuc:
                print(isim, ":", kur)

        elif (secim == "4"):
            secilenkur = input("İşlem yapmak istediğiniz kurun kısaltmasını girin: ")
            secilenkur += " "
            tlmiktari = float(input("Elinizde ki TL miktarını girin: "))
            print("Hesaplanıyor...")
            time.sleep(1)
            for isim, kur in sonuc:
                if isim == secilenkur:
                    kur = kur.replace(",", ".")
                    kur = float(kur)
                    print("\nMiktar: ", tlmiktari / kur, "\n")

        elif (secim == "5"):
            secilenkur = input("İşlem yapmak istediğiniz kurun kısaltmasını girin: ")
            secilenkur += " "
            dovizmiktari = float(input("Elinizde ki döviz miktarını girin: "))
            print("Hesaplanıyor...")
            time.sleep(1)
            for isim, kur in sonuc:
                if isim == secilenkur:
                    kur = kur.replace(",", ".")
                    kur = float(kur)
                    print("\nMiktar: ", dovizmiktari * kur, "\n")

        elif (secim == "q"):
            break

        else:
            print("Yanlış bir tuşlama yaptınız...")

else:
    print("Bağlantı başarısız...")