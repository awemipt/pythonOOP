class Matrix:
    def __init__(self, *args):
        if len(args) == 3:
            rows, cols, fill_value = args
            if type(fill_value) not in [int, float] or any(map(lambda x: type(x) != int, [rows, cols])):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
            self.rows = rows
            self.cols = cols
            self.__matrix = [[fill_value for _ in range(cols)] for _ in range(rows)]
        elif len(args) == 1:
            lst2d, = args
            n = len(lst2d)
            m = len(lst2d[0])
            self.cols = m
            self.rows = n
            for row in lst2d:
                if len(row) != m:
                    raise TypeError('список должен быть прямоугольным, состоящим из чисел')
                for x in row:
                    if type(x) not in (int, float):
                        raise TypeError('список должен быть прямоугольным, состоящим из чисел')

            self.__matrix = lst2d

    def __check_indx(self, i, j):
        if any([i < 0, j < 0, i >= self.rows, j >= self.cols]):
            raise IndexError('недопустимые значения индексов')

    def __getitem__(self, item):
        i, j = item
        self.__check_indx(i, j)
        return self.__matrix[i][j]

    def __setitem__(self, key, value):
        if type(value) not in (int, float):
            raise TypeError('значения матрицы должны быть числами')
        i, j = key
        self.__check_indx(i, j)
        self.__matrix[i][j] = value

    def __add__(self, other):
        if type(other) is int:
            other = Matrix(self.rows, self.cols, other)
        if any([self.rows != other.rows, self.cols != other.cols]):
            raise ValueError('операции возможны только с матрицами равных размеров')
        ans = []
        for row1, row2 in zip(self.__matrix, other.__matrix):
            row = [a + b for a, b in zip(row1, row2)]
            ans.append(row)
        return Matrix(ans)

    def __sub__(self, other):
        if type(other) is int:
            other = Matrix(self.rows, self.cols, other)
        if any([self.rows != other.rows, self.cols != other.cols]):
            raise ValueError('операции возможны только с матрицами равных размеров')
        ans = []
        for row1, row2 in zip(self.__matrix, other.__matrix):
            row = [a - b for a, b in zip(row1, row2)]
            ans.append(row)
        return Matrix(ans)

    def print(self):
        for row in self.__matrix:
            for x in row:
                print(x, end=' ')
            print()

mt = Matrix([[1, 2], [3, 4],[5]])
mt2 = Matrix([[1, 2], [3, 4]])
res = mt[0, 0] # 1
print(res)
res = mt[0, 1] # 2
res = mt[1, 0] # 3
res = mt[1, 1]
mt -= mt2
mt.print()