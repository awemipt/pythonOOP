class FloatValue:
    @classmethod
    def check_value(cls, value):
        if not type(value) is float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.check_value(value)
        setattr(instance, self.name, value)

class Cell:
    value = FloatValue()
    def __init__(self, value=0.):
        self.value = value


class TableSheet:
    def __init__(self, N, M):
        self.cells = [[Cell() for i in range(M)] for j in range(N)]

N, M = 5, 3
table = TableSheet(N, M)
for i in range(N):
    for j in range(M):
        table.cells[i][j] = Cell(1.*(j+1) + M * i)

for i in range(N):
    for j in range(M):
        print(table.cells[i][j].value, end =' ')
    print()