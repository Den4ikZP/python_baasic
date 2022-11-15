class Student:
    def __init__(self, answer):
        self.answer = answer
    def check(self):
        for x, y in sorted(self.answer.items(), key=lambda j: sum(j[1]) / len(j[1])):
            print(x)


sp = {'Anton': [3, 3, 4],
      'Vasua': [5, 5, 3],
      'Kolua': [5, 4, 5],
      'Denys': [5, 5, 5],
      'Oleg': [3, 3, 3],
      'Vanua': [4, 4, 4]}


one = Student(sp)
one.check()
