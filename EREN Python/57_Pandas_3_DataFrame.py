import pandas as pd

#seri1 = [1,3,5,7,9]
#seri2 = [0,2,4,6,8]

#baslıklıveri = dict(ürün1 = seri1,ürün2 = seri2)
#veriler = pd.DataFrame(baslıklıveri)
#print(veriler)

#------------------------------------------------------------

#veri = [["Elma",10],["Armut",15]]
#baslık = ["ürün","Fiyat"]
#satırno = [1,2]
#df = pd.DataFrame(veri,columns=baslık,index=satırno)
#print(df)

#------------------------------------------------------------

sözlük= {"Ürün":["Elma","Armut","Çilek"],"Fiyat":[10,15,20]}
veri = pd.DataFrame(sözlük)
print(veri)