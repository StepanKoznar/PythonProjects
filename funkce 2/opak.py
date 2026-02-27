
def max_2(s):
    maxi = 0
    max2 = 0
    for i in range (len(s)):
        if s[i] > maxi:
            max2 = maxi
            maxi = s[i]
        if s[i] > max2 and s[i]<maxi:
            max2 = s[i]
    return max2

seznam = [1,545,40,7405,1,11,19,1,215,141,2474,25,12,41,5,5,5674,4154,5674,45,4,865]
print("2.maximální je: " + str(max_2(seznam)))
print("maximální je: " + str(max(seznam)))

x = 8
for i in range (x):
    print((x-i)*" "+ i*"/" + i*"\\" +(x-i)*" ")
for i in range (round(x/4)):
    print((x-1)*" "+"||"+ (x-1)*" ")

def prvocislo (l):
    for i in range (2,l):
        if l%(i) == 0:
            return False
        else: pass
    return True

print(prvocislo(4))

def prvocisl (l):
    for i in range (l-2):
        if l%(i+2) == 0:
            return False
        else: pass
    return True
print(prvocisl(4))

