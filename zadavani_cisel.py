cislo_jako_text = input("Zadej cislo: ")


try:
    cislo = int(cislo_jako_text)
except:
    cislo = 0



while True:
    cislo_jako_text = input("Zadej cislo: ")
    try:
        cislo = int(cislo_jako_text)
        break
    except:pass

print ("zadané číslo + 10 = " + str(cislo+10))