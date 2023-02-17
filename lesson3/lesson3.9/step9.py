class Cell:
    def __init__(self, data):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class TableValues:
    def __init__(self, rows, cols, type_data):
        self.rows = rows
        self.cols = cols
        self.type = type_data
        self.table = [[Cell(0) for j in range(cols)] for i in range(rows)]

    def __check_indx(self, i, j):
        if any([i < 0, j < 0, i >= self.rows, j >= self.cols]):
            raise IndexError('неверный индекс')

    def __setitem__(self, key, value):
        if type(value) != self.type:
            raise TypeError('неверный тип присваиваемых данных')
        i, j = key
        self.__check_indx(i, j)
        self.table[i][j].data = value

    def __getitem__(self, item):
        i, j = item
        self.__check_indx(i, j)
        return self.table[i][j].data

    def __iter__(self):
        for row in self.table:
            yield (x.data for x in row)

table = TableValues(2, 2, str)
table[0,0] = 's'
for row in table:
    for value in row:
        print(value, end =' ')
    print()
# table[0,0] = 1

