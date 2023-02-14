class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def __call__(self, matrix, *args, **kwargs):
        tmp = len(matrix[0])
        for row in matrix:
            for x in row:
                if len(row) != tmp:
                    raise ValueError("Неверный формат для первого параметра matrix.")
                if type(x) not in (int, float):
                    raise ValueError("Неверный формат для первого параметра matrix.")
        ans = []
        tmp = []
        for i in range(0, len(matrix), self.step[0]):

            for j in range(0, len(matrix[i]), self.step[1]):
                if i + self.size[0] - 1 < len(matrix[i]) and j + self.size[1] -1 < len(matrix):
                    m = matrix[i][j]
                    for i_ in range(i, i + self.size[0]):
                        for j_ in range(j, j + self.size[1]):
                            if matrix[i_][j_] > m:
                                m = matrix[i_][j_]
                    tmp.append(m)
            if tmp:
                ans.append(tmp)
            tmp = []
        return ans


mp = MaxPooling(step=(2, 2), size=(2, 2))
res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])  # [[6, 8], [9, 7]]
res = mp([[1, 5, 2], [7, 0, 1], [4, 10, 3]])
print(res)
