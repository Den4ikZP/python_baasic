def move(n, x, y):
    def z(x, y):
        return ({1, 2, 3} - {x} - {y}).pop()
    if n:
        z = z(x, y)
        move(n-1, x, z)
        print(f'Переложить диск {n} со стержня номер {x} на стержень номер {y}')
        move(n-1, z, y)
n = int( input('n = ') )
move(n, 1, 3)
