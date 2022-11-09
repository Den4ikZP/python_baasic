with open('zen.txt') as file:
    stroka = len(file.readlines())
    file.seek(0)
    alpha = {}
    word = 0
    bukva = 0
    for i in file.readlines():
        for j in i.replace('--', '').strip().split():
            word += 1
            for k in j.lower():
                if k.isalpha():
                    bukva += 1
                    if k not in alpha:
                        alpha[k] = 1
                    else:
                        alpha[k] += 1
    alpha = {x: y for y, x in alpha.items()}
    print(f'Количество букв в файле: {bukva}\n'
          f'Количество слов в файле: {word}\n'
          f'Количество строк в файле: {stroka}\n'
          f'Наитболее редкая буква: {alpha[min(alpha)]}')