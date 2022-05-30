
print("1. feladat")
#filenev=input("Adja meg a bemeneti fájl nevét! ")
#sor=int(input("Adja meg egy sor számát! "))
#oszlop=int(input("Adja meg egy oszlop számát! "))
filenev= "nehez.txt"
sor=1
oszlop=1


f=open(filenev)
sorok=f.read().split("\n")[:-1]
f.close()

adatok=[]
for _sor in sorok:
    adatok.append(_sor.split(" "))


adatok2=[]
for _sor in adatok:
    #['0', '0', '0', '0', '0', '0', '0', '0', '6']
    temp=[]
    for elem in _sor:
        temp.append(int(elem))

    adatok2.append(temp)

#print(adatok)
#print(adatok2)

tabla=adatok[:9]
lepesek=adatok[9:]
#print(tabla)
#print(lepesek)

print("3. feladat")

print("Az adott helyen szereplő szám: "+str(tabla[sor-1][oszlop-1]))
