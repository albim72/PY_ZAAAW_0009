import os
mojekody = '''
a=5
b=11
print(f'wynik: {a*(b+3)}')
'''

exec(mojekody)
print(type(mojekody))

code = input('rób co chcesz.... ')
exec(code)

def policzObwod(k):
    return 4*k

def policzPole(k):
    return k**2

expression = input('podaj swoją komendę..... ')

for k in range(1,5):
    if(expression == 'policzObwod(k)'):
        print(f'jesli długość boku działki wynosi k={k} jej obwód wynosi {eval(expression)}')
    elif(expression == 'policzPole(k)'):
        print(f'jesli długość boku działki wynosi k={k} jej pole wynosi {eval(expression)}')
    else:
        print('nie ma takiej opcji')

        break
g = "6.3"
print(g*9)
print(eval(g)*9)
print(float(g)*9)

wr = "True"
print(wr*12)
print(eval(wr)*12)
