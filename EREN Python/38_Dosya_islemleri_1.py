
# w aynı isimde dosya varsa o dosyayı siler ve yeni dosya oluşturur
# a ile dosyayı silmez ekleme yapar
# x ise aynı isimde dosya varsa hata verir w gibi silip yeni oluşturmaz

#dosya = open("Merhaba","w")
# f5 ile değil sağ üstteki run ile run et kodu ayrıca desktop almayı unutma cd .. ile alabilirsin yada tekrar klasöre dönmek istiyorsan cd (klasör ismi)  

#dosya = open("C:/Users\MONSTER/Desktop/Merhaba","x") 

dosya = open("C:/Users\MONSTER/Desktop/Merhaba","a") 
# direkt f5 ile çalıştırabilirsin slashlar değişti unutma 


dosya.write("\nMerhaba Ben Eren")


dosya.close()                                 