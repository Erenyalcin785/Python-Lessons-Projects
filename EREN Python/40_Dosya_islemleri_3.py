with open("Merhaba","r") as Dosya:
    Dosya.seek(5) #ilk 5 karakteri atlar
    Dosya.read(5) # atlandıktan sonra 5 karakteri okur
    print(Dosya.tell()) # kaçıncı sırada oldugumuzu söyler 