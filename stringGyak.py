"""
be=input("Kérek egy kisbetűt: ")
print(be.upper())

be=input("Kérek egy nagybetűt: ")
print(be.lower())


for i in range(70):
    print(be, end="")

print()
print(be.ljust(70,be))


be=input("Kérek egy szöveget: ")
if len(be)>=12:
    if be[11]=="k":
        print("igaz")
    else:
        print("nem igaz")

print(be[:3])
print(be[-3:])
szo=be[:3].upper() + be[3:-3].lower() + be[-3:].upper()
#print(be[-3:].upper)
print(szo)
"""

'''
#Géza egy láma -> láma egy Géza -> Láma egy géza
be=input("Kérek egy mondatot: ")
#szavakra bontás
fordit=be.split(" ")
print(fordit)

#megfordítás
fordit.reverse()

print(fordit)
#egyesítés
print(" ".join(fordit).capitalize())
'''

be="És Kérjen és, be egy mondatotés. Vizsgálja meg, hogy az és szó szerepel-e benne. Ha igen, akkor számolja meg hányszor. és"
darab=be.replace(",","").replace(".","").split(" ")

db=0
for szo in darab:
    if szo=="és":
        db+=1

if db==0:
    print("Nem volt egy sem")
else:
    print(str(db)+" darab volt")


print(str(
        (" "+
         be.lower()
             .replace(",","")
            +" ")
         .count(" és ")
        )
          +" darab volt"
      )

