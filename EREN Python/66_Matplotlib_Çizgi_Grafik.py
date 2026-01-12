import matplotlib.pyplot as plt 
import numpy as np

#plt.figure()
#plt.axis()
#plt.title("Örnek Çizgi Grafik")
#plt.xlabel("Yıl")
#plt.ylabel("Fiyat")

#x =["2016","2017","2018","2019","2020","2021"]
#y = [100,200,300,150,250,350]
#z= y-np.mean(y)

#plt.plot(x,y)
#plt.plot(x,z)
#plt.show()

#----------------------------------------------

plt.title("Örnek Çizgi Grafik")
plt.xlabel("Yıl")
plt.ylabel("Fiyat")

yıl = ["2015","2016","2017","2018","2019","2020","2021"]
seri1 = [10,8,5,15,25,35,12]
seri2 =np.sqrt(seri1)

#plt.plot(yıl,seri1,color="green",marker="x",ms=10,mec="black",mfc="purple") #marker kırılıma işaret atar, #ms o işaretin boyutu #mec işaretin dış çizgi rengi , mfc ise kırılım noktasının iç rengi
#plt.plot(yıl,seri2,color="red",marker="o",ms=20,mec="blue",mfc="orange")

#--------------------------------

#plt.plot(yıl,seri1,color="green",linestyle="dotted") #linestyle içine 4 ifade var dotted(:),dashed(--),dashbot(-.),solid(-) solid orjinale dönderir
#plt.plot(yıl,seri2,color="red",linestyle="dashed")

#--------------------------------

plt.plot(yıl,seri1,"-r",label="Seri1") #kısaltarak renk ve çizgi türünü belirledik
plt.plot(yıl,seri2,"--b",label="Seri2")
plt.legend()#label görmek için yazdık içine giricegimiz sayı, yerini belirliyor grafikte 
plt.grid(axis="y",color="purple",linestyle="-.")#arka planı kareli yapıyor içine yazdıgımız ifade sadece x veya y kordinatına göre ızgara yapmamızı sağlıyor 

plt.show()