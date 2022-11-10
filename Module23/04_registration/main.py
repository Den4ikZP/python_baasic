def logs(lg):
    with open('registrations_good.txt', 'a', encoding='utf-8') as good_log, open('registrations_bad.txt', 'a',
                                                                                 encoding='utf-8') as bad_log:
        try:
            if len(lg) != 3:
                raise IndexError
            for i in lg[0]:
                if not i.isalpha or i in '!#$%&()*+,-./:;<=>?@[\]^_{|}~':
                    raise NameError
            if '@' not in lg[1] and '.' not in lg[1]:
                raise SyntaxError
            if 10 >= int(lg[2]) or 99 < int(lg[2]):
                raise ValueError
        except IndexError:
            bad_log.write(f'{str(lg[0:])} НЕ присутствуют все три поля' + '\n')
        except NameError:
            bad_log.write(f'{str(lg[0])} {str(lg[1])} {str(lg[2])} Поле «Имя» содержит НЕ только буквы' + '\n')
        except SyntaxError:
            bad_log.write(f'{str(lg[0])} {str(lg[1])} {str(lg[2])} Поле «Имейл» НЕ содержит @ и . (точку)' + '\n')
        except ValueError:
            bad_log.write(
                f'{str(lg[0])} {str(lg[1])} {str(lg[2])} Поле «Возраст» НЕ является числом от 10 до 99' + '\n')
        else:
            good_log.write(f'{str(lg[0])} {str(lg[1])} {str(lg[2])}' + '\n')


[logs(l.strip().split()) for l in open('registrations.txt', encoding='utf-8').readlines()]
