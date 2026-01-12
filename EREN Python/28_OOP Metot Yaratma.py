class İnsan:
    def __init__(self,Ad,Soyad,Dogumyıl):
        self.Ad = Ad
        self.Soyad = Soyad
        self.Dogumyıl = Dogumyıl

    def bilgi(self):
        print("Merhaba Benim Adım {}, Soyadım {}. {} Yılında Doğdum.".format(self.Ad,self.Soyad,self.Dogumyıl))
    
    def yas(self):
        
        return 2025 - self.Dogumyıl

İnsan1 = İnsan("Ahmet","Can",1998)
İnsan2 = İnsan("Selim","Mert",1988)    

İnsan1.bilgi()
İnsan2.bilgi()

print(İnsan1.yas())
print(İnsan2.yas())