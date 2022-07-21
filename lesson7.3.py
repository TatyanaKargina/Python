class Cell:
    def __init__(self, cell):
        self.cell = cell
        self.symbol = '*'

    def __str__(self):
        return str(f'Количество ячеек - {self.cell}')

    def __sub__(self, other):
        return Cell(abs(self.cell - other.cell))

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell // other.cell)

    def __add__(self, other):
        return Cell(abs(self.cell + other.cell))

    def make_order(self, count):
        x = self.cell
        while x > 0:
            for k in range(1,count+1):
                print(self.symbol, end ='')
                x -= 1
                if x <= 0:
                    break
            print('\n', end = '')



a = Cell(6)
b = Cell(12)
c = Cell(6)
d = Cell(3)

print(a + b)
print(a - b)
print(a * b)
print(c / d)

a.make_order(3)
b.make_order(3)