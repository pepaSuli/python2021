import random

f=open("ajto.txt","r")

kodok=[]
for egySor in f:
    kodok.append(egySor[:-1])
    #kodok.append(egySor.strip())

f.close()

print(kodok)

#239451
print("2. feladat")
be=input("Adja meg, mi nyitja a zárat! ")

print("3. feladat")
sorszam=1
talalat=[]
for kod in kodok:
    if kod==be:
       talalat.append(sorszam)

    sorszam+=1

#szám lista összefűzése
print("A nyitó kódszámok sorai: " + " ".join(str(szam) for szam in talalat))

#A nyitó kódszámok sorai: 1 4 5 8 10…

#kicsit más megoldás
talalat=[]
for index,kod in enumerate(kodok,1):
    if kod==be:
       talalat.append(index)

#szám lista összefűzése
print("A nyitó kódszámok sorai: " + " ".join(str(szam) for szam in talalat))


dupla=[]
for index,kod in enumerate(kodok,1):
    for karakter in kod:
        if kod.count(karakter) > 1:
            dupla.append(index)
            
       
if len(dupla)>0:
    print(dupla[0])
else:
    print("Nem volt")

#5. feladat
ujkod=""
valaszthato=["0","1","2","3","4","5","6","7","8","9"]
while len(ujkod)<len(be):
    szam=random.randint(0,len(valaszthato)-1)
    ujkod+=valaszthato[szam]
    valaszthato.pop(szam)

print("5. feladat")
print("Egy " + str(len(ujkod)) + " hosszú kódszám: "+ujkod)





    
