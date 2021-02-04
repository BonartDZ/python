import math

class Cell:

    def __init__(self, cell_count):
        self.cell_count = int(cell_count)

    def __add__(self, other):
        return Cell(self.cell_count + other.cell_count)

    def __sub__(self, other):
        if self.cell_count > other.cell_count:
            return Cell(self.cell_count - other.cell_count)
        print("отрицательное значение недопустимо")
        return '\n'

    def __mul__(self, other):
        return Cell(self.cell_count * other.cell_count)

    def __truediv__(self, other):
        return Cell(self.cell_count // other.cell_count)

    def make_order(self, cell_count_row):
        len_row, tail_row = self.cell_count // cell_count_row, self.cell_count % cell_count_row
        cell_str = '\n'.join(['*' * cell_count_row] * len_row + (['*' * tail_row]))
        return cell_str

    def __str__(self):
        return f'{self.cell_count}'

c = Cell(20)
c1 = Cell(17)
print(c + c1)
print(c - c1)
print(c * c1)
print(c / c1)
print((c * c1).make_order(50))

