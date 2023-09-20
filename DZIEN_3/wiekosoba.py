from dataclasses import dataclass
from datetime import datetime

@dataclass
class NowaOsoba:
    first_name:str
    last_name:str
    year_of_birth:int

    @property
    def age(self):
        return datetime.now().year - self.year_of_birth

    @property
    def czypelnoletnia(self):
        return self.age>=18



p = NowaOsoba("Janusz","Gierej",2010)
print(p)
print(p.age)
print(p.czypelnoletnia)

