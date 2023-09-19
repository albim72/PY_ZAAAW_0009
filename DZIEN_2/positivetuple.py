class PositiveTuple(tuple):
    def __new__(cls, *numbers):
        skipped = 0
        pos_number = []
        for x in numbers:
            if x>=0:
                pos_number.append(x)
            else:
                skipped += 1
        instance = super().__new__(cls,pos_number)
        instance._skipped = skipped
        return instance

posnb = PositiveTuple(9,0,-5,-6,98,0,34,12,3,5,17,-3,-5,-6,-11,34,56)
print(type(posnb))
print(posnb)
print(f'wartości odrzuconych: {posnb._skipped}')
