# e = True
while True:
    try:
        
        x = int(input("1.Sayı"))    
        y = int(input("2.sayı"))
        # if y == 0:
        #     print("Sıfıra bölemezsiniz!")
        #     continue
        print(x / y)
        # e = False   # doğru giriş yapıldı, döngü bitecek
        # break --- burda break yazabilirsin ama videoda else olayını öğrendin ve gerek yokmuş else yazıp içine break koyarsan işlemde hata yoksa döngüden çıkıyor 

    except ZeroDivisionError:
        print("Sıfıra bölemezsiniz!")
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz!")
    else:
        break


