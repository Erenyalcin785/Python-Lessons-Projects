print(dir(list))                                     #dir
print(divmod(10,6))
print("-------------")
x = "Eren Yalçın"
t = 0
for i in enumerate(x):                              #enumerate
    print(i)
print("---------------")
y = "eren"
z = ["EREN"]                                        #len
print(len(y))
print(len(z))
print("---------------")

e = [1,2,3,5,4]                                     #max
print(max(e))
print("--------------")

h = ["A","AB","ABC"]                                #max with key
print(max(h,key = len))
print("-------")

print(round(pow(2,3.215)))                           #round
print("----------")

print("ankara","istanbul","adana",sep="___")         #sep=
print("----------")

print(list(range(0,101,5)))                          #range
print("----------")

o = ["a","b","c",12]                                 #reversed 
print(list(reversed(o)))    


p = [1,2,3,4]
d = ["a","b","c","d"]
print(*zip(p,d))