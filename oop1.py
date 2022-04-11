class Kutya:
    def __init__(self,nev):
        self.nev=nev

    def ugat(self):
        print("VAU-VAU ("+self.name+")")

egyKutya=Kutya("Armageddon")
print(egyKutya.nev)
egyKutya.ugat()
