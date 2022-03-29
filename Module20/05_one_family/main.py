people = {
    'Сидоров Никита': 35,
    'Сидорова Алина': 34,
    'Сидоров Павел': 10,
    'Иванов Петя': 15,
    'Иванов Коля': 20,
    'Иванова Лена': 25
}

surname = input('Введите фамилию: ')

for name, age in people.items():
    if surname in name:
        print(name, age)
