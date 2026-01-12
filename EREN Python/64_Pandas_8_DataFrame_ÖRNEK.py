import pandas as pd
import numpy as np

veri = pd.DataFrame(pd.read_excel("C:/Users/MONSTER/Desktop/Araclar.xlsx"))

#print(round(veri["Model Yıl"].mean()))

#print(veri[veri["Km"].min()==veri["Km"]])

#print(veri.sort_values("Fiyat"))

#arac = veri.groupby(["Marka",]).get_group("Acura")
#1print(arac)

#print(veri.groupby("Marka")["Fiyat"].mean().sort_values)


#print(veri.groupby("Marka", as_index=False)["Fiyat"].mean().sort_values("Fiyat"))

#print(veri.groupby("Marka")[["Fiyat"]].mean().sort_values("Fiyat")) ##++++++ en iyisi 

seat = veri.groupby("Marka").get_group("Seat")
print(seat)
print(seat.groupby("Arac Tip Grubu")["Fiyat"].mean())
print(seat.groupby("Arac Tip Grubu")[["Fiyat","Model Yıl"]].mean())




