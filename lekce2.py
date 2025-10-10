print("hello")

odpoved = input("tohle se napiše do řádky:")

print(odpoved)
print(type(odpoved))

try:
    odpoved_jako_cislo = int(odpoved)
except:
    print("zadej číslo ne pismeno ******* nastavuju na 0")
    odpoved_jako_cislo = 0




print("ahoj " + "vole")
print(22 + odpoved_jako_cislo)
