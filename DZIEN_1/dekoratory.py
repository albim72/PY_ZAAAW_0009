import math
import time

def pomiarczasu(funkcja):
    def wrapper():
        wynik = []
        starttime = time.perf_counter()
        funkcja()
        endtime = time.perf_counter()
        wynik.append(endtime-starttime)
        print(wynik[0])
    return wrapper

def sleep(funkcja):
    def wrapper():
        time.sleep(3)
        return funkcja()
    return wrapper


@pomiarczasu
@sleep
def biglista():
    sum([i**3 for i in range(10_000_000)])

biglista()

def debug(funkcja):
    def wrapper(*args,**kwargs):
        print(f'wołana funkcja to: {funkcja.__name__}')
        funkcja(*args)
    return wrapper

@debug
def info(i):
    print(f'informacja: {i}')

info("kod 32545435345")

#przykład ekstra

def trace(funkcja):
    def wrapper(*args,**kwargs):
        result = funkcja(*args,**kwargs)
        print(f'{funkcja.__name__}({args!r},{kwargs!r}) -> {result!r}')
        return result
    return wrapper


@trace
def fibonacci(n):
    # funkcja zwraca ntą liczbę z ciągu Fibonacciego
    if n in (0,1):
        return n
    return (fibonacci(n-2) + fibonacci(n-1))


print(fibonacci(9))
