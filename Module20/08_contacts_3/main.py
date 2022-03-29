first = dict()
while True:
    print('Введите номер действия: ')
    print('1. Добавить контакт')
    print('2. Найти человека')
    one = int(input())
    if one == 1:
        name = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').split())
        if name in first:
            print('Такой человек уже есть в контактах.')
            print(first)
            continue
        first[name] = input('Введите номер телефона: ')
        print('', first)
    elif one == 2:
        name = input('Введите фамилию для поиска: ')
        for key, value in first.items():
            if name.title() in key:
                strip = ' '.join(key)
                print(strip, value)
    else:
        print('Ввод не коретен')