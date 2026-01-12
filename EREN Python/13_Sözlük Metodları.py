bilgi ={
        "ad":"Eren",
        "soyad":"Yalçın",
        "DYer":"Adana",
        "TCno":12345678900
}
print(bilgi.keys())
print(bilgi.values())
print(bilgi.items())
print(bilgi.get("ad"))

bilgi.update({"Cinsiyet":"Erkek"})
print(bilgi)
print(bilgi.__len__())

bilgi.pop("TCno")
print(bilgi)