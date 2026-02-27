from importlib.metadata import pass_none

import numpy as np

#for i in range(10):
    #cislo = np.random.randint(10,20) #<10;20)
    #rnd = np.random.random() #desetinný cislo
    #print(cislo)
    #print(rnd)
print("Game: Guess the number")
pocet_pokusu=0
nahodne_cislo = np.random.randint(1,21)
while True:
    while True:
        h_cislo = input("Hádej číslo od 1 do 20:")
        try:
            cislo= int(h_cislo)
            break
        except:
            print("není číslo")
    pocet_pokusu += 1
    if cislo > 0 and cislo < 21:
        if cislo == nahodne_cislo:
            break
        elif cislo > nahodne_cislo:
            print("Číslo je mensí")
            pass
        elif cislo < nahodne_cislo:
            print("Číslo je větší")
            pass
    else:
        print("zkus znovu číslo mimo interval")
print("")
print("Uhodnuté číslo je: " + str(nahodne_cislo))
print("počet pokusů:" + str(pocet_pokusu))



