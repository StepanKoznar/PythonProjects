#string řetezec znaků

text = "ahoj"
text2 ='ahooj'
text3 = "Sean 0'Connery"
text4 = 'tak rekl:"to je"'
text5 = 'Sean 0\'Connery'
text6 = "cesta k souboru je c:\\hry\\soubor.txt"
text7 = "ahoj \n nazdar"

print(text)
print(text2)
print(text3)
print(text4)
print(text5)
print(text6)
print(text7)


a = "abc"
b = "def"


print(a+b)
print(a*3)

c = "a"
for i in range (5):
    c = c + "a"

print(c)


promenna = "Ahoj Karle, jak se máš?" #indexováni od 0

print(promenna[6])  #vypiše pismeno na 6 miste

print(len(promenna))
for i in range(len(promenna)):
    print(promenna[i])

    #len vrátí délku řetezce počet písmen
print(promenna[len(promenna)-1])

print(promenna[-1])

print(promenna[5:10])   #<5;10) , slicing

print(promenna[5:10:2]) #2 = skok

print(promenna[10:5:-2])    #<10;5) krok po 2

print(promenna[5:]) # od pátýho prvku až do konce

print(promenna[:5]) # od začátku do 5. prvku <0;5)

print(promenna[:5:-1])  #od posledního čísla až do 5., pozpátku

print(promenna[::-1])   #celý po zpátku

print(promenna.index(","))  #na kolikátým místě je znak v ""


