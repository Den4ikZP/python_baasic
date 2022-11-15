import random

class Parent:
    def __init__(self, name, age, *childrens):
        self.name = name
        self.age = age
        self.childrens = childrens
    def info(self):
        print(f'Мое имя {self.name}, мне {self.age}, лет мой ребенок(-и) {", ".join(self.childrens)}')
    def stop(self):
        print('Так! А ну успокойся(-елись)', ", ".join(self.childrens))
    def food(self):
        print('Надо покормить', ", ".join(self.childrens))


class Children:
    spokoi = ['Не спокойный', 'Спокойный', 'Агресивный']
    golod = ['Очень голодный', 'Слегка голодный', 'Не голодный', 'Сытый']
    def __init__(self, name, age, fill=random.choice(spokoi), hungry=random.choice(golod)):
        self.name = name
        self.age = age
        self.fill = fill
        self.hungry = hungry
    def test(self):
        print(self.name, self.age, self.fill, self.hungry)

my = Parent('Lena', 40, 'Sasha', 'Dima')
my.info()
my.stop()
my.food()

print()

my1 = Children('Kolya', 20)
my1.test()


