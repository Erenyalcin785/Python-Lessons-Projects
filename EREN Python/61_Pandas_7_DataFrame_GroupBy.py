import pandas as pd

veri = pd.DataFrame(pd.read_excel("C:/Users/MONSTER/Desktop/eczane.xlsx"))


#bolgeler = veri.groupby("BOLGE")   #tüm bölgeleri gruplara ayırır
#for i in bolgeler: 
 #print(i)

bolgeler = veri.groupby("BOLGE").get_group("KARŞIYAKA 2")
print(bolgeler)
