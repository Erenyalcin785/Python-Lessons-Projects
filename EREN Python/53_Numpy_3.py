import numpy as np

x =np.array([1,2,3,4,5,6,7,8,9,10])
print(x[0])
print(x[:3])

for i in x:
    print(i)


y = np.array([[1,2],[3,4],[5,6],[7,8],[9,10]])
for i in y:
    print(i)
    

print(y[ :,0])
print(y[ :,1])