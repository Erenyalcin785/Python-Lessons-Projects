# x = 5
# if x == 5:
#     print("Evet")
# else:
#     print("Hayır")
# ---------------------------------------
# Kullanıcı_adı ="Eren Yalçın"
# Kullanıcı_şifre ="1234567"

# if Kullanıcı_adı == "Eren Yalçın" and Kullanıcı_şifre =="1234567":
#     print("Doğru")
# else:
#     print("Yanlış")


Kullanıcı_adı = "Eren Yalçın"
Kullanıcı_şifre = "12345678"

if Kullanıcı_adı =="Eren Yalçın" and Kullanıcı_şifre =="12345678":
    print("Giriş Başarılı")
elif Kullanıcı_adı != "Eren Yalçın" and Kullanıcı_şifre != "12345678":
    print("Kullanıcı Adı ve şifresi hatalı")
elif Kullanıcı_adı != "Eren Yalçın":
    print ("Kullanıcı Adı Hatalı")
else: 
    print("Kullanıcı Şifre Hatalı")
 