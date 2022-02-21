
f=open("ajto.txt","r")

kodok=[]
for egySor in f:
    kodok.append(egySor[:-1])

f.close()

print(kodok)
