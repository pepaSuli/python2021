import random
import math


for i in range(1,21):
    ho=math.floor(random.random()*12)+1
    print(i,ho)

szamok=[]
darab=int(input("Kérek egy számot:"))
for i in range(0,darab):
    szamok.append(math.floor(random.random()*900)+100)

print(szamok)
print(max(szamok))

szamok.sort()
print(szamok)
print(szamok[len(szamok)-2])

szamok.reverse()
print(szamok[1])


#lottó 1
golyok=[]
for i in range(1,91):
    golyok.append(i)

print(golyok)
random.shuffle(golyok)
print(golyok)

print(golyok[0:5])
print(golyok[5:10])

for i in range(0,len(golyok)//5):
    print(golyok[i*5:i*5+5])
    print(i)


