f=open("penztar.txt")
kosar=[]
#szoveg=f.read()
#print(szoveg)
for sor in f:
    kosar\
           .append(sor.strip())

f.close()

print("2. feladat")
print("A fizetések száma: " + str(kosar.count("F")))

print("3. feladat")
print("Az első vásárló " + str(kosar.index("F")) + " darab árucikket vásárolt.")


sorszam=int(input("Vásárlás sorszáma: "))
arunev=input("Árucikk neve: ")
darab=int(input("Darabszám: "))

#a termék első indexe
aruIndex=kosar.index(arunev)
darabLista=kosar[:aruIndex]
#print(darabLista)
vasarlasDb=darabLista.count("F") + 1
#print(vasarlasDb)

print("5. feladat")
print("Az első vásárlás sorszáma: " + str(vasarlasDb))

#a termék utolsó indexe
utolsoIndex=0
for i in range(0,len(kosar)):
    if kosar[i*-1-1]==arunev:
        utolsoIndex=len(kosar)-i
        break
darabLista=kosar[:utolsoIndex]
vasarlasDb=darabLista.count("F") + 1
print("Az utolsó vásárlás sorszáma: " + str(vasarlasDb))

voltF=False
szam=0
for e in kosar:
    if e==arunev:
        














