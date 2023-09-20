from dataclasses import dataclass,Field
from datetime import datetime

# Field -> 'default',default factory','init','repr','hash','compare','metadata','kw_only'
params = {
    'firstname':Field(None,None,True,True,True,True,None,None),
    'lasttname':Field(None,None,True,True,True,True,None,None),
    'year_of_birth':Field(None,None,True,True,True,True,None,None)
}

def age(self):
    return datetime.now().year - self.year_of_birth

MetaPerson = dataclass(type('MetaPerson',(),{'__annotations__':params,'wiekosoby':property(age)}))

pr = MetaPerson('Nadia','Tracz',1990)
print(pr)
print(type(pr))
print(pr.wiekosoby)


