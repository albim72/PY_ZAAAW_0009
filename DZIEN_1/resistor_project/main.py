from oldresistor import OldResistor
from resistor import Resistor
from voltage import VoltageResistance
from bounded import BoundedResistance

print("____________ klasa OldResistor _____________")
r0= OldResistor(10.2E2)
print(r0)
print(r0._ohms)
r0.set_ohms(2.88E3)
print(r0.get_ohms())

print("____________ klasa Resistor _____________")

r1 = Resistor(50e3)
r1.ohms = 10e3
print(f"układ elektryczny:\noporność: {r1.ohms} omów,\nnapięcie: {r1.voltage} V,\nnatężenie: {r1.current} A")

print("____________ klasa VoltageResistance _____________")

r2 = VoltageResistance(1E3)
print(f"początokowe natężenie prądu: {r2.current} A")
r2.voltage=39
print(f"natężenie prądu: {r2.current} A")
print(f"napięcie prądu: {r2.voltage} V")

print("____________ klasa BoundedResistance _____________")

r3 = BoundedResistance(1E2)
try:
    print(r3.ohms)
    r3.ohms = 0
    print(f'opór po zmianie: {r3.ohms}')
except ValueError as d:
    print(d)
