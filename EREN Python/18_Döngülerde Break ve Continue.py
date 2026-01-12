# x = "Eren Yalçın"
# for i in x:
#    if i == " ":
#       break
#    print(i)

# for i in x:
#     if i == " ":
#       continue
#     print(i)

sayac = 2
for i in range(0,3):

    kullanıcı_adı =input("Kullanıcı Adı:")
    kullanıcı_şifre =input("Şifre:")

    sistemka = "eren"
    sistemsif = "123"

    if kullanıcı_adı == sistemka and kullanıcı_şifre == sistemsif:
        print("Giriş Başarılı, Hoşgeldiniz!")
        break

    elif (kullanıcı_adı != sistemka or kullanıcı_şifre != sistemsif) and sayac != 0:
        print("Hatalı Giriş Lütfen Tekrar Deneyiniz. Kalan Hakkınız {}".format(sayac))
        sayac -= 1
    else:
        print("Kalan Kullanımm Hakkınız {} Kapatılıyor...".format(sayac))
