import os

word = input('Введите строку: ')
os.chdir(input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ').replace(' ', '\\'))
name_file = input('Введите имя файла: ') + '.txt'

if os.path.exists(name_file):
    remap = input('Вы действительно хотите перезаписать файл? ')

    if remap == 'Да':
        open(name_file, 'w').write(word)
        print('Файл успешно перезаписан!')

else:
    open(name_file, 'w').write(word)
    print('Файл успешно сохранён!')
