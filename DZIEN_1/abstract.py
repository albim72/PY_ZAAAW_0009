from abc import ABC, abstractmethod

class Prototyp(ABC):
    def __init__(self,x):
        self.x = x

    def msg(self):
        return f'to jest mrtoda nieabstrakcyjna!'

    @abstractmethod
    def policz(self):
        pass

    @abstractmethod
    def policz_x(self):
        return self.x*7


print(type(Prototyp))

# p = Prototyp(4)

class Regular(Prototyp):

    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def policz(self):
        return 1001

    def policz_x(self):
        return super().policz_x() + self.y*3


rg = Regular(4,8)
print(f'wynik policz() =  {rg.policz()}')
print(f'wynik policz_x() =  {rg.policz_x()}')
print(rg.msg())
