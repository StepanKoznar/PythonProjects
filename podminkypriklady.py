vstup = input("zadej cislo")
try:
    cislo = int(vstup)
except:
    cislo = 0

print("vstup = " + vstup)

if cislo < 10:
    print("cislo je mensi nez 10")
elif 10 < cislo <20:
    print("cislo je vetsi nez 10 a mensi nez 20")
else:
    print("cislo je vetsi nez 20")

if cislo > 10:
    print("cislo je vesti nez 10")
if cislo%2 == 0 :
    print("cislo je sude")
else:
    print("cislo je liche")
if 10 < cislo < 20:
    print("cislo je vetsi nez 10, ale mensi nez 20")
