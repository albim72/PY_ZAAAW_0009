from oldresistor import OldResistor
from resistor import Resistor

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