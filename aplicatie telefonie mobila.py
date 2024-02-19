
import random
class operator():
    def __init__(self,nume,prefix_telefon='+4072'):
        self.nume=nume
        self.numar_abonati=0
        self.prefix_telefon=prefix_telefon
        self.abonati=[]
        self.numere_telefon={}
    def adaugareAbonat(self):
        print("---------------")
        nume=input("nume:")
        prenume=input("prenume:")
        cnp=input("cnp:")
        self.numere_telefon[cnp]=[None]
        valoare_contract=int(input("Val.contract:"))
        self.abonati.append(abonat(nume,prenume,cnp,valoare_contract))
        self.numar_abonati+=1
    def stergereAbonat(self):
        cnp=input("introduceti cnp:")
        for element in self.abonati:
            if cnp == element.returnCnp():
                self.abonati.remove(element)
    def afisareCont(self):
        for element in self.abonati:
            element.afisareAbonati()
            print(self.numere_telefon[element.returnCnp()])
    
    def returnPrefix(self):
        return self.prefix_telefon
    def adaugareTelefon(self):
        cnp=input("cnp:")
        for element in self.abonati:
            if cnp==element.returnCnp():
                numar_telefon=self.creareNumarTelefon()
                self.numere_telefon[cnp].append(numar_telefon)
    def creareNumarTelefon(self):
        numar=f"{self.returnPrefix()}"
        for i in range(1,8):
            numar+=str(random.randint(0,9))
        return numar
 
class abonat():
    def __init__(self,nume,prenume,cnp,valoare_contract):
        self.nume=nume
        self.prenume=prenume
        self.cnp=cnp
        self.valoare_contract=valoare_contract
 
    def afisareAbonati(self):
        print(self.nume+"-"+self.prenume+"-"+self.cnp+"-"+str(self.valoare_contract))
    def returnCnp(self):
        return self.cnp
Vodafone=operator("vodafone")
Vodafone.adaugareAbonat()
Vodafone.adaugareAbonat()
Vodafone.afisareCont()
Vodafone.adaugareTelefon()
Vodafone.adaugareTelefon()
Vodafone.afisareCont()