x = " eren1Yalçın "
y=x.islower()
print(y)
y = x.lower()
print(y)
y = x.isupper()
print(y)
y = x.isnumeric()
print(y)
y=x.isalnum()
print(y)
y = x.capitalize()
print(y)
y = x.title()
print(y)
y = x.swapcase()
print(y)
y = x.count("e")
print(y)
y =x .strip(" ")
print(y)
z = "Abdullah, Eren Yalçın"
e = z.split(" ")
print(e)
e =" / ".join(e)
print(e)
e = z.find("Eren")
print(e)
e = z.replace("Eren","Ahmet")
print(e)

Adı = "Eros"
Soyadı = "Izem"
Görevi = "Öğrenci"

Bilgileri = [Adı,Soyadı,Görevi]

print("kişnin adı:{},Kişinin Soyadı:{}, Kişinin Görevi:{}".format(Bilgileri[0],Bilgileri[1],Bilgileri[2]))