import matplotlib.pyplot as plt 



#seri1 = [1,2,3,4,5]
#seri2 = [6,7,8,9,10]
#plt.plot(seri1,seri2) # ilk değer x ikinci değer y kordinatını verir
#plt.show()


Yıl = [2015,2016,2017,2018,2019,2020,2021]
fiyat = [100,200,300,400,500,600,700]
plt.plot(Yıl,fiyat,color ="red",linewidth=2)
plt.axis([2015,2025,0,1000])
plt.title("2015-2021 FİYAT")
plt.xlabel("Yıl")
plt.ylabel("Fiyat")
plt.show()

