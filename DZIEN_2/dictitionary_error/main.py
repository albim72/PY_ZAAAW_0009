from error import IntFloatValueError, KeyValueConstructError

class CustomIntFloatDict(dict):
    empty_dict = {}

    def __init__(self,key=None, value=None):
        if key is None or value is None:
            self.get_dict()
        elif not isinstance(key,(tuple,list,)) or not isinstance(value,(tuple,list,)):
            raise KeyValueConstructError(key,value)
        else:
            zipped = zip(key,value)
            for k,val in zipped:
                if not isinstance(val,(int,float,))  :
                  raise IntFloatValueError(val)
                dict.__setitem__(self,k,val)


    def get_dict(self):
        return self.empty_dict


    def __setitem__(self, key, value):
        if not isinstance(value,(int, float, )):
            raise IntFloatValueError(value)
        return dict.__setitem__(self,key,value)

test_1 = CustomIntFloatDict()
print(test_1)

# test_2 = CustomIntFloatDict({'a','b'},[4,7])
# print(test_2)

# test_3 = CustomIntFloatDict(('a','b','c'),[10,"twenty",30])
# print(test_3)

test_4 = CustomIntFloatDict(('a','b','c'),[10,20,30])
print(test_4)
