import random
def hod_k6():
    """Simuluje hod kostkou """
    return(random.randint(1,6))
print(hod_k6())
"""Simuluje hod kostkou """
def pocet_pokusu():
    p = 0
    while True:
        x = hod_k6()
        p+=1
        if x==6:
            break
    return(p)
print(pocet_pokusu())

#def simulace_pokusu(n):
    #pole = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #while n != 0:
        #f = pocet_pokusu()
        #if f <= n:
            #pole[f-1] += 1
            #n -= 1

    #return pole

#print(simulace_pokusu(1000))

def simulace_pokusu1(n):
    pole_vysledku = [0]*20
    for i in range(n):
        attempt = pocet_pokusu()
        if attempt > 20:
            attempt = 20
        pole_vysledku[attempt-1] +=1

    return pole_vysledku

random.seed(5)
print(simulace_pokusu1(10000))
