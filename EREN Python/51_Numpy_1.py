import numpy as np

dizi = np.array([1,2,3,4,5,6,7,8])
dizi2 =np.array([[1,2],[3,4],[5,6],[7,8]])
dizi3= dizi.reshape(2,4)

print(dizi)
print(dizi2)
print(dizi2.shape)
print(dizi3)
print("-----------------------------")

dizi4 = np.array([1,2,3,4,5],dtype=int)
dizi5 = np.array([1,2,3.5,4.1,5],dtype=float)
dizi6 = np.array([1,2,3,4,5],dtype=bool)

print(dizi4)
print(dizi5)
print(dizi6)