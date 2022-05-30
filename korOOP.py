import math

class kor:
    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.r=r

    def nagyit(self, mennyivel=1):
        self.r+=mennyivel

    def kicsinyit(self, mennyivel=1):
        self.r-=mennyivel

    def kerulet(self):
        return 2*self.r*math.pi

    def terulet(self):
        return self.r**2*math.pi/2

k=kor(0,0,10)
print(k.r)
k.nagyit()
print(k.r)
k.nagyit(100)
print(k.r)
k.kicsinyit(100)
print(k.r)
k.kicsinyit(-100)
print(k.r)
print(k.kerulet())
print(k.terulet())
