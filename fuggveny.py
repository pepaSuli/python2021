'''
def negyzet(a):
    return a**2

q=negyzet(10)
print(q)
print(negyzet(8))

osszeg=0
for i in range(10):
    osszeg+=negyzet(i+1)

print(osszeg)

'''
import random

def koszon(nev="kedves barátom"):
    koszonesek=("Jó napot kívánok","Szevasz","Helló", "Csá", "Szia")
    
    print(random.choice(koszonesek),nev)


koszonCount=1
def koszon2(nev="kedves barátom"):
    koszonesek=("Jó napot kívánok","Szevasz","Helló", "Csá", "Szia")    

    print(koszonesek[koszonCount],nev)
#    koszonCount=koszonCount+1
    

koszon("Józsi")
koszon("Béla")
koszon("Juci")
koszon2()

koszon2("Elemér")
