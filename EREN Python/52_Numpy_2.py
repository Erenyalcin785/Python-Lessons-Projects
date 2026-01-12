import numpy as np

sıfır = np.zeros((5,5),dtype=int)
bir = np.ones((3,4),dtype=int)
on = np.ones((3,4),dtype=int)*10
print(sıfır)
print(bir)
print(on)

a = np.full((5,5),20,dtype=int)
print(a)

b= np.eye(3) #birim matris
print(b)

c = np.diag([1,2,3]) #dioganal matris
print(c)

d = np.arange(0,100,5) #0-100 5 er artarak listeleme 
print(d)

e = np.linspace(0,100,5) #0-100 kaç elemanlı olsun 
print(e)

t =np.random.rand(3,4)
print(t)

p =np.random.randint(0,10,size=(3,4))
print(p)

l = np.random.randn(2,4)
print(l)