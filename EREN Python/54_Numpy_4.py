import numpy as np

#x =np.arange(11)
#print(x)
#y =np.delete(x,[3,6])
#print(y)

#--------------------------------------

#x = np.arange(16).reshape(4,4)
#y = np.delete(x,[1],axis=1)
#print(x)
#print(y)

#------------------------------------

#x = np.arange(16)
#y= np.append(x,100)

#print(x)
#print(y)

#--------------------------------------

#x = np.arange(9).reshape(3,3)
#y = np.append(x,[[100,200,300]],axis=0)

#print(x)
#print(y)

#---------------------------------------

x =np.array([8,6,4,9,8])
y=np.array([1,2,4,5,6])

print(np.setdiff1d(x,y))
print(np.union1d(x,y))
print(np.in1d(x,y))
print(np.unique(x))
print(np.sort(x))