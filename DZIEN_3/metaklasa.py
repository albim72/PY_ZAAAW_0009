class MojaMeta(type):
    def __new__(cls,nazwa,dziedziczenie,atrybuty):
        print(f'nazwa klasy: {nazwa}')
        print(f'klasy dziedziczone: {dziedziczenie}')
        print(f'słownik atrybutów: {atrybuty}')
        return type.__new__(cls,nazwa,dziedziczenie,atrybuty)

class Podstawowa:
    pass

class Pierwsza(Podstawowa,metaclass=MojaMeta):
    pass

class Druga(Pierwsza):
    pass

class Ekstra:
    pass

class Trzecia(Ekstra,Druga):
    @property
    def info(self):
        return "krótka informacja"
