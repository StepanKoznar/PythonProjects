import numpy as np

#for i in range(10):
    #cislo = np.random.randint(10,20) #<10;20)
    #rnd = np.random.random() #desetinný cislo
    #print(cislo)
    #print(rnd)

cislo_1 = input("hadej cislo: ")
cislo = np.random.randint(10,21) #<10;20)
while True:
    cislo = input("hadej cislo: ")
    try: cislo_1 = int("hadej_cislo")

    except:print("neni číslo")


    if cislo == cislo_1:
        print("spravne")
    else:
        print("hádej znovu")
