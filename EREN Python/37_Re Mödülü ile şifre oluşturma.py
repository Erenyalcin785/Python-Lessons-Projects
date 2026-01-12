import re

dogumtarihi ="2001"
karakter = ["\?","\*","\!","\."]

def sifrekontrol(sifre):
    if len(sifre) <8:
        raise Exception("Şifreniz En Az 8 karakterden Oluşmalı")
    elif not re.search("[a-z]",sifre):
         raise Exception("Şifreniz En Az Bir Küçük Harf içermelidir")
    elif not re.search("[A-Z]",sifre):
         raise Exception("Şifreniz En Az Bir büyük Harf içermelidir")
    elif not re.search("[0-9]",sifre):
         raise Exception("Şifreniz En Az Bir Tane Rakam içermelidir")
    elif not re.search(str(karakter),sifre):
         raise Exception("Şifreniz En Az Bir Karakter ('?' , '\' , '!', '.')içermelidir")
    elif sifre.startswith(dogumtarihi)==True:
         raise Exception("Şifreniz Dogum Tarihiniz ile Bağlayamaz ")
    elif sifre.endswith(dogumtarihi)== True:
         raise Exception("Şifreniz Dogum Tarihinizle Bitemez ")
    else:
         print("Şifreniz Oluşturulmuştur")


while True:
     
    try:
        sifre = input("Lütfen Şifre Oluşturunuz")
        sifrekontrol(sifre)
        break
    except Exception as hata:
         print(hata)
    
          
    