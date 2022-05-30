f=open("naplo.txt")

naplo=[]
naplo2={}
honap=0
nap=0

temp=[]
datum=""
for e in f:
    if e[0]=="#":
        if datum!="":
            naplo2[datum]=temp
        honap=e.split(" ")[1]
        nap=e.strip().split(" ")[2]
        datum=e.strip().replace("# ","")
        temp=[]
    else:
        naplo.append(honap+" "+nap + " "+e.strip())
        temp.append(e.strip())

if datum!="":
    naplo2[datum]=temp

print(naplo)
print(naplo2.keys())

f.close()

print("2. feladat")
print("A naplóban " + str(len(naplo))+ " bejegyzés van.")
print("A naplóban " + str(sum(len(e) for e in naplo2.values()))+ " bejegyzés van.")

print("3. feladat")
hIgazolt=sum(e[-7:].count("X") for e in naplo)
hIgazolatlan=sum(e[-7:].count("I") for e in naplo)
print(hIgazolt)
print(hIgazolatlan)

#darab=[e[-7:] for e in naplo]
#print(darab)
#print("q w e XXXXXXX"[-7:-1])

def hetnapja(honap,nap):
    napnev=("vasárnap", "hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat")
    napszam=(0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335)
    napsorszam= (napszam[honap-1]+nap) % 7
    return napnev[napsorszam]

print("5. feladat")
honap=int(input("Hónap: "))
nap=int(input("Nap: "))

print(hetnapja(honap,nap))

print("6. feladat")
nap=input("Hét napja: ")
ora=int(input("óra: "))

darab=sum(e[-7+ora:-6+ora].count("I")+e[-7+ora:-6+ora].count("X") \
            for e in naplo \
            if hetnapja(int(e[:2]),int(e[3:4]))==nap)
print(darab)

print("7. feladat")
hianyzasok={}
for e in naplo:
    hianyzasok[e.split(" ")[2]+" "+e.split(" ")[3]]=0

for e in naplo:
    hianyzasok[e.split(" ")[2]+" "+e.split(" ")[3]]+=1

print(max(hianyzasok.values()))
print([kulcs for kulcs,ertek in hianyzasok.items() if ertek==max(hianyzasok.values())]) 


#print(hianyzasok)
