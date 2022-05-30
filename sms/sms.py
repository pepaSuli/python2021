import smsmodul
import math

f=open("sms.txt")
sorok=f.read().split("\n")[1:-1]
f.close()


print(sorok)
smsek=[]
for i in range(0,len(sorok)//2):
    smsek.append(smsmodul.adatok(sorok[i*2],sorok[i*2+1]))

print("2. feladat")
print(f"{smsek[-1].uzenet}")
print("{}".format(smsek[-1].uzenet))

print("3. feladat")
minIndex=0
maxIndex=0

for i in range(0,len(smsek)):
    if len(smsek[i].uzenet)> len(smsek[maxIndex].uzenet):
        maxIndex=i
    if len(smsek[i].uzenet)<len(smsek[minIndex].uzenet):
        minIndex=i

print("óra:{} perc:{} telefonszám:{} üzenet:{}".format(smsek[maxIndex].ora,
                                                       smsek[maxIndex].perc,
                                                       smsek[maxIndex].telefonszam,
                                                       smsek[maxIndex].uzenet))


print("óra:{} perc:{} telefonszám:{} üzenet:{}".format(smsek[minIndex].ora,
                                                       smsek[minIndex].perc,
                                                       smsek[minIndex].telefonszam,
                                                       smsek[minIndex].uzenet))


stat=[0,0,0,0,0]

for a in smsek:
    if len(a.uzenet)<=20:
        stat[0]+=1
    elif len(a.uzenet)<=40:
        stat[1]+=1
    elif len(a.uzenet)<=60:
        stat[2]+=1
    elif len(a.uzenet)<=80:
        stat[3]+=1
    else:
        stat[4]+=1

print(stat)

stat=[0,0,0,0,0]
for a in smsek:    
    stat[math.ceil(len(a.uzenet)/20)-1]+=1
print(stat)

print("4. feladat")
print("1-20:{} db, 21-40:{} db, 41-60:{} db, 61-80:{} db, 81-100:{} db".format(stat[0],stat[1],stat[2],stat[3],stat[4]))

stat=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
stat=[]
for i in range(0,24):
    stat.append(0)

for a in smsek:
    stat[a.ora]+=1

ossz=0
for a in stat:
    if a>10:
        ossz+=a-10
print("5. feladat Ernőnek {} sms-t kell fizetnie".format(ossz))


elozo=-1
idotav=[]
for a in smsek:
    if a.telefonszam="123456789":
        if elozo!=-1:
            idotav.append(a.idoperc()-elozo)
            elozo=a.idoperc()
print(idotav)





    

        
