from dataclasses import dataclass

class Liczba:
    def __init__(self,x):
        self.x=x

    def __repr__(self):
        return f"reprezentacja xxx -> {self.x}"

zk = Liczba(2)
print(zk)
print(zk.x)

@dataclass
class DLiczba:
    x:int

dl = DLiczba(22)
print(dl)
print(dl.x)

@dataclass
class Dane:
    nazwa:str
    filia:str
    licznik:int=0
    cena:float=0.0

    def __repr__(self):
        return f"towar: {self.nazwa}, liczba sztuk: {self.licznik}, cena: {self.cena} zł"

    def __call__(self, *args, **kwargs):
        return f"kowota do zapłaty: {self.licznik * self.cena} zł"

    def opisz(self):
        return f"produkt: {self.nazwa}"


dn = Dane("talerz",45,4,67)
print(dn)
print(dn())
print(dn.opisz())
