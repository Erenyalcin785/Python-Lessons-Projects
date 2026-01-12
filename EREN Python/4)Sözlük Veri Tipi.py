Kimlik = {"İsim":"Ahmet",
          "Soyisim":"Taner",
          "Yas":41,
          "D_Yeri":"Ankara"}
print(Kimlik)

print(Kimlik["İsim"])
print(Kimlik["Yas"])

Kimlik["İsim"] ="Mehmet"

print(Kimlik["İsim"])

Kimlik["TC_no"] = 12345678900
print(Kimlik)

Kullanıcılar = {"Ahmetcan":{

    "tc_no":12345678900,
    "Do_yeri":"Ankara",
    "Yaş": 29
},
      "Arzu" :{
    "tc_no":1235685715,
    "Do_yeri":"İstanbul",
    "Yaş": 25
}         
}

print(Kullanıcılar["Arzu"])