class adatok:
    #9 11 123456789     sor1
    #Szia, mikor jossz? sor2
    def __init__(self,sor1,sor2):
        vag=sor1.split(" ")
        self.ora=int(vag[0])
        self.perc=int(vag[1])
        self.telefonszam=vag[2]

        self.uzenet=sor2
        
