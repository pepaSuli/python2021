#   Készítette: Papp Péter
#   Dátum: 2021.12.03
#
#
import random
import datetime

#random.seed(123)
szamok=[]

megegyszer = True 
while megegyszer:
    szamok.clear()
    #két szám generálás, 1-99
    szamok.append(random.randint(1,9))
    szamok.append(random.randint(1,9))

    #print(szamok)

    #művelet generálás, 0:+, 1:-, 2:*, [3:/]

    muvelet=random.randint(0,2)

    feladvany=str(szamok[0])
    if muvelet==0:
        feladvany=feladvany+" + "
    elif muvelet==1:
        feladvany=feladvany+" - "
    elif muvelet==2:
        feladvany=feladvany+" * "
        
    feladvany=feladvany + str(szamok[1]) + " = "

    #másik megoldás, formázással
    #szoveg="{} {} {} ="
    #print(szoveg.format(szamok[0],"+",szamok[1]))
      
    #print(feladvany)


    startIdo=datetime.datetime.now()
    print(startIdo)
    #válasz bekérése
    valasz=input(feladvany)

    print(datetime.datetime.now()-startIdo)

    #a helyes válasz kiszámítása
    joValasz=0
    if muvelet==0:
        joValasz=szamok[0]+szamok[1]
    elif muvelet==1:
        joValasz=szamok[0]-szamok[1]
    elif muvelet==2:
        joValasz=szamok[0]*szamok[1]

    if joValasz==int(valasz):
        print("Helyes válasz!")
    else:
        print("Nem helyes válasz!")
        megyeszer=False






