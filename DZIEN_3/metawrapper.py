from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(f"Pełna nazwa metody: {func.__qualname__}")
        return func(*args,**kwargs)
    return wrapper

def debugmethods(cls):
    for key,val in vars(cls).items():
        if callable(val):
            setattr(cls,key,debug(val))
    return cls


class DebugMeta(type):
    def __new__(cls,clsname,bases,atrs):
        obj = super().__new__(cls,clsname,bases,atrs)
        obj = debugmethods(obj)
        return obj

class Base(metaclass=DebugMeta):
    pass

class Calculate(Base):
    def add(self,x,y):
        return 2*x+3*y

    def multi(self,x,y):
        return 3*x*y

mobl = Calculate()
print(mobl.add(3,4))
print(mobl.multi(3,4))
