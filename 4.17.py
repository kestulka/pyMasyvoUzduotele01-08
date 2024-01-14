# sugeneruokite atsitiktini dvimati masyva A[n][m], kuriame n ir m yra atsitiktiniai skaiciai is intervalo [10, 30].
# masyvo elementai yra atsitiktiniai skaiciai is intervalo [-100; 100].
# Issaugokite si masyva txt faile. Apskaiciuokite dvimacio masyvo kiekvienos eilutes aritmetini vidurki
# ji issaugokite masyve B[m]

import random
import os # extra funkcijai

# extra funkcija istrinti byla

def istrintiRez(failas):
    if os.path.exists(failas):
        os.remove(failas)
        print(f"Failas '{failas}' buvo istrintas")
    else:
        print(f" '{failas}' nebuvo rastas.")

# funkcija istrina sena byla, todel paleidus koda kiekviena karta gauname unikalu masyva
istrintiRez("rez1.txt")


# masyvo kurimas
def gautiDvimatiMasyva():

    n = random.randint(10, 30)
    m = random.randint(10, 30)
    dviMas= []

    for i in range(n):
        eil = []
        for j in range(m):
            eil.append(random.randint(-100, 100))
        dviMas.append(eil)
    return dviMas

# prasitestuoti
# dvimatisMasyvas = gautiDvimatiMasyva()
# print("dvimatis masyvas: ")
# for eilute in dvimatisMasyvas:
#     print(eilute)

# rezultatu irasymas
def rezultatas(masyvas, failas):
    with open(failas, "w") as f:
        for eilute in masyvas:
            t = str(eilute)
            txt = t[1:-1].replace(', ', '\t')
            f.write(f'{txt}\n')

# vidurkio skaiciavimas
def vidurkis(dvimatisMasyvas):
    return [sum(eilute) / len(eilute) for eilute in dvimatisMasyvas]

# sukuriam dvimati masyva ir issaugom
dvimatisMasyvas = gautiDvimatiMasyva()
rezultatas(dvimatisMasyvas, "rez1.txt")

# apskaiciuojam vidurki ir priskiriam ji naujam masyvui
masyvasB = vidurkis(dvimatisMasyvas)

# isvedam
print("\nAritmetiniai vidurkiai: masyve B:")
print(masyvasB)




