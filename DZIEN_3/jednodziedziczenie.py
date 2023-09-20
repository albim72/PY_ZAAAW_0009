class MultiBases(type):
    def __new__(cls,clsname,bases,clsdict):
        if len(bases) > 1:
            raise TypeError('Wielodziedziczenie zabronione')
        return super().__new__(cls,clsname,bases,clsdict)


class Base(metaclass=MultiBases):
    pass

class A(Base):
    pass

class B(Base):
    pass

class Test:
    pass

class C(Test,B):
    pass
