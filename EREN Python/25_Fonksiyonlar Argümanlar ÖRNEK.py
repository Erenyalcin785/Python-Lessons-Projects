# def ortlama(*args):
#     sonuc = 0
#     for i in args:
#         sonuc += i
#         sonuc2 = sonuc / len(args)
#         return round(sonuc2,3)
    

# print(ortlama(5,10,14))

def ortalama(*args,x):
    sonuc = 0
    for i in args:
        sonuc += i
        sonuc2 = sonuc / len(args)
    if sonuc2>x:
         print("{} sayısı ortalamadan küçüktür".format(x))
    else:
        print("{} sayısı ortalamadan büyüktürr".format(x))  

        return sonuc2

ortalama(3,5,5,10,20,30,x = 8)
