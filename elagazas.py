szam=100

if szam > 20:
    print("nagyobb")
    print("mint 20")
print("vizsgálat vége")


if szam % 2 == 0:
    print("páros")
else:
    print("páratlan")



#bekérés jön itten bizony
be=input("Kérek egy számot: ")
print(be)

if int(be) % 2 == 0:
    print("páros")
else:
    print("páratlan")


szam=int(input("Kérek még egy számot: "))
if szam > 10:
    if szam % 12 == 0:
        print(str(szam) + " osztható 12-vel")
    else:
        print(str(szam) + " nem osztható 12-vel")
 

ora=int(input("Hány óra van? "))
if ora<=8:
    print("Jó reggelt!")
elif ora<=17:
    print("Jó napot!")
elif ora<=21:
    print("Jó estét!")
else:
    print("Jó éjszakát!")


