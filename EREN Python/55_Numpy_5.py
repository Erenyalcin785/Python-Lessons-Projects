import numpy as np

x =np.array([8,6,2,4,5,2])
y =np.array([1,8,9,2,4,4])

print(np.add(x,y))
print(np.subtract(x,y))
print(np.divide(x,y))
print(np.multiply(x,y))

#print(x+y)
#print(x*y)

print(np.min(x))
print(np.max(x))
print(np.sqrt(x))
print(np.log(x))
print(np.sum(x))
print(np.mean(x)) #aritmatik ortalama
print(np.median(x)) # medyan
print(np.var(x)) # varyans
print(np.std(x)) # standart sapması
print(np.sqrt(np.var(x)))