
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

