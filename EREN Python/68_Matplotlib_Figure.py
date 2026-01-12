import matplotlib.pyplot as plt 
import numpy as np

#fig= plt.figure()
#konum = fig.add_axes([0.1,0.1,0.8,0.6])#ilk parametre soldan boşluk 2. kısım sağdan boş diğerleride işte üstten alttan

#yıl =["2018","2019","2020","2021"]
#fiyat=[1500,2500,3500,4000]
#konum.plot(yıl,fiyat)
#konum.set_xlabel("Yıl")
#konum.set_ylabel("Fiyat")
#konum.set_title("Fiyat Grafiği")

#tamamen aynı ama set_ kullanmazsan hata alırsın çünkü figure bir obje.

#plt.show()

#-----------------------------------------------------

#x = np.linspace(-10,9,20)
#y = x**2
#z = x**3

#fig = plt.figure()
#grafik1= fig.add_axes([0.1,0.1,0.8,0.8])
#grafik1.plot(x,y,c="red")
#grafik1.set_xlabel("X Değerleri")
#grafik1.set_ylabel("Y Değerleri")
#grafik1.set_title("Örnek Grafik1")


#grafik2= fig.add_axes([0.3,0.6,0.2,0.2])
#grafik2.plot(x,z,c="b")
#grafik2.set_xlabel("X Değerleri")
#grafik2.set_ylabel("Y Değerleri")
#grafik2.set_title("Örnek Grafik2")

#plt.show()

#------------------------------------------------------

x = np.linspace(-10,9,20)
y = x**2
z = x**3

fig,grafik=plt.subplots(nrows=2,ncols=1)

grafik[0].plot(x,y,c="red")
grafik[0].set_title("1. Grafik")
grafik[1].plot(x,z,c="b")
grafik[1].set_title("2. Grafik")

plt.tight_layout()
plt.show()





