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
"""
Függvény nyit(jo, proba:karaktersorozat): logikai érték
egyezik:=(hossz(jo)=hossz(proba))
Ha egyezik akkor
elteres=ascii(jo[1])-ascii(proba[1])
Ciklus i:=2-től hossz(jo)
Ha ( elteres - (ascii(jo[i])-ascii(proba[i])) ) mod 10 <> 0
akkor egyezik:=hamis
Ciklus vége
Elágazás vége
nyit:=egyezik
"""
#print("6. feladat")
def nyit(jo,proba):
    egyezik=len(jo)==len(proba)
    if egyezik:
        elteres=ord(jo[0])-ord(proba[0])
        for i in range(1,len(jo)):
            if (elteres - (ord(jo[i]) - ord(proba[i]))) % 10 != 0:
                egyezik=False
    return egyezik


#7. feladat
siker = []
for elem in kodok:
    if len(elem) != len(be):
        siker.append([elem, 'hibás hossz'])
    elif nyit(be, elem) == False:
        siker.append([elem, 'hibás kódszám'])
    elif nyit(be, elem) == True:
        siker.append([elem, 'sikeres'])

kimenet = open('siker.txt', 'w')
for elem in siker:
    print(' '.join(elem), file=kimenet)
kimenet.close()

    
