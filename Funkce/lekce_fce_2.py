def secti(a, b):
    globalni_promena = 20
    vysledek = a+b+globalni_promena
    return [vysledek, globalni_promena]

def secti_tuple(a, b):
    globalni_promena = 20
    vysledek = a + b + globalni_promena
    return vysledek, globalni_promena
globalni_promena = 10
y = secti(5,3)
print(y)
print("**********")
print(type(y))
print(secti_tuple(5,3))
print(type(secti_tuple(5,3)))
