#przykład 1

def liczby():
    for i in range(17):
        yield i*3

ml = []
print(liczby())
for p in liczby():
    ml.append(p)
    print(p)

print(ml)

#przykład 2

def wznowienia(n,k):
    print("wstrzymanie działania....")
    yield 1001
    print("wznowienie działania")

    print("wstrzymanie działania....")
    yield n+k
    print("wznowienie działania")

    print("wstrzymanie działania....")
    yield n-k
    print("wznowienie działania")

    print("wstrzymanie działania....")
    yield n*k
    print("wznowienie działania")

    print("wstrzymanie działania....")
    yield n**k
    print("wznowienie działania")

print(wznowienia(8,7))

for i in wznowienia(8,7):
    print("_"*15)
    print(f'yield zwraca wartość: {i}')
    print("_"*15)
