from abc import ABCMeta,abstractmethod

class ISilnik(metaclass=ABCMeta):
    @abstractmethod
    def dane_silnika(self,rodzaj,poj):raise NotImplementedError
    
    @abstractmethod
    def stan(self,opis,ilekm,remonty):raise NotImplementedError
