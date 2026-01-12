print(abs(-5))
print(round(22/7,3))

x = [5<6,6<7,7<8] # hepsi doğru oldugunda yalnızca 1 tane true döndürür
print(all(x))

y = [5<6,10<7,9<8] # 1 tane doğru olması yeterli 
print(any(y))

print(bool("Ahmet")) 

print(chr(30))

z=list()
z.append("Eren")
print(z)

e = "Eren Yalçın"
print(list(e))
print(e)

u = "Eren Yalçın"
l = set(u)
print(l)