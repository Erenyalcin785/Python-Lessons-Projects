import pandas as pd 
import numpy as np
#sayılar = pd.Series([0,1,2,3,4,5])
#ondalık = pd.Series([0.1,1.16,2.05])
#karakter = pd.Series(["merhaba","eren","nasılsın"])
#print (sayılar)
#print(ondalık)
#print(karakter)

#-------------------------------------------

#x ={"Armut":2000,
    #"Elma":3000,
    #"Çilek":4000} 

#y = pd.Series(x)
#print(y)

#-------------------------------------------

x =np.random.randint(1,500,50)
y = pd.Series(x)
print(y)