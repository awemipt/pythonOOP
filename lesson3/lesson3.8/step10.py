class Cell:
    def __init__(self, value):
        self.value = value


class SparseTable:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.data = {}

    def add_data(self, row, col, data):
        if row + 1 > self.rows:
            self.rows = row + 1
        if col + 1> self.cols:
            self.cols = col + 1
        self.data[(row, col)] = data

    def remove_data(self,row ,col):
        if (row, col) not in self.data:
            raise IndexError('ячейка с указанными индексами не существует')
        del self.data[(row, col)]
        self.cols = max(self.data, key= lambda x: x[1])[1] + 1
        self.rows = max(self.data, key= lambda x: x[0])[0] + 1

    def __setitem__(self, key, value):
        i, j = key
        if (i, j) not in self.data:
            self.add_data(i, j, Cell(value))
            return
        self.data[(i, j)].value = value

    def __getitem__(self, item):
        i, j = item
        if (i, j) not in self.data:
            raise ValueError('данные по указанным индексам отсутствуют')
        return self.data[(i, j)].value

st = SparseTable()
st.add_data(2, 5, Cell("cell_25"))
st.add_data(0, 0, Cell("cell_00"))
st[2, 5] = 25 # изменение значения существующей ячейки
st[11, 7] = 'cell_117' # создание новой ячейки
print(st[0, 0]) # cell_00
# st.remove_data(2, 5)
print(st.rows, st.cols) # 12, 8 - общее число строк и столбцов в таблице
# val = st[2, 5] # ValueError
# st.remove_data(12, 3) # IndexError