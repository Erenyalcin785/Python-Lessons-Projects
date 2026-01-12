class İnsan():
    def __init__(self,ad,soyad,sacrengi,boy,kilo):
        self.ad = ad
        self.soyad = soyad
        self.sacrengi = sacrengi
        self.boy = boy
        self.kilo = kilo

class Ogrenci(İnsan):
    def __init__(self, ad, soyad, sacrengi, boy, kilo, bolum, yas):
        super().__init__(ad, soyad, sacrengi, boy, kilo)
        self.bolum = bolum
        self.yas = yas

insan1 = İnsan("Eren", "Yalçın"," Siyah",183,85)
Ogrenci1 = Ogrenci("Ali","Kemal","Sarı",190,100,"Fen",19)

print(insan1.kilo)
print(Ogrenci1.bolum)