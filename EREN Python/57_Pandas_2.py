import pandas as pd

#x = pd.Series(["a","b",1],[1,2,3])
#print(x[2])
#print(x[[2,3]])

#----------------------------------------------

#x = pd.Series([1,2,3,4,5])
#print(x.sum())
#print(x.mean())
#print(x.var())
#print(x.std())
#print(x.kurtosis())

#----------------------------------------------

zaman =[2015,2016,2017,2018,2019,2020,2021]
fiyat =[3000,4000,5000,6000,7000,8000,9000]

seri = pd.Series(fiyat,zaman)
print(seri.mean())
print(seri.count())
print(seri.describe())
