class Exam:
    def __init__(self):
        self._python_grade = 0
        self._algo_grade = 0
        
    @staticmethod
    def _check_grade(value):
        if not (0 <= value <= 100):
            raise ValueError('Ocena musi zawierać się w przedziale 0-100')
        
    @property
    def python_grade(self):
        return self._python_grade
    
    @python_grade.setter
    def python_grade(self,value):
        self._check_grade(value)
        self._python_grade = value

    @property
    def algo_grade(self):
        return self._algo_grade

    @algo_grade.setter
    def algo_grade(self, value):
        self._check_grade(value)
        self._algo_grade = value
        
