from math import sqrt, pi
class Circle:
    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r
    def square(self):
        print(pi * self.r ** 2)
    def perimetr(self):
        print(2 * pi * self.r)
    def increase(self, k):
        print(f'x = {self.x * k}, y = {self.y * k}, r = {self.r * k}')
    def intersection(self, x1, y1, r2):
        print('Yes' if sqrt(sqrt(abs(self.x) - abs(self.y)) + sqrt(abs(x1) - abs(y1))) < self.r + r2 else 'No')
sp = Circle(110, 10, 1)
sp.square()
sp.perimetr()
sp.increase(5)
sp.intersection(115, 15, 1)


