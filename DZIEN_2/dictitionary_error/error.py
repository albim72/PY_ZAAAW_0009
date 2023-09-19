class IntFloatValueError(Exception):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return f'wartość {self.value} jest niewłaściwa! Akceptowalne są jedynie typy int i float!'

class KeyValueConstructError(Exception):
    def __init__(self,key,value):
        self.key = key
        self.value = value

    def __str__(self):
        return (f"klucze i wartości powinny być przekazane w listach lub krotkach!.\n"
                f"klucz: {self.key} jest w typie {type(self.key)}\n"
                f"wartość: {self.value} jest w typie {type(self.value)}\n")
