#Bu kısımda 4 uygulama programı yazalım bakalım Python'da ne kadar ilerlemişiz.
#1. Program: 4 işlem yapan hesap makinası
#2. Program: Kullanıcı ad, soyad, doğum tarihi, cinsiyet bilgilerini alıp dosyaya kaydeden program
#3. Program: Kullanıcı adı ve parola ile doğru giriş yapıldığında(dosyadan kontrol edilecek) 
            ##dosyadan kayıtlı kullanıcı bilgilerini çeken ekrana yazdıran program
#4. Program: Girilen ismin binary karşılığını dosyaya yazan ve 
            ##dosyadaki binary veriyi karakter dizisi(unicode - utf8) olarak okuyan program


#1. Program - Hesap makinası Let's begin :)
metin == """
(1) Toplama
(2) Çıkarma
(3) Çarpma
(4) Bölme
Seçiminizi yapınız
Çıkmak için (q) ya basınız
"""
#devam edecek :)
d ="Devam etmek için bir tuşa basınız"
while True:
    try:
        print(metin)
        sec = input("Yapmak İstediğiniz İşlemi Seçiniz: ")
        if sec == "1":
            sayi = int(input("Birinci Sayı: "))
            sayi2 = int(input("İkinci Sayı: "))
            sonuc = sayi + sayi2
            print("{} + {} = {}".format(sayi, sayi2, sonuc))
            input(d)
        elif sec == "2":
            sayi = int(input("Birinci Sayı: "))
            sayi2 = int(input("İkinci Sayı: "))
            sonuc = sayi - sayi2
            print("{} - {} = {}".format(sayi, sayi2, sonuc))
            input(d)
        elif sec == "3":
            sayi = int(input("Birinci Sayı: "))
            sayi2 = int(input("İkinci Sayı: "))
            sonuc = sayi * sayi2
            print("{} * {} = {}".format(sayi, sayi2, sonuc))
            input(d)
        elif sec == "4":
            try:
                sayi = int(input("Birinci Sayı: "))
                sayi2 = int(input("İkinci Sayı: "))
                sonuc = sayi / sayi2
                print("{} / {} = {}".format(sayi, sayi2, sonuc))
                input(d)
            except ZeroDivisionError:
                print("0'a bölünmez")
        elif sec == "Q":
            break
        elif sec == "q":
            break
        else:
            print("Lütfen Belirtilen Seçeneklerden Birini Seçiniz")
    except:
        print("Lütfen Rakam Giriniz")
#2.Program 
ad = input("Adınızı Girin: ")
soyad = input("Soyadınızı Girin: ")
dogum_tarihi = input("Doğum Tarihinizi Girin: ")
cinsiyet = input("Cinsiyetinizi Girin: ")

with open("deneme.txt","a+") as bilgiler:
    bilgiler.write("\nKullanıcı adı: {}".format(ad))
    bilgiler.write("\nKullanıcı Soyadı: {}".format(soyad))
    bilgiler.write("\nKullanıcı doğum tarihi: {}".format(dogum_tarihi))
    bilgiler.write("\nKullanıcı Cinsiyeti: {}".format(cinsiyet))


