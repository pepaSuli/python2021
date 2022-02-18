import math

"""
lista = list((2,23,14,76,23,2,4,6,100,200))

print(lista)

for elem in lista:
    elem=elem*2
    print(elem)

print(lista)

for i in range(8):
    print(lista[i])
    lista[i]*=2

print(lista)


for i in range(len(lista)):
    print(lista[i])
"""

#2 jegyűek gyöke
#for i in range(10,100):
#    print( round(math.sqrt(i), 2) )
    
for i in range(10,100):
    if round( math.sqrt(i), 0 ) == math.sqrt(i):
        print( i, round( math.sqrt(i), 2),sep="********" )
    
    
