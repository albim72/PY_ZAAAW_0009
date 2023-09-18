from ipojazd import IPojazd
from isilnik import ISilnik

class Pojazd(IPojazd,ISilnik):
    def spalanie(self, odl, jedn):
        return jedn*100/odl

    def kosztprzejazdu(self, odl, jedn, cena_j):
        return self.spalanie(odl,jedn)*(odl/100)*cena_j

    def dane_silnika(self, rodzaj, poj):
        return f"rodzaj: {rodzaj}, pojemność [l]: {poj}"

    def stan(self, opis, ilekm, remonty):
        return (f"stan silnika -> remonty: {remonty}, liczba przejechanych km: {ilekm}, "
                f"informacje dodatkowe: {opis}")
