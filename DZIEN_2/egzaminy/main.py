from project import Project
from egzamin import Exam
from grade import Egzamin

print("_____ klasa Project _____")
p1 = Project()
p1.grade = 96
assert p1.grade == 96

print(f'ocena projektu: {p1.grade}')


print("_____ klasa Exam _____")
g1 = Exam()
g1.python_grade = 70
g1.algo_grade = 72


assert g1.python_grade == 70
assert g1.algo_grade == 72

print(f'oceny: {g1.python_grade}, {g1.algo_grade}')

print("_____ klasa Grade - Egzamin _____")

print("I termin")
fexam = Egzamin()
fexam.python_grade = 77
fexam.algo_grade = 49
fexam.math_grade = 33

print(f'egzaminy: python {fexam.python_grade}, algotymy {fexam.algo_grade}, matematyka {fexam.math_grade}')

print("II termin")
sexam = Egzamin()
sexam.python_grade = 80
sexam.algo_grade = 51
sexam.math_grade = 56

print(f'egzaminy: python {sexam.python_grade}, algotymy {sexam.algo_grade}, matematyka {sexam.math_grade}')

print("wyniki pierwszego terminu z archiwum:")
print(f'egzaminy: python {fexam.python_grade}, algotymy {fexam.algo_grade}, matematyka {fexam.math_grade}')
