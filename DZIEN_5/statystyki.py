liczby = [900,1001,-456,0,3,15,67,88,-90,-3,16,-333,267,899,32,-10,0,9,12,-4,811,2]

def pokaz_statystyki(dane):
    minimum = min(dane)
    maksimum = max(dane)
    rozstep = maksimum-minimum
    liczba_el = len(dane)
    sr_arytm = sum(dane)/liczba_el
    return minimum,maksimum,rozstep,liczba_el,sr_arytm

wynik = pokaz_statystyki(liczby)
print(wynik)
print(type(wynik))

mini,maksi,roz,le,srart = pokaz_statystyki(liczby)
print(f'wartość maksymalna: {maksi}, mimnimalna: {mini}, rozstęp: {roz}, liczba elementów: {le},'
      f'średnia arytmetyczna: {srart}')
