from dataclasses import dataclass

@dataclass
class Article:
    title:str
    author:str
    content:str

    def __repr__(self):
        return f'autor: {self.author}, tytuł: {self.title}'

@dataclass(init=False)
class PythonArticle(Article):
    # language:str
    # price:int=30
    def __init__(self,title,price=30):
        self.title = title
        self.price = price
        self.language = "Python"
        self.autor = "Jan Kot"
        self.content = "opis wybranych zastosowań jezyka Python"

    def __repr__(self):
        return f"język: {self.language}, cena: {self.price} zł"


a = Article("Programowanie w C","Eryk Kos","blabla")

print(a)

art = PythonArticle("Python a ML")
print(art)


