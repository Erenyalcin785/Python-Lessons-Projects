from datetime import*
import time


# x = datetime.today()
# print(x)


# y = datetime.now()
# z= datetime.ctime(y)
# print(y)
# print(z)


# dogumgunu = datetime(1976,12,16)
# bugun = datetime.today()
# fark = bugun - dogumgunu
# print(fark.days)

 
# bugun = datetime.today()
# fark = timedelta(days= 225)
# gelecek = bugun + fark
# print(gelecek)


while True:
    zaman = time.strftime("%H: %M: %S")
    print(zaman)
    time.sleep(3)