def kontrol(x):
    if len(x) <5:
        raise Exception("Şifreniz en az 5 karakterden oluşmalıdır")
    else:
        print("Şifreniz Oluşturulmuştur")

x = input("Lütfen Şifre Belirleyiniz...")

try:
 kontrol(x)
except Exception as hata:
   print(hata)
