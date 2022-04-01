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
  
