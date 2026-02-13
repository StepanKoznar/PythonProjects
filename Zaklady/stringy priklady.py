promenna = "Ahoj Karle, jak se máš?"

for i in range(len(promenna)):
    print(promenna[i])           #vypiše po posmenech popredu
print("********************")
for i in range(len(promenna)):
    print(promenna[-i-1])        #vypiše po posmenech pozpatku
print("********************")
for i in range(len(promenna)):
    print(promenna[:i+1])        # vypise pyramidu znaku
print("********************")
for i in range(len(promenna)-1):
    print(promenna[i:i+2])
print("********************")
for i in range(len(promenna)-2):
    print(promenna[i:i+3])       #vypise vedle sebe pocet pismen
print("********************")
for i in range(int(len(promenna)/2)+1):
    print(promenna[i],promenna[-i-1])
print("********************")


a = " fwafsawfaw "

print(a.strip())                #maže mezery

print("********************")

a = "5"

print(a.zfill(5))               #vyplní nuly

print("********************")
