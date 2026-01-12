import matplotlib.pyplot as plt 
for i in plt.style.available:
    print(i)


plt.style.use("dark_background") ## tırnak içine çıkan tüm ifadeleri koyabilirsin.

x = ["2015","2016","2017","2018","2019","2020","2021"]
y = [102,84,58,156,251,356,121]
plt.plot(x,y)
plt.show()