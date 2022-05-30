import smsmodul

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
