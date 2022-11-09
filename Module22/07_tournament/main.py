k = int(input())
x = open('first_tour.txt')
spisok = []
for i in x.readlines():
    i = i.strip().split()
    if int(i[2]) > k:
        spisok.append(i)
spisok = sorted(spisok, key=lambda x: -(int(x[2])))
with open('second_tour.txt', 'w') as f:
    f.write(str(len(spisok)) + '\n')
    for x, y in enumerate(spisok, 1):
        f.write(f'{x}) {y[1][0]}. {y[0]} {y[2]}' + '\n')


