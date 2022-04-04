#második verzió
#első verzió
f=open("naplo.txt")
adatok=f.read().split("\n")
f.close()


naplo=[]
honap=0
nap=0
for e in adatok:
    if e[0]=="#":
        # 01 15
        honap=e[2:4]
        nap=e[5:]
        #print(honap)
    else:
        temp=[]
        temp.append(honap)
        temp.append(nap)
        #név + hiányzás berakása
        vag=e.split(" ")
        temp.append(" ".join(vag[0:2]))
        temp.append(vag[2])
        naplo.append(temp)

print("2. feladat\nA naplóban " + str(len(naplo)) + " hiányzás van.")

igazolt=0
igazolatlan=0
for e in naplo:
    igazolt+=e[3].count("X")
    igazolatlan+=e[3].count("I")


igazolt=sum([e[3].count("X") for e in naplo])

print("3. feladat\nAz igazolt hiányzások száma " + str(igazolt) + ", az igazolatlanoké " + str(igazolatlan)+" óra.")





  
