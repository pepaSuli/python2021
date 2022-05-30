
f=open("titanic.txt")
adatok=f.read().split("\n")
f.close()

print("2. feladat: " + str(len(adatok)) + " db")


print("3. feladat: "+str(sum(int(e.split(";")[1])+ int(e.split(";")[2]) for e in adatok )) + " fő")

ossz=0
for e in adatok:
    temp=e.split(";")
    tulelo=int(temp[1])
    eltunt=int(temp[2])
    ossz+=tulelo
    ossz+=eltunt

print("3. feladat: "+str(ossz) + " fő")

kulcsSzo=input("4. feladat: Kulcsszó: ")
van=False
#find()
talalat=[e for e in adatok if e.find(kulcsSzo)>-1]
if len(talalat)>0:
    print("Van találat!")
else:
    print("Nincs találat!")

#5.
print("5. feladat")
print("\n".join([e.split(";")[0]+" " + str(int(e.split(";")[1])+int(e.split(";")[2]))+ " fő" for e in talalat]))

print("6. feladat")
print("\n".join([e.split(";")[0] for e in adatok if 0.6<=int(e.split(";")[2])/(int(e.split(";")[1])+int(e.split(";")[2]))]))

print("7. feladat")

print(max(int(e.split(";")[1]) for e in adatok ))

print([e.split(";")[0] for e in adatok if str(max(int(e.split(";")[1]) for e in adatok )) in e ][0])

#másként, rövidebben?
adatok2=[[e.split(";")[0],int(e.split(";")[1]),int(e.split(";")[2])] for e in adatok]
print(adatok2)

talalat=[e for e in adatok2 if e[0].find(kulcsSzo)>-1]
if len(talalat)>0:
    print("Van találat!")
else:
    print("Nincs találat!")

print("5. feladat")
print("\n".join([e[0]+" " + str(e[1]+e[2])+ " fő" for e in talalat]))


print("6. feladat")
print("\n".join([e[0] for e in adatok2 if 0.6<=e[2]/(e[1]+e[2])]))

print("7. feladat")
#print(max(e[1] for e in adatok2 ))
print([e[0] for e in adatok2 if max(i[1] for i in adatok2 ) == e[1]][0])


