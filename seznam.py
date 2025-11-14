#datové struktury "list"
promenna = [1, 2, 3, 4, 5] #vektor

print(promenna)

p2 = [1, "abc", 5.5, True, [1,2,"a"]]
print(p2)
print("********************")
print(type(p2))
print("********************")
print(p2[1][1])
print("********************")
print(type(p2[4][1]))
print("********************")
print(p2[1:3])
print("********************")
print(p2[2])
print("********************")
print(type(p2[2]))              #hodnota
print("********************")
print(type(p2[2:3]))            #list
x = [1, 2, 8, 4, 6, 11, 7, 4]

for i in range(len(x)):
    print(x[i])
print("********************")
for i in range(len(x)):
    if i % 2 == 0:
        print(x[i])

print("********************")

for i in range(0,len(x),2):
    print(i+1)

print("********************")
pole = [5, 2, 9, 1, 7, 3, 10, 6, 4]

maximalni_prvek = pole[0]
pozice_max_prvku = 0

for i in range(1,len(pole)):
    if maximalni_prvek < pole[i]:
       maximalni_prvek = pole[i]
       pozice_max_prvku = i

print(maximalni_prvek,"je maximální prvek a je na pozici",pozice_max_prvku)

print("********************")
pole = [5, 2, 9, 1, 7, 3, 10, 6, 4]

minimalni_prvek = pole[0]
pozice_min_prvku = 0

for i in range(1,len(pole)):
    if minimalni_prvek > pole[i]:
       minimalni_prvek = pole[i]
       pozice_min_prvku = i

print(minimalni_prvek,"je minimální prvek a je na pozici",pozice_min_prvku)
print("********************")
print("********************")
min_prvek = pole[0]
pozice_min_prvku1 = 0

for i in range(1,len(pole)):
    if min_prvek > pole[i]:
       min_prvek = pole[i]
       pozice_min_prvku1 = i

print(min_prvek,"je minimální prvek a je na pozici",pozice_min_prvku1)

print("********************")
pole = [5, 2, 9, 1, 7, 3, 10, 6, 4]

soucet = 0

for i in range(len(pole)):
    soucet = soucet + pole[i]
    #soucet += pole[i]

print(soucet/len(pole))
print("********************")
print("********************")
#kolik prvku v poli je větších než 5

pole = [5, 2, 9, 1, 7, 3, 10, 6, 4]

pocitadlo = 0
limit = 5

for i in range(len(pole)):
    if pole[i] > limit:
        pocitadlo += 1

print("počet čísel větších než 5 je " + str (pocitadlo))


#součet vsech prvku

pole = [5, 2, 9, 1, 7, 3, 10, 6, 4]

soucet = 0

for i in range(len(pole)):
    soucet = soucet + pole[i]
    #+=

print(soucet)

print("********************")
print("********************")
pole = [5, 2, 9, 1, 7, 3, 10, 6, 4]

nove_pole = []

for i in range(len(pole)-1,-1,-1):
    nove_pole.append(pole[i])

print(nove_pole)





