def kvadraticka(a, b, c):
    diskriminant = b**2-4*a*c
    odm_diskriminant = diskriminant **0.5
    if diskriminant > 0:
        x1 = (-b + odm_diskriminant) / (2 * a)
        x2 = (-b - odm_diskriminant) / (2 * a)
        return [x1 , x2]
    elif diskriminant == 0:
        x3 = (-b-odm_diskriminant) /(2*a)
        return [x3]
    else:
        x4 = str("nemá řešení v realných číslech")
        return [x4]



#print(kvadraticka(1,2,1))
#print(kvadraticka(1,3,1))
#print(kvadraticka(1,1,1))
print("******************")
def kvadratic_test():
    results=[]
    for i in range(5):
        results.append(kvadraticka(1,i,1))
    return results
vysledky = kvadratic_test()
for vysledek in vysledky:
    print(vysledek)
    #print(type(vysledek))



