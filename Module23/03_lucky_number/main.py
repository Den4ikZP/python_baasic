import random
with open('out_file.txt', 'w') as file:
    count = 777
    total = 0
    while total < count:
        num = input('Введите число: ')
        total += int(num)
        try:
            if 3 == random.randint(1, 3):
                raise ValueError
        except ValueError:
            print('Вас постигла неудача!')
            break
        file.writelines(str(num) + '\n')
    else:
        print('Вы успешно выполнили условие для выхода из порочного цикла!')
