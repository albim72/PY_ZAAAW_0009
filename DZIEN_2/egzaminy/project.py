class Project:
    def __init__(self):
        self._grade = 0

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self,value):
        if not(0<=value<=100):
            raise ValueError('Ocena musi zawierać się w przedziale 0-100')
        self._grade = value
