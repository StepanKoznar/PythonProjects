def odpocet(n):
    if n == 0:
        return "BOOM"
    else:
        print("Odpocet T-" +str(n))
        return odpocet(n-1)
print(odpocet(7))