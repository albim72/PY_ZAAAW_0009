from abc import ABCMeta,abstractmethod

class IPojazd(metaclass=ABCMeta):
    @abstractmethod
    def spalanie(self,odl,jedn):raise NotImplementedError
    
    @abstractmethod
    def kosztprzejazdu(self,odl,jedn,cena_j):raise NotImplementedError
