class UjemnaSilnia(Exception):
    def __init__(self,n):
        self.n = n

    def __str__(self):
        return f"została zadana wartość: {self.n}. Wartość argumentu musi być nieujemna!"
