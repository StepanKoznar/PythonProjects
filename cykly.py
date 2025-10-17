for i in range(0,10): #i nazev, range (n) 0,1,2,3,n-1, i<0;n),  range (a,n)=interval, range (a,n,s) s=krok
    print(i/10)
    print("ahoj")

for i in range(0,11,2):
    print(i)
for i in range(6):
    print(i*2)

for i in range(0,11):
    if i%2==0:
        print(i)

for i in range(5):
    for j in range(5):
        print(str(i) + "," + str(j))
#****************************************************************************************#
a = 0

while a == 0:
    x = input("napis cislo:")
    try:
        a = int(x)
    except:
        a = 0

print (a)

#****************************************************************************************#
for i in range(10):
    print(i)
    if i > 5:
        break # comninue = ukonci smycku, break = okamzite okuncuje for-cyklus
    print("ahoj")

#****************************************************************************************#

while True:
    x = input("napis cislo:")
    try:
        a = int(x)
        break
    except:
        pass
print(a)

#****************************************************************************************#

