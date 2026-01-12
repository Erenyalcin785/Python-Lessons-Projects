import matplotlib.pyplot as plt 
import numpy as np

cs = [1.75,1.5,0.5,3,3.25,2]
puan =[17,15,7,19,20,16]

plt.title("Not Dağılım Grafiği")
plt.xlabel("Saat")
plt.ylabel("Puan")
plt.axis([0,4,0,21])
renkler = np.random.randint(0,100,6)

#plt.scatter(cs,puan,s=300,c="r",marker="o",edgecolors="blue",alpha=0.5)
#s= nokta boyutu c= rengi ayarlar marker= şekli ayarlar edgecolors=dış çizgi rengi alpha= saydamlık ayarı

renkler = np.random.randint(0,100,6)
plt.scatter(cs,puan,s=100,c=renkler,cmap="Reds") # cmap ton belirler bu satırla rastgele kırmızının tonları seçiliyor 
plt.colorbar()#renk barı ekler
plt.show()