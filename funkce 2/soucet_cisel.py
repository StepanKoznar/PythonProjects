def soucet(n):
    souc = 0
    for i in range(n+1):
        souc = souc + i
    return souc
print(soucet(6))
print("************")
def soucet1(n):
    if n <= 1:
        return 1
    else:
        return n + soucet1(n-1)
print(soucet1(6))

