class Voin:
    def __init__(self, first=100, second=100):
        self.first = first
        self.second = second
        while self.first > 0 and self.second > 0:
            who = input('Кто бьет, 1 или 2? ')
            if who == '1':
                self.second -= 20
                print(f'Атаковал первый юнит, у второго осталось здоровья {self.second}')
            elif who == '2':
                self.first -= 20
                print(f'Атаковал второй юнит, у первого осталось здоровья {self.first}')
            if self.first == 0:
                print('Выиграл второй юнит')
            elif self.second == 0:
                print('Выиграл первый юнит')
Voin()
