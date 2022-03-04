f=open("penztar.txt")
kosar=[]
#szoveg=f.read()
#print(szoveg)
for sor in f:
    kosar.append(sor.strip())    

f.close()

print("2. feladat")
print("A fizetések száma: " + str(kosar.count("F")))

print("3. feladat")
print("Az első vásárló " + str(kosar.index("F")) + " darab árucikket vásárolt.")

