def dodawanie(self,x,y):
    return x+y

def odejmowanie(self,x,y):
    return x-y

def mnozenie(self,x,y):
    return x*y

def inna(self,x,y):
    return 0

class Dzialanie(type):
    def __init__(cls,clasname,bases,attrs):
        if clasname == "Dodaj":
            cls.operacja = dodawanie
        elif clasname == "Odejmij":
            cls.operacja = odejmowanie
        elif clasname == "Pomnoz":
            cls.operacja = mnozenie
        else:
            cls.operacja = inna

class Opisz(metaclass=Dzialanie):
    pass

p1 = Opisz()
print(f'wynik działania {p1.__class__.__name__} = {p1.operacja(0,0)}')

class Dodaj(metaclass=Dzialanie):
    pass

p2 = Dodaj()
print(f'wynik działania {p2.__class__.__name__} = {p2.operacja(3,6)}')


class Odejmij(metaclass=Dzialanie):
    pass

p3 = Odejmij()
print(f'wynik działania {p3.__class__.__name__} = {p3.operacja(3,6)}')

class Pomnoz(metaclass=Dzialanie):
    pass

p3 = Pomnoz()
print(f'wynik działania {p3.__class__.__name__} = {p3.operacja(3,6)}')
