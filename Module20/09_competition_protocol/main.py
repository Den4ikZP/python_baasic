resList = dict()
protocol = int(input('Сколько записей вносится в протокол?: '))
for i in range(1, protocol + 1):
    c, d = input(f'{i}-я запись: ').split()
    c = int(c)
    resList[d] = c
resList = sorted(resList.items(), key=lambda x: x[1], reverse=True)
for i in range(3):
    print("%d место. %s (%d)" % (i+1, resList[i][0], resList[i][1]))
