vstup = input("zadej cislo")
try:
    cislo = int(vstup)
except:
    cislo = 0

print("vstup = " + vstup)

if cislo > 5:
    print("cislo")
    print(cislo)
    print("je")
    print("vetsi nez 5")
    if cislo > 10:
        print("nevim")
else:
    print("neni vetsi nez 5")
if cislo < 7:
    print("ale cislo je mensi nez 7")
print("konec")

a = int(input("zadej A"))
b = int(input("zadej B"))
c = int(input("zadej C"))

d = b**2 - 4*a*c
if d > 0:
    print("dve reseni v R.")

elif d == 0:
    print("jedno reseni v R.")

else:
    print("nula reseni v R.")


print("nula reseni v R.")
print("jedno reseni v R.")
print("dve reseni v R.")
