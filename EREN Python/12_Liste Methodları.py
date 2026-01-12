Liste = [1,2,5,"Merhaba",2.5]
Liste.append("Eren Yalçın")
print(Liste)
Liste.insert(3,"Eren Yalçın")
print(Liste)
Liste.remove(2)
print(Liste)
Liste.pop(3)
print(Liste)
liste2 = Liste.copy()
print(liste2)
Liste.extend(liste2)
print(Liste)
Liste += liste2
print(Liste)
print(Liste.count(1))


Liste3 = [1,3,5,7,3]
Liste3.sort(reverse=True)
print(Liste3)
Liste3.sort()
print(Liste3)
Liste3.reverse()
print(Liste3)
Liste3.clear()
print(Liste3)