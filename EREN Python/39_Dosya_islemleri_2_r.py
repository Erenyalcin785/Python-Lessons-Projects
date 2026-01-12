# dosya = open("Merhaba","r")


# for i in dosya:
#     print(i)

# dosya.close()

#_________________________________________________

# dosya = open("Merhaba","r")

# print(dosya.readline())
# print(dosya.readline())
# print(dosya.readline())


# dosya.close()

#_________________________________________________


dosya = open("Merhaba","r")

liste = dosya.readlines()
print(liste[2])

dosya.close()