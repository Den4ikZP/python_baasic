with open('people.txt', encoding='utf-8') as file:
    count = 0
    for j, i in enumerate(file.readlines(), 1):
        i = i.strip()
        try:
            if len(i) < 3:
                count += int(len(i))
                raise ValueError
            else:
                count += int(len(i))
        except ValueError:
            print(f'Ошибка: менее трёх символов в строке {j}.')
    print(f'Общее количество символов: {count}.')
