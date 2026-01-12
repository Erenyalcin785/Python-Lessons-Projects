
# def toplam(*x):
#     return x

# print(toplam(1,5))

# def toplam(*x):

#     sayac = 0
#     for i in x:
#         sayac += i
    
#     return sayac

#  print(toplam(1,3,6,5))

#---------------------

# def isim(*x):
#      return "merhaba,benim adım {}".format(x[0],)

# print(isim("Eren"))

#---------------------

# def kalori(**meyve):   
#     return meyve

# print(kalori(elma=45,armut=50))

#---------------------

def kimlik(**bilgi):
    for i in bilgi.values():
        print(i)


kimlik(Ad ="Ahmet",Soyad="Can",Yas = 25)










