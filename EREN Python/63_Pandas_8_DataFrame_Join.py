import pandas as pd 

seri1 = pd.DataFrame({
    "Sehir":["Ankara","İstanbul","İzmir","Adana"],
    "Sıcaklık":[15,20,30,35]
})

seri2 = pd.DataFrame({
    "Sehir":["Ankara","İstanbul","İzmir","Mersin"],
    "Havadurumu":["Yağmurlu","Bulutlu","Açık","Kapalı"]
})

sonuc = pd.merge(seri1,seri2,on="Sehir",how="outer")
print(sonuc)