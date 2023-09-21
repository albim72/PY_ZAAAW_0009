from pyparsing import Word,OneOrMore,Optional,Group,Suppress,alphanums

class Gate:
    def __init__(self):
        self.is_open = False

    def __str__(self):
        return 'open' if self.is_open else 'closed'

    def open(self):
        print('opening the gate')
        self.is_open = True

    def close(self):
        print('closing the gate')
        self.is_open = False

class Garage:
    def __init__(self):
        self.is_open = False

    def __str__(self):
        return 'open' if self.is_open else 'closed'

    def open(self):
        print('opening the garage')
        self.is_open = True

    def close(self):
        print('closing the garage')
        self.is_open = False

class Aircondition:
        def __init__(self):
            self.is_on = False

        def __str__(self):
            return 'on' if self.is_on else 'off'

        def turn_on(self):
            print('turning on the air condition')
            self.is_on = True

        def turn_off(self):
            print('turning off the air condition')
            self.is_on = False


class Heating:
    def __init__(self):
        self.is_on = False

    def __str__(self):
        return 'on' if self.is_on else 'off'

    def turn_on(self):
        print('turning on the air heating')
        self.is_on = True

    def turn_off(self):
        print('turning off the air heating')
        self.is_on = False


class Boiler:
    def __init__(self):
        self.temperature = 47

    def __str__(self):
        return f'boiler temperature: {self.temperature} C'

    def increase_temperature(self,amount):
        print(f"increasing the boiler's temperature {amount} degrees")
        self.temperature += amount

    def decrease_temperature(self,amount):
        print(f"decreasing the boiler's temperature {amount} degrees")
        self.temperature -= amount
        
class Fridge:
    def __init__(self):
        self.temperature = 2

    def __str__(self):
        return f'fridge temperature: {self.temperature} C'

    def increase_temperature(self,amount):
        print(f"increasing the fidge's temperature {amount} degrees")
        self.temperature += amount

    def decrease_temperature(self,amount):
        print(f"decreasing the fridge's temperature {amount} degrees")
        self.temperature -= amount