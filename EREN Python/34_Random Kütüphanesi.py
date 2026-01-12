import random

# x = random.random()
# y = random.uniform(0,100)
# z = random.randint(50,100)
# print(x)
# print(y)
# print(z)

# e = ["Ahmet","Mehmet","Ali"]
# r = random.choice(e)
# print(r)

liste = range(0,100)
p = random.sample(liste,10)
print(p)

i = 0 

for i in range(len(p)):
    value = p[i]

    if value < 50:
        print("Wow Unlucky! Your Number = {}".format(value))
    else:
        print("Wow Lucky! Your Number = {}".format(value))