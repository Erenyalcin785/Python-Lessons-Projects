import pandas as pd 
from numpy import sqrt
from numpy import log

veri=pd.DataFrame(pd.read_excel("C:/Users/MONSTER/Desktop/Hisse.xlsx"))
#print(veri[["Kod","Kapanış (TL)"]]) # istenilen sütünü çeker
#print(veri.loc[[0,2,5,150]]) # istenilen satırı çekme 
#print(veri.loc[0:5,"Kod":"Aylık Getiri (%)"])# ilk değer satırın indexi 2. değer sütunun ismini alır  kontrol eder kesişim varsa veriyi döndürür

#veri["Karakök Fiyat"] = sqrt (veri["Kapanış (TL)"]) # verinin sonuna yeni bir değeri sütün ekller
# print(veri)

veri.insert(2,column="Log Fiyat",value=(log(veri["Kapanış (TL)"])))
print(veri)