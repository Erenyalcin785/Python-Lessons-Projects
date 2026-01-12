
#-------------------------SINIF YARATMA--------------------------------
#class Insan:
#     Ad ="Eren"
#     Soyad = "Yalçın"
#     Yas = 24
#     Sacrengi = "Siyah"

# print(Insan.Ad)
# print(Insan.Sacrengi)
#----------------------------------------------------------------------

class Insan:
    def __init__(self,Ad,Soyad,Yas,Sacrengi):

        self.Ad = Ad
        self.Soyad = Soyad
        self.Yas = Yas
        self.Sacrengi = Sacrengi

Insan1 = Insan("Eren", "Yalçın", 24, "Siyah")
Insan2 = Insan("Mina","Aysel",25,"Sarı")

print(Insan1.Ad)
print(Insan2.Ad)


