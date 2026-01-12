import pandas as pd

veri = pd.DataFrame(pd.read_excel("C:/Users/MONSTER/Desktop/Hisse.xlsx"))
#print(veri.head(3)) #baştan ilk 3 veriyi getirir
#print(veri.tail(3)) #sondan ilk 3 veriyi getirir
#print(veri["Kapanış (TL)"].head(3)) # istenilen sütünda istenilen kadarı getirme 
#print(veri[["Kod","Kapanış (TL)"]].head(3)) # istenilen sütünların istenilen kadarını getirme 
#print(veri[5:][["Kod","Kapanış (TL)"]].head(3)) #5. indexten başlayıp yapıcak

#print(veri[veri["Günlük Getiri (%)"]>2]) #Günlük getirisi 2 den büyük olanları yazdırıyor 

filtre = veri[(veri["Günlük Getiri (%)"]>2) &(veri["Haftalık Getiri (%)"]<1)] # iki sütün için filreleleme 
print(filtre)