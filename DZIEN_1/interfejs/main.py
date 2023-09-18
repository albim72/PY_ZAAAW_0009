from pojazd import Pojazd

pj = Pojazd()

odl=567
jd = 51
cn = 6.08

print(f'spalanie [l/100km]: {pj.spalanie(odl,jd):.2f}')
print(f'koszty przejazdu na trasie {odl} km -> {pj.kosztprzejazdu(odl,jd,cn):.2f} zł')
