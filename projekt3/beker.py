# adatbekérő class
# rendszám, sofőr, indulKm, megállKm, tankolás

class beker:
    def __init__(self):
        pass

    def form(self):
        self.rendszam=input("Rendszám: ")
        self.sofor=input("Sofőr: ")
        self.indulKm=int(input("Indul (km): "))
        self.megallKm=int(input("Megáll (km): "))
        self.tankol=int(input("Tankolt liter (0, ha nem): "))


if __name__=="__main__":
    adat=beker()
    adat.form()
    print("megtett km: "+str(adat.megallKm-adat.indulKm ))
    
else:
    print("Ez egy modul")
