text = "Studenti_kybernetiky_jsou_rádi,_když_mají_3_testy_v_jedne_hodině."
x = len(text)
y=0
while True:
    for i in range(5, 0, -1):
            print(text[y:i+y])
            y += i
    if y>x:
        break
