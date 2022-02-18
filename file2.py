f=open("adatok.txt")
f2=open("adatokSorszam.txt","w")

sorszam=1
for egySor in f:
  f2.write(str(sorszam)+" "+egySor)
  sorszam+=1







f2.close()
f.close()
