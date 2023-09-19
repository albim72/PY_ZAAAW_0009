from project import Project
from egzamin import Exam

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
