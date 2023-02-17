class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = '_' + str(owner.__class__) + '__' + name

    def __set__(self, instance, value):
        if type(value) != int:
            raise ValueError('возможны только целочисленные значения')
        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value


class TableValues:
    def __init__(self, rows, cols, cell=CellInteger):
        if cell is None:
            raise ValueError('параметр cell не указан')
        self.cells = tuple([tuple([cell() for j in range(cols)]) for i in range(rows)])

    def __getitem__(self, item):
        return self.cells[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.cells[key[0]][key[1]].value = value

tb = TableValues(3, 2, cell=CellInteger)
tb[0, 0] = 1
print(tb)
assert tb[0, 0] == 1, "некорректно работает запись и/или считывание значения в ячейку таблицы по индексам"

table = TableValues(3, 2, cell=CellInteger)
print(table[0, 1])
table[0, 0] = 10
table[1, 1] = 10
# table[0, 0] = 1.45 # генерируется исключение ValueError

# вывод таблицы в консоль
for row in table.cells:
    for x in row:
        print(x.value, end=' ')
    print()