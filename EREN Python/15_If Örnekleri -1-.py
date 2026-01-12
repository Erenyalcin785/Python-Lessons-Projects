# Kullanıcı_Adı = input("Lütfen Kullanıcı Adını Giriniz:")
# Kullanıcı_Sifre = input("Lütfen Şifrenizi Giriniz:")

# SistemKA = "Kirpi12"
# SistemSif = "erenoska12"

# if Kullanıcı_Adı == SistemKA and Kullanıcı_Sifre == SistemSif:
#     print("Merhaba {}, Hoşgeldin!".format(SistemKA))
# elif Kullanıcı_Adı != SistemKA and Kullanıcı_Sifre != SistemSif:
#     print("Kullanıcı adı ve şifre Hatalı")
# elif Kullanıcı_Adı != SistemKA:
#     print("Kullanıcı Adı Hatalı")
# elif Kullanıcı_Sifre != "erenoska12":
#     print("Merhaba {}, Kullanıcı Şifren Hatalı!".format(SistemKA))


# --------------------------------------------------

# print("Merhaba, Vücut Kitle Endeksi Hesaplama Uygulamasına Hoşgeldiniz!")

# Boy = int(input("Lütfen boyunuzu cm cinsinden giriniz:"))
# Kilo = int(input("Lütfen Kilonuzu Giriniz:"))

# Endeks = round(((Kilo)/ (Boy/100)**2),3)

# if Endeks <= 18.5:
#     print("Vücut Kitle Endeksiniz {}'dir. Düşük Kilolu Grubundasınız!".format(Endeks))
# elif Endeks > 18.5 and Endeks <= 24.9:
#     print("Vücut Kitle Endeksiniz {}'dir. Normal Kilolu Grubundasınız!".format(Endeks))
# elif Endeks > 25 and Endeks <= 29.9:
#     print("Vücut Kitle Endeksiniz {}'dir. Yüksek Kilolu Grubundasınız!".format(Endeks))
# elif Endeks > 30 and Endeks <= 40:
#     print("Vücut Kitle Endeksiniz {}'dir. Obez Grubundasınız!".format(Endeks))
# elif Endeks > 40:
#     print("Vücıt Kitle Endeksiniz {}'dir Aşırı Obez Grubundasınız".format(Endeks))

# --------------------------------------------------------


# İsim = str(input("Lütfen Adınızı Giriniz:"))
# Yas = int(input("Lütfen Yaşınızı Giriniz:"))
# Egitim = str(input("Lütfen Eğitim Durumunuzu Giriniz"))
# Egitim2 = ("İlkokul","Ortaokul","Lise","Üniversite")

# if Egitim not in Egitim2:
#     print("Lütfen Geçerli Bir Eğitim Durumu Giriniz!")
# elif Yas >= 18 and Egitim =="Lise"or Egitim == "Üniversite":
#     print("Merhaba {}!, Ehliyet Şartları Geçerli".format(İsim))
# else:
#     print("Merhaba {}!, Ehliyet Şartları Geçersiz".format(İsim))

# --------------------------------------------------------

# Sayi = int(input("Lütfen Bir Sayı Giriniz:"))
# Kontrol = Sayi > 0 and Sayi % 2 == 1

# if Kontrol == True:
#     print("Girdiginiz Sayi {}, Pozitif ve Tek Sayıdır!".format(Sayi))
# else:
#     print("Girdiginiz Sayi {}, Pozitif ve Tek Sayı Değildir!".format(Sayi))

# --------------------------------------------------------

print("""Hesap Makinasi Hoş Geldiniz!
      
[1] Toplama
[2] Çıkarma
[3] Çarpma
[4] Bölme
[5] Üs Alma
[Q] Çıkış    
""")

İslem = input("Lütfen Yapmak İstediğiniz İşlemi Seçiniz:")

if İslem == "1":
    sayı1 = float(input("Lütfen İlk Sayıyı Giriniz:"))
    sayı2 = float(input("Lütfen İkinci Sayıyı Giriniz:"))
    sayı3 = sayı1 + sayı2
    print("İşlem Sonucu = {}".format(sayı3))
elif İslem == "2":
    sayı1 = float(input("Lütfen İlk Sayıyı Giriniz:"))
    sayı2 = float(input("Lütfen İkinci Sayıyı Giriniz:"))
    sayı3 = sayı1 - sayı2
    print("İşlem Sonucu = {}".format(sayı3))
elif İslem == "3":
    sayı1 = float(input("Lütfen İlk Sayıyı Giriniz:"))
    sayı2 = float(input("Lütfen İkinci Sayıyı Giriniz:"))
    sayı3 = sayı1 * sayı2
    print("İşlem Sonucu = {}".format(sayı3))
elif İslem == "4":
    sayı1 = float(input("Lütfen İlk Sayıyı Giriniz:"))
    sayı2 = float(input("Lütfen İkinci Sayıyı Giriniz:"))
    sayı3 = sayı1 / sayı2
    print("İşlem Sonucu = {}".format(sayı3))
elif İslem == "5":
    sayı1 = float(input("Lütfen İlk Sayıyı Giriniz:"))
    sayı2 = float(input("Lütfen Kuvvet Derecesini Giriniz:"))
    sayı3 = sayı1 ** sayı2
    print("İşlem Sonucu = {}".format(sayı3))
elif İslem == "Q" or İslem == "q":
    print("Hoşçakalın...")