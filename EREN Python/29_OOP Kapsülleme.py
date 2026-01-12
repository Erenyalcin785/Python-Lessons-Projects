class Memur:
    def __init__(self,Ad,Soyad,Maas):
        self.Ad= Ad
        self.Soyad = Soyad
        self.__Maas = Maas
        self.__Zam = 0.20
   
    def zamoranı(self):
      self.__Maas  = self.__Maas+ self.__Maas*self.__Zam
     
    
    def getMaas(self):
       return self.__Maas
    def getZam(self):
       return self.__Zam
    
    def setZam(self,YeniOran):
       self.__Zam = YeniOran


memur1= Memur("Eren","Yalçın",10000)
memur1.setZam(0.50)
memur1.zamoranı()
print(memur1.getMaas())


# print(memur1.Ad)
# print(memur1.getMaas())
# print(memur1.getZam())
